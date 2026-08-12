# Lesson 10: Sharing and Remote Access
**Hands-On Lab (Student Practice) (Asset D)**

## Lab Objectives

- Enable File Sharing and identify network services using Bonjour.
- Connect to SMB file sharing servers via the Finder GUI and the Command Line.
- Familiarize yourself with rapid sharing on Apple Silicon via Mac Sharing Mode and understand the limitations of disk repair tools in this state.

---

## Exercise 1: File Sharing and Network Service Discovery (Bonjour) via Finder

**What you will learn:** Basic hands-on experience enabling a file sharing service on the Mac and locating similar servers on the local network using Bonjour zero-configuration technology through the Finder interface.

1. Open the **System Settings** application.
2. Navigate to **General** and then click on **Sharing**.
3. In the services list, toggle the switch next to **File Sharing** to turn it on.
4. Click the information (**i**) button next to File Sharing. Here you can view shared folders (such as the Public folder) and configure access permissions. When finished, click **Done**.
5. Now, let's locate computers on the network: Open a new **Finder** window.
6. Under **Locations** in the sidebar, click on **Network** (or use the shortcut `Shift + Command + K`).
7. The network window will display all servers broadcasting their presence via Bonjour. 
8. Double-clicking on one of the computers will initiate a quick connection (click **Connect As** to enter authentication credentials if required).

> [!NOTE]
> **Diagnostics Note:** If you do not see other computers in the Network window, it is highly likely that the Wi-Fi network is blocking mDNS traffic (a security feature known as Client Isolation, commonly found on public or guest routers).

---

## Exercise 2: Direct Connection to a File Server (SMB)

**What you will learn:** Establishing a direct, address-based connection (using the SMB protocol) to a file server, and learning the workflow for saving server paths as favorites.

1. Open a **Finder** window.
2. From the top menu bar, select **Go** > **Connect to Server** (or use the shortcut `Command + K`).
3. In the Server Address field, type the server path using the SMB protocol, for example:
   `smb://192.168.1.10/SharedFiles`
   *(Your instructor will provide the exact address for this lab).*

4. Click the `+` button to save the address to your favorite servers list, then click **Connect**.
5. Authenticate as a **Registered User**, enter your password, and check the box to **Remember this password in my keychain** for future convenience. 
6. Click **Connect**. The network drive will mount and appear under Locations in the Finder sidebar or directly on your desktop.

---

## Exercise 3: Rapid Sharing (Mac Sharing Mode)

**What you will learn:** Utilizing the Share Disk tool from the Recovery Mode on Apple Silicon Macs to extract data from a "failing Mac" (acting as an SMB server), while understanding the limitations of Disk Utility over this connection type.

> [!WARNING]
> **Attention:** Because this lab is conducted in a production environment, avoid shutting down live computers to perform this exercise unless explicitly authorized by the instructor.

1. On the Mac you wish to share (the "Target Mac"), boot into **Recovery Mode** (press and hold the power button while the Mac is powered off until the Options screen appears).
2. After user authentication, click on **Utilities** in the menu bar and select **Share Disk**.
3. Select the desired volume (e.g., `Macintosh HD`) and click **Start Sharing**.
4. Connect a Thunderbolt data cable between the two Macs.
5. On the "Host Mac," open **Finder** and navigate to **Network**. The Target Mac will appear there as a file server (SMB).
6. Click on it, select **Connect As**, and enter the Target Mac's Admin password to decrypt the volume.
7. **Critical IT Emphasis:** If you open Disk Utility on the Host Mac right now, **you will not see the physical disk of the Target Mac**. This setup essentially functions as an SMB share. You cannot run First Aid from the Host Mac on the shared volume. 
8. Once your data copy is complete, eject the drive from the Host Mac. Then, on the Target Mac, click **Stop Sharing** and proceed to Restart.

---

## Bonus Exercise for IT Professionals: The Command Line (Terminal)

**What you will learn:** Executing more complex sharing operations from the command line, such as scanning the network for hidden mDNS services and mounting SMB drives directly from the Terminal.

1. **Discovering and Publishing Services with `dns-sd` and `sharing`**:
   To view the list of sharing services (Share Points) currently configured on the system, open the Terminal and type:
   ```bash
   sharing -l
   ```
   To scan for other SMB servers announcing themselves on the local network, utilize the mDNS tool:
   ```bash
   dns-sd -B _smb._tcp
   ```
   *(This command runs continuously. Press `Control + C` to stop the scan).*

2. **Connecting to a Server from the Command Line (`mount_smbfs`)**:
   Network drives can be mounted directly via the Terminal instead of relying on the GUI windows.
   First, create a mount point directory:
   ```bash
   mkdir ~/Desktop/MyServer
   ```
   Then initiate the connection (a password prompt will appear):
   ```bash
   mount_smbfs //username@server_address/share_name ~/Desktop/MyServer
   ```
   To cleanly unmount the drive when finished: 
   ```bash
   umount ~/Desktop/MyServer
   ```
