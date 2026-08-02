# Lesson 04: Encryption and Keys
**Hands-On Lab (Student Practice)**

## Objective
Practical experience in managing System Ownership and Secure Tokens via the graphical interface, understanding their connection to the FileVault encryption mechanism, enabling FileVault, and creating/managing a Recovery Key.

## Scenario
As part of the enterprise IT department, you must ensure that users on the computer have received System Ownership via a Secure Token. Afterward, you must enable encryption on the Data Volume and generate a Personal Recovery Key (PRK) to prevent data loss in case of a forgotten password. Everything will be done using macOS's built-in graphical tools.

## Prerequisites

* An Apple Silicon-based Mac.
* A Local Account with Administrator privileges.
* It is recommended to connect laptops to a power source during encryption changes.
* *Note: As per course rules, any destructive or formatting labs must be performed on the provided external USB Drive, but enabling FileVault on the primary drive is permitted for this exercise as it does not destroy data.*

---

### Part 1: Checking System Ownership (Secure Token Status) via GUI
Before FileVault can be enabled, the system requires verification that the user has a Secure Token. The Directory Utility allows us to check this visually.

1. Open the **Directory Utility** (find it via Spotlight, or navigate to `/System/Library/CoreServices/Applications/`).
2. Click the lock icon in the corner and enter your administrator password to allow changes.
3. In the top toolbar, switch to the **Directory Editor** tab.
4. Ensure the "Viewing" dropdown is set to **Users** and that you are reading from the local node.
5. Find your username in the left list and click it.
6. In the Attributes list on the right, look for an attribute named **AuthenticationAuthority**.
7. Inside its Value field, look for the string `SecureToken`. Its presence indicates that this user holds a security token and can manage encryption.

### Part 2: Checking Hardware Encryption Status
On Apple Silicon Macs, the hardware AES engine encrypts data 24/7 even before FileVault is enabled. Let's verify this.

1. Open the **Disk Utility** application (from the Utilities folder or via Spotlight).
2. In the sidebar, select your Mac's Data Volume (usually named `Macintosh HD - Data`).
3. Look below the Volume name in the main pane.
4. Note that the format displayed is `APFS (Encrypted)`. This means the volume is already hardware-encrypted and ready to be wrapped by FileVault without waiting for data encryption.

### Part 3: Enabling FileVault via System Settings
Now we will officially enable data protection.

1. Open **System Settings** and navigate to **Privacy & Security**.
2. Scroll down to the **FileVault** section.
3. Click the **Turn On** button.
4. You will be prompted to enter an administrator password to confirm.
5. In the pop-up window, you will be asked how you want to recover access if you forget your password. Choose the option to create a local recovery key (Create a recovery key and do not use my iCloud account).
   *Note: In macOS Tahoe, if you are signed in with an Apple Account and iCloud Keychain is active, the system might default to iCloud recovery automatically. For this lab, make sure to select the local PRK option.*
6. The system will present you with the Personal Recovery Key (PRK). You must copy or write it down carefully in a secure external location. **Do not save the recovery key in a text file on this computer!**
7. Click **Continue**. Encryption will be configured and activated almost instantly.

### Part 4: Managing Authorized Users for Decryption
After enabling FileVault, you must check which users can unlock the disk at boot.

1. Stay in the **FileVault** window under `Privacy & Security`.
2. If there are other users on the computer who are not currently authorized, an **Options** button or a list of users will appear under the status.
3. Clicking this button will show you the users on the system for whom you can enable disk unlock capabilities (which requires entering the password of a user with a Secure Token).

### Part 5: Using the Recovery Key (Simulation Scenario)
In this part, we will test whether the PRK we created allows us to recover data in an emergency.

1. Restart your Mac.
2. At the Login Window, which now acts as the Pre-boot decryption screen for the encrypted Data Volume, enter an incorrect password 3 consecutive times, or click the question mark (?) icon next to the password field.
3. The system will offer you to unlock the encryption using a Recovery Key. Click the option to enter a key.
4. Type the Personal Recovery Key (PRK) you generated in Part 3. Ensure absolute accuracy (including letters and dashes).
5. If entered correctly, FileVault will unlock, and you will be given the option to reset your local account password or just continue directly into the system.

---

## Extra / Technical Deep Dive

Behind the scenes of the graphical interface we just explored, there are several powerful Command Line Interface (CLI) tools used by network administrators, MDM servers, and automation scripts. Open the **Terminal** app and try running these commands:

* **Checking Secure Token Status:**
  Instead of digging through Directory Utility, you can ask the system for a direct answer regarding System Ownership:
  `sysadminctl -secureTokenStatus username` (Replace `username` with your short name). If it returns `ENABLED`, it means you have System Ownership.

* **Checking FileVault Status:**
  You can check the system encryption status with one quick command:
  `fdesetup status`

* **Checking Bootstrap Token Status:**
  To see if the Mac communicated with an MDM server and escrowed a Bootstrap Token (which allows automatic granting of Secure Tokens to new employees), use:
  `sudo profiles status -type bootstraptoken` (This requires your admin password).
