# Lesson 15: Diagnostics
**Hands-on Lab (Student Exercise)**

This document contains the practical exercise for Lesson 15. The exercise focuses on troubleshooting methods, entering Safe Mode, collecting system data via the graphical interface (System Information), and diagnosing managed profiles.

---

## Lab 1: Diagnosing Networks using Wireless Diagnostics

**Objective:** To become familiar with the hidden Wireless Diagnostics tool in the operating system, monitor network performance, and identify channel conflicts.

### Steps:

1.  **Accessing the Hidden Tool:**

    -   In the top Menu Bar, hold down the `Option` (⌥) key and click the Wi-Fi symbol.
    -   Notice the rich information that immediately appears (IP address, MAC address, signal quality, and transmission rate).
    -   From the menu that opens, select `Open Wireless Diagnostics`.

2.  **Bypassing the Setup Assistant:**

    -   When the application window opens, a "Diagnostics Assistant" will appear, designed to generate a lengthy report. **Ignore it.**
    -   Leave the assistant window open, but go to the `Window` menu in the top Menu Bar (the application's Menu Bar).

3.  **Monitoring Performance:**

    -   From the `Window` menu, select `Performance`.
    -   Examine the displayed graphs: Rate, Quality, and Signal.
    -   Wait about a minute and observe the changes in the graph. This tool is excellent for identifying sudden jumps or drops in connection (Dropouts).
    -   Close the Performance window.

4.  **Scanning Networks and Channels:**

    -   Return to the `Window` menu and select `Scan`.
    -   Click `Scan Now` (or wait for the automatic scan to complete).
    -   This window will display all networks in the vicinity (including some that may not appear in the regular menu), which channels they use, and the noise level on each channel. This is an ideal tool for IT support needing to identify interference caused by overlapping channels.
    -   Close the Scan window.

5.  **Packet Sniffer – *Demonstration Only*:**
    -   From the `Window` menu, select `Sniffer`.
    -   Observe the option to select a network channel and bandwidth. Clicking `Start` will disconnect you from the internet and begin capturing packets floating in the air on that channel, saving them as a file for analysis. (For the purpose of this exercise, there is no need to start capturing).

---

## Lab 2: Principle of Isolation and Entering Safe Mode

**Objective:** To isolate system-level issues by using Safe Mode, which disables third-party extensions and clears caches.

### Steps:

1.  **Shutting Down the System:**

    -   Go to the Apple menu () and select `Shut Down`. Wait for the computer to completely power off.

2.  **Starting in Safe Mode (Apple Silicon):**

    -   Press and hold the Mac's power button. Do not release.
    -   Continue holding until you see `Loading startup options` on the screen.
    -   On the options screen, single-click your system drive (usually `Macintosh HD`).
    -   Press and hold the `Shift` key on the keyboard.
    -   The `Continue` button will now change to `Continue in Safe Mode`. Click it and release `Shift`.

3.  **Checking the System in Safe Mode:**

    -   Log in to your user account (Local Account). You may need to enter your password twice.
    -   Check the top right corner of the screen (or the login screen) to confirm that `Safe Boot` appears in red. You might also experience slow responsiveness or screen flickering – this is normal and results from disabling graphics acceleration.
    -   **Principle of Isolation:** This is the time to check if the issue you were experiencing still exists. If the problem has disappeared, it is likely caused by LaunchDaemons, LaunchAgents, or other third-party background applications that were not loaded.

4.  **Exiting Safe Mode:**

    -   Restart the computer normally (Apple menu > `Restart`).
    -   Upon startup, the system resumes its normal operation (disk integrity verification performed in the background and cache clearing may sometimes resolve the issue "on their own" even after returning to normal mode).

---

## Lab 3: Investigating the System using System Information

**Objective:** To collect comprehensive system information using the built-in graphical interface System Information, and export data for support purposes.

### Steps:

1.  **Opening System Information:**

    -   Hold down the `Option` (⌥) key on the keyboard, and click the Apple menu () in the top left corner of the screen (or right in a Hebrew system).
    -   Select `System Information...` (this option replaces "About This Mac" when `Option` is held down).

2.  **Extracting Hardware Information:**

    -   In the window that opens, in the Sidebar, select the `Hardware` category.
    -   Review data such as the processor model (Chip), amount of memory (Memory), and Serial Number.
    -   Click the `Storage` sub-category to see details of available storage space.

3.  **Extracting Software Information and Uptime:**

    -   In the Sidebar, scroll down to the `Software` category and click it.
    -   Find your exact macOS version.
    -   Look for the `Time since boot` data (time since the last startup).
    -   *Note:* The number of Uptime days is critical data for isolating resource issues. A Mac with tens of days of Uptime may experience performance problems.

4.  **Exporting Data to a Report:**

    -   In the top Menu Bar, click `File` and select `Save...`.
    -   Save the report (`.spx` format) to the `Desktop` folder.
    -   Navigate to the Desktop, double-click the created file, and verify that System Information reopens and displays the saved data. This technique is perfect for adding diagnostic data to trouble tickets.

---

## Lab 4: Enterprise Seasoning - Isolating Profiles in the GUI

**Objective:** To isolate issues in scenarios involving a Mobile Device Management (MDM) server and Configuration Profiles enforced on the user, using the System Settings interface.

### Steps:

1.  **Locating Profiles via the GUI:**

    -   Open `System Settings`.
    -   Navigate in the sidebar menu to `Privacy & Security`.
    -   Scroll down and click `Profiles` (if no profiles are installed on this computer, this menu may not appear).
    -   Examine the installed profiles to understand which settings are enforced (e.g., VPN agent, content filtering, USB restrictions).

2.  **Examining Profile Content (Payloads):**

    -   Double-click one of the profiles in the list (or select it and click the information button).
    -   Review the various details (Payloads) to see exactly which access rights or restrictions apply to the Mac.

3.  **Attempting to Remove a Profile for Isolation:**

    -   If you identify a problematic profile, try selecting it and clicking the minus button (`-`) at the bottom of the list to remove it.
    -   *Note:* In most real-world managed environments, the profile will be configured as Non-Removable and cannot be removed here. You will need to remove it via the MDM server to complete the isolation process. In this lab, we will suffice with familiarizing ourselves with the location and the attempt.

---

## Extra Exercise / Technical Iceberg Tip

Although macOS GUI interfaces provide most of the necessary information for diagnosis, in fleet management (MDM) or remote work, advanced IT professionals rely on command-line tools. Here are the equivalent methods in Terminal for the operations we just performed:

1.  **Generating a System Report in Terminal (`system_profiler`):**

    Instead of using System Information, you can run the following command in Terminal to retrieve only network information and save it directly to a text file on the Desktop:
    ```bash
    system_profiler SPNetworkDataType > ~/Desktop/NetworkInfo.txt
    ```

2.  **Locating Profiles via Terminal (`profiles`):**

    Instead of navigating to System Settings, you can display all installed Configuration Profiles on the Mac directly in the console:
    ```bash
    sudo profiles show -type configuration
    ```
    This tool also displays profiles that might be hidden from the end-user, allowing IT professionals to quickly locate and isolate conflicting settings.

<!-- src_hash: 19926c30ded6dbb0cf817e6a443bf04bb76be4f11bf5e437d24d7723c531af9c -->

