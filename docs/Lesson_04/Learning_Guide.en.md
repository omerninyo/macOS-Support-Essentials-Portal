# Lesson 04: Encryption and Keys
**Student Reference Guide**


## Lesson Objectives

* Data Encryption
* Modern Privilege Management
* Enterprise Solutions
**[Image Recommendation]:** A super minimalist abstract vector diagram showing a data vault with a digital key overlay.
**Presenter Notes:**


## Overview

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/f51cfe24-e5d0-4d6c-ab56-8bbb41c1cc26/"></iframe></div>

## System Ownership & FileVault Encryption

This document consolidates all concepts, commands, and tools relevant to Lesson 4, covering Secure Tokens, FileVault encryption architecture, and Bootstrap Token mechanisms within deployment and management environments.

---

### Core Terminology and Glossary

* **Secure Token:** A cryptographic chain (wrapped by the user's password) granting a local account "Volume Ownership" over the Data Volume, enabling critical tasks such as FileVault activation or software updates on Apple Silicon hardware. The initial user created via Setup Assistant receives a Secure Token automatically.
* **FileVault:** Built-in macOS volume encryption protecting the Data Volume using full XTS-AES-128 encryption. On Apple Silicon Macs, data is natively encrypted at the hardware layer at all times; enabling FileVault wraps the existing hardware encryption key with the user's account password with zero performance penalty.
* **Volume Ownership:** Security paradigm on Apple Silicon Macs requiring cryptographic authorization to perform system-level operations such as erasing the Mac, modifying boot security policies, or upgrading the OS. Derived directly from users possessing a Secure Token.
* **Bootstrap Token:** An enterprise escrowed token pushed to the MDM server during Device Enrollment. Maintained securely within MDM, it automatically grants a Secure Token to standard users or directory/cloud accounts (such as Managed Apple Accounts - MAID) logging in later, without requiring the initial user's credentials.
* **Recovery Key (PRK / IRK):** A backup key generated upon FileVault activation to ensure access recovery in the event of forgotten user credentials.
* **PRK - Personal Recovery Key:** An alphanumeric key displayed to the end user for secure recordkeeping, or escrowed automatically via iCloud (in macOS Tahoe, iCloud escrow is often enabled by default for personal accounts).
  * **IRK - Institutional Recovery Key:** Legacy certificate-based key utilized by enterprises via MDM payloads allowing administrators to unlock volumes. Modern deployments standardize on escrowed PRKs.
* **VEK (Volume Encryption Key) & KEK (Key Encryption Key):** VEK is the hardware encryption key stored securely within the Secure Enclave. KEK is derived from user authentication credentials and wraps the VEK to unlock the volume during boot.
* **Virtualization (Exclaves):** In macOS 26 Tahoe, FileVault encryption is supported within virtualized environments via Exclave technology emulating Secure Enclave functionality.
* **SSH Pre-boot:** Introduced in macOS 26 Tahoe, allowing remote SSH connectivity to headless servers during Pre-boot authentication to unlock FileVault.

**Brief History of FileVault Architecture:**

| FileVault Generation | Release Year (OS Version) | Encryption Method | Key Characteristics |
|---|---|---|---|
| FileVault 1 | 2003 (Panther 10.3) | Encrypted Disk Image (DMG) | Encrypted user home directories only; fragile design susceptible to recovery tools (e.g., VileFault). |
| FileVault 2 | 2011 (Lion 10.7) | Full-disk CPU-based software | Full disk volume encryption; introduced modest CPU overhead and performance impact. |
| Modern FileVault | 2017+ (T2 / Apple Silicon) | Dedicated Hardware AES Engine & Secure Enclave | Zero performance impact; hardware-level native encryption utilizing key wrapping architecture. |

---

### Comprehensive Command Line Interface (CLI) Guide for Encryption and Tokens

Managing Secure Token state and FileVault configuration relies primarily on the `sysadminctl` and `fdesetup` utilities. These represent essential core tools for system administrators and technical support engineers.

#### Secure Token Management via `sysadminctl`

* **Query Secure Token status for current user:**

  ```bash
  sysadminctl -secureTokenStatus $USER
  ```

* **Query Secure Token status for a specific user (e.g., `johndoe`):**

  ```bash
  sysadminctl -secureTokenStatus johndoe
  ```

* **Grant Secure Token to another user account:** (Requires existing admin user with active Secure Token)
  ```bash
  sysadminctl -secureTokenOn newuser -password newuserpass -adminUser adminname -adminPassword adminpass
  ```

* **Remove Secure Token from a user account:** (Caution: Removing Secure Token from all users can lock the system out of administrative operations!)
  ```bash
  sysadminctl -secureTokenOff otheruser -password userpass -adminUser adminname -adminPassword adminpass
  ```

#### FileVault Management via `fdesetup`

* **Query FileVault status (verifies active status and encryption state):**

  ```bash
  fdesetup status
  ```

* **Enable FileVault via Terminal (for current logged-in user):**

  ```bash
  sudo fdesetup enable
  ```
  *(Prompts for credentials and outputs a Personal Recovery Key to stdout).*

* **Disable FileVault encryption (initiates volume decryption):**

  ```bash
  sudo fdesetup disable
  ```

* **List users enabled for Pre-boot unlocking:**

  ```bash
  sudo fdesetup list
  ```

* **Remove specific user authorization (e.g., `johndoe`) from Pre-boot unlocking:**

  ```bash
  sudo fdesetup remove -user johndoe
  ```

* **Rotate Personal Recovery Key (PRK) and generate a new key:**

  ```bash
  sudo fdesetup changerecovery -personal
  ```

* **Force immediate FileVault state synchronization:**

  ```bash
  sudo fdesetup sync
  ```

* **Enable FileVault silently via input plist (ideal for automated MDM workflows):**

  ```bash
  sudo fdesetup enable -inputplist < /path/to/fdesetup.plist
  ```

#### Advanced Cryptographic Inspection via `diskutil` and `profiles`

* **List all Cryptographic Users associated with the APFS Data Container:**

  ```bash
  diskutil apfs listcryptousers /
  ```
  *(Displays UUIDs of all cryptographic entities authorized to decrypt the Data Volume, including enabled users, PRKs, and IRKs).*

* **Query Bootstrap Token status against MDM server:**

  ```bash
  sudo profiles status -type bootstraptoken
  ```
  *(A positive response, such as `profiles: Bootstrap Token supported on server` or `escrowed to server`, confirms the token is securely escrowed).*

* **Force immediate Bootstrap Token escrow to MDM server:**
  ```bash
  sudo profiles install -type bootstraptoken
  ```

---

### Troubleshooting and Quick Solutions (Cheat Codes)

1. **Issue:** "Insufficient User Privileges" – A newly created local administrator account cannot authorize macOS updates on Apple Silicon or disable FileVault.
   * **Solution:** The user lacks a Secure Token and consequently lacks Volume Ownership. Verify status using `sysadminctl -secureTokenStatus`. If disabled, log in as the original administrator (created during Setup Assistant) and grant a token using `sysadminctl -secureTokenOn`.

2. **Issue:** A Personal Recovery Key (PRK) must be rotated due to potential compromise.
   * **Solution:** Execute `sudo fdesetup changerecovery -personal` to generate a new PRK locally, or trigger a re-escrow action via MDM to generate and record a new PRK centrally.

3. **Issue:** FileVault is enabled, but a newly created local user (in an unmanaged environment without Bootstrap Token) does not appear at the login window after restart.
   * **Solution:** Only users with a Secure Token listed in `fdesetup list` can pass Pre-boot Authentication. Log in with the primary administrator, authorize the user via `sysadminctl`, and verify inclusion in the cryptographic user list.

4. **Issue:** Account password was changed outside macOS, and FileVault requires the old password to unlock.
   * **Solution:** The KEK remains wrapped by the legacy password. The user must update their password through System Settings while authenticated to re-wrap the KEK in the Secure Enclave.

---

## Recommended Reading and References

* [Use secure token, bootstrap token, and volume ownership in deployments](https://support.apple.com/guide/deployment/use-secure-token-bootstrap-token-and-volume-dep24dbdcf9e/web) - IT administrator reference on cryptographic authorization in deployment.
* [Intro to FileVault for Mac](https://support.apple.com/guide/security/intro-to-filevault-secd73eaebd1/web) - Deep technical overview of FileVault architecture on Apple Silicon.
* [Manage FileVault with mobile device management](https://support.apple.com/guide/deployment/manage-filevault-with-device-management-depf2a6327b/web) - Guide for managing enterprise recovery key escrow.
* [Protect data on your Mac with FileVault](https://support.apple.com/en-us/HT204837) - End-user guide for enabling FileVault encryption.

## Summary Video

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/i7byyZYgNUY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


!!! tip "Visual Aid (Student Reference)"
    These images illustrate the interface or mechanism relevant to the lesson topic.

![Disk_image_performance_the_cost_of_encryption_rise_p2_28](../assets/images/Lesson_04/L04_DeepDive_Disk_image_performance_the_cost_of_encryption_rise_p2_28.png)
![Slide100_image109](../assets/images/Lesson_04/L04_LegacySlide_Slide100_image109.png)
![Slide100_image110](../assets/images/Lesson_04/L04_LegacySlide_Slide100_image110.png)
![Slide101_image111](../assets/images/Lesson_04/L04_LegacySlide_Slide101_image111.png)
![Slide101_image112](../assets/images/Lesson_04/L04_LegacySlide_Slide101_image112.png)
![Slide70_image84](../assets/images/Lesson_04/L04_LegacySlide_Slide70_image84.png)
![Slide70_image85](../assets/images/Lesson_04/L04_LegacySlide_Slide70_image85.png)
![Slide94_image102](../assets/images/Lesson_04/L04_LegacySlide_Slide94_image102.png)
![Slide94_image103](../assets/images/Lesson_04/L04_LegacySlide_Slide94_image103.png)

<!-- src_hash: f2f168910b41db2fa1a37309aad8c98c70cf26a3803634a3ef1cdc6267ae3b4e -->
