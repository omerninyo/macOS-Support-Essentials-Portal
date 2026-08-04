# Lesson 04: Encryption and Keys
**Student Learning Guide**

## Lesson Objectives

* Data Encryption
* Modern Permission Management
* Enterprise Solutions
**[Image Recommendation]:** A super minimalist abstract vector diagram showing a data vault with a digital key overlay.
**Presenter Notes:**


## Overview

<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/f51cfe24-e5d0-4d6c-ab56-8bbb41c1cc26/"></iframe></div>

## System Ownership and Encryption (System Ownership & FileVault)

This document summarizes all the concepts, commands, and tools relevant to Lesson 4, which deals with Secure Tokens, the FileVault encryption mechanism, and the Bootstrap Token mechanism in deployment and management environments.

---

### Glossary and Core Concepts

* **Secure Token:** A cryptographic chain (wrapped with the user's password) that allows a local Mac account to gain cryptographic "ownership" over the Data Volume, and authorize critical tasks like enabling FileVault or updating software on Apple Silicon Macs. The first user created through Setup Assistant receives it automatically.
* **FileVault:** macOS's built-in encryption that fully encrypts the Data Volume using XTS-AES-128. On Apple Silicon Macs, data is natively hardware-encrypted at all times, and enabling FileVault actually just "wraps" the existing key with the user's password without performance impact.
* **Volume Ownership:** A mechanism on Apple Silicon Macs that requires special privileges to perform system-level tasks like erasing the Mac, changing boot settings, or upgrading the OS. Derived directly from users who have a Secure Token.
* **Bootstrap Token:** A temporary, enterprise "master key" pushed to the MDM server during enrollment. The token is escrowed to the MDM and can automatically grant a Secure Token to permanent users or cloud accounts (like Managed Apple Accounts - MAID) who log in later, without needing the original user's password.
* **Recovery Key - PRK/IRK:** When FileVault is enabled, a backup key is created in case the login password is lost.
* **PRK - Personal Recovery Key:** An alphanumeric key displayed to the user to safely store, or alternatively, saved in their iCloud account (in Tahoe, iCloud recovery is often enabled automatically for consumers).
  * **IRK - Institutional Recovery Key:** A legacy key used by organizations via MDM. Modern organizations prefer escrowing individual PRKs instead of using one global IRK.
* **VEK (Volume Encryption Key) & KEK (Key Encryption Key):** VEK is the hardware key in the Secure Enclave encrypting the data. KEK is generated from your password to "wrap" and unlock the VEK.
* **Virtual Machine (VM) exclaves:** In macOS 26 Tahoe, FileVault is fully supported in macOS VMs using Secure Enclave virtualization (exclaves).
* **SSH Pre-boot:** In macOS 26 Tahoe, headless servers can be unlocked remotely via SSH during the pre-boot phase.

**FileVault Version History Brief:**

| FileVault Version | Release Year (OS) | Encryption Method | Notable Features |
|---|---|---|---|
| FileVault 1 | 2003 (Panther 10.3) | Disk Image (DMG) | Encrypted only the home folder; considered fragile and easily hacked (VileFault tool demonstrated this). |
| FileVault 2 | 2011 (Lion 10.7) | Software via CPU | Full disk encryption, created light overhead and slightly impacted performance. |
| Modern | 2017+ (T2 / Apple Silicon) | Hardware (AES Engine & Secure Enclave) | Zero performance hit, chip-level encryption working via key wrapping. |

---

### Massive CLI Command List for Encryption and Tokens

Managing Secure Tokens and FileVault relies heavily on `sysadminctl` and `fdesetup`. These are core commands every macOS support tech or network admin must know deeply.

#### Managing Secure Tokens with `sysadminctl`

* **Check Secure Token status for current user:**
  ```bash
  sysadminctl -secureTokenStatus $USER
  ```
* **Check status for specific user (e.g., `johndoe`):**
  ```bash
  sysadminctl -secureTokenStatus johndoe
  ```
* **Grant Secure Token to another user:** (Requires an admin user who already has a Secure Token)
  ```bash
  sysadminctl -secureTokenOn newuser -password newuserpass -adminUser adminname -adminPassword adminpass
  ```
* **Remove Secure Token from a user:** (Caution - removing the token from all users can lock out critical privileges!)
  ```bash
  sysadminctl -secureTokenOff otheruser -password userpass -adminUser adminname -adminPassword adminpass
  ```

#### Managing FileVault with `fdesetup`

* **Check FileVault status (is it active and who encrypts the volume):**
  ```bash
  fdesetup status
  ```
* **Enable FileVault via Terminal (for current user):**
  ```bash
  sudo fdesetup enable
  ```
  *(System will ask for password and output a Personal Recovery Key to the terminal).*
* **Disable and remove encryption (Volume Decryption):**
  ```bash
  sudo fdesetup disable
  ```
* **Show list of users authorized to unlock the disk at boot:**
  ```bash
  sudo fdesetup list
  ```
* **Remove a specific user (e.g., `johndoe`) from authorized disk unlockers:**
  ```bash
  sudo fdesetup remove -user johndoe
  ```
* **Rotate the Personal Recovery Key (PRK) and create a new one:**
  ```bash
  sudo fdesetup changerecovery -personal
  ```
* **Immediate FileVault sync (check if refresh needed for changed keys or passwords):**
  ```bash
  sudo fdesetup sync
  ```
* **Enable encryption with a silent Plist file (Ideal for MDM deployment):**
  ```bash
  sudo fdesetup enable -inputplist < /path/to/fdesetup.plist
  ```

#### Advanced Cryptographic Diagnostics with `diskutil` and `profiles`

* **List all Cryptographic Users for the APFS Data Container:**
  ```bash
  diskutil apfs listcryptousers /
  ```
  *(Shows UUIDs of every crypto entity that can decrypt the Data Volume).*
* **Check Bootstrap Token status with the MDM server:**
  ```bash
  sudo profiles status -type bootstraptoken
  ```
  *(Positive response, e.g., `profiles: Bootstrap Token supported on server` or `escrowed to server`, means the token is safely stored on the server waiting to grant future tokens).*
* **Manually trigger Bootstrap Token Escrow:**
  ```bash
  sudo profiles install -type bootstraptoken
  ```

---

### Troubleshooting and Cheat Codes

1. **Problem:** "Missing User Privileges" – You created an additional Local Account (Admin), but they can't authorize OS updates on an Apple Silicon Mac, or disable FileVault.
   * **Solution:** The user lacks a Secure Token and consequently Volume Ownership. Check with `sysadminctl -secureTokenStatus`. If missing, use the original Admin account (that ran Setup Assistant) to grant the token via `sysadminctl -secureTokenOn`.

2. **Problem:** You need to rotate a Recovery Key known to have leaked.
   * **Solution:** Use `sudo fdesetup changerecovery -personal`, or ensure via the MDM system you ran an `Escrow` command to force new PRK generation.

3. **Problem:** FileVault is on, but a new locally created user doesn't appear on the login screen immediately after reboot.
   * **Solution:** Only users with a Secure Token listed in `fdesetup list` can pass Pre-boot Authentication. Log in with the main user, add the new user via `sysadminctl`, and ensure they are added to the cryptographic list.

4. **Problem:** Password changed via external directory sync, and user needs old password to unlock FileVault.
   * **Solution:** The FileVault KEK hasn't updated. Have the user change their password securely through macOS System Settings, which properly resyncs the KEK with the Secure Enclave.

---

## Recommended Reading and Links

* [Use secure token, bootstrap token, and volume ownership in deployments](https://support.apple.com/guide/deployment/use-secure-token-bootstrap-token-and-volume-dep24dbdcf9e/web)
* [Intro to FileVault for Mac](https://support.apple.com/guide/security/intro-to-filevault-secd73eaebd1/web)
* [Manage FileVault with mobile device management](https://support.apple.com/guide/deployment/manage-filevault-with-device-management-depf2a6327b/web)
* [Protect data on your Mac with FileVault](https://support.apple.com/en-us/HT204837)

## Summary Video

<!-- YouTube Summary Video -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/i7byyZYgNUY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

!!! tip "Presentation Visuals"
    These images illustrate the relevant interface or mechanism for the lesson.

![Disk_image_performance_the_cost_of_encryption_rise_p2_28](../assets/images/Lesson_04/L04_DeepDive_Disk_image_performance_the_cost_of_encryption_rise_p2_28.png)
![Slide100_image109](../assets/images/Lesson_04/L04_LegacySlide_Slide100_image109.png)
![Slide100_image110](../assets/images/Lesson_04/L04_LegacySlide_Slide100_image110.png)
![Slide101_image111](../assets/images/Lesson_04/L04_LegacySlide_Slide101_image111.png)
![Slide101_image112](../assets/images/Lesson_04/L04_LegacySlide_Slide101_image112.png)
![Slide70_image84](../assets/images/Lesson_04/L04_LegacySlide_Slide70_image84.png)
![Slide70_image85](../assets/images/Lesson_04/L04_LegacySlide_Slide70_image85.png)
![Slide94_image102](../assets/images/Lesson_04/L04_LegacySlide_Slide94_image102.png)
![Slide94_image103](../assets/images/Lesson_04/L04_LegacySlide_Slide94_image103.png)
