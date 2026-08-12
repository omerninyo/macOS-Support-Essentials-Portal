# Lesson 04: Encryption and Keys
**Hands-On Lab (Student Exercise)**

## Objective
Gain practical, hands-on experience managing System Ownership and Secure Tokens via the Graphical User Interface (GUI). You will understand their relationship to the FileVault encryption framework, actively provision FileVault, and generate and manage a Personal Recovery Key (PRK).

## Scenario
As a systems engineer in the enterprise IT department, you must verify that the local user has successfully acquired System Ownership via a Secure Token. Next, you are tasked with enabling FileVault encryption on the Data Volume and generating a Personal Recovery Key (PRK) to prevent catastrophic data loss in the event of a forgotten password. All workflows will be executed utilizing macOS's built-in GUI utilities.

## Prerequisites

* An Apple Silicon-based Mac.
* A Local Account with Administrator privileges.
* It is highly recommended to connect portable Macs to a power source during encryption changes.

> [!CAUTION]
> As per the course guidelines, destructive labs must be performed on your provisioned external USB drive. However, this specific exercise for enabling FileVault is safe to execute on your internal system drive, as it does not compromise data integrity.

---

## Exercise 1: Verifying System Ownership (Secure Token Status) via GUI

> **Key Takeaway:** Confirming whether our account holds the cryptographic "master key" (Secure Token) required to manage disk encryption.

Before FileVault can be enabled, macOS requires verification that the user possesses a Secure Token. The Directory Utility provides a visual method to audit this status.

1. Launch the **Directory Utility** application (Search via Spotlight, or navigate directly to `/System/Library/CoreServices/Applications/`).
2. Click the padlock icon in the corner and authenticate with your administrator password to unlock changes.
3. On the top toolbar, select the **Directory Editor** tab.
4. Ensure the `Viewing` dropdown menu is set to **Users** and that you are querying the local node (`Local`).
5. Locate your specific username in the left-hand column and select it.
6. In the Attributes list on the right, look for an attribute named **AuthenticationAuthority**.
7. Within its Value field, identify the `SecureToken` string. Its presence mathematically guarantees that this user holds a security token and is authorized to manage encryption.

---

## Exercise 2: Auditing Hardware-Level Encryption Status

> **Key Takeaway:** Proving via Disk Utility that our data is encrypted at the bare-metal hardware level, even when the FileVault mechanism appears "Off" in System Settings!

On Apple Silicon Macs, the hardware AES engine continuously encrypts data 24/7, prior to FileVault even being enabled. Let's verify this architecture.

1. Open the **Disk Utility** application (from the Utilities folder or via Spotlight).
2. In the sidebar, select your Mac's Data Volume (typically named `Macintosh HD - Data`).
3. Inspect the information directly under the Volume name in the center pane.
4. Note that the displayed format is `APFS (Encrypted)`. This confirms that the volume is already hardware-encrypted and primed to be "wrapped" by FileVault, requiring zero wait time for actual data encryption.

---

## Exercise 3: Enabling FileVault via the User Interface (System Settings)

> **Key Takeaway:** Fully provisioning the enterprise encryption framework and generating the mission-critical recovery key.

We will now officially activate the data protection mechanism.

1. Open **System Settings** and navigate to **Privacy & Security**.
2. Scroll down to the **FileVault** section.
3. Click the **Turn On** button.
4. Authenticate with your administrator password when prompted.
5. A dialog will ask how you wish to unlock your disk if you forget your password. Select the option to generate a local PRK (Create a recovery key and do not use my iCloud account).

   > [!NOTE]
   > In macOS Tahoe, if you are signed in to an Apple Account with iCloud Keychain enabled, the system might automatically default to iCloud escrow. For the purpose of this enterprise lab, ensure you strictly select the local PRK generation option.

6. The system will display your Personal Recovery Key (PRK). You must carefully transcribe or copy it to a secure, external location. **Never save the recovery key in a plaintext file on the local machine!**
7. Click **Continue**. The encryption framework will be provisioned and activated almost instantaneously.

---

## Exercise 4: Managing Authorized Decryption Users

> **Key Takeaway:** Understanding how granting decryption authorization to another user requires authentication from a user who already possesses a Secure Token.

Following FileVault activation, it's crucial to audit which users are authorized to unlock the disk at boot.

1. Remain in the **FileVault** pane under `Privacy & Security`.
2. If there are other users on the Mac who are not currently authorized, an **Options** button or a list of users will be visible below the FileVault status.
3. Clicking this button will display the system users who can be granted the capability to unlock the drive (this action will prompt for the password of the user holding the Secure Token).

---

## Exercise 5: Utilizing the Recovery Key (Simulation Scenario)

> **Key Takeaway:** Simulating an emergency lockout and executing a practical recovery using the PRK generated earlier.

In this phase, we will validate whether our generated PRK successfully allows data extraction in a crisis scenario.

1. Execute a Restart on your Mac.
2. At the Login Window, which now acts as the Pre-boot decryption screen for the encrypted Data Volume, intentionally enter an incorrect password 3 consecutive times, or click the question mark (?) icon next to the password field.
3. The system will prompt you to unlock the encryption using a Recovery Key. Select the option to enter the key.
4. Input the Personal Recovery Key (PRK) you generated in Exercise 3. Ensure absolute precision (including case sensitivity and hyphens).
5. Upon successful validation, the FileVault encryption will be unlocked, and you will be presented with the option to reset your local account password or seamlessly bypass it to enter the OS.

---

## IT Pro Bonus Lab: The Command Line (Terminal)

> [!NOTE]
> **No Need to Memorize!**
> Behind the scenes of the GUI we just explored, robust command-line binaries operate—the same tools leveraged by automated MDM servers. Feel free to copy and paste these into the Terminal application for hands-on experimentation, but note that we will formally master the CLI in Lesson 08.

* **Audit Secure Token Status:**
  Instead of digging through Directory Utility, you can query the system for a direct response regarding System Ownership:
  `sysadminctl -secureTokenStatus username` (replace `username` with your short name). An `ENABLED` response confirms you hold System Ownership.

* **Audit FileVault Status:**
  You can instantly check the system encryption status with a single command:
  `fdesetup status`

* **Audit Bootstrap Token Status:**
  To verify if the Mac has communicated with an MDM server and escrowed a Bootstrap Token (which enables automated Secure Token grants for newly provisioned employees), execute:
  `sudo profiles status -type bootstraptoken` (This action requires administrator authentication).
