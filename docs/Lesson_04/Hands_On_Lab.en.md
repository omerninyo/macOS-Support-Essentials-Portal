# Lesson 04: Encryption and Keys
**Hands-On Lab (Student Exercise)**

## Objective
Hands-on experience managing System Ownership and Secure Token status via the graphical user interface, understanding its relationship to the FileVault encryption mechanism, enabling FileVault, and generating and managing a Recovery Key.

## Scenario
As part of the enterprise IT department, you must verify that system users possess Volume Ownership via a Secure Token. Next, you must enable encryption on the Data Volume and generate a Personal Recovery Key (PRK) to prevent data lockout in the event of a forgotten password. All operations will be conducted using native macOS GUI tools.

## Prerequisites

* Apple Silicon Mac.
* Local Account with Administrator privileges.
* Power adapter connection recommended for laptops during encryption state changes.
* *Note: In accordance with course guidelines, destructive labs (formatting, etc.) must be performed on the provided external USB flash drive. However, enabling FileVault on the primary system volume is permitted for this exercise as it preserves user data.*

---

## Exercise 1: Verifying System Ownership (Secure Token Status) via GUI
Before FileVault can be enabled, the system requires verification that the target account holds a Secure Token. Directory Utility allows us to inspect this visually.

1. Launch **Directory Utility** (located via Spotlight search or navigating to `/System/Library/CoreServices/Applications/`).
2. Click the lock icon in the lower corner and enter your administrator password to authenticate for editing.
3. In the top toolbar, select the **Directory Editor** tab.
4. Ensure the Viewing drop-down menu is set to **Users** and that you are querying the local node (Local).
5. Locate your user account in the left sidebar and select it.
6. In the right attribute pane, search for the attribute named **AuthenticationAuthority**.
7. Inspect the Value field for the string `SecureToken`. Its presence confirms that the user holds a Secure Token and can manage encryption policies.

## Exercise 2: Inspecting Hardware-Level Encryption State
On Apple Silicon Macs, the hardware AES engine encrypts volume data 24/7 prior to FileVault activation. We will verify this state now.

1. Launch **Disk Utility** (located in `/Applications/Utilities` or via Spotlight).
2. In the sidebar, select your Mac's Data Volume (typically named `Macintosh HD - Data`).
3. Inspect the information pane below the volume name.
4. Note that the format displays `APFS (Encrypted)`. This confirms that hardware-level encryption is active and ready for FileVault wrapping without requiring lengthy volume encryption passes.

## Exercise 3: Enabling FileVault via User Interface (System Settings)
We will now formally enable full-disk protection.

1. Open **System Settings** and navigate to **Privacy & Security**.
2. Scroll down to the **FileVault** section.
3. Click **Turn On**.
4. Enter administrator credentials when prompted for authorization.
5. In the pop-up wizard, select your preferred recovery method. Choose the option to generate a local recovery key (Create a recovery key and do not use my iCloud account).
   *Note: In macOS Tahoe, if authenticated with an Apple Account with iCloud Keychain enabled, the system may default to iCloud escrow. For this lab, ensure you select generating a local PRK.*

6. The system will present your Personal Recovery Key (PRK). Carefully copy or record it in a secure external location. **Do not save the recovery key in a plain text file on this Mac!**
7. Click **Continue**. FileVault configuration will finalize almost instantaneously.

## Exercise 4: Managing Accounts Authorized for Decryption
Following FileVault activation, verify which user accounts are authorized to unlock the disk during boot.

1. Remain in **System Settings -> Privacy & Security -> FileVault**.
2. If additional local user accounts are present on the system that are not yet authorized, an **Options** button or user list will appear under the status pane.
3. Selecting this option displays system accounts that can be authorized for Pre-boot unlocking (requiring authentication from an existing Secure Token holder).

## Exercise 5: Utilizing a Recovery Key (Simulation Scenario)
In this exercise, we will test whether our Personal Recovery Key (PRK) allows emergency data recovery.

1. Restart your Mac (**Restart**).
2. At the login window (acting as the Pre-boot decryption interface for the encrypted Data Volume), enter an incorrect password 3 consecutive times, or click the question mark icon (?) adjacent to the password field.
3. The system will present an option to unlock encryption using a Recovery Key. Select the option to enter your key.
4. Type the Personal Recovery Key (PRK) generated in Exercise 3. Ensure exact precision (including letters and hyphens).
5. Upon successful entry, FileVault will unlock the volume, granting access to reset your local account password or proceed into the system.

---

## Bonus Exercise for IT Professionals: Command Line Interface (CLI)

Behind the GUI tools we explored, powerful CLI commands drive automated enterprise workflows and MDM policies. Launch **Terminal** and test the following commands:


* **Querying Secure Token Status:**

  Instead of searching Directory Utility, query system ownership directly:
  `sysadminctl -secureTokenStatus username` (replace `username` with your short username). A response of `ENABLED` confirms system ownership.

* **Querying FileVault Status:**

  Inspect system encryption state in a single command:
  `fdesetup status`

* **Querying Bootstrap Token Status:**

  Verify if the Mac has escrowed a Bootstrap Token with the MDM server to enable automatic Secure Token issuance for new enterprise users:
  `sudo profiles status -type bootstraptoken` (requires administrator password).

<!-- src_hash: 97a60107816ee398ca26059621b638caa002d15a58f1ad6ff703df7f90525734 -->
