# Lesson 14: Recovery and Erase Environment
**Hands-On Lab (Student Exercise)**

---

## Exercise 1: Booting into 1TR (Apple Silicon) and Recovery (Intel)

**Objective:** To understand the differences in entering the recovery environment depending on the processor architecture.

### Part A: Entering 1TR on an Apple Silicon Mac

1. Ensure the Mac is completely shut down (Apple menu > Shut Down).
2. Press and hold the power button (Power/Touch ID) continuously.
3. Continue to hold even when the Apple logo appears, until you see the text **Loading startup options** on the screen.
4. On the options screen that appears, click the gear icon (Options) and then click **Continue**.
5. Select an administrator (Admin) user from the list and enter their password to unlock the Recovery window.
6. You are now in the 1TR environment of Apple Silicon. Notice the main window containing the available graphical tools. This environment runs from a completely separate volume that is immune to erasure.

### Part B: Entering Recovery on an Intel-based Mac (For Comparison/Familiarity)

1. Ensure the Mac is completely shut down.
2. Press the power button and immediately after, press and hold the Command and R keys together on the keyboard.
3. Release the keys when the Apple logo or a globe icon (in the case of Internet Recovery) appears.
4. Enter an administrator password if prompted, until the macOS Utilities window appears, similar to that of Apple Silicon.

---

## Exercise 2: Navigating Disk Utility in Recovery Mode

**Objective:** To become familiar with the disk management tool in Recovery mode and see how the system is built "under the hood", without actually performing a wipe at this stage.

1. In the main Recovery window, select the **Disk Utility** app and click **Continue**.
2. In the app's top menu bar, click the **View** button and select **Show All Devices**.
3. Examine the hierarchy in the sidebar: note the physical disk at the top of the list, the Container above it, and the different Volumes inside it (with an emphasis on Macintosh HD and Macintosh HD - Data).
4. Click on Macintosh HD, and then click the **First Aid** button at the top of the window to see the health check wizard, but there is no need to run it now.
5. *Instructor Note:* In the Apple Silicon environment, you cannot format the entire physical disk all at once from this window, but only erase the system's Volume Group. This ensures that the 1TR environment itself will be preserved and not destroyed.
6. Close Disk Utility (via the top menu Disk Utility > Quit).
7. Exit recovery mode by clicking on the Apple menu and selecting **Restart** to reboot the Mac back into the normal operating system (macOS).

---

## Exercise 3: Secure and Instant Erasure using EACS (Erase All Content and Settings)

**Objective:** To reset the Mac to an out-of-the-box experience (OOBE) state quickly and safely via System Settings, using the encryption key destruction mechanism (Crypto-Erase).

> **Warning to Students:** This exercise will permanently delete all data, users, and settings from your Mac! Ensure that all previous exercises have been completed and there is no important data that is unbacked up.

1. Boot the Mac normally and log in with an Admin Local Account.
2. Open **System Settings**.
3. Navigate in the sidebar to **General** > **Transfer or Reset**.
4. Click the **Erase All Content and Settings** button.
5. The Erase Assistant tool will ask for the administrator (Admin) password - enter it and click Unlock.
6. The system will present a window detailing everything about to be erased (Apple Account, Touch ID fingerprints, paired Bluetooth devices, wallet data, and more).
7. Follow the instructions. If you are signed in with an Apple Account, you will be asked to enter a password to sign out (this action disables the Activation Lock so the computer will not be locked on the next boot).
8. After signing out, a final red warning screen will appear. Click **Erase All Content and Settings** to confirm.
9. The Mac will restart, the screen will go black, and after a very short time, you will see the "Hello" screen of the Setup Assistant. The cryptographic key erasure (Crypto-Erase) was performed successfully, and the system was reset without needing to reinstall the files themselves!

---

## Exercise 4: Simulating "Enterprise Seasoning" - Remote Wipe and Activation Lock

**Objective:** To understand what happens when the MDM server intervenes and sends a remote wipe command to a device, and how IT personnel deal with releasing a device locked with Activation Lock by a previous user.

### Part A: Discussion and Scenario - Remote Wipe Command

1. **Scenario:** The Mac was stolen or lost. The IT admin logs into the MDM console (e.g., Jamf Pro) and sends a remote wipe command to the device.
2. **Discussion (What actually happens):** When the command reaches the Mac, it performs the exact same EACS process we practiced earlier. The Secure Enclave destroys the encryption key, the data instantly becomes unreadable, and the system resets immediately afterward.

### Part B: Administrative Activation Lock Bypass (Bypass Code)

1. **Scenario:** An employee left the company and left behind a wiped Mac. When you turned on the computer for the first time (Setup Assistant), the screen shows a prompt to enter the previous employee's Apple ID and password.
2. The Mac is corporate-owned and managed in an MDM, so the administrative bypass code is backed up on the server.
3. As an IT person, you must access the MDM interface, locate the record of the locked Mac (by serial number), and navigate to the security and management tab of the device.
4. Find the **Activation Lock Bypass Code** field and copy the 16-character code.
5. On the locked Mac displaying the login prompt, do not enter an email address! Instead, click on the top menu on **Recovery Assistant**.
6. Select the option to **Activate with MDM key** or "Enter code".
7. Enter the complex 16-character code you copied from the MDM console.
8. The Mac will immediately release the lock against Apple's servers, and you will be able to continue setting up the computer from scratch.

---

## Extra Exercise / Technical Tip of the Iceberg

As IT professionals, we will sometimes need to access more advanced tools located under the surface or when the graphical interface is insufficient. Recovery mode includes access to the Terminal shell, through which important commands can be executed for unique cases.

In Recovery mode (after entering 1TR as detailed in Exercise 1), select from the top menu bar **Utilities** > **Terminal**.

### Built-in Password Reset Tool
Sometimes we are required to reset a user password (provided we have a Recovery Key or appropriate permissions). Instead of looking for a complex wizard, we can simply call it from the command line:
```bash
resetpassword
```
This command will automatically pop up the Reset Password Assistant graphical interface, where we can select the user and set a new password.

### Checking System and Recovery Partitions
To see the physical and logical layout of all drives including hidden recovery partitions that do not appear in Disk Utility, run:
```bash
diskutil list
```
In the output, you will notice that the Recovery environment loads a minimal file system from a virtual disk (Ramdisk) and displays a large number of small Volumes needed to boot Apple Silicon recovery tools.


<!-- src_hash: 14bd3e12fe5c318ffee393a1d106156e7c7884e12f2af7e4e5f1481955121aee -->

