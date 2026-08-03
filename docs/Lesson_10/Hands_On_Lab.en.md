# Lesson 10: Sharing and Remote Access
**Hands-On Lab (Student Exercise) (Asset D)**

## Lab Objectives

- Enabling File Sharing and identifying network services (Bonjour).
- Connecting to file servers (SMB) via Finder and the command line.
- Understanding quick sharing on Apple Silicon using Mac Sharing Mode and understanding diagnostic tool limitations.

---

## Exercise 1: File Sharing and Network Service Discovery (Bonjour) via Finder
In this section, we will learn how to enable services on our Mac and discover similar services on the local network (using Bonjour/mDNS protocol).

1. Open **System Settings**.
2. Navigate to **General** and click **Sharing**.
3. In the services list, toggle the switch next to **File Sharing**.
4. Click the Info button (**i**) next to File Sharing. Here you can view shared folders (such as Public folder) and configure permissions. Click **Done** when finished.
5. Now let's discover computers on the network: Open a new **Finder** window.
6. Under **Locations** in the sidebar, click **Network** (or press `Shift + Command + K`).
7. The Network window displays all servers advertising themselves via Bonjour.
8. Double-clicking any computer allows rapid connection (click **Connect As** to enter credentials).

> **Diagnostic Note:** If you do not see other computers, the Wi-Fi network may be blocking mDNS traffic (Client Isolation mode exists on certain routers). To verify this via Terminal, refer to the `dns-sd` command in the bonus section.

---

## Exercise 2: Direct Connection to a File Server (SMB)

In enterprise environments, you often need to type the full path to a server instead of relying on automatic discovery.

1. Open a **Finder** window.
2. In the top Menu Bar, select **Go** > **Connect to Server** (or press `Command + K`).
3. In the Server Address field, type the full server path using SMB protocol, for example:
   `smb://192.168.1.10/SharedFiles`
   *(The instructor will provide the exact lab address).*

4. Click the `+` button to save the address to Favorites, then click **Connect**.
5. Authenticate as a **Registered User**, enter credentials, and check **Remember this password in my keychain** for future convenience.
6. Click **Connect**. The network volume will appear under Locations in Finder or on the Desktop.

---

## Exercise 3: Quick Sharing (Mac Sharing Mode)

This exercise demonstrates extracting data from an Apple Silicon-based Mac while preserving FileVault encryption.
*(Note: Because this lab is conducted in a production environment, avoid shutting down live computers during class unless explicitly approved by the instructor).*

1. On the target Mac you wish to share ("Target Mac"), boot into **Recovery Mode** (press and hold power button from shut down state until Options appears).
2. After user authentication, click **Utilities** in the Menu Bar and select **Share Disk**.
3. Select the desired volume (such as `Macintosh HD`) and click **Start Sharing**.
4. Connect a data cable (Thunderbolt) between both computers.
5. On the "Host Mac", open **Finder** and go to **Network**. The "Target Mac" will appear as a file server!
6. Click it, select **Connect As**, and enter the Admin password of the Target Mac to decrypt storage.
7. **Critical IT Note:** If you open Disk Utility on the Host Mac, **you will not see the physical disk of the Target Mac**. This mode operates as an SMB server. You cannot run First Aid from the Host Mac on the shared Mac.
8. Upon completing file transfer, perform Eject, then on the Target Mac click **Stop Sharing** and Restart.

---

## IT Pro Bonus Exercise: Command Line (Terminal)

1. **Locating and Publishing Services using `dns-sd` and `sharing`**:
   To view the list of Share Points currently configured on the system, open Terminal and type:
   ```bash
   sharing -l
   ```
   To search for other SMB servers advertising on the local network, use the mDNS tool:
   ```bash
   dns-sd -B _smb._tcp
   ```
   *(This command runs continuously. Press `Control + C` to stop).*

2. **Connecting to a Server via Command Line (mount_smbfs)**:
   You can mount network shares directly via Terminal instead of using GUI windows:
   ```bash
   mkdir ~/Desktop/MyServer
   mount_smbfs //username@server_address/share_name ~/Desktop/MyServer
   ```
   To unmount, simply type `umount ~/Desktop/MyServer`.

<!-- src_hash: 4bb3d1aff5e9fd9201914e8d9d6a11220b1c0fe2edb0e552b96aa625745ff3d7 -->
