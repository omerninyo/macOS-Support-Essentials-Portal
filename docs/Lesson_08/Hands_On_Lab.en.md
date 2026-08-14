# Lesson 08: Terminal and System Services
**Hands-On Lab (Student Exercise)**

In this lab, you will gain hands-on experience with the architecture operating behind the graphical interface. We will inspect the directory structure responsible for system background services, investigate macOS configuration files (Property Lists / Plists), and utilize Activity Monitor and Console logs to analyze real memory pressure and monitor the built-in Apple MDM daemon in action.

!!! warning "Important Note"
    In some steps within the lab environment, you will be required to enter your administrator password to authorize privileged actions (`sudo`). Note that when typing your password in the Terminal, no visual feedback or asterisks will appear, but the system is actively capturing your keystrokes.

---

## Exercise 1: Resource Analysis Using Activity Monitor

**Objective:** Practical evaluation of the Memory Pressure index rather than traditional free memory counting.

1. Open the **Activity Monitor** application (found in the `/Applications/Utilities` folder, or by searching via Spotlight using `Cmd + Space`).
2. In the window that opens, ensure you are on the **CPU** tab. Locate an active process in the list (such as `Safari` or `Terminal`).
3. Double-click the process. A detailed inspection window will display technical metrics: memory usage, allocated ports, and the **Parent Process**. Notice that for the vast majority of user applications, the parent process is **launchd (1)**. Close the inspector window.
4. Switch to the **Memory** tab.
5. Look at the bottom pane displaying the **Memory Pressure** graph.
   * What color is it currently showing? (Green, Yellow, or Red).
   * Check the **Swap Used** metric. How much space is Swap consuming? If this metric is 0 bytes or negligible, your Mac is managing memory with optimal efficiency without needing to page data to disk.

---

## Exercise 2: Inspecting Configuration Files (Plists) via Terminal

**Objective:** Navigating backstage directories and reading/validating macOS Property List files.

1. Open the **Terminal** application.
2. Navigate to the system-wide preferences directory:
   ```bash
   cd /Library/Preferences
   ```
3. List the directory contents with detailed permissions and metadata:
   ```bash
   ls -la
   ```
   *Notice that almost all configuration files end with the `.plist` extension.*
4. Inspect the configuration file that manages system login window behaviors:
   ```bash
   plutil -p com.apple.loginwindow.plist
   ```
   *This command parses the binary/XML format and prints the key-value pairs in a readable structure (e.g., whether the login screen displays a list of users or username/password input fields).*
5. Check if the configuration file has any structural syntax errors:
   ```bash
   plutil -lint com.apple.loginwindow.plist
   ```
   *If the file syntax is valid, the command returns `OK`.*

---

## Exercise 3: Managing System Services (LaunchDaemons) with `launchctl`

**Objective:** Observing critical system Daemons and third-party persistent services running in the background.

1. In the Terminal, request a full printout of all background Daemons currently running at the system domain level (`sudo` is required since these are infrastructure services):
   ```bash
   sudo launchctl print system
   ```
   *(Enter your administrator password when prompted).*
   *A comprehensive diagnostic report will output. Scroll up to inspect service names, their current Process IDs (PIDs) if actively running, or exit/status codes if idle or suspended.*
2. Open a new Finder window and navigate directly to the third-party Daemons directory:
   * From the top menu bar, click **Go** > **Go to Folder...** (or press `Cmd + Shift + G`).
   * Enter: `/Library/LaunchDaemons` and press Enter.
3. This directory hosts persistence background services deployed by enterprise software such as Microsoft, Jamf, or security tools.
   *(If the directory is empty, no third-party system services are currently installed on the Mac).*
4. **New in macOS Tahoe:** Explore the sealed system path for native Apple services, as well as the new `LaunchAngels` directory managed directly by the `RunningBoard` framework:
   * Press `Cmd + Shift + G` in Finder and navigate to: `/System/Library/LaunchAngels`

---

## Exercise 4: Live Tracing of the MDM Agent (`mdmclient`)

**Objective:** Troubleshooting enterprise MDM operations by isolating Apple's native management daemon and monitoring communication events.

1. Open the **Console** application (located in `/Applications/Utilities`).
2. In the search bar at the top-right corner, enter `mdmclient` and press Enter.
3. Notice that the Console app is now filtering only log events related to the operating system's built-in MDM agent.
4. Leave the Console window open on one side of your screen.
5. Open **System Settings** and navigate to **Privacy & Security** > **Profiles** (or **Device Management**).
   * *(If an MDM profile is installed on the Mac, accessing this pane triggers the system to interrogate the `mdmclient` daemon).*
6. Watch the Console window. Observe new real-time log entries streaming as the system queries profile states. In enterprise troubleshooting scenarios, this is where you identify network handshakes, APNs check-ins, or SSL certificate trust failures.
7. Close all applications. The lab exercise is complete!
