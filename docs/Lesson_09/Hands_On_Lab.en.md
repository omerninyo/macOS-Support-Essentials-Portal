# Lesson 09: Networking
**Hands-On Lab (vEXP)**

## Objective
In this lab, we will practice managing Network Configurations visually and practically. We'll learn how to set Network Locations and manage interface priorities (Service Order) from System Settings. In the second part, we will use built-in graphical tools like Activity Monitor and the Wireless Diagnostics wizard to perform network diagnostics, and in the third part, we will examine the built-in Firewall and monitor its activity using the Console application.

## Prerequisites

* A Mac computer updated to macOS 26 (Tahoe).
* A user with Admin privileges.
* Access to the System Settings interface.
* An active network connection (Wi-Fi or cable).

---

## Exercise 1: Managing Network Locations and Service Order

In this scenario, we will simulate transitioning between an "office" network configuration and a "home" network configuration, while changing DNS servers and interface settings through the Graphical User Interface (GUI).

### Step 1: Viewing and Managing Network Locations

1. Open **System Settings** and navigate to the **Network** menu.
2. Scroll to the bottom of the window (below the interfaces list) and click the `...` actions button.
3. In the opened menu, select **Locations** and then **Edit Locations**.
4. Ensure the currently active location is selected (usually `Automatic`, which is the macOS default).

### Step 2: Creating a New Network Location

1. In the Edit Locations window, click the plus (`+`) button to create a new profile.
2. Name the new location `Office-Lab` and click **Done**.
3. Click the `...` menu again -> **Locations**, and make sure `Office-Lab` is now checked. (Switching to the new location briefly disconnects the network and applies clean settings for this profile).

### Step 3: Changing DNS Settings in the New Network Location
Now, we will configure different DNS servers (e.g. Google DNS servers) that will be valid *only* in the location we created, for the Wi-Fi connection.

1. Under the **Network** menu, click on the **Wi-Fi** interface.
2. Click the **Details...** button next to the network you are connected to.
3. In the sidebar of the pop-up window, select **DNS**.
4. Under the list of DNS servers (IPv4 or IPv6 addresses), click the plus (`+`) button and type `8.8.8.8`. Click the plus again and type `8.8.4.4`.
5. Click **OK** to save.

### Step 4: Playing with Service Order

1. Return to the main **Network** screen in System Settings.
2. Click the `...` menu at the bottom, and select **Set Service Order**.
3. In the opened window, drag one of the other interfaces (e.g. Ethernet or your iPhone USB connection, if present) above the Wi-Fi connection.
4. Explain to yourself: This action tells the system that if both connections are available simultaneously, the top interface in the list is the one through which all internet traffic will go out. Click **OK**.
5. Finally, return to **Locations** and switch the Mac back to the **Automatic** location to cancel the DNS changes we made.

---

## Exercise 2: Network Diagnostics Using Built-In Graphical Tools

As corporate support professionals, it's important to know what tools exist in the system to check network health, without opening Terminal.

### Step 1: Monitoring Network Traffic in Activity Monitor

1. Open the **Activity Monitor** application from the `Applications/Utilities` folder.
2. Switch to the **Network** tab at the top.
3. Here you can see in real-time which process is consuming your bandwidth (Data Sent / Data Received).
4. At the bottom of the window, review the graph showing the system's overall network traffic (Packets in/out). This is an excellent tool for identifying applications that "choke" the network, like background cloud syncs stuck in a loop.

### Step 2: Reviewing Connection Data via System Information

1. Click the **Apple - ** menu in the top left corner, hold the **Option - ⌥** key and click on **System Information...** (This option replaces "About This Mac" when holding the Option key).
2. In the left sidebar, scroll down under the **Network** category and click on **Locations**.
3. Review the displayed information. Here, all IP settings, Subnet Masks, and MAC addresses for all your interfaces across different locations are concentrated in one place.

### Step 3: Wireless Diagnostics

1. Hold the **Option - ⌥** key on the keyboard, and left-click the **Wi-Fi** icon in the Menu Bar at the top of the screen.
2. Notice the rich information revealed: IP address, Transmit Rate (Tx Rate), and signal and noise strength (RSSI and Noise).
3. Click on **Open Wireless Diagnostics...**.
4. A network diagnostics wizard will open. You can click **Continue** and let the system analyze the Wi-Fi environment to locate stability issues, background noise from neighbors' routers, and other interferences.

---

## Exercise 3: Firewall and Monitoring Blocks in Console

In managed environments (MDM), the Application Layer Firewall is often enabled to protect corporate computers from hostile connections on public networks.

### Step 1: Enabling and Checking Firewall Settings

1. Open **System Settings** -> navigate to **Network** -> click on **Firewall**.
2. If the firewall is turned off, turn it on.
3. Click the **Options...** button.
4. Review the list of applications. Here you can add or remove applications, and configure for each one whether it is allowed to receive incoming connections (Allow incoming connections) or blocked (Block).
5. Ensure the setting "Automatically allow built-in software to receive incoming connections" is checked, click **OK** to save.

### Step 2: Monitoring Firewall Warnings in Console
When the firewall blocks incoming communication, it logs this in the system logs.

1. Open the **Console** application (from `Applications/Utilities`).
2. In the left sidebar, ensure **Mac** (or your computer's name) is selected under "Devices".
3. Click the **Start** button in the top toolbar to begin collecting live logs.
4. In the search bar in the top right corner, type the term `socketfilterfw` (this is the name of the process that manages the Application Firewall in the system) and press Enter.
5. Now, try to open a new application that requires network access, or ask a classmate to try sending you a ping or AirDrop. If there's a block (Drop) or if the system grants the application temporary approval, you will see the messages pop up here in real time. This tool is essential for troubleshooting when corporate software stops working due to incoming communication blocks.

---

## Extra Exercise / Technical Tip of the Iceberg

As System or IT Support professionals, we sometimes want to perform network operations remotely (via SSH or an MDM script). macOS has dedicated CLI tools that correspond exactly to the graphical interface we saw.

**Examples for Advanced Users (in Terminal):**

1. **Quickly Changing DNS for the Wi-Fi interface (`networksetup`):**

   ```bash
   sudo networksetup -setdnsservers Wi-Fi 8.8.8.8 8.8.4.4
   ```
   *This command applies the exact same Google DNS servers we configured manually earlier through the interface. To reset back to the local router's DNS, use the word `Empty` instead of addresses.*

2. **Checking Firewall Status Behind the Scenes (`socketfilterfw`):**

   ```bash
   /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate
   ```
   *The CLI tool that manages the Application Firewall. The command prints back to the screen whether the firewall is on or off, without needing to open System Settings.*
