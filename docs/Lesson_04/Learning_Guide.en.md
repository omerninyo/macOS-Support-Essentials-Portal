# Lesson 04: Encryption & Keys
**Student Learning Guide**

## Lesson Objectives

* Data Encryption
* Modern Privilege Management
* Enterprise Solutions

## Overview

<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/f51cfe24-e5d0-4d6c-ab56-8bbb41c1cc26/"></iframe></div>

## System Ownership & FileVault

This document synthesizes core concepts, commands, and tools for Lesson 4, covering Secure Token, FileVault encryption, and Bootstrap Token mechanisms in enterprise deployment and management environments.

---

### Glossary and Core Terminology

* **Secure Token:** A cryptographic chain (wrapped in the user's password) that grants a local account on macOS cryptographic "ownership" over the Data Volume, enabling authorization for critical tasks such as FileVault activation or software updates on Apple Silicon Macs. The initial user account created during Setup Assistant receives a Secure Token automatically.
* **FileVault:** Built-in volume encryption in macOS that fully encrypts the Data Volume using XTS-AES-128. On Apple Silicon Macs, data is inherently encrypted at the hardware level at all times; enabling FileVault wraps the existing hardware key with the user's password without impacting performance.
* **Volume Ownership:** A mechanism on Apple Silicon Macs requiring explicit authorization to execute system-level actions such as erasing the Mac, modifying boot security settings, or upgrading the OS. Ownership is directly derived from local accounts holding a Secure Token.
* **Bootstrap Token:** An enterprise escrowed token pushed to the MDM server during device enrollment. Escrowed in MDM, the Bootstrap Token automatically grants Secure Tokens to standard or cloud accounts (such as Managed Apple Accounts - MAIDs) logging in later, without requiring credentials from the original administrative user.

!!! info "Understanding Enterprise Tokens and Certificates"
    macOS and Apple management ecosystems utilize several types of tokens and certificates. Below is a breakdown of common terms:
    
    * **APNs Certificate / Token:** Secures and authenticates the encrypted communication channel between the MDM server, Apple Push Notification service (APNs), and managed devices.
    * **Service Token:** Authenticates the MDM server with **Apple Business Manager (ABM)** for Automated Device Enrollment.
    * **Content Token:** Authenticates the MDM server with **Apps & Books (VPP)** for volume license assignment.
    * **Secure Token:** Local cryptographic token in macOS allowing a user account to unlock a FileVault-encrypted volume.
    * **Bootstrap Token:** Organizational token allowing MDM to issue Secure Tokens to accounts automatically without end-user interaction.

    | Attribute | Certificate | Token |
    |---|---|---|
    | **Purpose** | Identity verification (like a passport) | Temporary authorization to access a resource (like a boarding pass) |
    | **Issuing Entity** | Certificate Authority (CA) | Authentication Server / Identity Provider (IdP) |
    | **Validity** | Long-term (months / years) | Dynamic / Short-term (minutes / hours) |
    | **Format** | X.509 (`.crt`, `.cer`, `.pem`) | JWT, SAML, Opaque String |
    | **Verification Method** | Certificate chain validation against CA (Public Key) | Local signature and validity check |

* **Recovery Key (PRK / IRK):** When FileVault encryption is enabled, a backup recovery key is generated to recover data in the event of lost user login credentials.
  * **PRK - Personal Recovery Key:** An alphanumeric key presented to the end user for safe keeping or saved to iCloud (in Tahoe, automatic iCloud backup is often offered for personal setups).
  * **IRK - Institutional Recovery Key:** Legacy institutional master key managed via MDM payload allowing IT administrators to unlock drives. Modern best practice relies on escrowing individual PRKs via MDM.
* **VEK (Volume Encryption Key) & KEK (Key Encryption Key):** VEK is the hardware encryption key stored in the Secure Enclave. KEK is the key derived from the user's login password, used to "wrap" the VEK and unwrap it upon boot.
* **Virtualization (Exclaves):** In macOS 26 Tahoe, FileVault encryption is supported in virtual machines via Exclave technology simulating the Secure Enclave.
* **SSH Pre-boot:** macOS 26 Tahoe introduces remote SSH access during Pre-boot phase to unlock FileVault on headless servers.

**FileVault Version History Overview:**

| FileVault Version | Release Year (OS) | Encryption Scheme | Key Characteristics |
|---|---|---|---|
| FileVault 1 | 2003 (Panther 10.3) | Disk Image File (DMG) | Encrypted user Home directory only; fragile and vulnerable to extraction tools (e.g., VileFault). |
| FileVault 2 | 2011 (Lion 10.7) | Software via CPU | Full Disk Encryption (FDE); caused minor CPU overhead and slight performance impact. |
| Modern | 2017+ (T2 / Apple Silicon) | Hardware (AES Engine & Secure Enclave) | Zero performance impact; hardware-level key wrapping architecture. |

---

### Terminal Commands (CLI) for Encryption and Token Management

Management of Secure Tokens and FileVault relies primarily on `sysadminctl` and `fdesetup`. These core utilities are essential for macOS system administrators.

#### Secure Token Management via `sysadminctl`

* **Check Secure Token status for the current user:**

  ```bash
  sysadminctl -secureTokenStatus $USER
  ```

* **Check Secure Token status for a specific user (e.g., `johndoe`):**

  ```bash
  sysadminctl -secureTokenStatus johndoe
  ```

* **Grant Secure Token to another user account:** (Requires an existing admin account with Secure Token)
  ```bash
  sysadminctl -secureTokenOn newuser -password newuserpass -adminUser adminname -adminPassword adminpass
  ```

* **Remove Secure Token from a user:** (Caution: Removing Secure Tokens from all accounts will block critical system permissions!)
  ```bash
  sysadminctl -secureTokenOff otheruser -password userpass -adminUser adminname -adminPassword adminpass
  ```

#### FileVault Management via `fdesetup`

* **Check FileVault status (active/inactive and encryption state):**

  ```bash
  fdesetup status
  ```

* **Enable FileVault via Terminal (for the current user):**

  ```bash
  sudo fdesetup enable
  ```
  *(Prompts for credentials and outputs a Personal Recovery Key to stdout).*

* **Disable FileVault encryption (decrypt volume):**

  ```bash
  sudo fdesetup disable
  ```

* **List user accounts authorized to unlock the drive at boot:**

  ```bash
  sudo fdesetup list
  ```

* **Remove a specific user (e.g., `johndoe`) from FileVault access:**

  ```bash
  sudo fdesetup remove -user johndoe
  ```

* **Rotate Personal Recovery Key (PRK) and generate a new key:**

  ```bash
  sudo fdesetup changerecovery -personal
  ```

* **Synchronize FileVault user keys (checks for out-of-sync credentials):**

  ```bash
  sudo fdesetup sync
  ```

* **Enable FileVault silently via input plist (ideal for MDM scripting):**

  ```bash
  sudo fdesetup enable -inputplist < /path/to/fdesetup.plist
  ```

#### Advanced Cryptographic Diagnostics with `diskutil` & `profiles`

* **List all cryptographic users for the APFS Data Container:**

  ```bash
  diskutil apfs listcryptousers /
  ```
  *(Displays UUIDs of cryptographic entities capable of decrypting the volume, including user accounts, PRK, or IRK).*

* **Check Bootstrap Token status with MDM server:**

  ```bash
  sudo profiles status -type bootstraptoken
  ```
  *(Positive output such as `profiles: Bootstrap Token supported on server` or `escrowed to server` indicates the token is safely stored on MDM for future token delegation).*

* **Force escrow of Bootstrap Token to MDM:**
  ```bash
  sudo profiles install -type bootstraptoken
  ```

---

### Troubleshooting and Quick Solutions

1. **Issue:** "User missing authorization privileges" – A secondary local admin account was created, but cannot approve macOS updates on Apple Silicon or turn off FileVault.
   * **Solution:** The user lacks a Secure Token and consequently lacks Volume Ownership. Verify using `sysadminctl -secureTokenStatus`. If missing, log in as the original admin (created via Setup Assistant) and grant a token using `sysadminctl -secureTokenOn`.

2. **Issue:** Rotating a compromised Recovery Key across an enterprise fleet.
   * **Solution:** Execute `sudo fdesetup changerecovery -personal` locally or push a re-escrow profile via MDM to force PRK regeneration and server backup.

3. **Issue:** FileVault is enabled, but a newly created local user (in an unmanaged environment without Bootstrap Token) does not appear on the login screen after a restart.
   * **Solution:** Only accounts holding a Secure Token and listed in `fdesetup list` can pass Preboot Authentication before the OS loads. Log in as primary admin, grant Secure Token via `sysadminctl`, and confirm addition to `fdesetup list`.

4. **Issue:** Password was changed externally/out-of-band, and FileVault still requires the old password at boot.
   * **Solution:** The KEK remains wrapped with the old password. The user must perform a standard password update via System Settings to re-key and synchronize the Secure Enclave.

---

## Recommended Reading & Links

* [Use secure token, bootstrap token, and volume ownership in deployments](https://support.apple.com/guide/deployment/use-secure-token-bootstrap-token-and-volume-dep24dbdcf9e/web) - Technical IT guide on enterprise encryption authentication.
* [Intro to FileVault for Mac](https://support.apple.com/guide/security/intro-to-filevault-secd73eaebd1/web) - In-depth security architecture breakdown for Apple Silicon encryption.
* [Manage FileVault with mobile device management](https://support.apple.com/guide/deployment/manage-filevault-with-device-management-depf2a6327b/web) - IT documentation on managing enterprise FileVault recovery keys.
* [Protect data on your Mac with FileVault](https://support.apple.com/en-us/HT204837) - Basic end-user instructions for enabling FileVault data protection.

## Summary Video

<!-- Summary Video from YouTube -->
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

<!-- src_hash: 43cdd177f578d063a1e5e118677149d2ea1e0c4cd0d20797fd2234c5c0e5be0c -->
