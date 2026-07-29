# Lesson 02: User Management and Data Security
**Hands-On Lab (Student Exercise)**

## Lab 1: Passwordless Security (Passkeys) and Introduction to the Passwords App

**Lab Objective:**

Hands-on experience creating a completely new Passkey against a remote server, understanding the authentication process using the Secure Enclave, and reviewing the result within macOS's secrets management app.

**Prerequisites:**

* A Mac computer running macOS 15 or later.
* Touch ID configured, or the alternative computer password.

**Lab Steps:**

### Part A: Creating the Passkey

1. Open the Safari browser on your computer.
2. Navigate to the lab site (a public testing environment by FIDO developers): [https://webauthn.io/](https://webauthn.io/).
3. In the **Username** box, choose a unique username (for example, your name combined with a random number: `OmerAppleClass123`).
4. Ensure the Attestation type is set to `None` (for demonstration purposes) and click the **Register** button.
5. macOS will detect the registration request and pop up a dialog box. The dialog will ask if you want to create a Passkey for this user.
6. Authenticate your identity using **Touch ID** (or entering the local computer password).
7. After authentication, you will see a successful login message on the site. In the background, your Mac's Secure Enclave generated a cryptographic key pair and saved the private key in iCloud Keychain without exposing it to the network.

### Part B: Passwordless Authentication

1. Now, on the same [webauthn.io](https://webauthn.io/) page, scroll back up and click the **Authenticate** button (after making sure your username is still registered in the box).
2. A Safari window will pop up asking "Do you want to use your Passkey?".
3. Touch **Touch ID** again.
4. You have immediately logged into the site, without typing a password and without the possibility of forgetting it (Passwordless Sign-In).

### Part C: Viewing Secrets in the Passwords App

1. Open Spotlight (Command + Space shortcut) and type **Passwords**. Press Enter to open the app.
2. Authenticate your identity with Touch ID to unlock the built-in secrets manager.
3. In the Sidebar, select the **Passkeys** category.
4. In the list, find the entry for `webauthn.io`.
5. Click on it. Note that there is no visible "password" (because it does not exist as plain, exposed text), but it explicitly indicates that it is a Passkey along with its creation date.

<!-- src_hash: a279ee5cc7d6745b4f210a02b7244164447a9e5a4488292ff8d887470bc3a3dd -->


!!! tip "Visual Aids (Student Guide)"
    These images illustrate the relevant interface or mechanism for this lesson.

![Slide87_image22](../assets/images/Lesson_02/L02_LegacySlide_Slide87_image22.jpg)
![Slide87_image23](../assets/images/Lesson_02/L02_LegacySlide_Slide87_image23.jpg)
![Slide89_image24](../assets/images/Lesson_02/L02_LegacySlide_Slide89_image24.jpg)
![Slide90_image25](../assets/images/Lesson_02/L02_LegacySlide_Slide90_image25.jpg)
![Slide91_image26](../assets/images/Lesson_02/L02_LegacySlide_Slide91_image26.jpg)
![26-Tahoe-Fast-User-Lockscreen-scaled](../assets/images/Lesson_02/L02_TahoeUI_26-Tahoe-Fast-User-Lockscreen-scaled.png)
![26-Tahoe-Settings-Lock-Screen-scaled](../assets/images/Lesson_02/L02_TahoeUI_26-Tahoe-Settings-Lock-Screen-scaled.png)
![26-Tahoe-Settings-Touch-ID-scaled](../assets/images/Lesson_02/L02_TahoeUI_26-Tahoe-Settings-Touch-ID-scaled.png)
