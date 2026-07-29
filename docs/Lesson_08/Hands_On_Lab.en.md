# Lesson 08: Terminal and System Services
**Hands-On Lab (Student Practice - vEXP)**

In this lab, you will get hands-on experience with the world behind the graphical user interface. We will examine the structure of files responsible for system services, investigate Mac configuration files (Plists), and use Activity Monitor and logs to track actual memory consumption and the activity of the built-in MDM agent.

**Important Note:** In some of the lab activities, you will be required to enter your user password to authorize privileged actions (`sudo`). Please note that when you type the password in the Terminal, no asterisks appear, but the system is capturing your keystrokes.

---

## Part 1: Resource Analysis with Activity Monitor

1. Open the **Activity Monitor** application (you can find it in the `Applications/Utilities` folder, or via Spotlight search by pressing `Cmd+Space`).
2. In the opened window, ensure you are on the **CPU** tab. Find a process in the list (you can also use a process of a known running app, like Safari or Terminal).
3. Double-click it. A new window will display technical data: memory, allocated pages, and the Parent Process. You will see that for the vast majority of central apps, the parent process is **launchd (1)**. Close the info window.
4. Switch to the **Memory** tab.
5. Notice the **Memory Pressure** graph at the bottom of the screen.
   * What color is it? (Green, Yellow, or Red).
   * Look at the **Swap Used** data. How much space does the Swap take? If the figure is 0 bytes or close to it, your computer is managing memory with excellent efficiency without the need to write to the hard drive.

---

## Part 2: Investigating Configuration Files (Plists) and Using the Terminal

1. Open the **Terminal**.
2. Run the following command to navigate to the built-in system preferences folder:
   `cd /Library/Preferences`
3. Run the command to display files with extended permissions:
   `ls -la`
   Notice that almost all settings files end with the `.plist` extension.
4. Let's try to check the configuration file for the system's connection to login screens. Type:
   `plutil -p com.apple.loginwindow.plist`
   *This command bypasses the binary file's encryption and prints the content to the screen in a readable format. You can see defined values (like whether the system will show a list of users or a name and password field on the login screen).*
5. Let's check if a specific file has a syntax error. Type:
   `plutil -lint com.apple.loginwindow.plist`
   *If the file is valid, the system will return the message `OK`.*

---

## Part 3: Managing System Agents (LaunchDaemons) with launchctl

In this part, we will examine how `launchd` manages processes in the system using the `launchctl` tool.

1. In the Terminal window, let's request a printout of all the Daemons currently running at the system level. (`sudo` is required because these are infrastructure services):
   `sudo launchctl print system`
   (Enter your password).
   *A very long output will scroll across the screen. You can scroll up and see a named list of services, alongside their PID numbers (if they are currently running) or error codes and suspension statuses (if they are waiting).*
2. Open a new Finder window, and navigate to the third-party Daemons folder:
   *In the top menu, click Go > Go to Folder... (or press `Cmd+Shift+G`).*
   *Type: `/Library/LaunchDaemons` and press Enter.*
3. Here reside the agents of companies like Microsoft, Jamf, or security software.
   *(If the folder is empty, it means your computer has no third-party system services installed).*
4. **New in Tahoe:** Take a peek at Apple's locked system paths, and the new `LaunchAngels` path managed directly by the RunningBoard mechanism.
   *Type: `/System/Library/LaunchAngels` and press Enter.*

---

## Part 4: Observing the MDM Agent (mdmclient)

1. Open the **Console** application (from `Applications/Utilities`).
2. In the search bar at the top right corner, type the word `mdmclient` and press Enter.
3. Notice that the Console app now filters only activities related to the operating system's MDM agent.
4. Leave the Console open on the side of the screen.
5. Open System Settings (**System Settings**) and navigate to **Privacy & Security** > **Profiles**.
   * (If you have any MDM profile installed on the computer, entering this area causes the system to query the mdmclient).
6. Look at the Console window. Pay attention to the new lines popping up in the background in real-time, indicating information gathering or a communication attempt. In case of organizational network issues, this is where we would locate connection errors (for example, blocked SSL certificates or a failed connection attempt).
7. Close all applications. The lab is complete!
