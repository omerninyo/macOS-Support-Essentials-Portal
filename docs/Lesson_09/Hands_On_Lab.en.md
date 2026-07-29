# Lesson 09: Networking
**Hands-on Lab (Student Exercise)**

## Objective
In this lab, we will practice managing Network Configurations visually and practically. We will learn how to configure Network Locations and manage Service Order priorities within System Settings. In the second part, we will use built-in graphical tools like Activity Monitor and Wireless Diagnostics to perform network diagnostics. In the third part, we will examine the built-in Firewall and monitor its activity using the Console application.

## Prerequisites

*   A Mac computer updated to macOS 26 (Tahoe).
*   A user account with Admin privileges.
*   Access to the System Settings interface.
*   An active network connection (Wi-Fi or cable).

---

## Exercise 1: Managing Network Locations and Service Order

In this scenario, we will simulate switching between an "Office" network configuration and a "Home" network configuration, changing DNS servers and interface settings via the graphical user interface (GUI).

### Step 1: Viewing and Managing Network Locations

1.  Open **System Settings** and navigate to the **Network** menu.
2.  Scroll to the bottom of the window (below the list of interfaces) and click the actions button marked with three dots `...`.
3.  In the menu that appears, select **Locations** and then **Edit Locations**.
4.  Verify that the currently active location is selected (usually `Automatic`, which is the macOS default).

### Step 2: Creating a New Network Location

1.  In the Locations editing window, click the plus button (`+`) to create a new profile.
2.  Name the new location `Office-Lab` and click **Done**.
3.  Click the three dots `...` menu again -> **Locations**, and verify that `Office-Lab` is now marked with a V as active. (Switching to the new location temporarily disconnects the network and applies clean settings for this profile).

### Step 3: Changing DNS Settings in the New Network Location
Now, we will configure different DNS servers (for example: Google DNS servers) that will be valid *only* in the location we created, for the Wi-Fi connection.

1.  Under the **Network** menu, click the **Wi-Fi** interface.
2.  Click the **Details...** button next to the network you are connected to.
3.  In the sidebar of the pop-up window, select **DNS**.
4.  Under the list of DNS servers (IPv4 or IPv6 addresses), click the plus button (`+`) and type `8.8.8.8`. Click the plus button again and type `8.8.4.4`.
5.  Click **OK** to save.

### Step 4: Experimenting with Service Order

1.  Return to the main **Network** screen in System Settings.
2.  Click the three dots `...` menu at the bottom, and select **Set Service Order**.
3.  In the window that opens, drag one of the other interfaces (e.g., Ethernet or your iPhone USB connection, if present) above the Wi-Fi connection.
4.  Explain to yourself: This action tells the system that if both connections are available simultaneously, the interface at the top of the list is the one through which all outgoing internet traffic will pass. Click **OK**.
5.  Finally, return to **Locations** and switch your Mac back to the **Automatic** location to revert the DNS changes we made.

---

## Exercise 2: Network Diagnostics Using Built-in Graphical Tools

As enterprise support personnel, it is important to know which tools are available in the system for checking network integrity, without opening Terminal.

### Step 1: Monitoring Network Traffic in Activity Monitor

1.  Open the **Activity Monitor** application from the `Applications/Utilities` folder.
2.  Switch to the **Network** tab at the top.
3.  Here you can see in real-time which process is consuming your bandwidth (Data Sent / Data Received).
4.  At the bottom of the window, review the graph showing the system's overall network traffic (Packets in/out). This is an excellent tool for identifying applications that are "hogging" the network, such as a cloud sync stuck in the background.

### Step 2: Reviewing Connection Data Using System Information

1.  Click the **Apple - ** menu in the top-left corner, hold down the **Option - ⌥** key, and click **System Information...** (this option replaces "About This Mac" when holding the Option key).
2.  In the left sidebar, scroll down under the **Network** category and click **Locations**.
3.  Review the information displayed. Here, all your IP, Subnet Mask, and MAC addresses for all your interfaces in different locations are consolidated in one place.

### Step 3: Wireless Diagnostics

1.  Hold down the **Option - ⌥** key on the keyboard, and left-click the **Wi-Fi** icon in the Menu Bar at the top of the screen.
2.  Notice the rich information revealed: IP address, transmission rate (Tx Rate), and signal and noise strength (RSSI and Noise).
3.  Click **Open Wireless Diagnostics...**.
4.  A network diagnostics wizard will open. You can click **Continue** and let the system analyze the Wi-Fi environment to identify stability issues, background noise from neighbors' routers, and other interferences.

---

## Exercise 3: Firewall and Monitoring Blocks in Console

In managed environments (MDM), the Application Layer Firewall is often enabled to protect corporate computers from hostile connections on public networks.

### Step 1: Enabling and Checking Firewall Settings

1.  Open **System Settings** -> go to **Network** -> click **Firewall**.
2.  If the firewall is off, turn it on.
3.  Click the **Options...** button.
4.  Review the list of applications. Here you can add or remove applications, and configure for each whether it is allowed to receive incoming connections (Allow incoming connections) or blocked (Block).
5.  Ensure that "Automatically allow built-in software to receive incoming connections" is checked, click **OK** to save.

### Step 2: Monitoring Firewall Alerts in Console
When the firewall blocks incoming communication, it logs this in the system logs.

1.  Open the **Console** application (from `Applications/Utilities`).
2.  In the left sidebar, ensure that **Mac** (or your computer's name) is selected under "Devices".
3.  Click the **Start** button in the top toolbar to begin collecting live logs.
4.  In the search bar in the top-right corner, type `socketfilterfw` (this is the name of the process that manages the Application Firewall in the system) and press Enter.
5.  Now, try opening a new application that requires network access, or ask a classmate to try sending you a ping or AirDrop. If there is a block (Drop) or if the system grants the application temporary approval, you will see the messages pop up here in real-time. This tool is essential for troubleshooting issues where corporate software stops working due to blocked incoming communication.

---

## Extra Exercise / Technical Iceberg Tip

As System or IT Support personnel, we sometimes want to perform network operations remotely (via SSH or an MDM script). macOS has dedicated CLI tools that correspond exactly to the graphical interface we've seen.

**Examples for Advanced Users (in Terminal):**

1.  **Quickly change DNS for the Wi-Fi interface (`networksetup`):**

    ```bash
    sudo networksetup -setdnsservers Wi-Fi 8.8.8.8 8.8.4.4
    ```
    *This command applies the exact same Google DNS servers we configured manually earlier via the interface. To reset back to the local router's DNS, use the word `Empty` instead of the addresses.*

2.  **Check Firewall status behind the scenes (`socketfilterfw`):**

    ```bash
    /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate
    ```
    *The CLI tool that manages the Application Firewall. This command prints back to the screen whether the firewall is enabled or disabled, without needing to open System Settings.*

<!-- src_hash: d6933b33de53199cdbca3000074e2dffeb4abfff24b02615c1650a5ab843cb51 -->


!!! tip "Visual Aids (Student Guide)"
    These images illustrate the relevant interface or mechanism for this lesson.

![Slide131_image161](../assets/images/Lesson_09/L09_LegacySlide_Slide131_image161.png)
![Slide131_image45](../assets/images/Lesson_09/L09_LegacySlide_Slide131_image45.jpg)
![Slide133_image161](../assets/images/Lesson_09/L09_LegacySlide_Slide133_image161.png)
![Slide133_image45](../assets/images/Lesson_09/L09_LegacySlide_Slide133_image45.jpg)
![Slide134_image164](../assets/images/Lesson_09/L09_LegacySlide_Slide134_image164.png)
![Slide23_image41](../assets/images/Lesson_09/L09_LegacySlide_Slide23_image41.jpg)
![Slide74_image14](../assets/images/Lesson_09/L09_LegacySlide_Slide74_image14.jpg)
![Slide74_image15](../assets/images/Lesson_09/L09_LegacySlide_Slide74_image15.jpg)
![Slide99_image103](../assets/images/Lesson_09/L09_LegacySlide_Slide99_image103.png)
![Slide99_image30](../assets/images/Lesson_09/L09_LegacySlide_Slide99_image30.jpg)
![Slide99_image31](../assets/images/Lesson_09/L09_LegacySlide_Slide99_image31.jpg)
![26-Tahoe-Finder-Connect-to-Server-scaled](../assets/images/Lesson_09/L09_TahoeUI_26-Tahoe-Finder-Connect-to-Server-scaled.png)
![26-Tahoe-Finder-Network-scaled](../assets/images/Lesson_09/L09_TahoeUI_26-Tahoe-Finder-Network-scaled.png)
![26-Tahoe-Settings-Network-scaled](../assets/images/Lesson_09/L09_TahoeUI_26-Tahoe-Settings-Network-scaled.png)
![26-Tahoe-Settings-Wi-Fi-scaled](../assets/images/Lesson_09/L09_TahoeUI_26-Tahoe-Settings-Wi-Fi-scaled.png)
