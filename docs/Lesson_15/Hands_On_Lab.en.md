# Lesson 15: Diagnostics
**Hands-On Lab (Student Exercise)**

This document contains the practical exercise for Lesson 15. The exercise focuses on troubleshooting isolation methods, booting into Safe Mode, gathering system data in the System Information GUI, and diagnosing managed profiles.

---

## Lab 1: Network Diagnostics using Wireless Diagnostics

**Objective:** Get familiar with the hidden Wireless Diagnostics tool in the operating system to monitor network performance and locate channel conflicts.

### Steps:

1. **Accessing the Hidden Tool:**

   - In the top Menu Bar, hold the `Option` (⌥) key and click the Wi-Fi icon.
   - Note the rich information displayed immediately (IP address, MAC address, signal quality, and transmit rate).
   - From the drop-down menu, select `Open Wireless Diagnostics`.

2. **Bypassing the Setup Assistant:**

   - Upon opening, a "Diagnostics Assistant" will appear designed to generate a long report. **Ignore it**.
   - Leave the assistant window open, but go to the `Window` menu in the top menu bar (the application's Menu Bar).

3. **Performance Monitoring:**

   - From the `Window` menu, select `Performance`.
   - Examine the displayed graphs: Rate, Quality, and Signal.
   - Wait about a minute and observe changes in the graph. This tool is excellent for spotting momentary connection jumps or dropouts.
   - Close the Performance window.

4. **Network and Channel Scanning (Scan):**

   - Return to the `Window` menu and select `Scan`.
   - Click `Scan Now` (or wait for the automatic scan).
   - This window will display all networks in the vicinity (including some that might not appear in the regular menu), which Channels they use, and what the Noise level is on each channel. This is an ideal tool for IT support needing to locate interference caused by overlapping channels.
   - Close the Scan window.

5. **Traffic Capture (Sniffer) – *Demonstration Only*:**
   - From the `Window` menu, select `Sniffer`.
   - Take a look at the option to select a network Channel and bandwidth. Clicking `Start` will disconnect you from the internet and begin capturing packets floating in the air for that channel and save them as a file for analysis. (For this lab, no need to start a capture).

---

## Lab 2: The Isolation Principle and Entering Safe Mode

**Objective:** Isolate system-level issues using Safe Mode, which disables third-party extensions and clears memory Caches.

### Steps:

1. **System Shutdown:**

   - Go to the Apple menu () and select `Shut Down`. Wait for the computer to completely turn off.

2. **Booting in Safe Mode (Apple Silicon):**

   - Press and hold the power button of the Mac. Do not release.
   - Keep holding until you see the `Loading startup options` text on the screen.
   - On the options screen, select (single click) your system drive (usually `Macintosh HD`).
   - Press and hold the `Shift` key on the keyboard.
   - The `Continue` button will now change to `Continue in Safe Mode`. Click it and release the `Shift` key.

3. **Checking the System in Safe Mode:**

   - Log into your user account (Local Account). You might need to enter the password twice.
   - Check the top right corner of the screen (or the login screen) to ensure the red `Safe Boot` text appears. You might also experience sluggish responsiveness or screen flickering – this is normal and is due to the hardware graphic acceleration being disabled.
   - **The Isolation Principle:** This is the time to check if the issue you were experiencing still exists. If the problem disappeared, it is likely caused by LaunchDaemons, LaunchAgents, or other third-party background software that wasn't loaded.

4. **Exiting Safe Mode:**

   - Restart the computer normally (Apple menu > `Restart`).
   - Upon reboot, the system resumes normal operation (the behind-the-scenes disk check and cache clearing sometimes resolve the issue "on their own" even after returning to normal mode).

---

## Lab 3: Investigating the System Using System Information

**Objective:** Gathering comprehensive information about the system using the built-in System Information graphical interface, and exporting data for support purposes.

### Steps:

1. **Opening System Information:**

   - Hold the `Option` (⌥) key on the keyboard, and click the Apple menu () in the top left corner of the screen.
   - Select `System Information...` (This option replaces "About This Mac" when `Option` is held down).

2. **Extracting Hardware Information:**

   - In the opened window, in the Sidebar, select the `Hardware` category.
   - Review details like the processor model (Chip), amount of Memory, and Serial Number.
   - Click the `Storage` sub-category to see a breakdown of available storage space.

3. **Extracting Software Information and Uptime:**

   - In the sidebar, scroll down to the `Software` category and click it.
   - Find your exact macOS version.
   - Look for the `Time since boot` data (Uptime).
   - *Note:* The number of Uptime days is a critical piece of data for isolating resource issues. A Mac with dozens of Uptime days might experience performance problems.

4. **Exporting Data to a Report:**

   - In the top menu bar, click `File` and select `Save...`.
   - Save the report (`.spx` format) in the `Desktop` folder.
   - Navigate to the desktop, double-click the newly created file, and verify that System Information reopens and displays the saved data. This technique is perfect for attaching diagnostic data to support Tickets.

---

## Lab 4: Support in a Managed Environment (Enterprise Seasoning) - Isolating Profiles in GUI

**Objective:** Isolating issues when a management server (MDM) and enforced Configuration Profiles are involved, using the System Settings interface.

### Steps:

1. **Locating Profiles via the Interface (GUI):**

   - Open `System Settings`.
   - Navigate in the sidebar to `Privacy & Security`.
   - Scroll down and click on `Profiles` (If no profiles are installed on this computer, this menu might not appear).
   - Review the installed profiles to understand which settings are enforced (e.g., VPN agent, content filter, USB restrictions).

2. **Examining Profile Content (Payloads):**

   - Double-click one of the profiles in the list (or select it and click the info button).
   - Review the various details (Payloads) to see exactly what access rights or restrictions apply to the Mac.

3. **Attempting Profile Removal for Isolation:**

   - If you identify a problematic profile, try selecting it and clicking the minus (`-`) button at the bottom of the list to remove it.
   - *Note:* In most real managed environments, the profile will be set as Non-Removable and you won't be able to remove it here; you will need to remove it via the MDM server to complete the isolation process. In this lab, we settle for familiarizing ourselves with the location and the attempt.

---

## Extra Exercise / Technical Tip of the Iceberg

Although macOS GUI interfaces provide most of the information needed for diagnostics, in fleet management (MDM) or remote work, advanced IT professionals rely on command-line tools. Here are the Terminal equivalents for the actions we just performed:


1. **Generating a System Report in the Terminal (`system_profiler`):**

   Instead of using System Information, you can run the following command in the Terminal to pull only network information and save it directly to a text file on the Desktop:
   ```bash
   system_profiler SPNetworkDataType > ~/Desktop/NetworkInfo.txt
   ```

2. **Locating Profiles via the Terminal (`profiles`):**

   Instead of navigating to System Settings, you can display all Configuration Profiles installed on the Mac directly in the console:
   ```bash
   sudo profiles show -type configuration
   ```
   This tool also displays profiles that might be hidden from the end user, allowing IT staff to locate and isolate conflicting settings quickly.
