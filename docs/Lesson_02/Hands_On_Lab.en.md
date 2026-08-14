# Lesson 02: User Management & Data Security
**Hands-On Lab**

---

## Objective
Gain practical experience creating various local macOS account types and groups, provisioning a Passkey against a remote server, and managing core TCC (Transparency, Consent, and Control) privacy permissions.

## Scenario
As an enterprise IT administrator, you have been tasked with preparing a macOS environment for collaborative workflows in upcoming labs. You need to provision a standard user account, a headless "Sharing Only" account for network services, and bundle them into a local group. Afterward, you will guide a user through generating a Passkey for secure, passwordless authentication.

## Prerequisites
* A Mac running macOS 26 (Tahoe) or later.
* Touch ID configured, or the local administrator password.
* Administrator privileges to authorize system modifications.

---

## Exercise 1: User & Group Management (Environment Prep)

> **What you will learn:** Hands-on experience provisioning the accounts required for future modules, and understanding the architectural difference between a Standard user and a Sharing Only account.

1. Open **System Settings** and navigate to **Users & Groups**.
2. Click **Add Account** and authenticate with your Administrator password (or Touch ID).
3. Create a Standard User:
   * **New Account:** Select `Standard`.
   * **Full Name:** Type `Student`.
   * **Account Name:** Auto-populates as `student`.
   * **Password:** Set a simple password (e.g., `1234`) for lab purposes, then click **Create User**.
4. Click **Add Account** again.
5. Create a Sharing User:
   * **New Account:** Select `Sharing Only`.
   * **Full Name:** Type `GuestShare`.
   * **Account Name:** Auto-populates as `guestshare`.
   * **Password:** Set a simple password and click **Create User**.
6. Next, create a local group: Scroll to the bottom of the Users & Groups window and click **Add Group**.
7. Set the Group Name to `LabUsers` and click **Create Group**.
8. Click the info (i) button next to your newly created `LabUsers` group.
9. In the user list, check the boxes next to `Student` and `GuestShare` to add them to the group. Click **Done**.

!!! note
    A `Sharing Only` account does not receive a Home Folder in `/Users` and cannot log into the macOS desktop. Its sole enterprise purpose is authenticating remote access for services like File Sharing.

---

## Exercise 2: Passwordless Security (Passkeys) & The Passwords App

> **What you will learn:** Experiencing the future of enterprise authentication—generating a Passkey and securely storing it in iCloud Keychain with zero friction and no hardcoded passwords.

1. Open **Safari** on your Mac.
2. Navigate to the demo site: [https://webauthn.io/](https://webauthn.io/).
3. In the **Username** field, enter a unique identifier (e.g., `OmerAppleClass123`).
4. Ensure the Attestation type is set to `None` and click **Register**.
5. macOS will intercept the registration request and present a native system prompt.
6. Authenticate using **Touch ID** (or your Mac's password).
7. Upon authentication, the Secure Enclave generates a cryptographic key pair and securely stores the private key.
8. Now, on the same page, click **Authenticate**. 
9. When Safari prompts "Do you want to use your Passkey?", tap Touch ID again. You have successfully authenticated without typing a password!
10. Open the native **Passwords** app (via Spotlight).
11. In the sidebar, select **Passkeys** and locate the entry for `webauthn.io`. Notice that there is no textual password exposed to the user.

---

## IT Bonus Exercise: Privacy Protections with TCC

> **What you will learn:** Witnessing firsthand how Apple's TCC framework intercepts and blocks basic shell commands, and how to grant explicit administrative authorization via System Settings.

!!! note "Copy-Paste Only!"
    In this bonus exercise, we are using the `ls` Terminal command (which lists directory contents) purely to trigger a real-time system block. There is no need to analyze the syntax right now. We will master the command line in Lesson 08.

1. Launch the **Terminal** app.
2. Type the command `ls ~/Desktop` and press Enter.
3. You will likely encounter a native macOS prompt requesting permission for Terminal to access files in your Desktop folder.
4. If you click **Don't Allow**, Terminal will output an `Operation not permitted` error—even though POSIX permissions dictate that you are the owner of the directory!
5. To resolve this, open **System Settings** -> **Privacy & Security** -> **Files and Folders**, grant Terminal the necessary toggle, and attempt the command again.
