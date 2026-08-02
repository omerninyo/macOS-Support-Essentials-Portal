# Lesson 02: User Management and Data Security
**Hands-On Lab (Student Practice)**

## Lab 1: Passwordless Security (Passkeys) and the Passwords App

**Lab Objective:**
Hands-on experience creating a Passkey against a remote server, understanding the authentication process using the Secure Enclave, and reviewing the outcome in the macOS secrets management app.

**Prerequisites:**
* A Mac computer running macOS 26 (Tahoe) or later.
* A configured fingerprint reader (Touch ID), or use of the computer password.

**Lab Steps:**

### Part A: Creating the Passkey
1. Open the Safari browser on your Mac.
2. Navigate to the lab website: [https://webauthn.io/](https://webauthn.io/).
3. In the **Username** box, choose a unique username (e.g., `OmerAppleClass123`).
4. Ensure the Attestation type is set to `None` and click **Register**.
5. macOS will detect the registration request and pop up a prompt.
6. Verify your identity by touching **Touch ID** (or entering the computer password).
7. Upon successful authentication, the Secure Enclave generates a cryptographic key pair and securely stores the private key.

### Part B: Passwordless Authentication
1. Now, back on the [webauthn.io](https://webauthn.io/) page, scroll up and click the **Authenticate** button.
2. A Safari window will pop up asking "Do you want to use your Passkey?".
3. Touch **Touch ID** again.
4. You have successfully logged in without needing to type a password!

### Part C: Viewing Secrets in the Passwords App
1. Open Spotlight (Command + Space) and type **Passwords**. Press Enter.
2. Authenticate with Touch ID to open it.
3. In the sidebar, select the **Passkeys** category.
4. In the list, find the entry for `webauthn.io`.
5. Click on it. Notice that there is no textual password displayed; instead, it explicitly states that this is a hardware-based Passkey.

### Part D: Privacy Security with TCC (Bonus Lab)
**Lab Objective:** To see the Transparency, Consent, and Control mechanism in action.
1. Open the **Terminal** app.
2. Type the command `ls ~/Desktop` and press Enter.
3. An OS prompt will likely pop up asking you to allow Terminal to access files in your Desktop folder.
4. If you click **Don't Allow**, you will see an `Operation not permitted` error in Terminal - even though in terms of POSIX permissions, you own the folder!
5. To fix this, go to **System Settings** -> **Privacy & Security** -> **Files and Folders** (or **Full Disk Access**) and grant Terminal the required permission.
