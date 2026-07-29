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

## System Ownership & FileVault

This document summarizes all the concepts, commands, and tools relevant to Lesson 4, which deals with Secure Tokens, the FileVault encryption mechanism, and Bootstrap Token mechanisms in management and deployment environments.

---

### Glossary and Core Concepts

* **Secure Token:** A cryptographic chain (wrapped in the user's password) that allows a local account on the Mac to gain cryptographic "ownership" over the Data Volume, and authorize critical tasks such as enabling FileVault or software updates on Apple Silicon Macs. The first user created through Setup Assistant receives it automatically.
* **FileVault:** macOS's built-in encryption that fully encrypts the Data Volume using XTS-AES-128. On Apple Silicon Macs, data is always natively encrypted at the hardware level, and turning on FileVault essentially "wraps" the existing key with the user's password without affecting performance.
* **Volume Ownership:** A mechanism on Apple Silicon Macs that requires special permissions to perform system-level tasks like erasing a Mac, changing startup settings, or upgrading the OS. It is derived directly from users who possess a Secure Token.
* **Bootstrap Token:** A temporary and organizational "master key" pushed to the MDM server during enrollment. The token is stored in the MDM (via the Escrow process) and can automatically grant a Secure Token to regular users or cloud accounts (like Managed Apple Account - MAID) who log in later, without needing the password of the original user.
* **Recovery Key - PRK/IRK:** When turning on FileVault encryption, a backup key is generated in case the login password is lost.
* **PRK - Personal Recovery Key:** An alphanumeric key presented to the user to store safely, or alternatively, saved to their iCloud account.
  * **IRK - Institutional Recovery Key:** A key used by organizations via MDM, so that only organizational administrators can unlock drives using a special Payload (Configuration Profile).

**Brief History of FileVault Versions:**

| FileVault Version | Release Year (OS) | Encryption Method | Notable Features |
|---|---|---|---|
| FileVault 1 | 2003 (Panther 10.3) | Disk Image (DMG) | Encrypted only the home folder, considered fragile and easy to crack (a tool called VileFault demonstrated this). |
| FileVault 2 | 2011 (Lion 10.7) | Software via CPU | Whole-disk encryption, created a slight load and slightly degraded performance. |
| Modern | 2017+ (T2 / Apple Silicon) | Hardware (AES Engine & Secure Enclave) | Zero performance impact, built-in chip-level encryption using key wrapping. |

---

### Massive CLI Commands List for Encryption and Token Management

Managing the Secure Token and FileVault arrays is primarily done using the `sysadminctl` and `fdesetup` commands. These are core commands every macOS support technician or network administrator must know thoroughly.

#### Managing Secure Tokens using `sysadminctl`

* **Check Secure Token status for the current user:**

  ```bash
  sysadminctl -secureTokenStatus $USER
  ```
* **Check status for a specific user (e.g., `johndoe`):**

  ```bash
  sysadminctl -secureTokenStatus johndoe
  ```
* **Grant Secure Token to another user:** (Requires an admin user who already has a Secure Token)
  ```bash
  sysadminctl -secureTokenOn newuser -password newuserpass -adminUser adminname -adminPassword adminpass
  ```
* **Remove Secure Token from a user:** (Caution - removing the token for all users might lock the Mac out of critical permissions!)
  ```bash
  sysadminctl -secureTokenOff otheruser -password userpass -adminUser adminname -adminPassword adminpass
  ```

#### Managing FileVault using `fdesetup`

* **Check FileVault status (whether it's on/off and who is encrypting the Volume):**

  ```bash
  fdesetup status
  ```
* **Enable FileVault via Terminal (for the current user):**

  ```bash
  sudo fdesetup enable
  ```
  *(The system will prompt for a password and output a Personal Recovery Key to the terminal).*

* **Disable and remove encryption (Decryption of the Volume):**

  ```bash
  sudo fdesetup disable
  ```
* **List users authorized to unlock encryption during boot:**

  ```bash
  sudo fdesetup list
  ```
* **Remove a specific user (e.g., `johndoe`) from authorized disk unlockers:**

  ```bash
  sudo fdesetup remove -user johndoe
  ```
* **Change the Personal Recovery Key (PRK) and create a new one:**

  ```bash
  sudo fdesetup changerecovery -personal
  ```
* **Immediate FileVault sync (check if a refresh is needed for changed keys or passwords):**

  ```bash
  sudo fdesetup sync
  ```
* **Enable encryption mechanism with a silent Plist file (ideal for distribution in MDM workflows - requires admin privileges and XML config):**

  ```bash
  sudo fdesetup enable -inputplist < /path/to/fdesetup.plist
  ```

#### Advanced Cryptographic Diagnostics with `diskutil` and `profiles`

* **List all Cryptographic Users for the Data Container in APFS:**

  ```bash
  diskutil apfs listcryptousers /
  ```
  *(Displays the UUID of every cryptographic entity that can decrypt the Data Volume, including users with a token, PRK, or IRK).*

* **Check the status of the Bootstrap Token with the MDM server:**

  ```bash
  profiles status -type bootstraptoken
  ```
  *(A positive response, e.g., `profiles: Bootstrap Token supported on server` or `escrowed to server`, indicates the token was successfully saved to the server and is waiting to fetch future Secure Tokens).*

---

### Troubleshooting and Quick Fixes (Cheat Codes)

1. **Problem:** "User is missing permissions" – You created an additional Local Account (Admin), but it cannot approve OS updates on an Apple Silicon Mac, or disable FileVault.
   * **Solution:** The user lacks a Secure Token and consequently lacks "Volume Ownership". Check using `sysadminctl -secureTokenStatus`. If missing, use the original Admin account (which went through Setup Assistant) to grant a Secure Token using the `sysadminctl -secureTokenOn` command.

2. **Problem:** You need to rotate (change) a Recovery Key that is known to have leaked in the organization.
   * **Solution:** Use `sudo fdesetup changerecovery -personal` (for a personal key), or verify through the MDM system that you ran a new `Escrow` command to force the creation of a new PRK against the management catalog.

3. **Problem:** FileVault is enabled and running, but a new locally created user (in a non-MDM managed environment with no Bootstrap Token) does not appear on the login screen immediately after a reboot.
   * **Solution:** Only users with a Secure Token who appear in the `fdesetup list` can pass the hardware-level Preboot Authentication before the OS loads. Log in with the main user, add the user via `sysadminctl`, and verify they are added to the cryptographic list.

---

## Recommended Links and Further Reading

* [Use secure token, bootstrap token, and volume ownership in deployments](https://support.apple.com/guide/deployment/use-secure-token-bootstrap-token-and-volume-dep24dbdcf9e/web) - Technical article for IT admins on how encryption authentication is performed in the enterprise.
* [Intro to FileVault for Mac](https://support.apple.com/guide/security/intro-to-filevault-secd73eaebd1/web) - In-depth technical overview of encryption architecture on Apple Silicon processors.
* [Manage FileVault with mobile device management](https://support.apple.com/guide/deployment/manage-filevault-with-device-management-depf2a6327b/web) - Guide for managing organizational recovery keys for FileVault.
* [Protect data on your Mac with FileVault](https://support.apple.com/en-us/HT204837) - Basic end-user guide on how to turn on encryption and protect files.

## Summary Video

<!-- Summary Video from YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/DDXfEIRgAxs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>





!!! tip "Visual Aid (Student Reference)"
    These images illustrate the relevant interface or mechanism for the lesson topic.



<!-- src_hash: ec3425e45d98a697010571ca97af0d09b82fd166707206d1f6e714f5a68ab878 -->


!!! tip "Visual Aids (Student Guide)"
    These images illustrate the relevant interface or mechanism for this lesson.

![Disk_image_performance_the_cost_of_encryption_rise_p2_28](../assets/images/Lesson_04/L04_DeepDive_Disk_image_performance_the_cost_of_encryption_rise_p2_28.png)
![Slide100_image109](../assets/images/Lesson_04/L04_LegacySlide_Slide100_image109.png)
![Slide100_image110](../assets/images/Lesson_04/L04_LegacySlide_Slide100_image110.png)
![Slide101_image111](../assets/images/Lesson_04/L04_LegacySlide_Slide101_image111.png)
![Slide101_image112](../assets/images/Lesson_04/L04_LegacySlide_Slide101_image112.png)
![Slide70_image84](../assets/images/Lesson_04/L04_LegacySlide_Slide70_image84.png)
![Slide70_image85](../assets/images/Lesson_04/L04_LegacySlide_Slide70_image85.png)
![Slide94_image102](../assets/images/Lesson_04/L04_LegacySlide_Slide94_image102.png)
![Slide94_image103](../assets/images/Lesson_04/L04_LegacySlide_Slide94_image103.png)
