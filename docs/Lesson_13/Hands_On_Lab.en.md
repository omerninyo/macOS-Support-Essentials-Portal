# Lesson 13: The Boot Process
**Part D: Hands-On Lab (vEXP)**

## Hands-On Lab: Exploring Boot Modes, Startup Security, and Disk Sharing

### Objective
This lab will focus on understanding the architecture of Apple Silicon Macs at the Boot level. We will enter the macOS Recovery environment, use the Startup Security Utility to lower the security level to Reduced Security (to allow future Kext installations), and then enable the Share Disk feature (also known as Mac Sharing Mode) to access the Mac's data from another computer. Finally, we will verify the system protections via the GUI.

### Prerequisites

- 2 Apple Silicon based Macs (one will act as the Host entering Recovery, and the other as the Client for remote access).
- A working USB-C to USB-C or Thunderbolt 3/4 cable.
- An account with Admin privileges on both computers.

---

### Part 1: Entering Recovery and Changing Security Policy (Startup Security Utility)

**1. Shut Down and Boot into Startup Options:**

1. Ensure the computer (the Host) is completely shut down from the Apple Menu (Apple Menu > Shut Down).
2. Press and continuously hold the power button (Touch ID) without letting go.
3. Keep holding until you see the message "Loading startup options…" beneath the Apple logo.
4. When the Startup Options screen appears, select the gear icon (Options) and click **Continue**.

**2. User Authentication in Recovery:**

1. On the authentication screen, select your Admin user from the list.
2. Type the account password and click **Continue**.

**3. Accessing Startup Security Utility:**

1. From the top Menu Bar, click on the **Utilities** menu and select **Startup Security Utility**.
2. In the window that opens, select your system drive (usually "Macintosh HD").
3. Click the **Security Policy...** button in the bottom right corner.

**4. Switching to Reduced Security Mode:**

1. Change the radio button from **Full Security** (default) to **Reduced Security**.
2. Check the first checkbox that allows Kext management:
   `Allow user management of kernel extensions from identified developers`
3. Click **OK**.
4. The system will prompt you to enter the Admin password again to authorize this critical Firmware change. Enter and confirm it.
5. Wait a few seconds for the policy to apply, then close the Startup Security Utility window by pressing Command + Q.

---

### Part 2: Simulating Disk Sharing (Share Disk / Mac Sharing Mode)

This mode effectively replaces the Target Disk Mode functionality known from older Intel Macs.

**1. Enabling Sharing from the Mac in Recovery:**

1. While still inside the macOS Recovery environment, go to the top Menu Bar again.
2. Click on **Utilities** and select **Share Disk**.
3. In the window that appears, select the drive you want to share (Macintosh HD).
4. Click **Start Sharing**.
5. A screen will now display indicating the computer is sharing the drive and waiting for a physical connection.

**2. Connecting to the Drive from the Second Mac (Client):**

1. Connect the two computers using the USB-C or Thunderbolt cable.
2. On the second Mac (which is powered on and active in standard macOS), open a **Finder** window.
3. In the Sidebar, under the **Locations** or **Network** category, locate the sharing Mac's name and click it.
4. In the top right corner of the window, click the **Connect As...** button.
5. Choose **Registered User** and enter the Admin username and password of the *sharing* Mac (the Host).
6. Click **Connect**.
7. The Macintosh HD drive of the first Mac will now mount, and you can browse files, copy important data, or diagnose disk issues.

**3. Ending Sharing and Returning to Normal:**

1. On the second Mac, click the Eject icon next to the shared drive in Finder.
2. Disconnect the connection cable between the computers.
3. On the first Mac, click the **Stop Sharing** button to end disk sharing mode.
4. From the top Apple menu (), select **Restart** to reboot the computer into macOS.

---

### Part 3: Verifying System Protections Status via GUI

Now, after lowering the security level and restarting the computer, we will check how the system reports this.

**1. Opening System Information:**

1. On the first Mac (now running normally in macOS), click the Apple menu () while holding the **Option** (⌥) key on the keyboard. The "About This Mac" option will change to **System Information...**.
2. Click **System Information...** to open the diagnostic tool.

**2. Checking SIP (System Integrity Protection) Status:**

1. In the left sidebar of the System Information tool, click the **Software** category.
2. In the right pane, look for the **System Integrity Protection** row.
3. Ensure the status is listed as `Enabled`.
   *(Important note: Lowering the security level to Reduced Security does not turn off SIP. System protection remains active, but we allow specific "exceptions" for Kexts).*

**3. Checking Existing Kernel Extensions:**

1. In the same sidebar, under **Software**, click **Extensions**. (Wait a few seconds for the list to load).
2. Here you can see all system extensions and sort them by columns (such as 'Loaded' to see what is currently running on the system).
3. If it were necessary to approve a new Kext, this approval would take place via **System Settings > Privacy & Security**.

> **Note (Best Practice):** At the end of the entire lab, it is recommended to repeat the steps in Part 1 and restore the security policy in the Startup Security Utility back to **Full Security** to protect the Mac.

---

### Enterprise Seasoning - MDM Environment Expectations

* **Recovery Lock:** In strict organizations, the MDM admin can send a profile that enables Recovery Lock. This means the user will be stopped even before the Options screen and will be required to enter an admin password (or a key generated by the MDM) to load Recovery, preventing them from changing Startup Security or sharing their disk without IT approval.
* **Enterprise Kext Locking:** In an organization, current policy is usually to avoid lowering Security entirely. Instead of the end-user manually approving Kexts, the MDM system seamlessly deploys Kext approvals (using the Team ID) in the background, or better yet – forces software vendors to use modern System Extensions that run in User Space instead of Kernel Space.

---

## Extra Lab / Technical Deep Dive

If you want to verify the status of the extensions policy and system protections directly from the command line (as sysadmins often do to quickly gather information on servers or via MDM), you can use the Terminal:

1. Open the **Terminal** app.
2. To check the user's kernel extension consent policy status:
   ```bash
   spctl kext-consent status
   ```
   *The expected output is `Kernel Extension User Consent: ENABLED`, indicating we allowed installing Kexts from identified developers in the Startup Security Utility.*

3. To check the SIP (System Integrity Protection) status:
   ```bash
   csrutil status
   ```
   *The output should confirm that SIP is `enabled`, as Reduced Security does not completely disable it.*
