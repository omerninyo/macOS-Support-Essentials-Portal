# Lesson 16: Log Analysis
**Hands-On Lab**

## Lab Objective
This lab focuses on the advanced use of macOS 26 built-in diagnostic tools. We will practice reading, filtering, and analyzing the Unified Logging System using the graphical interface (Console.app). Next, we will learn how to generate and analyze the Sysdiagnose archive. The exercise will conclude with a corporate "Escape Room" scenario where you will use the system's visual tools to locate the specific log line (the "Smoking Gun") that proves MDM commands are being blocked.

## Prerequisites

* A Mac running macOS 26 (Tahoe).
* Admin access to view extended logs in Console and to create a Sysdiagnose.
* (Recommended for Exercise 4) A Mac connected to an MDM server.

---

## Exercise 1: Visual Control in Console and Noise Filtering

**Scenario:** The modern logging system generates thousands of lines per second. Your goal is to understand how to stop the stream and focus solely on the processes that interest you, while avoiding background noise.

### Step 1: Starting Live Monitoring in Console

1. Open the **Console** application from the `Applications > Utilities` folder (or via Spotlight search).
2. In the left Sidebar, under the **Devices** category, ensure your local Mac is selected.
3. In the top toolbar, click the **Start** button (if the stream hasn't started yet). You will notice an endless stream of data and fleeting events.
4. Click the **Pause** button to stop the stream. This is always the first step in active log investigation.

### Step 2: Filtering by Process

1. Click **Start** again to resume the stream.
2. In the search bar in the top right corner, type the word `mdmclient` and press Enter.
3. By default, Console searches for this word in all fields and adds a filter under the **Any** tag.
4. Click the small arrow next to the word "Any" (in the gray filter bar created under the search bar), and change the setting to **Process**.
5. The stream is now significantly reduced, and you only see the actions of the local MDM agent.

### Step 3: Excluding Noise

1. While the stream is running, locate a recurring log line that is irrelevant to your investigation.
2. Right-Click on that line and select **Hide messages like this** (or **Hide process**).
3. Notice how a new filter with a minus sign is automatically added to the top search bar. This action allows you to clear the view of irrelevant information.

---

## Exercise 2: Advanced Search in the GUI (Saved Searches & Multiple Filters)

**Scenario:** Now we will learn to build more complex queries to simulate a search for specific system components, just as a network administrator searches for anomalous events, and save them for future use.

### Step 1: Building a Complex Filter

1. Delete all existing filters in the search bar (using the small X on each filter tag).
2. Type `com.apple.TCC` (the service responsible for privacy permissions in macOS) and press Enter.
3. Change the filter type from Any to **Subsystem**.
4. Now, type the word `error` in the search bar and press Enter.
5. Change the filter type for the word error from Any to **Message Type** (or simply leave it as Any and see the difference).
6. You now have a query that displays only errors belonging to the permissions system.

### Step 2: Saved Searches

1. If this is a query you need to run on a daily basis in your work, click the **Save** button located below the search bar (to the right of the gray filter bar).
2. Give the search a clear name, for example, "TCC Errors".
3. The saved search will now appear in the top toolbar of the Console application, and can be clicked at any time with a single click.

### Step 3: Live Viewing (Streaming)

1. Delete existing filters, type `SoftwareUpdate` in the search bar, and change the filter to **Process**.
2. Ensure Console is in **Start** mode.
3. Open **System Settings** and navigate to **General > Software Update**.
4. Simultaneously track the Console window and see how the update check operation is reflected visually and immediately through log writes.

---

## Exercise 3: Generating and Analyzing a Sysdiagnose via the GUI

**Scenario:** Apple's support engineers (or your organization's Tier 3 team) need a comprehensive snapshot of the system from the moment of the crash or failure. You must generate the massive Sysdiagnose report, which contains hundreds of megabytes of diagnostic data.

### Step 1: Creating the Archive via Activity Monitor

1. Open the **Activity Monitor** application (from `Applications > Utilities`).
2. In the application's top menu bar, look for the tools icon or gear icon named **System Diagnostics Options** (depending on the OS version).
3. Click it and select **Run System Diagnostics**.
4. You must agree to Apple's warning terms (explaining that the report contains sensitive PII data) and enter your administrator password.
5. The process takes between 3 to 10 minutes and collects extensive background information. Wait patiently.

*(Note: You can also generate the file without Activity Monitor by using the global keyboard shortcut `Shift + Control + Option + Command + Period (.)`. The screen will flash briefly to confirm the process has started).*

### Step 2: Exploring the Archive

1. At the end of the process, a Finder window will automatically pop up displaying the compressed archive file (in `.tar.gz` format) in the hidden path `/private/var/tmp/`.
2. Drag the file to your Desktop and extract it (Unzip) by double-clicking it.
3. Enter the extracted folder. Review the rich folder structure – you will find lists of open processes, network connection statuses, memory details, and more.
4. Locate the main file named `system_logs.logarchive`.
5. Double-clicking it will open it directly in the **Console** application. You are now able to "time travel" and filter historical logs exactly as you did in the previous exercise.

---

## Exercise 4: The Corporate "Escape Room" - Locating an MDM Block (The Smoking Gun)

**Escape Room Scenario:** An end user claims they are not receiving profiles and commands from the corporate MDM. As an IT professional, you suspect the corporate Firewall is blocking the Mac's communication to Apple's servers on port 5223. You must provide definitive proof from the logs to the Network team so they can remove the block.

### Step 1: Simulating MDM Activity

1. Open **System Settings** and navigate to **Privacy & Security > Profiles** (or under Device Management in newer versions).
2. If you have an installed MDM profile, double-click it to see its status. (If you don't have a profile, checking for software updates as we did earlier will generate network traffic you can track as an alternative exercise).

### Step 2: Investigating the Network Event in Console

1. Open the **Console** application.
2. Type `apsd` (Apple Push Service Daemon) or `mdmclient` in the search bar and change the filter to **Process**.
3. Now, type keywords indicating network failures, such as `timeout`, `failed`, or `unreachable`, in the search bar and leave the filter on **Any**.

### Step 3: Locating the "Smoking Gun"

1. Scan the results until you locate the exact network error (usually under the subsystem of `com.apple.mdmclient` or `com.apple.apsd`).
2. Look for output similar to one of the following options:

   * `NSURLErrorDomain error -1001 (The request timed out)`
   * `Failed to connect to MDM server: Host is down`
   * `Certificate trust failed`
   * `APNs connection dropped / failed to establish`
3. Copy this log line. **This is the escape room solution**. This line serves as the required proof for the corporate network team that the Mac is trying to reach out, but the Firewall is dropping or intercepting the packet.

---

## Extra / Technical Deep Dive

As we learned, in this course we focus on using the system's GUI tools. However, for advanced system administrators who connect to endpoints remotely via SSH, these actions can also be performed directly from the command line (CLI).

**1. Investigating logs from the Terminal (instead of using Console):**

The `log show` command allows you to extract information and filter it using "Predicates" (which correspond to the graphical filters):
```bash
log show --predicate 'process == "apsd" AND eventType == error' --info --last 2h
```
*Explanation: The command will display errors from the Apple Push Service Daemon from the last two hours with extended details.*

**2. Generating Sysdiagnose via command (instead of Activity Monitor):**

If you need to generate diagnostics remotely without a graphical interface, run the following command which routes the archive file to the Desktop:
```bash
sudo sysdiagnose -f ~/Desktop/
```
