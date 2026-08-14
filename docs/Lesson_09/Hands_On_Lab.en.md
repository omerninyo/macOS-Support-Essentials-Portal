# Lesson 09: Networking
**Hands-On Lab (Student Exercise)**

## Objective
In this lab, we will practice managing Network Configurations visually and hands-on. We will learn how to configure Network Locations and manage the Service Order of network interfaces from within System Settings. In the second part, we will use built-in graphical tools like Activity Monitor and Wireless Diagnostics for network troubleshooting. In the third part, we will examine the built-in Firewall and monitor its activity using the Console app.

## Prerequisites

* A Mac updated to macOS 26 (Tahoe).
* A user account with Admin privileges.
* Access to the System Settings interface.
* An active network connection (Wi-Fi or Ethernet).

---

## Exercise 1: Managing Network Locations and Service Order

**What you will learn:** Experiencing the transition between an "Office" network configuration and a "Home" network configuration, while changing DNS servers and interface settings through the Graphical User Interface (GUI).

### Step 1: Viewing and Managing Network Locations

1. Open **System Settings** and navigate to the **Network** menu.
2. Scroll to the bottom of the window (below the list of interfaces) and click the action button marked with three dots `...`.
3. In the opened menu, choose **Locations** and then **Edit Locations**.
4. Verify that the currently active location is selected (usually `Automatic`, which is the macOS default).

### Step 2: Creating a New Network Location

1. In the Locations editing window, click the plus (`+`) button to create a new profile.
2. Name the new location `Office-Lab` and click **Done**.
3. Click the three dots menu `...` again -> **Locations**, and verify that `Office-Lab` is now checked (✓) as active. (Switching to the new location momentarily disconnects the network and applies clean settings for this profile).

### Step 3: Changing DNS Settings in the New Network Location
Now, we will configure different DNS servers (for example: Google DNS servers) that will be valid *only* in the location we just created, for the Wi-Fi connection.

1. Under the **Network** menu, click on the **Wi-Fi** interface.
2. Click the **Details...** button next to the network you are connected to.
3. In the sidebar of the pop-up window, select **DNS**.
4. Under the list of DNS servers (IPv4 or IPv6 addresses), click the plus (`+`) button and type `8.8.8.8`. Click the plus again and type `8.8.4.4`.
5. Click **OK** to save.

### Step 4: Configuring Service Order

1. Return to the main **Network** screen in System Settings.
2. Click the three dots menu `...` at the bottom, and select **Set Service Order**.
3. In the opened window, drag one of the other interfaces (e.g., Ethernet or your iPhone USB connection, if present) to be above the Wi-Fi connection.
4. Understand the mechanism: This action tells the system that if both connections are available simultaneously, the interface at the top of the list is the one through which all outbound network traffic will route. Click **OK**.
5. When finished, return to **Locations** and revert the Mac to the **Automatic** location to cancel the DNS changes we made.

---

## Exercise 2: Network Diagnostics Using Built-in Graphical Tools

**What you will learn:** Getting hands-on with built-in system tools for verifying network health without opening the Terminal (Activity Monitor and Option-Click shortcuts).

### Step 1: Monitoring Network Traffic in Activity Monitor

1. Open the **Activity Monitor** application from `Applications/Utilities`.
2. Switch to the **Network** tab at the top.
3. Here you can see in real-time which process is consuming your bandwidth (Data Sent / Data Received).
4. At the bottom of the window, review the graph displaying the overall system network traffic (Packets in/out). This is an excellent tool for identifying applications that are hogging bandwidth, such as background cloud sync getting stuck.

### Step 2: Reviewing Connection Data via System Information

1. Click the **Apple menu - ** in the top left corner, hold down the **Option - ⌥** key, and click on **System Information...** (this option replaces "About This Mac" when holding the Option key).
2. In the left sidebar, scroll down under the **Network** category and click on **Locations**.
3. Review the displayed information. This is a centralized place where all IP settings, Subnet Masks, and MAC addresses of all your interfaces across different locations are aggregated.

### Step 3: Wireless Diagnostics

1. Hold down the **Option - ⌥** key on the keyboard, and left-click the **Wi-Fi** icon in the Menu Bar at the top of the screen.
2. Notice the rich information revealed: IP address, transmission speed (Tx Rate), and signal and noise strength (RSSI and Noise).
3. Click on **Open Wireless Diagnostics...**.
4. A network diagnostic wizard will open. You can click **Continue** and let the system analyze the Wi-Fi environment to locate stability issues, background noise from neighboring routers, and other interferences.

---

## Exercise 3: The Firewall and Monitoring Blocks in Console

**What you will learn:** Activating the enterprise Application Layer Firewall and tracking its operation through system logs.

### Step 1: Enabling and Checking Firewall Settings

1. Open **System Settings** -> Navigate to **Network** -> Click on **Firewall**.
2. If the firewall is turned off, enable it.
3. Click the **Options...** button.
4. Review the list of applications. Here you can add or remove applications, and configure for each whether it is allowed to receive inbound connections (Allow incoming connections) or is blocked (Block).
5. Verify that the setting "Automatically allow built-in software to receive incoming connections" is checked, click **OK** to save.

### Step 2: Monitoring Firewall Warnings in Console
When the firewall blocks incoming communication, it records it in the system logs.

1. Open the **Console** application (from `Applications/Utilities`).
2. In the left sidebar, ensure that **Mac** (or your computer's name) is selected under "Devices".
3. Click the **Start** button in the top toolbar to begin collecting live logs.
4. In the search bar in the top right corner, type the term `socketfilterfw` (this is the name of the process that manages the Application Firewall in the system) and press Enter.
5. Now, try to open a new application that requires network access, or ask a classmate to try sending you a ping or an AirDrop. If there is a block (Drop) or if the system grants the application temporary permission, you will see the messages pop up here in real-time. This tool is essential for troubleshooting when enterprise software stops working due to blocked inbound communication.

---

## Bonus Exercise for IT Professionals: The Command Line (Terminal)

As System or IT Support personnel, we often want to perform network operations remotely (via SSH or an MDM script). The macOS system includes dedicated CLI tools that correspond exactly to the graphical interface we've seen.

> [!NOTE]
> **Note:** CLI operations in a network environment are intended for advanced users and typically require sudo privileges.

**Examples for Advanced Users (in Terminal):**

1. **Quick DNS change for the Wi-Fi interface (`networksetup`):**

   ```bash
   sudo networksetup -setdnsservers Wi-Fi 8.8.8.8 8.8.4.4
   ```
   *This command applies exactly the same Google DNS servers that we manually configured earlier through the interface. To reset back to the local router's DNS, use the word `Empty` instead of the addresses.*

2. **Checking Firewall status behind the scenes (`socketfilterfw`):**

   ```bash
   /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate
   ```
   *The CLI tool that manages the Application Firewall. The command prints back to the screen whether the firewall is enabled or disabled, without needing to open System Settings.*
