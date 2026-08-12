# Lesson 13: The Boot Process
**Part D: Hands-On Lab**

## Objective
This lab focuses on understanding the Apple Silicon boot architecture. We will enter the macOS Recovery environment, utilize the Startup Security Utility to downgrade the security policy to Reduced Security (simulating the prerequisite for installing Kexts), and then activate the Share Disk feature (also known as Mac Sharing Mode) to access the Mac's data from another computer. Finally, we will verify the system protections via the graphical interface.

### Prerequisites

- 2 Apple Silicon-based Macs (one will act as the Host entering Recovery, and the other as the Client for remote access).
- A functional USB-C to USB-C or Thunderbolt 3/4 cable.
- An account with Admin privileges on both computers.

---

## Exercise 1: Accessing Recovery and Modifying Security Policy (Startup Security Utility)

**What you will learn:** How to access the modern 1TR (One True Recovery) environment and modify the security policy of the startup disk to permit external system extensions.

**1. Shut Down and Boot to Startup Options:**

1. Ensure the Host Mac is completely powered off via the Apple Menu ( > Shut Down).
2. Press and hold the power button (Touch ID) continuously without releasing it.
3. Keep holding until you see the message "Loading startup options…" underneath the Apple logo.
4. When the Startup Options screen appears, click the gear icon (Options) and click **Continue**.

**2. User Authentication in Recovery:**

1. On the authentication screen, select your Admin user from the list.
2. Enter the account password and click **Continue**.

**3. Accessing the Startup Security Utility:**

1. In the top Menu Bar, click the **Utilities** menu and select **Startup Security Utility**.
2. In the window that opens, select your system drive (typically "Macintosh HD").
3. Click the **Security Policy...** button in the bottom right corner.

**4. Downgrading to Reduced Security:**

1. Change the radio button selection from **Full Security** (the default) to **Reduced Security**.
2. Check the first box to allow Kext management:
   `Allow user management of kernel extensions from identified developers`
3. Click **OK**.
4. The system will prompt you to enter the Admin password again to authorize this critical Firmware modification. Enter it and confirm.
5. Wait a few seconds for the policy to apply, then close the Startup Security Utility window by pressing Command + Q.

---

## Exercise 2: Simulating Share Disk (Mac Sharing Mode)

**What you will learn:** How to share the startup disk for direct access over a physical connection to extract data or perform diagnostics. This effectively replaces the legacy Target Disk Mode from Intel-based Macs.

**1. Enabling Sharing from the Mac in Recovery:**

1. While still inside the macOS Recovery environment, navigate back to the top Menu Bar.
2. Click **Utilities** and select **Share Disk**.
3. In the window that appears, select the volume you wish to share (Macintosh HD).
4. Click **Start Sharing**.
5. A screen will now display indicating the Mac is sharing its disk and awaiting a physical connection.

**2. Connecting to the Disk via the Second Mac (Client):**

1. Connect the two computers using the USB-C or Thunderbolt cable.
2. On the second Mac (which is powered on and running standard macOS), open a **Finder** window.
3. In the Sidebar, under the **Locations** or **Network** category, locate the sharing Mac's name and click it.
4. In the top right corner of the window, click the **Connect As...** button.
5. Select **Registered User** and enter the Admin username and password of the *sharing* Mac (the Host).
6. Click **Connect**.
7. The first Mac's Macintosh HD volume will now mount, allowing you to browse files, backup crucial data, or diagnose disk issues.

**3. Terminating the Share and Returning to Normal:**

1. On the second Mac, click the Eject icon next to the shared drive in Finder.
2. Disconnect the cable between the computers.
3. On the first Mac, click the **Stop Sharing** button to exit the disk sharing mode.
4. From the top Apple menu (), select **Restart** to boot the computer back into macOS.

---

## Exercise 3: Verifying System Protections via GUI

**What you will learn:** How to verify the security level and active extensions within the OS after booting. Now that we've downgraded the security and restarted, let's observe how the system reports this state.

**1. Opening System Information:**

1. On the first Mac (now running macOS normally), click the Apple menu () while holding down the **Option** (⌥) key. The "About This Mac" option will transform into **System Information...**.
2. Click **System Information...** to launch the diagnostic tool.

**2. Checking SIP (System Integrity Protection) Status:**

1. In the left sidebar of the System Information tool, click the **Software** category.
2. In the right pane, locate the **System Integrity Protection** row.
3. Verify that the status is listed as `Enabled`.
   > [!NOTE]
   > Downgrading to Reduced Security does not disable SIP. System Integrity Protection remains active, but we are simply permitting specific "exceptions" for Kexts.

**3. Inspecting Loaded Kernel Extensions (Extensions):**

1. In the same sidebar, under **Software**, click **Extensions**. (Wait a few seconds for the list to populate).
2. Here you can view all system extensions and sort them by columns (such as 'Loaded' to see what is currently running on the system).
3. If you were required to approve a new Kext, this approval would take place via **System Settings > Privacy & Security**.

> [!TIP]
> **Best Practice:** At the conclusion of this lab, it is highly recommended to repeat the steps from Exercise 1 and revert the security policy in the Startup Security Utility back to **Full Security** to properly secure the Mac.

---

### Enterprise Seasoning - MDM Environment Expectations

* **Recovery Lock:** In strictly managed environments, an MDM administrator can deploy a profile that enables Recovery Lock. This means the end-user will be halted even before the Options screen and required to enter an admin password (or an MDM escrowed key) just to load Recovery, preventing them from altering Startup Security or sharing their disk without IT authorization.
* **Enterprise Kext Lockdown:** In the enterprise, modern policy typically dictates avoiding Reduced Security entirely. Rather than end-users approving Kexts manually, the MDM system can deploy Kext approvals (via Team ID) silently in the background—or ideally—force software vendors to utilize modern System Extensions that run safely in User Space instead of Kernel Space.

---

## Bonus Exercise for IT Pros: The Command Line (Terminal)

If you'd like to verify the status of extension policies and system protections directly from the command line (as SysAdmins often do to rapidly gather telemetry across fleets or via MDM), you can use the Terminal:

1. Open the **Terminal** app.
2. To check the user consent policy status for Kernel Extensions:
   ```bash
   spctl kext-consent status
   ```
   > The expected output is `Kernel Extension User Consent: ENABLED`, verifying that we permitted the installation of Kexts from identified developers within the Startup Security Utility.

3. To check the System Integrity Protection (SIP) status:
   ```bash
   csrutil status
   ```
   > The output should confirm that SIP is `enabled`, demonstrating that Reduced Security does not fully disable it.
