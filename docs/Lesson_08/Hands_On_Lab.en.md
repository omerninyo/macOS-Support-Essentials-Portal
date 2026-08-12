# Lesson 08: Terminal and System Services
**Hands-On Lab (Student Exercise)**

In this lab, you will gain practical experience with the environment operating behind the graphical interface. We will explore the directory structure responsible for system services, investigate Mac configuration files (Plists), and utilize Activity Monitor and logs to track true memory consumption and the activity of the built-in MDM agent.

> [!WARNING]
> **Important Note:** In some steps of the lab environment, you will be required to enter your user password to authorize privileged actions (`sudo`). Note that when typing your password in the Terminal, no asterisks will appear, but the system is capturing your keystrokes.

---

## Exercise 1: Resource Analysis Using Activity Monitor

**Objective:** Gaining hands-on experience evaluating the Memory Pressure metric rather than traditional free memory counting.

1. Open the **Activity Monitor** application (found in the `Applications/Utilities` folder, or by searching via Spotlight using `Cmd+Space`).
2. In the window that opens, ensure you are on the **CPU** tab. Locate a process in the list (you can select a known running application, such as Safari or Terminal).
3. Double-click the process. A new window will display technical data: memory, allocated ports, and the Parent Process. You will notice that for the vast majority of core applications, the Parent Process is **launchd (1)**. Close the info window.
4. Switch to the **Memory** tab.
5. Look at the bottom of the screen at the **Memory Pressure** graph.
   * What color is it? (Green, Yellow, or Red).
   * Check the **Swap Used** metric. How much space is Swap consuming? If this metric is 0 bytes or close to it, your Mac is managing memory with excellent efficiency without needing to write to the hard drive.

---

## Exercise 2: Investigating Configuration Files (Plists) and Using the Terminal

**Objective:** Navigating behind the scenes and reading a macOS configuration file.

1. Open the **Terminal**.
2. Run the following command to navigate to the built-in system preferences directory:
   `cd /Library/Preferences`
3. Run the command to list files with extended permissions:
   `ls -la`
   *Notice that almost all configuration files end with the `.plist` extension.*
4. Let's inspect the configuration file that manages the system's login window behavior. Type:
   `plutil -p com.apple.loginwindow.plist`
   *This command bypasses the binary file encryption and prints the content to the screen in a readable format. You will see defined values (such as whether the system displays a list of users or name and password fields at the login screen).*
5. Let's check if a specific file has a Syntax Error. Type:
   `plutil -lint com.apple.loginwindow.plist`
   *If the file is structurally sound, the system will return an `OK` message.*

---

## Exercise 3: Managing System Agents (LaunchDaemons) with launchctl

**Objective:** Observing critical system Daemons and third-party tools that constantly run in the background.

1. In the Terminal window, let's request a printout of all Daemons currently running at the system level. (`sudo` is required since these are infrastructure services):
   `sudo launchctl print system`
   *(Enter your password).*
   *A very long output will scroll across the screen. You can scroll up to view the name list of services, alongside their PID numbers (if currently running) or status codes (if waiting/stopped).*
2. Open a new Finder window and navigate to the third-party Daemons directory:
   * From the top menu bar, click Go > Go to Folder... (or press `Cmd+Shift+G`).
   * Type: `/Library/LaunchDaemons` and press Enter.
3. This is where agents from companies like Microsoft, Jamf, or security software reside.
   *(If the folder is empty, it means your Mac does not have any third-party system services installed).*
4. **New in Tahoe:** Take a peek at the locked system path for Apple services, as well as the new `LaunchAngels` path managed directly by the RunningBoard mechanism.
   * Press `Cmd+Shift+G` and navigate to: `/System/Library/LaunchAngels`

---

## Exercise 4: Observing the MDM Agent (mdmclient)

**Objective:** Troubleshooting MDM issues by identifying Apple's built-in Daemon and monitoring communication errors.

1. Open the **Console** application (from `Applications/Utilities`).
2. In the search bar at the top right corner, type the word `mdmclient` and press Enter.
3. Notice that the Console app is now filtering only activities related to the operating system's MDM agent.
4. Leave the Console open on the side of your screen.
5. Open **System Settings** and navigate to **Privacy & Security** > **Profiles**.
   * *(If you have any MDM profile installed on the computer, entering this area triggers the system to query the mdmclient).*
6. Watch the Console window. Look for new lines popping up in real-time, indicating information gathering or connection attempts. In the event of organizational network issues, this is where we will spot connection errors (e.g., blocked SSL certificates or failed connection attempts).
7. Close all applications. The lab is complete!
