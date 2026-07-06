# Lesson 08: Terminal and Background Services
**Hands-On Lab (Student Exercise)**

In this lab, you will get practical familiarity with the world behind the graphical interface. We will examine the structure of files responsible for system services, investigate Mac configuration files (Plists), and use Activity Monitor and logs to track real memory consumption and the activity of the built-in MDM agent.

**Important Note:** In some of the lab environment operations, you will be required to enter your user password to authorize privileged actions (`sudo`). Note that when you type the password in the Terminal, asterisks do not appear, but the system receives the input.

---

## Part 1: Analyzing Resources with Activity Monitor

1. Open the **Activity Monitor** application (you can find it in the `Applications/Utilities` folder, or via Spotlight search by pressing `Cmd+Space`).
2. In the window that opens, ensure you are on the **CPU** tab. Find a process in the list (you can also choose a process of a known running application, like Safari or Terminal).
3. Double-click on it. A new window will display the technical data: memory, allocated pages, and the Parent Process. You will see that for the vast majority of central applications, the parent process is **launchd (1)**. Close the info window.
4. Switch to the **Memory** tab.
5. Look at the bottom of the screen at the **Memory Pressure** graph.
   * What color is it? (Green, yellow, or red).
   * Look at the **Swap Used** figure. How much space does the Swap take? If the figure is 0 bytes or close to it, your computer is managing memory excellently without needing to write to the hard drive.

---

## Part 2: Investigating Configuration Files (Plists) and Using Terminal

1. Open the **Terminal**.
2. Run the following command to navigate to the built-in system preferences folder:
   `cd /Library/Preferences`
3. Run the command that displays files with extended permissions:
   `ls -la`
   Notice that almost all settings files end with the `.plist` extension.
4. Let's try to inspect the configuration file for the system's connection to login screens. Type:
   `plutil -p com.apple.loginwindow.plist`
   *This command bypasses the binary file encryption and prints the content to the screen in a readable manner. You will be able to see configured values (such as whether the system will display a user list or a name and password field on the login screen).*
5. Let's check if a specific file has a Syntax Error. Type:
   `plutil -lint com.apple.loginwindow.plist`
   *If the file is valid, the system will return the message `OK`.*

---

## Part 3: Managing System Agents (LaunchDaemons) with launchctl

In this part, we will see how `launchd` manages processes in the system using the `launchctl` tool.

1. In the Terminal window, let's request a printout of all Daemons currently running at the system level. (`sudo` is required because these are infrastructure services):
   `sudo launchctl print system`
   (Enter your password).
   *A very long output will scroll across the screen. You can scroll up and see a name list of services, alongside their PID numbers (if they are currently running) or error codes and suspension statuses (if they are waiting).*
2. Open a new Finder window, and navigate to the third-party Daemons folder:
   *From the top menu, click Go > Go to Folder... (or press `Cmd+Shift+G`).*
   *Type: `/Library/LaunchDaemons` and press Enter.*
3. Here lie the agents of companies like Microsoft, Jamf, or security software.
   *(If the folder is empty, it's a sign that your computer does not have third-party system services installed on it. Peek into the locked system path `/System/Library/LaunchDaemons` to see thousands of Apple items).*

---

## Part 4: Observing the MDM Agent (mdmclient)

1. Open the **Console** application (from `Applications/Utilities`).
2. In the search bar at the top right corner, type the word `mdmclient` and press Enter.
3. Notice that the Console app is now filtering only activities related to the operating system's MDM agent.
4. Keep the Console open on the side of the screen.
5. Open **System Settings** and navigate to **Privacy & Security** > **Profiles**.
   * (If you have any MDM profile installed on your computer, entering this area causes the system to query the mdmclient).
6. Look at the Console window. Notice the new lines popping up in the background in real-time, indicating information gathering or a communication attempt. In case of network issues in the organization, this is where we would locate connection errors (for example, blocked SSL certificates or a failed connection attempt).
7. Close all applications. The lab is complete!


<!-- src_hash: f47155635ead8efe8ee672235087522c2535e38a51892de8c69f772e4a5dccb8 -->
