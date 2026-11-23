# Lesson 15: Diagnostics
**Hands-On Lab (Student Exercise)**

This document contains the practical exercises for Lesson 15. The lab focuses on fault isolation methodologies, invoking Safe Mode, gathering system telemetry via the GUI (System Information), and diagnosing managed MDM profiles.

---

## Lab 1: Built-In Hardware Isolation at Boot (Apple Diagnostics)

> **What You Will Learn:** Launch Apple's offline hardware test suite (`Apple Diagnostics`) on Apple Silicon to isolate physical hardware faults (memory, battery, sensors, wireless module) from macOS software issues, and interpret official AppleCare reference codes.

*(Note: Live Wi-Fi analysis with Wireless Diagnostics was practiced in Lesson 09; here we focus on bare-metal hardware isolation outside macOS).*

### Execution Steps:

1. **Shut Down and Enter Startup Options:**
   - Open the Apple menu (``) and click **Shut Down**. Wait until the Mac powers off completely.
   - Press and hold the **Power / Touch ID** button continuously until **Loading startup options...** appears, then release.

2. **Launch Apple Diagnostics from Startup Options:**
   - Once the internal disk and **Options** gear icons appear, press and hold **`Command (⌘) + D`** on the keyboard for several seconds until the display switches into the diagnostics loader.
   - Select **English** (and connect to Wi-Fi if prompted; offline testing is also supported).

3. **Run the Hardware Sweep & Read Reference Codes:**
   - Apple Diagnostics automatically tests internal components for 2-3 minutes.
   - Review the resulting **Reference Code**:
     - **`ADP000`** = **No issues found** (hardware is healthy—focus troubleshooting on software/profiles!).
     - Hardware fault codes (such as `PPT004` for battery or `CNW001` for wireless hardware) provide direct escalation evidence for AppleCare or an Authorized Service Provider.
   - Click **Shut Down** at the bottom of the screen to proceed directly into Lab 2 (`Safe Mode`).

---

## Lab 2: The Isolation Principle and Safe Mode

**Objective:** Isolate system-level faults by utilizing Safe Mode, which disables third-party extensions and flushes system caches.

### Execution Steps:

1. **System Shutdown:**

   - Navigate to the Apple menu () and select `Shut Down`. Wait for the Mac to power off completely.

2. **Booting into Safe Mode (Apple Silicon):**

   - Press and hold the power button on the Mac. Do not release it.
   - Continue holding until you see `Loading startup options` on the screen.
   - On the options screen, select (single click) your primary system volume (usually `Macintosh HD`).
   - Press and hold the `Shift` key on the keyboard.
   - The `Continue` button will now toggle to `Continue in Safe Mode`. Click it and release the `Shift` key.

3. **Testing the System in Safe Mode:**

   - Log into your user account (Local Account). You might be prompted to enter your password twice.
   - Verify in the top right corner of the screen (or on the login screen) that the red `Safe Boot` indicator is present. You might experience sluggish UI responsiveness or screen tearing—this is expected and results from hardware graphics acceleration being disabled.
   - **The Isolation Principle:** This is the moment to verify if your original issue persists. If the problem is gone, it is highly likely caused by third-party LaunchDaemons, LaunchAgents, or background endpoint agents that were prevented from loading.

4. **Exiting Safe Mode:**

   - Restart the Mac normally (Apple menu > `Restart`).
   - Upon reboot, the system resumes standard operations (the underlying directory checks and cache flushes often resolve transient issues "magically" upon returning to normal boot).

---

## Lab 3: System Auditing via System Information

**Objective:** Gather comprehensive system telemetry using the native System Information GUI and export data for IT support workflows.

### Execution Steps:

1. **Launching System Information:**

   - Hold down the `Option` (⌥) key on the keyboard, and click the Apple menu () in the top left corner of the screen.
   - Select `System Information...` (This option replaces "About This Mac" while the `Option` key is held).

2. **Extracting Hardware Telemetry:**

   - In the launched window, from the Sidebar, select the `Hardware` category.
   - Review data points such as the CPU model (Chip), total RAM (Memory), and the Serial Number.
   - Click the `Storage` sub-category to view a detailed breakdown of available storage capacity.

3. **Extracting Software Details and Uptime:**

   - In the Sidebar, scroll down to the `Software` category and select it.
   - Locate your exact macOS version and build number.
   - Find the `Time since boot` metric.
   - *Note:* The system Uptime metric is critical for isolating resource exhaustion issues. A Mac with dozens of days of Uptime is susceptible to performance degradation.

4. **Exporting Data to a Report:**

   - In the top Menu Bar, click `File` and select `Save...`.
   - Save the report (as a `.spx` format) to your `Desktop`.
   - Navigate to the Desktop, double-click the generated file, and verify that System Information relaunches and displays the captured offline data. This technique is perfect for attaching diagnostic data to IT Helpdesk Tickets.

---

## Lab 4: Enterprise IT Support (Enterprise Seasoning) - Profile Isolation via GUI

**Objective:** Isolate faults where a Mobile Device Management (MDM) server is involved and Configuration Profiles are enforced on the user, utilizing the System Settings interface.

### Execution Steps:

1. **Locating Profiles via the GUI:**

   - Open `System Settings`.
   - Navigate the sidebar to `Privacy & Security`.
   - Scroll to the bottom and click on `Profiles` (If no profiles are installed on the machine, this menu item might be hidden).
   - Review the installed profiles to understand which restrictions are enforced (e.g., VPN payloads, Content Filters, USB blocking).

2. **Auditing Profile Payloads:**

   - Double-click one of the profiles in the list (or select it and click the info button).
   - Review the various Payloads to see exactly what access rights or restrictions are applied to the Mac.

3. **Attempting Profile Removal for Isolation:**

   - If you suspect a profile is causing interference, try selecting it and clicking the minus (`-`) button at the bottom of the list to remove it.
   - *Note:* In most real-world managed enterprise environments, the profile will be deployed as Non-Removable and cannot be deleted from here; IT must remove it via the MDM server console to complete the isolation process. For this lab, understanding the location and the removal attempt is sufficient.

---

## Bonus Exercise for IT Professionals: The Command Line (Terminal)

While macOS GUI tools provide most of the telemetry required for standard diagnostics, in MDM fleet management or remote support scenarios, advanced IT engineers rely on command-line tools. Here are the Terminal equivalents for the tasks we just performed:


1. **Generating a System Report via Terminal (`system_profiler`):**

   Instead of using System Information, you can execute the following command in Terminal to extract only network-related telemetry, saving it directly to a text file on the Desktop:
   ```bash
   system_profiler SPNetworkDataType > ~/Desktop/NetworkInfo.txt
   ```

2. **Locating Profiles via Terminal (`profiles`):**

   Instead of navigating System Settings, you can display all Configuration Profiles installed on the Mac directly in the console:
   ```bash
   sudo profiles show -type configuration
   ```
   This CLI tool will also expose payloads that might be hidden from the end-user GUI, allowing IT staff to rapidly pinpoint and isolate conflicting configurations.

<!-- src_hash: 600bc9766e983032ca83fc6dbe4c5311ec6d2594d57d6afb2a2d7187881bbfc3 -->
