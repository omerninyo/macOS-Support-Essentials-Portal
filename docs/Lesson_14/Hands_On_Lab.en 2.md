# Lesson 14: Recovery Environment and Erasure
**Hands-On Lab**

---

## Exercise 1: Booting into 1TR (Apple Silicon) and Recovery (Intel)

**Objective:** Understand the differences in entering the recovery environment depending on the processor architecture.

### Part A: Entering 1TR on an Apple Silicon Mac

1. Ensure the Mac is completely shut down (Apple menu > Shut Down).
2. Press and hold the power button (Touch ID) continuously.
3. Keep holding even when the Apple logo appears, until you see **Loading startup options** on the screen.
4. On the options screen, notice the new **3D SSD icon** for the Recovery disk (introduced in macOS 26 Tahoe).
5. Click on the gear icon (Options) and then click **Continue**.
6. Select an Admin user from the list and enter their password to unlock the Recovery window.
7. You are now in the 1TR environment for Apple Silicon. Note the main window with the available GUI tools. This environment runs from a completely separate, erasure-proof volume.

### Part B: Entering Recovery on an Intel-based Mac (For Comparison/Familiarity)

1. Ensure the Mac is completely shut down.
2. Press the power button and immediately press and hold the Command and R keys on the keyboard together.
3. Release the keys when the Apple logo or a spinning globe (for Internet Recovery) appears.
4. Enter an admin password if prompted, until the macOS Utilities window appears, similar to Apple Silicon.

---

## Exercise 2: Navigating Disk Utility in Recovery Mode

**Objective:** Familiarize yourself with the disk management tools in Recovery mode and see how the system is built "under the hood," without actually erasing anything at this stage.

1. In the main Recovery window, select the **Disk Utility** app and click **Continue**.
2. In the top menu of the app, click the **View** button and select **Show All Devices**.
3. Examine the hierarchy in the sidebar: note the physical disk at the top, the Container below it, and the various Volumes inside (focusing on `Macintosh HD` and `Macintosh HD - Data`).
4. Click on `Macintosh HD`, and then click the **First Aid** button at the top of the window to see the health check wizard, but there is no need to run it now.
5. *Instructor Note:* On Apple Silicon, you cannot format the entire physical disk at once from this window; you can only erase the System Volume Group. This ensures the 1TR environment itself is preserved.
6. Quit Disk Utility (via the top menu `Disk Utility > Quit`).
7. Exit the recovery environment by clicking the Apple menu and selecting **Restart** to boot the Mac back into the standard macOS.

---

## Exercise 3: Secure and Immediate Erasure via EACS (Erase All Content and Settings)

**Objective:** Reset the Mac to an out-of-the-box (OOBE) state quickly and securely via System Settings, using the Crypto-Erase mechanism.

> **Warning for Students:** This exercise will permanently delete all data, users, and settings from your Mac! Ensure all previous exercises are completed and there is no important data left unbacked up. Remember to perform this lab on the external USB drive if instructed by the facilitator.

1. Boot the Mac normally and log in with a Local Admin account.
2. Open **System Settings**.
3. Navigate in the sidebar to **General** > **Transfer or Reset**.
4. Click the **Erase All Content and Settings** button.
5. The Erase Assistant tool will ask for the Administrator password - enter it and click Unlock.
6. The system will display a window detailing everything that is about to be deleted (Apple Account, Touch ID fingerprints, paired Bluetooth devices, wallet data, etc.).
7. Follow the instructions. If you are signed in with an Apple Account, you will be asked to enter a password to sign out (this disables Activation Lock so the Mac won't lock on the next boot).
8. After signing out, a final red warning screen will appear. Click **Erase All Content and Settings** to confirm.
9. The Mac will restart, the screen will go black, and after a very short time, you will see the "Hello" screen of the Setup Assistant. The cryptographic key deletion (Crypto-Erase) was successful, and the system is reset without needing to reinstall the files themselves!

---

## Exercise 4: "Enterprise Seasoning" Simulation - Remote Wipe and Activation Lock

**Objective:** Understand what happens when an MDM server intervenes and sends a remote wipe command, and how IT professionals handle a device locked by Activation Lock from a previous user.

### Part A: Discussion and Scenario - Remote Wipe Command

1. **Scenario:** The Mac is lost or stolen. The IT admin logs into the MDM console (e.g., Jamf Pro) and sends a remote wipe command to the device.
2. **Discussion (What actually happens):** When the command reaches the Mac, it performs exactly the same EACS process we practiced earlier. The Secure Enclave destroys the encryption key, the data instantly becomes unreadable, and the system resets immediately after.

### Part B: Administrative Activation Lock Bypass Code

1. **Scenario:** An employee left the company and left an erased Mac behind. When you first turn on the computer (Setup Assistant), the screen demands the Apple ID and password of the former employee.
2. The Mac is organization-owned and MDM-managed, so the administrative bypass code is backed up on the server.
3. As an IT professional, you must access the MDM interface, locate the locked Mac's record (by Serial Number), and navigate to the security and management tab of the device.
4. Find the **Activation Lock Bypass Code** field and copy the 16-character code.
5. On the locked Mac displaying the login prompt, do NOT enter an email address! Instead, click on **Recovery Assistant** in the top menu.
6. Select the option **Activate with MDM key** or "Enter code".
7. Enter the complex 16-character code you copied from the MDM console.
8. The Mac will immediately release the lock against Apple's servers, and you can continue to set up the computer from scratch.

---

## Extra Exercise / Technical Tip of the Iceberg

As IT professionals, we sometimes need to access advanced tools located under the surface or when the GUI is insufficient. The Recovery mode includes access to the Terminal shell, through which important commands can be run for unique cases.

In Recovery mode (after entering 1TR as detailed in Exercise 1), select **Utilities** > **Terminal** from the top menu bar.

### The Built-in Password Reset Tool
Sometimes we need to reset a user password (provided we have a Recovery Key or appropriate permissions). Instead of searching for a complicated wizard, we can simply call it from the command line:
```bash
resetpassword
```
This command will automatically pop up the Reset Password Assistant (a graphical wizard), where we can select the user and set a new password.

### macOS 26 Tahoe Diagnostics
To generate a comprehensive diagnostic archive straight to an external USB drive for offline analysis by IT or Apple Support:
```bash
recoverydiagnose
```
This tool is new to macOS 26 Tahoe and helps in scenarios where the system is failing to boot and traditional logs are inaccessible.

### Checking System and Recovery Partitions
To see the physical and logical layout of all drives, including the hidden recovery partitions that do not appear in Disk Utility, run:
```bash
diskutil list
```
In the output, you will notice that the Recovery environment loads a minimal file system from a virtual disk (Ramdisk) and displays a large number of small Volumes necessary for booting the Apple Silicon recovery tools.
