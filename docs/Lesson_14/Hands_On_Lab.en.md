# Lesson 14: Recovery and Erase Environment
**Hands-on Lab (Student Practice)**

---

## Exercise 1: Booting to 1TR (Apple Silicon) and Recovery (Intel)

**Objective:** To understand the differences in accessing the recovery environment based on processor architecture.

### Part A: Entering 1TR on an Apple Silicon Mac

1.  Ensure your Mac is completely shut down (Apple menu > Shut Down).
2.  Press and hold the Power/Touch ID button continuously.
3.  Continue holding even when the Apple logo appears, until you see **Loading startup options** on the screen.
4.  On the options screen that appears, note the new **3D SSD** icon for the recovery disk (a new feature in macOS 26 Tahoe).
5.  Click the gear icon (Options) and then click **Continue**.
6.  Select an Admin user from the list and enter their password to unlock the Recovery window.
7.  You are now in the Apple Silicon 1TR environment. Note the main window containing the available graphical tools. This environment runs from a completely separate, erase-resistant volume.

### Part B: Entering Recovery on an Intel-based Mac (for comparison/familiarization)

1.  Ensure your Mac is completely shut down.
2.  Press the power button and immediately press and hold the Command and R keys together on the keyboard.
3.  Release the keys when the Apple logo or a globe icon appears (in the case of Internet Recovery).
4.  Enter an administrator password if prompted, until the macOS Utilities window appears, similar to the Apple Silicon version.

---

## Exercise 2: Navigating Disk Utility in Recovery Mode

**Objective:** To familiarize yourself with the disk management tool in Recovery mode and see how the system is structured "under the hood," without performing an actual erase at this stage.

1.  In the main Recovery window, select the **Disk Utility** application and click **Continue**.
2.  In the top menu bar of the application, click the **View** button and select **Show All Devices**.
3.  Examine the hierarchy in the sidebar: note the physical disk at the top of the list, the Container above it, and the various Volumes within it (with emphasis on Macintosh HD and Macintosh HD - Data).
4.  Click on Macintosh HD, then click the **First Aid** button at the top of the window to see the integrity check wizard, but there is no need to run it now.
5.  *Instructor's Note:* In an Apple Silicon environment, you cannot format the entire physical disk at once from this window; you can only erase the system's Volume Group. This ensures that the 1TR environment itself is preserved and not destroyed.
6.  Close Disk Utility (via the top menu Disk Utility > Quit).
7.  Exit Recovery mode by clicking the Apple menu and selecting **Restart** to reboot the Mac back into the regular operating system (macOS).

---

## Exercise 3: Secure and Instant Erase using EACS (Erase All Content and Settings)

**Objective:** To perform a factory reset of the Mac to an Out-of-Box Experience (OOBE) quickly and securely through System Settings, using the encryption key destruction mechanism (Crypto-Erase).

> !!! warning "Warning to Students:"
> This exercise will permanently delete all data, users, and settings from your Mac! Ensure all previous exercises are completed and no important information is unbacked up. Remember to perform this lab on a USB drive if instructed to do so by the instructor.

1.  Start your Mac normally and log in with a Local Admin Account.
2.  Open **System Settings**.
3.  Navigate in the sidebar to **General** > **Transfer or Reset**.
4.  Click the **Erase All Content and Settings** button.
5.  The Erase Assistant tool will request the system administrator (Admin) password – enter it and click Unlock.
6.  The system will display a window detailing everything that is about to be erased (Apple Account, Touch ID fingerprints, linked Bluetooth devices, Wallet data, and more).
7.  Follow the instructions. If you are logged into an Apple Account, you will be prompted to enter a password to sign out (this action disables Activation Lock so the computer does not lock on the next boot).
8.  After signing out, a final red warning screen will appear. Click **Erase All Content and Settings** for final confirmation.
9.  The Mac will restart, the screen will darken, and after a very short time, you will see the "Hello" screen of the Setup Assistant. The cryptographic key was successfully erased (Crypto-Erase), and the system was reset without the need to reinstall the files themselves!

---

## Exercise 4: "Enterprise Flavor" Simulation - Remote Wipe and Activation Lock

**Objective:** To understand what happens when an MDM server intervenes and sends a remote wipe command to a device, and how IT professionals deal with releasing a device locked by Activation Lock by a previous user.

### Part A: Discussion and Scenario - Remote Wipe Command

1.  **Scenario:** The Mac is stolen or lost. The IT administrator logs into the MDM console (e.g., Jamf Pro) and sends a remote wipe command to the device.
2.  **Discussion (What actually happens):** When the command reaches the Mac, it performs exactly the same EACS process we practiced earlier. The Secure Enclave destroys the encryption key, and the information immediately becomes unreadable, with the system resetting immediately afterward.

### Part B: Administrative Activation Lock Release (Bypass Code)

1.  **Scenario:** An employee left the company and left behind a reset Mac. When you first powered on the computer (Setup Assistant), the screen displays a request to enter the previous employee's Apple ID and password.
2.  The Mac is corporately owned and managed by MDM, so the administrative bypass code is backed up on the server.
3.  As an IT professional, you need to access the MDM interface, locate the record of the locked Mac (by serial number), and navigate to the device's security and management tab.
4.  Locate the **Activation Lock Bypass Code** field and copy the 16-character code.
5.  On the locked Mac displaying the login request, do not enter an email address! Instead, click **Recovery Assistant** in the top menu.
6.  Select the option to **Activate with MDM key** or "Enter Code".
7.  Enter the complex 16-character code you copied from the MDM console.
8.  The Mac will immediately unlock against Apple's servers, and you can proceed to set up the computer again from scratch.

---

## Bonus Exercise for IT Professionals: Command Line (Terminal)

As IT professionals, we sometimes need to access more advanced tools that are beneath the surface or when the graphical interface is insufficient. Recovery mode includes access to the Terminal shell, through which important commands can be run for unique cases.

In Recovery mode (after entering 1TR as detailed in Exercise 1), select **Utilities** > **Terminal** from the top menu bar.

### Built-in Password Reset Tool
Sometimes it is necessary to reset a user's password (if we have a Recovery Key or appropriate permissions). Instead of searching for a complicated wizard, we can simply call it from the command line:
```bash
resetpassword
```
This command will automatically launch the graphical Reset Password Assistant interface, where we can select the user and set a new password.

### New Diagnostics in macOS 26 Tahoe
To collect logs and hardware data directly to an external USB drive when the Mac refuses to boot:
```bash
recoverydiagnose
```
The command will create a comprehensive archive for further offline analysis, a new and important tool in Tahoe for diagnosing complex issues.

### Checking System and Recovery Partitions
To see the physical and logical division of all drives, including hidden recovery partitions that do not appear in Disk Utility, run:
```bash
diskutil list
```
In the output, you will notice that the Recovery environment loads a minimal file system from a virtual disk (Ramdisk) and displays many small Volumes required for the Apple Silicon recovery tools to boot.

<!-- src_hash: 550633d5d16bfa29e041e6560305758a5b084e5085d58725ca0374b30f343b8b -->
