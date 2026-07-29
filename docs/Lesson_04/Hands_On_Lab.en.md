# Lesson 04: Encryption and Keys
**Hands-On Lab (Student Exercise)**

## Objective
Hands-on experience in managing system ownership and Secure Token via the graphical interface, understanding its relationship to the FileVault encryption mechanism, enabling FileVault, and creating and managing a Recovery Key.

## Scenario
As part of the corporate IT department, you must ensure that users on the computer have gained system ownership via a Secure Token. Next, you need to enable encryption on the Data Volume, and generate a Personal Recovery Key (PRK) to prevent data lock-in in case of a forgotten password. Everything will be done using macOS's built-in GUI tools.

## Prerequisites

* An Apple Silicon-based Mac computer.
* A Local Account user with Administrator privileges.
* A power connection is recommended for laptops during encryption changes.

---

### Part 1: Checking System Ownership (Secure Token Status) via GUI
Before FileVault can be enabled, the system requires verification that the user has a Secure Token. The Directory Utility tool allows us to visually inspect this.

1. Open the **Directory Utility** (you can find it by searching in Spotlight, or navigating to `/System/Library/CoreServices/Applications/`).
2. Click the padlock icon in the corner and enter your administrator password to allow changes.
3. In the top toolbar, switch to the **Directory Editor** tab.
4. Ensure the Viewing dropdown is set to **Users** and that you are reading from the Local node.
5. Find your username in the left-hand list and click on it.
6. In the Attributes list on the right, look for an attribute named **AuthenticationAuthority**.
7. Within its Value field, locate the string `SecureToken`. Its presence indicates that this user holds a secure token and can manage encryption.

### Part 2: Checking Encryption Status at the Hardware Level
On Apple Silicon Macs, the hardware AES engine encrypts data 24/7 even before FileVault is enabled. We will check this now.

1. Open the **Disk Utility** application (from the Utilities folder or via Spotlight).
2. In the sidebar, select your Mac's Data Volume (usually named `Macintosh HD - Data`).
3. Look below the Volume name in the main pane.
4. Note that the format displayed is `APFS (Encrypted)`. This means the volume is already hardware-encrypted and ready to be wrapped by FileVault without waiting for data encryption itself.

### Part 3: Enabling FileVault via GUI (System Settings)
We will now officially activate the data protection mechanism.

1. Open **System Settings** and navigate to **Privacy & Security**.
2. Scroll down to the **FileVault** area.
3. Click the **Turn On** button.
4. You will be prompted to enter an administrator password for confirmation.
5. In the pop-up window, you will be asked how you want to restore access if you forget your password. Choose to create a local recovery key (Create a recovery key and do not use my iCloud account).
6. The system will display the Personal Recovery Key (PRK) to you. You must carefully copy or write it down in a secure external location. **Do not save the recovery key in a text file on the current computer!**
7. Click **Continue**. The encryption will be configured and enabled almost immediately.

### Part 4: Managing Users Authorized to Decrypt
After enabling FileVault, you should check which users can unlock the disk at startup.

1. Remain in the **FileVault** window under `Privacy & Security`.
2. If there are other users on the computer who are not currently authorized, an additional button will appear under the status named **Options** or a list of users.
3. Clicking this button will show you the users in the system for whom the drive unlock capability can be enabled (which requires entering the password of the user holding the Secure Token).

### Part 5: Using a Recovery Key (Simulation Scenario)
In this section, we will test whether the Recovery Key (PRK) we generated allows us to extract data in an emergency.

1. Restart the Mac.
2. At the Login Window, which now acts as the Pre-boot decryption screen of the encrypted Data Volume, enter an incorrect password 3 times in a row, or click the question mark (?) icon appearing next to the password field.
3. The system will offer to unlock the encryption using a Recovery Key. Click the option to enter a key.
4. Type in the Recovery Key (PRK) you generated in Part 3. Ensure absolute accuracy (including letters and hyphens).
5. If entered correctly, the FileVault encryption mechanism will unlock and you will be given the option to reset your local account password or just proceed directly into the system.

---

## Extra Exercise / Technical Tip of the Iceberg

Behind the scenes of the user interface we just explored, there are several powerful command-line interface (CLI) tools used by network administrators, MDM servers, and automation scripts. Open the **Terminal** application and try running the following commands:


* **Checking Secure Token status:**

  Instead of digging through Directory Utility, you can ask the system for a direct answer regarding system ownership:
  `sysadminctl -secureTokenStatus username` (replace `username` with your short username). If the system returns `ENABLED`, it means you have system ownership.

* **Checking FileVault status:**

  You can check the system encryption status in one quick command:
  `fdesetup status`

* **Checking Bootstrap Token status:**

  To check if the Mac communicated with a management server (MDM) and deposited (Escrowed) a Bootstrap Token that enables automatic Secure Tokens granting for new employees, you can use the command:
  `sudo profiles status -type bootstraptoken` (this action will require typing an admin password).

<!-- src_hash: 5a60911f6cdfe3374a246e96cae7e2da44c1dc7f7c7da51da76cdf0053337e06 -->

