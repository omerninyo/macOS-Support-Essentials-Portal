# Lesson 04: Encryption and Keys
**Student Reference Guide**

## Lesson Objectives

* Data Encryption
* Modern Permission Management
* Enterprise Solutions

---

## 🎧 Listen to the Summary — Before or After Class

<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/f51cfe24-e5d0-4d6c-ab56-8bbb41c1cc26/"></iframe></div>

---

## System Ownership & FileVault

This document consolidates all core concepts, workflows, and tools relevant to Lesson 4, which covers Secure Tokens, the FileVault encryption framework, and Bootstrap Token mechanisms in enterprise deployment environments.

### Glossary and Core Concepts

* **Secure Token:** A cryptographic chain (wrapped in the user's password) that allows a local macOS account to gain cryptographic "ownership" of the Data Volume. It authorizes mission-critical tasks like enabling FileVault or authorizing software updates on Apple Silicon Macs. The first user created via the Setup Assistant automatically receives this token.
* **FileVault:** The built-in macOS encryption framework that fully encrypts the Data Volume using XTS-AES-128. On Apple Silicon Macs, data is inherently hardware-encrypted at all times. Enabling FileVault essentially "wraps" the existing encryption key with the user's password, adding robust security with zero performance penalty.
* **Volume Ownership:** A mechanism on Apple Silicon Macs requiring specialized permissions to execute system-level tasks such as erasing the Mac, modifying startup security settings, or upgrading macOS. This capability is directly derived from users possessing a Secure Token.
* **Bootstrap Token:** A temporary, enterprise-grade "master key" escrowed to the MDM server during the enrollment process. Held securely in the MDM (escrow process), this token can automatically grant a Secure Token to subsequently logging-in standard users or cloud identities (like Managed Apple Accounts - MAIDs) without requiring the original admin's credentials.

> [!TIP]
> **Decoding Tokens and Certificates in the Enterprise**
> The macOS ecosystem and Apple management frameworks utilize various tokens and certificates. Here is a definitive guide to the common terminology:
> 
> * **APNs Certificate / Token:** Secures and authenticates the encrypted communication channel between your MDM, Apple's servers, and the devices.
> * **Service Token:** Authenticates the MDM server against **Apple Business Manager (ABM)**.
> * **Content Token:** Authenticates the MDM server against the Apps & Books (VPP) library.
> * **Secure Token:** A local cryptographic token on macOS that permits a user to unlock a FileVault-encrypted disk.
> * **Bootstrap Token:** An institutional token allowing the MDM to transparently grant a Secure Token to end-users without their direct involvement.

* **Recovery Key (PRK/IRK):** When FileVault encryption is turned on, a fallback key is generated to safeguard data in the event of a lost login password.
  * **PRK - Personal Recovery Key:** An alphanumeric string presented to the user to store safely, or alternatively, escrowed to their iCloud account.
  * **IRK - Institutional Recovery Key:** An enterprise key leveraged via MDM, ensuring that only IT administrators can unlock restricted drives using a specialized payload (the modern standard heavily favors MDM-escrowed PRKs).
* **VEK (Volume Encryption Key) & KEK (Key Encryption Key):** The VEK is the hardware encryption key secured within the Secure Enclave. The KEK is the key derived from your user password, used to "wrap" the VEK and unlock it during the boot process.
* **Virtualization (Exclaves):** In macOS 26 Tahoe, FileVault encryption is now fully supported in virtual machines thanks to the Exclave technology, which simulates a Secure Enclave.
* **SSH Pre-boot:** macOS 26 Tahoe introduced the capability to connect remotely via SSH to headless servers during the Pre-boot phase to unlock FileVault.

---

### Massive CLI Reference for Encryption and Token Management

> [!NOTE]
> **Leveraging the Terminal for Encryption Management**
> Managing the Secure Token architecture and FileVault is predominantly handled using the `sysadminctl` and `fdesetup` binaries. These are essential tools for macOS system administrators, but memorizing them is not required at this stage of the course. Feel free to copy and paste them during the lab. We will dive deep into the command-line interface in Lesson 08.

#### Managing Secure Tokens via `sysadminctl`

* **Check Secure Token status for the current user:**
  ```bash
  sysadminctl -secureTokenStatus $USER
  ```
* **Check status for a specific user (e.g., `johndoe`):**
  ```bash
  sysadminctl -secureTokenStatus johndoe
  ```
* **Grant a Secure Token to another user:** (Requires an admin user who already possesses a Secure Token)
  ```bash
  sysadminctl -secureTokenOn newuser -password newuserpass -adminUser adminname -adminPassword adminpass
  ```
* **Revoke a Secure Token from a user:** (Caution - removing the token from all users can lock the Mac out of critical permissions!)
  ```bash
  sysadminctl -secureTokenOff otheruser -password userpass -adminUser adminname -adminPassword adminpass
  ```

#### Managing FileVault via `fdesetup`

* **Check FileVault status (Enabled/Disabled and who is encrypting the Volume):**
  ```bash
  fdesetup status
  ```
* **Enable FileVault via Terminal (for the current user):**
  ```bash
  sudo fdesetup enable
  ```
  *(The system will prompt for a password and output a Personal Recovery Key to the terminal).*
* **Disable and remove encryption (Volume Decryption):**
  ```bash
  sudo fdesetup disable
  ```
* **List authorized users capable of unlocking encryption at boot:**
  ```bash
  sudo fdesetup list
  ```
* **Remove a specific user (e.g., `johndoe`) from the authorized unlock list:**
  ```bash
  sudo fdesetup remove -user johndoe
  ```
* **Rotate the Personal Recovery Key (PRK) and generate a new one:**
  ```bash
  sudo fdesetup changerecovery -personal
  ```
* **Force a FileVault sync (verify if a refresh is needed for changed keys or passwords):**
  ```bash
  sudo fdesetup sync
  ```
* **Enable encryption silently using a Plist file (Ideal for MDM deployments - requires admin rights and XML configuration):**
  ```bash
  sudo fdesetup enable -inputplist < /path/to/fdesetup.plist
  ```

#### Advanced Cryptographic Diagnostics with `diskutil` and `profiles`

* **Display all Cryptographic Users for the APFS Data Container:**
  ```bash
  diskutil apfs listcryptousers /
  ```
  *(Outputs the UUID of every cryptographic entity capable of decrypting the Data Volume, including users with a token, PRK, or IRK).*

* **Verify the Bootstrap Token status against the MDM server:**
  ```bash
  sudo profiles status -type bootstraptoken
  ```
  *(A positive response, such as `profiles: Bootstrap Token supported on server` or `escrowed to server`, indicates the token is successfully securely stored on the server, ready to grant future Secure Tokens).*

* **Force push the Bootstrap Token to the management server:**
  ```bash
  sudo profiles install -type bootstraptoken
  ```

---

### Troubleshooting & Quick Fixes (Cheat Codes)

1. **Issue:** "Missing user privileges" – You provisioned a new Local Account (Admin), but it cannot authorize macOS updates on an Apple Silicon Mac or disable FileVault.
   * **Solution:** The user lacks a Secure Token and consequently lacks Volume Ownership. Verify using `sysadminctl -secureTokenStatus`. If missing, leverage the original admin account (the one that went through the Setup Assistant) to grant them a Secure Token via the `sysadminctl -secureTokenOn` command.

2. **Issue:** You need to rotate a Recovery Key that was compromised in the enterprise.
   * **Solution:** Execute `sudo fdesetup changerecovery -personal` (for a personal key), or utilize your MDM platform to issue an `Escrow` command, forcing the generation of a fresh PRK synchronized with your management catalog.

3. **Issue:** FileVault is enabled, but a newly created local user (in an unmanaged non-Bootstrap Token environment) does not appear on the Login Window after a reboot.
   * **Solution:** Only users possessing a Secure Token and appearing on the `fdesetup list` can bypass the Pre-boot Authentication phase that runs on the bare metal before the OS loads. Log in with the primary user, provision the new user using `sysadminctl`, and verify they are added to the cryptographic list.

4. **Issue:** A password was changed outside the Mac environment, and now the legacy password is required to unlock FileVault.
   * **Solution:** The KEK is still protected by the legacy password. The user must seamlessly update their password through System Settings to resync the key within the Secure Enclave.

---

## Recommended Links & Further Reading

* [Use secure token, bootstrap token, and volume ownership in deployments](https://support.apple.com/guide/deployment/use-secure-token-bootstrap-token-and-volume-dep24dbdcf9e/web) - Technical article for IT admins.
* [Intro to FileVault for Mac](https://support.apple.com/guide/security/intro-to-filevault-secd73eaebd1/web) - In-depth overview of the encryption architecture on Apple Silicon.
* [Manage FileVault with mobile device management](https://support.apple.com/guide/deployment/manage-filevault-with-device-management-depf2a6327b/web) - Guide on managing enterprise recovery keys.
* [Protect data on your Mac with FileVault](https://support.apple.com/en-us/HT204837) - Basic end-user guide on enabling encryption.

---

## 🎬 Summary Video

<!-- Summary Video from YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/i7byyZYgNUY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

## 💡 Presentation Visuals

> [!NOTE]
> These images can be projected in class when explaining the topic, or integrated into slide decks.

!!! tip "Visual Demonstration (Student Aid)"
    These screenshots illustrate the GUI or underlying mechanism relevant to the lesson's topic.

![Disk_image_performance_the_cost_of_encryption_rise_p2_28](../assets/images/Lesson_04/L04_DeepDive_Disk_image_performance_the_cost_of_encryption_rise_p2_28.png)
![Slide100_image109](../assets/images/Lesson_04/L04_LegacySlide_Slide100_image109.png)
![Slide100_image110](../assets/images/Lesson_04/L04_LegacySlide_Slide100_image110.png)
![Slide101_image111](../assets/images/Lesson_04/L04_LegacySlide_Slide101_image111.png)
![Slide101_image112](../assets/images/Lesson_04/L04_LegacySlide_Slide101_image112.png)
![Slide70_image84](../assets/images/Lesson_04/L04_LegacySlide_Slide70_image84.png)
![Slide70_image85](../assets/images/Lesson_04/L04_LegacySlide_Slide70_image85.png)
![Slide94_image102](../assets/images/Lesson_04/L04_LegacySlide_Slide94_image102.png)
![Slide94_image103](../assets/images/Lesson_04/L04_LegacySlide_Slide94_image103.png)
