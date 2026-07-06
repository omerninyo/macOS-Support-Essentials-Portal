# Lesson 10: Sharing and Remote Access
**Hands-On Lab (Student Practice)**

## Lab Objectives

- Enabling File Sharing and discovering network services (Bonjour) via the graphical interface.
- Connecting to File Sharing servers (SMB) using Finder.
- Getting familiar with fast computer-to-computer sharing using Mac Sharing Mode.

---

## Exercise 1: File Sharing and Discovering Network Services (Bonjour) via Finder
In this step, we will learn how to enable services on our Mac and discover similar services on the local network (using the system's built-in Bonjour protocol).

1. Open the **System Settings** app.
2. Navigate to **General** and then click on **Sharing**.
3. In the services list, toggle the switch next to **File Sharing**.
4. Click the info (**i**) button next to File Sharing. Here you can see the default shared folders (such as your Public Folder) and configure permissions for different users. When finished, click **Done**.
5. Now, we will locate other computers on the local network broadcasting services: Open a new **Finder** window.
6. In the Sidebar, under the **Locations** category, click on **Network**. (Alternatively, in the top menu bar click on **Go** and select **Network**, or use the shortcut `Shift + Command + K`).
7. The Network window will display all computers and servers available on the local network announcing themselves using Bonjour.
8. Double-clicking on one of the computers will display its shared folders and allow quick connection (for example, click on **Connect As** in the top right corner to enter credentials).

> **Diagnostic Note:** The Bonjour protocol operates on a local network basis only (mDNS). If you do not see other computers, there might be a network block, a router isolating users (Client Isolation), or a Firewall preventing this traffic.

---

## Exercise 2: Direct Connection to a File Server (SMB)
In an enterprise environment, we will typically be provided with the exact address of the file server and won't rely solely on automatic discovery.

1. Go to the **Finder** window.
2. In the top menu bar, click on **Go** and then select **Connect to Server** (Alternatively, use the keyboard shortcut `Command + K`).
3. In the address bar, type the server path using the SMB protocol. For example:
   `smb://server_address/share_name`
   *(The instructor will provide the specific server address for the lab in class, e.g., `smb://192.168.1.10/SharedFiles`)*.

4. Click the `+` button if you want to save this address in your favorites for quick access in the future.
5. Click the **Connect** button.
6. When the authentication prompt appears, select the **Registered User** option.
7. Enter the required username and password for the server. You can check **Remember this password in my keychain** to avoid password prompts next time.
8. Click **Connect** again.
9. Ensure the network Volume appears under **Locations** in the Finder sidebar, or as a mounted icon on the desktop. If you don't see it on the desktop, check in the Finder settings (under **Settings > General**) that the option to show connected servers is enabled.

---

## Exercise 3: Fast Sharing – Mac Sharing Mode
This exercise is intended to demonstrate how a Mac with an Apple Silicon processor shares its disk over the local network via a direct cable connection, a technique that replaces the traditional Target Disk Mode.

1. Ensure you have a high-quality Thunderbolt or USB-C cable designed for data transfer.
2. On the computer we want to share (the "Target Mac"), you need to boot into **Recovery Mode**:

   - Completely shut down the "Target Mac".
   - Turn it on by pressing and holding the Power Button until the text "Loading startup options" appears.
   - Click the settings icon (**Options**) and enter an Admin password to enter.
3. On the Recovery screen, navigate to the top menu bar, click on **Utilities**, and select **Share Disk** from the menu.
4. In the window that opens, select the desired Data Volume (usually named `Macintosh HD` or `Data`) and click the **Start Sharing** button.
5. Physically connect the cable between the two computers.
6. On the "Host Mac", open a **Finder** window. Under the **Locations** section in the sidebar, the "Target Mac" will now appear as a network drive.
7. Click on it. When prompted, click **Connect As** and enter the password of one of the users (with Admin privileges) from the "Target Mac" to decrypt the volume.
8. Upon finishing file transfers, you must perform a safe **Eject** on the "Host Mac" (clicking the eject icon next to the drive in Finder) before disconnecting the cable.
9. On the "Target Mac", click **Stop Sharing** and perform a normal Restart to the operating system.

---

## Extra Exercise / Technical Tip of the Iceberg

As IT professionals, we may sometimes want to discover network services or connect to servers via the terminal (for instance, when writing scripts or when the graphical interface is unresponsive).

1. **Discovering network services (Bonjour) using `dns-sd`**:
   You can use the following diagnostic command to listen for and discover File Sharing (SMB) services advertised on the local network, exactly as Finder does in the background:
   ```bash
   dns-sd -B _smb._tcp
   ```
   *The command will run continuously and print discovered servers. Press `Control + C` to stop it.*

2. **Connecting to an SMB server from the command line**:
   You can create a local folder, and mount the SMB server directly to it (instead of using the Connect to Server window):
   ```bash
   mkdir ~/NetworkShare
   mount_smbfs //username@server_address/share_name ~/NetworkShare
   ```
   *When finished, you can unmount the server using `umount ~/NetworkShare`.*

<!-- src_hash: c28294f8e4072fd2dbae6fdd5bed9a53ed8b0e16913c984ae35da0edb359ed3e -->
