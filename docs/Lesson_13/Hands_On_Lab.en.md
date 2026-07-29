# Lesson 13: The Boot Process
**Hands-on Lab (Student Exercise)**

## Hands-on Lab (Practical Exercise): Exploring Boot Modes, Startup Security, and Drive Sharing

### Objective
This exercise will focus on understanding the architecture of Apple Silicon computers at the Boot level. We will enter the macOS Recovery environment, use the Startup Security Utility to lower the security level to Reduced Security (to allow Kexts installation in the future), and then enable the Share Disk feature (also known as Mac Sharing Mode) to access the Mac's information from another computer. Finally, we will verify the system's protections through the graphical interface.

### Prerequisites

- 2 Apple Silicon-based Mac computers (one computer will serve as the Host entering Recovery, and the other as the Client for remote access).
- A functional USB-C to USB-C cable or Thunderbolt 3/4 cable.
- An account with Admin privileges on both computers.

---

### Part 1: Entering Recovery and Changing Security Policy (Startup Security Utility)

**1. Shut Down and Boot into Startup Options:**

1.  Ensure the computer (the Host) is completely shut down from the Apple Menu (Apple Menu > Shut Down).
2.  Press and hold the power button (Touch ID) continuously without releasing.
3.  Continue holding until you see the message "Loading startup options…" below the Apple logo.
4.  When the Startup Options screen appears, select the gear icon (Options) and click **Continue**.

**2. User Authentication in Recovery:**

1.  On the authentication screen, select your Admin user from the list.
2.  Enter the account password and click **Continue**.

**3. Accessing Startup Security Utility:**

1.  In the top menu bar, click the **Utilities** menu and select **Startup Security Utility**.
2.  In the window that opens, select your system drive (usually "Macintosh HD").
3.  Click the **Security Policy...** button in the bottom right corner.

**4. Switching to Reduced Security Mode:**

1.  Change the radio selection from **Full Security** (the default) to **Reduced Security**.
2.  Check the first checkbox that allows Kexts management:
    `Allow user management of kernel extensions from identified developers`

3.  Click **OK**.
4.  The system will ask you to re-enter the Admin password to confirm the critical Firmware change. Enter it and confirm.
5.  Wait a few seconds for the policy to be applied, then close the Startup Security Utility window by pressing Command + Q.

---

### Part 2: Simulating Drive Sharing (Share Disk / Mac Sharing Mode)

This mode effectively replaces the Target Disk Mode functionality familiar from older Intel Macs.

**1. Enabling Sharing from the Mac in Recovery:**

1.  While still in the macOS Recovery environment, access the top menu bar again.
2.  Click **Utilities** and select the **Share Disk** option.
3.  In the window that appears, select the drive you wish to share (Macintosh HD).
4.  Click **Start Sharing**.
5.  A screen will now be displayed indicating that the computer is sharing the drive and awaiting a physical connection.

**2. Connecting to the Drive via the Second Mac (Client):**

1.  Connect both computers using the USB-C or Thunderbolt cable.
2.  On the second Mac (which is powered on and active in the regular operating system), open a **Finder** window.
3.  In the sidebar, under the **Locations** or **Network** category, locate the name of the sharing Mac and click on it.
4.  In the top right corner of the window, click the **Connect As...** button.
5.  Select **Registered User** and enter the username and Admin password of the *sharing* Mac (the Host).
6.  Click **Connect**.
7.  The Macintosh HD drive of the first Mac will now appear, and you can browse files, copy important information, or diagnose disk issues.

**3. Ending Sharing and Returning to Normal Operation:**

1.  On the second Mac, click the Eject icon next to the shared drive in Finder.
2.  Disconnect the connection cable between the computers.
3.  On the first Mac, click the **Stop Sharing** button to end drive sharing mode.
4.  From the top Apple menu (), select **Restart** to reboot the computer into macOS.

---

### Part 3: Verifying System Protection Status via the Graphical Interface

Now, after lowering the security level and restarting the computer, we will check how the system reports this.

**1. Opening System Information:**

1.  On the first Mac (which is now running normally in macOS), click the Apple menu () while holding the **Option** (⌥) key on the keyboard. The "About This Mac" option will change to **System Information...**.
2.  Click **System Information...** to open the diagnostic tool.

**2. Checking SIP (System Integrity Protection) Status:**

1.  In the left sidebar of the System Information tool, click the **Software** category.
2.  In the right pane, look for the **System Integrity Protection** row.
3.  Ensure the status is indicated as `Enabled`.
    *(Important Note: Lowering the security level to Reduced Security does not disable SIP. System protection remains active, but we allow specific "exceptions" for Kexts).*

**3. Checking Existing Kernel Extensions (Extensions):**

1.  In the same sidebar, under **Software**, click **Extensions**. (Wait a few seconds for the list to load).
2.  Here you can see all system extensions and sort them by columns (such as 'Loaded' to see what is currently running on the system).
3.  If a new Kext needed to be approved, this approval would be done via **System Settings > Privacy & Security**.

!!! tip Attention (Best Practice):
    Upon completion of the entire exercise, it is recommended to repeat the steps in Part 1 and revert the security policy in Startup Security Utility back to **Full Security** to protect the Mac.

---

### Enterprise Seasoning - Expectations in an MDM Environment

*   **Recovery Lock:** In strict organizations, the MDM administrator can deploy a profile that enables Recovery Lock. This means the user will be stopped before the Options screen and required to enter an administrator password (or a key generated by the MDM) to load Recovery, preventing them from changing Startup Security or sharing their disk without IT approval.
*   **Enterprise Kext Locking:** In an organization, the current policy is often to completely avoid lowering security. Instead of end-users manually approving Kexts, the MDM system seamlessly distributes Kext approvals (via Team ID) in the background, or even better – compels software vendors to use modern System Extensions that run in User Space rather than Kernel Space.

---

## Extra Exercise / Technical Iceberg Tip

If you wish to verify the status of extension policies and system protections directly from the command line (as system administrators often do to quickly gather information on servers or via MDM), you can use Terminal:

1.  Open the **Terminal** application.
2.  To check the status of user kernel extension consent policy:
    ```bash
    spctl kext-consent status
    ```
    *The expected output is `Kernel Extension User Consent: ENABLED`, indicating that we have allowed Kexts installation from identified developers in Startup Security Utility.*

3.  To check the status of SIP (System Integrity Protection):
    ```bash
    csrutil status
    ```
    *The output should confirm that SIP is enabled (`enabled`), as Reduced Security does not completely disable it.*

<!-- src_hash: 878dcad7740b1184446e6d83e05e88d357092e143a28701d0f33744329284a7a -->


!!! tip "Visual Aids (Student Guide)"
    These images illustrate the relevant interface or mechanism for this lesson.

![Slide138_image169](../assets/images/Lesson_13/L13_LegacySlide_Slide138_image169.png)
![Slide138_image49](../assets/images/Lesson_13/L13_LegacySlide_Slide138_image49.jpeg)
![Slide141_image170](../assets/images/Lesson_13/L13_LegacySlide_Slide141_image170.jpg)
![Slide142_image171](../assets/images/Lesson_13/L13_LegacySlide_Slide142_image171.png)
![Slide142_image172](../assets/images/Lesson_13/L13_LegacySlide_Slide142_image172.png)
![Slide142_image173](../assets/images/Lesson_13/L13_LegacySlide_Slide142_image173.png)
![Slide142_image174](../assets/images/Lesson_13/L13_LegacySlide_Slide142_image174.png)
![Slide142_image175](../assets/images/Lesson_13/L13_LegacySlide_Slide142_image175.png)
![Slide142_image176](../assets/images/Lesson_13/L13_LegacySlide_Slide142_image176.png)
![Slide142_image177](../assets/images/Lesson_13/L13_LegacySlide_Slide142_image177.jpg)
![Slide80_image19](../assets/images/Lesson_13/L13_LegacySlide_Slide80_image19.jpg)
![Slide80_image93](../assets/images/Lesson_13/L13_LegacySlide_Slide80_image93.png)
![26-Tahoe-Boot-Camp-scaled](../assets/images/Lesson_13/L13_TahoeUI_26-Tahoe-Boot-Camp-scaled.png)
