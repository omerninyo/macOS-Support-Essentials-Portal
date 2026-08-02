# Lesson 13: The Boot Process
**Part D: Hands-on Lab - Student Exercise (vEXP)**

## Hands-on Lab (Practical Exercise): Exploring Boot Modes, Startup Security, and Drive Sharing

### Objective
This exercise will focus on understanding the architecture of Apple Silicon Macs at the boot level. We will enter the macOS Recovery environment, use the Startup Security Utility to lower the security level to Reduced Security (to allow Kexts installation in the future), and then enable the Share Disk feature (also known as Mac Sharing Mode) to access the Mac's data from another computer. Finally, we will verify the system protections through the graphical interface.

### Prerequisites

- 2 Apple Silicon-based Mac computers (one computer will serve as the Host to enter Recovery, and the other as the Client for remote access).
- A functional USB-C to USB-C cable or Thunderbolt 3/4 cable.
- An account with Admin privileges on both computers.

---

## Exercise 1: Entering Recovery and Modifying Security Policy (Startup Security Utility)

**1. Shut Down and Boot into Startup Options:**

1. Ensure the computer (the Host) is completely shut down from the Apple Menu (Apple Menu > Shut Down).
2. Press and hold the power button (Touch ID) continuously without releasing.
3. Continue holding until you see the message "Loading startup options…" below the Apple logo.
4. When the Startup Options screen appears, select the gear icon (Options) and click **Continue**.

**2. User Authentication in Recovery:**

1. On the authentication screen, select your Admin user from the list.
2. Enter the password for the account and click **Continue**.

**3. Accessing Startup Security Utility:**

1. In the top menu bar, click the **Utilities** menu and select **Startup Security Utility**.
2. In the window that opens, select your system drive (usually "Macintosh HD").
3. Click the **Security Policy...** button in the bottom right corner.

**4. Switching to Reduced Security Mode:**

1. Change the radio button selection from **Full Security** (the default) to **Reduced Security**.
2. Check the first checkbox that allows Kexts management:
   `Allow user management of kernel extensions from identified developers`

3. Click **OK**.
4. The system will ask you to re-enter your Admin password to confirm the critical firmware change. Enter it and confirm.
5. Wait a few seconds for the policy to be applied, then close the Startup Security Utility window by pressing Command + Q.

---

## Exercise 2: Simulating Drive Sharing (Share Disk / Mac Sharing Mode)

This mode effectively replaces the familiar Target Disk Mode functionality from older Intel Macs.

**1. Activating Sharing from the Mac in Recovery:**

1. While still in the macOS Recovery environment, access the top menu bar again.
2. Click **Utilities** and select the **Share Disk** option.
3. In the window that appears, select the drive you wish to share (Macintosh HD).
4. Click **Start Sharing**.
5. A screen will now be displayed indicating that the computer is sharing the drive and awaiting a physical connection.

**2. Connecting to the Drive via the Second Mac (Client):**

1. Connect the two computers using the USB-C or Thunderbolt cable.
2. On the second Mac (which is powered on and running its regular operating system), open a **Finder** window.
3. In the Sidebar, under the **Locations** or **Network** category, locate the name of the sharing Mac and click on it.
4. In the top right corner of the window, click the **Connect As...** button.
5. Select **Registered User** and enter the username and Admin password of the *sharing* Mac (the Host).
6. Click **Connect**.
7. The Macintosh HD drive of the first Mac will now appear, and you can browse files, copy important data, or diagnose disk issues.

**3. Ending Sharing and Returning to Normal Operation:**

1. On the second Mac, click the Eject symbol next to the shared drive in Finder.
2. Disconnect the cable between the computers.
3. On the first Mac, click the **Stop Sharing** button to end the drive sharing mode.
4. From the top Apple menu (), select **Restart** to restart the computer into macOS.

---

## Exercise 3: Verifying System Protection Status via the Graphical Interface

Now that we have lowered the security level and restarted the computer, we will check how the system reports this.

**1. Opening System Information:**

1. On the first Mac (which is now running normally in macOS), click the Apple menu () while holding down the **Option** (⌥) key on the keyboard. The "About This Mac" option will change to **System Information...**.
2. Click **System Information...** to open the diagnostic tool.

**2. Checking SIP (System Integrity Protection) Status:**

1. In the left sidebar of the System Information tool, click the **Software** category.
2. In the right pane, look for the **System Integrity Protection** row.
3. Verify that the status is listed as `Enabled`.
   *(Important Note: Lowering the security level to Reduced Security does not disable SIP. System protection remains active, but we allow specific "exceptions" for Kexts).*

**3. Checking Existing Kernel Extensions (Extensions):**

1. In the same sidebar, under **Software**, click **Extensions**. (Wait a few seconds for the list to load).
2. Here you can see all system extensions and sort them by columns (such as 'Loaded' to see what is currently running on the system).
3. If a new Kext needed to be approved, this approval would be done through **System Settings > Privacy & Security**.

!!! tip "Please Note (Best Practice):"
    At the end of the entire exercise, it is recommended to repeat the steps from Part 1 and revert the security policy in Startup Security Utility back to **Full Security** to protect your Mac.

---

### Enterprise Seasoning - Expectations in an MDM Environment

*   **Blocking Access to Recovery (Recovery Lock):** In strict organizations, an MDM admin can send a profile that activates Recovery Lock. This means the user will be stopped before the Options screen and required to enter an administrator password (or a key generated by the MDM) to load Recovery, preventing them from changing Startup Security or sharing their disk without IT approval.
*   **Enterprise Kext Locking:** In an organization, the current policy is usually to completely avoid lowering security. Instead of end-users manually approving Kexts, the MDM system distributes Kext approvals (via Team ID) seamlessly in the background, or even better – compels software vendors to use modern System Extensions that run in User Space rather than Kernel Space.

---

## Bonus Exercise for IT Professionals: Command Line (Terminal)

If you wish to verify the status of extension policies and system protections directly from the command line (as system administrators often do to quickly gather information on servers or via MDM), you can use Terminal:

1.  Open the **Terminal** application.
2.  To check the status of user kernel extension consent policy:
    ```bash
    spctl kext-consent status
    ```
    *The expected output is `Kernel Extension User Consent: ENABLED`, which indicates that we have allowed Kexts installation from identified developers in Startup Security Utility.*

3.  To check the status of SIP (System Integrity Protection):
    ```bash
    csrutil status
    ```
    *The output should confirm that SIP is `enabled`, as Reduced Security does not completely disable it.*

<!-- src_hash: 22c9f32fe160efafea67acdc8dcecdbb9568ced93ce5e9a4ab85955f87b32a1b -->
