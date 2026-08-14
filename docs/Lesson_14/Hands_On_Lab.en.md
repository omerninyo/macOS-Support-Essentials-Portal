# Lesson 14: Recovery Environment and Erasure
**Hands-On Lab**

---

## Exercise 1: Booting into 1TR (Apple Silicon) and Recovery (Intel)

**Objective:** Understand the architectural differences when accessing the Recovery environment based on the processor type.

### Part A: Entering 1TR on an Apple Silicon Mac

1. Ensure the Mac is completely powered off (Apple Menu > Shut Down).
2. Press and continuously hold the Power button (Touch ID).
3. Continue holding even when the Apple logo appears, until the screen displays **Loading startup options**.
4. On the options screen, observe the new **3D SSD** icon representing the recovery disk (New in macOS 26 Tahoe).
5. Click on the gear icon (**Options**) and then click **Continue**.
6. Select an Administrator user from the list and enter their password to unlock the Recovery window.
7. You are now inside the Apple Silicon 1TR environment. Note the main window displaying the available GUI tools. This environment runs from an entirely separate volume that is highly resilient to accidental erasures.

### Part B: Entering Recovery on an Intel-based Mac (For Comparison)

1. Ensure the Mac is completely powered off.
2. Press the Power button and immediately press and hold the **Command (⌘)** and **R** keys together.
3. Release the keys when the Apple logo or a spinning globe (for Internet Recovery) appears.
4. Enter an admin password if prompted, until the macOS Utilities window appears (similar to the Apple Silicon experience).

---

## Exercise 2: Navigating Disk Utility in Recovery Mode

**Objective:** Explore the disk management tools in Recovery Mode and visualize the underlying filesystem architecture, without performing an actual erasure at this stage.

1. From the main Recovery window, select the **Disk Utility** application and click **Continue**.
2. In the application's top menu bar, click the **View** button and select **Show All Devices**.
3. Examine the hierarchy in the sidebar: Observe the top-level physical disk, the Container beneath it, and the various Volumes nested within (focusing on `Macintosh HD` and `Macintosh HD - Data`).
4. Select `Macintosh HD`, then click the **First Aid** button at the top of the window to view the health check wizard (there is no need to run it right now).
5. *Instructor Note:* In the Apple Silicon environment, you cannot format the entire physical disk at once from this window; you can only erase the system's Volume Group. This safeguard ensures the 1TR environment itself remains intact.
6. Close Disk Utility (Top menu bar: Disk Utility > Quit).
7. Exit the Recovery environment by clicking the Apple menu and selecting **Restart** to boot the Mac back into the standard operating system (macOS).

---

## Exercise 3: Secure and Immediate Erasure via EACS (Erase All Content and Settings)

**Objective:** Reset the Mac to an Out-Of-Box Experience (OOBE) state rapidly and securely through System Settings, utilizing the Crypto-Erase mechanism.

!!! warning "Student Warning"
    This exercise will permanently wipe all data, users, and settings from your Mac! Ensure all previous exercises are complete and no critical data is left unbacked up. Remember to perform this lab on the external USB drive if instructed by your facilitator.

1. Boot the Mac normally and log in with a Local Admin account.
2. Open **System Settings**.
3. Navigate in the sidebar to **General** > **Transfer or Reset**.
4. Click the **Erase All Content and Settings** button.
5. The Erase Assistant will prompt for the administrator password—enter it and click **Unlock**.
6. The system will display a summary detailing everything scheduled for deletion (Apple Account, Touch ID fingerprints, paired Bluetooth devices, Wallet data, etc.).
7. Follow the on-screen prompts. If logged into an Apple Account, you will be prompted to enter the password to sign out (this disables Activation Lock to prevent the machine from locking upon reboot).
8. Following the sign-out, a final red warning screen will appear. Click **Erase All Content and Settings** to provide final confirmation.
9. The Mac will reboot, the screen will go black, and shortly after, you will be greeted by the Setup Assistant's "Hello" screen. The cryptographic key deletion (Crypto-Erase) was successful, and the system is reset without requiring a full OS reinstallation!

---

## Exercise 4: Enterprise Spice Simulation - Remote Wipe and Activation Lock

**Objective:** Understand the sequence of events when an MDM server dispatches a remote wipe command, and how IT administrators resolve Activation Lock on a device previously provisioned to another user.

### Part A: Discussion and Scenario - Remote Wipe Command

1. **Scenario:** A Mac is reported lost or stolen. The IT administrator logs into the MDM console (e.g., Jamf Pro) and dispatches a remote wipe command to the device.
2. **Discussion (Under the Hood):** Upon receiving the command, the Mac silently executes the exact same EACS process practiced previously. The Secure Enclave shreds the encryption key, rendering the data instantly unreadable, followed by an immediate system reset.

### Part B: Administrative Activation Lock Release (Bypass Code)

1. **Scenario:** An employee departs the organization and leaves behind a wiped Mac. Upon first boot (Setup Assistant), the screen displays a prompt requiring the previous user's Apple ID and password.
2. The Mac is corporate-owned and MDM-enrolled, meaning the administrative Bypass Code is safely escrowed on the server.
3. As an IT administrator, you must access the MDM interface, locate the locked Mac's record (via Serial Number), and navigate to the device's security/management tab.
4. Locate the **Activation Lock Bypass Code** field and copy the 16-character string.
5. On the locked Mac displaying the login prompt, do NOT enter an email address! Instead, click on **Recovery Assistant** in the top menu bar.
6. Select the option to **Activate with MDM key** (or "Enter Code").
7. Enter the complex 16-character code copied from the MDM console.
8. The Mac will instantly authenticate against Apple's servers, release the lock, and allow you to proceed with a fresh provisioning workflow.

---

## Bonus Exercise for IT Admins: The Command Line (Terminal)

As IT professionals, we occasionally need to leverage advanced under-the-hood tools, particularly when the GUI falls short. The Recovery environment includes access to the Terminal shell, allowing us to execute critical commands for unique edge cases.

While in Recovery Mode (after booting into 1TR as detailed in Exercise 1), select **Utilities** > **Terminal** from the top menu bar.

### The Built-In Password Reset Tool
Occasionally, you may need to reset a user password (provided you hold the Recovery Key or appropriate credentials). Instead of navigating complex GUI paths, you can invoke the tool directly via CLI:
```bash
resetpassword
```
This command instantly launches the graphical Reset Password Assistant, allowing you to select the target user and define a new password.

### Advanced Diagnostics in macOS 26 Tahoe
To capture logs and hardware data directly to an external USB drive when a Mac refuses to boot:
```bash
recoverydiagnose
```
This command generates a comprehensive archive for offline analysis—a vital new utility in Tahoe for diagnosing complex system failures.

### Inspecting System and Recovery Partitions
To visualize the physical and logical layout of all drives, including hidden recovery partitions excluded from Disk Utility, run:
```bash
diskutil list
```
In the output, you will observe that the Recovery environment mounts a minimal filesystem from a virtual Ramdisk and exposes multiple small Volumes essential for launching the Apple Silicon recovery toolset.
