# Lesson 04: Encryption and Keys
**Student Study Guide**


## Lesson Objectives

* Data Encryption
* Modern Authorization Management
* Enterprise Solutions
**[Image Recommendation]:** A super minimalist abstract vector diagram showing a data vault with a digital key overlay.
**Presenter Notes:**


## Overview

<!-- NotebookLM Podcast via Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/f51cfe24-e5d0-4d6c-ab56-8bbb41c1cc26/"></iframe></div>

## System Ownership & FileVault Encryption

This document aggregates all concepts, commands, and relevant tools for Lesson 4, which covers Secure Tokens, FileVault encryption mechanisms, and Bootstrap Token workflows in deployment and management environments.

---

### Glossary and Core Concepts

* **Secure Token:** A cryptographic wrapper (protected by the user's password) that enables a local macOS account to acquire cryptographic "ownership" over the Data Volume, permitting critical tasks such as enabling FileVault or authorizing software updates on Apple Silicon Macs. The initial user created via Setup Assistant receives a Secure Token automatically.
* **FileVault:** Built-in macOS full-disk encryption that secures the Data Volume using XTS-AES-128. On Apple Silicon Macs, data is hardware-encrypted by default, and enabling FileVault simply wraps the existing hardware key with the user's password with zero impact on performance.
* **Volume Ownership:** A mechanism on Apple Silicon Macs requiring special cryptographic authorization to perform system-level tasks such as erasing the Mac, modifying startup security policies, or upgrading the OS. Ownership is directly derived from accounts holding a Secure Token.
* **Bootstrap Token:** An enterprise token escrowed to the MDM server during device enrollment. It allows MDM to automatically grant a Secure Token to standard or network/cloud users (such as Managed Apple Accounts - MAIDs) logging in later, eliminating the requirement for the original initial user's password.

!!! info "Demystifying Enterprise Tokens and Certificates"
    macOS and Apple management environments utilize a variety of tokens and certificates. Below is a breakdown of commonly referenced terms:
    
    * **APNs Certificate / Token:** Secures and authenticates the encrypted communication channel between MDM, Apple servers, and managed endpoints.
    * **Service Token:** Authenticates the MDM server with **Apple Business Manager (ABM)**.
    * **Content Token:** Authenticates the MDM server with the **Apps & Books (VPP)** catalog.
    * **Secure Token:** A local cryptographic token in macOS that allows a user account to unlock a FileVault-encrypted volume.
    * **Bootstrap Token:** An institutional token allowing MDM to grant Secure Tokens to user accounts without manual end-user interaction.

    | Characteristic | Certificate | Token |
    |---|---|---|
    | **Purpose** | Identity proof (like a passport) | Temporary access authorization (like a boarding pass) |
    | **Issuer** | Certificate Authority (CA) | Authentication Server / Identity Provider (IdP) |
    | **Validity** | Long-term (months / years) | Dynamic / Short-term (minutes / hours) |
    | **Format** | X.509 (`.crt`, `.cer`, `.pem`) | JWT, SAML, Opaque String |
    | **Verification Method** | Certificate chain validation against CA (Public Key) | Local signature and validity check |
* **Recovery Key (PRK / IRK):** When FileVault encryption is enabled, a fallback key is generated to unlock the disk if the account password is lost.
* **PRK - Personal Recovery Key:** An alphanumeric string displayed to the user for safe keeping, or backed up to an iCloud account (in Tahoe, iCloud backup is enabled automatically by default for personal accounts).
  * **IRK - Institutional Recovery Key:** A legacy key mechanism used by organizations via MDM profiles, allowing IT admins to unlock encrypted drives using a master certificate payload. Modern deployments favor MDM-escrowed Personal Recovery Keys (PRKs).
* **VEK (Volume Encryption Key) & KEK (Key Encryption Key):** The VEK is the hardware encryption key stored within the Secure Enclave. The KEK is derived from the user's login password and is used to wrap/unwrap the VEK during startup authorization.
* **Virtualization (Exclaves):** In macOS 26 Tahoe, FileVault encryption is supported within virtual machines via Exclave technology, which virtualizes Secure Enclave primitives.
* **SSH Pre-boot:** macOS 26 Tahoe introduces remote SSH connectivity during the pre-boot phase, allowing administrators to unlock FileVault on headless servers.

**FileVault Versioning History:**

| FileVault Version | Release Year (OS) | Encryption Method | Notable Features |
|---|---|---|---|
| FileVault 1 | 2003 (Panther 10.3) | Encrypted Disk Image (DMG) | Encrypted only the user's home directory; susceptible to corruption and vulnerability exploits (e.g., VileFault tool). |
| FileVault 2 | 2011 (Lion 10.7) | Software-based via CPU | Full-disk encryption with minor CPU performance overhead. |
| Modern FileVault | 2017+ (T2 / Apple Silicon) | Hardware-bound (AES Engine & Secure Enclave) | Zero performance impact; hardware-level inline encryption using key wrapping. |

---

### Comprehensive Command Line (CLI) Reference for Encryption & Token Management

Managing Secure Tokens and FileVault relies primarily on the `sysadminctl` and `fdesetup` CLI tools. Every macOS administrator and IT support engineer must understand these core utilities.

#### Managing Secure Tokens via `sysadminctl`

* **Check Secure Token status for the current user:**

  ```bash
  sysadminctl -secureTokenStatus $USER
  ```

* **Check Secure Token status for a specific user (e.g., `johndoe`):**

  ```bash
  sysadminctl -secureTokenStatus johndoe
  ```

* **Grant Secure Token to another user:** (Requires an existing admin account holding a Secure Token)
  ```bash
  sysadminctl -secureTokenOn newuser -password newuserpass -adminUser adminname -adminPassword adminpass
  ```

* **Revoke Secure Token from a user:** (Warning: Stripping tokens from all user accounts may lock out critical system authorizations!)
  ```bash
  sysadminctl -secureTokenOff otheruser -password userpass -adminUser adminname -adminPassword adminpass
  ```

#### Managing FileVault via `fdesetup`

* **Check FileVault status (active status and encryption state of the volume):**

  ```bash
  fdesetup status
  ```

* **Enable FileVault via Terminal (for current user):**

  ```bash
  sudo fdesetup enable
  ```
  *(Prompt for password; prints the generated Personal Recovery Key in standard output).*

* **Disable FileVault encryption (initiates volume decryption):**

  ```bash
  sudo fdesetup disable
  ```

* **List user accounts authorized for pre-boot unlocking:**

  ```bash
  sudo fdesetup list
  ```

* **Remove a specific user (e.g., `johndoe`) from pre-boot authorization:**

  ```bash
  sudo fdesetup remove -user johndoe
  ```

* **Rotate the Personal Recovery Key (PRK) and generate a new key:**

  ```bash
  sudo fdesetup changerecovery -personal
  ```

* **Synchronize FileVault configuration (verifies and updates key/password associations):**

  ```bash
  sudo fdesetup sync
  ```

* **Enable FileVault non-interactively using an input plist (Ideal for MDM deployment scripts; requires admin credentials and XML payload):**

  ```bash
  sudo fdesetup enable -inputplist < /path/to/fdesetup.plist
  ```

#### Advanced Cryptographic Diagnostics via `diskutil` and `profiles`

* **List cryptographic users for the APFS Data Container:**

  ```bash
  diskutil apfs listcryptousers /
  ```
  *(Displays UUIDs for all cryptographic identities capable of unwrapping the volume encryption key, including Token-enabled users, PRK, or IRK).*

* **Check Bootstrap Token status with MDM server:**

  ```bash
  sudo profiles status -type bootstraptoken
  ```
  *(A positive response, such as `profiles: Bootstrap Token supported on server` or `escrowed to server`, indicates successful token escrow for future automated token grants).*

* **Force escrow/installation of Bootstrap Token to MDM:**
  ```bash
  sudo profiles install -type bootstraptoken
  ```

---

### Troubleshooting & Quick Solutions (Cheat Sheet)

1. **Issue:** "Account lacks authorization" – A new local admin account was created, but it cannot authorize OS updates on Apple Silicon or disable FileVault.
   * **Solution:** The user lacks a Secure Token and consequently lacks Volume Ownership. Verify status using `sysadminctl -secureTokenStatus`. If missing, log in as the original admin (created during Setup Assistant) and grant a Secure Token via `sysadminctl -secureTokenOn`.

2. **Issue:** A Personal Recovery Key (PRK) has been compromised and must be rotated across managed endpoints.
   * **Solution:** Execute `sudo fdesetup changerecovery -personal` locally, or issue a key re-escrow profile command from MDM to force PRK generation and secure escrowing to your console.

3. **Issue:** FileVault is enabled, but a newly created local user (in an environment without MDM Bootstrap Token support) is missing from the login screen during startup.
   * **Solution:** Only users holding a Secure Token and present in `fdesetup list` can authenticate through Preboot Authentication. Log in with an existing token-enabled account, grant a Secure Token to the new user via `sysadminctl`, and verify cryptographic inclusion.

4. **Issue:** Account password was changed out-of-band, and FileVault pre-boot unlock still requires the legacy password.
   * **Solution:** The Key Encryption Key (KEK) remains wrapped by the legacy password. The user must update their password natively through System Settings while logged in to synchronize the Secure Enclave key bindings.

---

## Recommended Resources & Further Reading

* [Use secure token, bootstrap token, and volume ownership in deployments](https://support.apple.com/guide/deployment/use-secure-token-bootstrap-token-and-volume-dep24dbdcf9e/web) - Technical article for IT administrators on deployment token workflows.
* [Intro to FileVault for Mac](https://support.apple.com/guide/security/intro-to-filevault-secd73eaebd1/web) - Deep dive technical overview of Apple Silicon encryption architecture.
* [Manage FileVault with mobile device management](https://support.apple.com/guide/deployment/manage-filevault-with-device-management-depf2a6327b/web) - Guide for managing enterprise FileVault recovery keys via MDM.
* [Protect data on your Mac with FileVault](https://support.apple.com/en-us/HT204837) - End-user guide on enabling FileVault encryption.

## Summary Video

<!-- Summary Video via YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/i7byyZYgNUY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


!!! tip "Visual Demonstration (Student Reference)"
    These images illustrate the interface or mechanisms relevant to this lesson.

![Disk_image_performance_the_cost_of_encryption_rise_p2_28](../assets/images/Lesson_04/L04_DeepDive_Disk_image_performance_the_cost_of_encryption_rise_p2_28.png)
![Slide100_image109](../assets/images/Lesson_04/L04_LegacySlide_Slide100_image109.png)
![Slide100_image110](../assets/images/Lesson_04/L04_LegacySlide_Slide100_image110.png)
![Slide101_image111](../assets/images/Lesson_04/L04_LegacySlide_Slide101_image111.png)
![Slide101_image112](../assets/images/Lesson_04/L04_LegacySlide_Slide101_image112.png)
![Slide70_image84](../assets/images/Lesson_04/L04_LegacySlide_Slide70_image84.png)
![Slide70_image85](../assets/images/Lesson_04/L04_LegacySlide_Slide70_image85.png)
![Slide94_image102](../assets/images/Lesson_04/L04_LegacySlide_Slide94_image102.png)
![Slide94_image103](../assets/images/Lesson_04/L04_LegacySlide_Slide94_image103.png)

<!-- src_hash: 7997fa06baba345d9fc86a3fbf6ff9a2acd8dce196c9f54f39804dcf21a9c5df -->
