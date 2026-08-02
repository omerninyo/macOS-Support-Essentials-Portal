# Lesson 10: Sharing and Remote Access
**Hands-On Lab (Student Practice) (Asset D)**

## Lab Objectives

- Enable File Sharing and discover network services (Bonjour).
- Connect to file sharing servers (SMB) via Finder and the command line.
- Become familiar with fast sharing on Apple Silicon via Mac Sharing Mode and understand repair tool limitations.

---

## Exercise 1: File Sharing and Network Service Discovery (Bonjour) via Finder
In this step, we will learn how to enable services on our Mac and discover similar services on the local network (using the built-in Bonjour/mDNS protocol).

1. Open the **System Settings** app.
2. Navigate to **General** and then click **Sharing**.
3. In the services list, toggle the switch next to **File Sharing**.
4. Click the info button (**i**) next to File Sharing. Here you can see default shared folders (like your Public folder) and configure permissions. When finished, click **Done**.
5. Now let's discover computers on the network: Open a new **Finder** window.
6. Under **Locations** in the sidebar, click **Network** (or press `Shift + Command + K`).
7. The Network window will display all servers announcing themselves via Bonjour.
8. Double-clicking any computer enables a quick connection (click **Connect As** to enter credentials).

> **Diagnostic Note:** If you do not see other computers, the Wi-Fi network might be blocking mDNS traffic (a Client Isolation state found on some routers). To verify this via Terminal, see the `dns-sd` command in the bonus section.

---

## Exercise 2: Direct Connection to a File Server (SMB)

In a corporate environment, you will often need to type the full path to a server instead of relying on automatic discoveries.

1. Open a **Finder** window.
2. In the top menu bar, select **Go** > **Connect to Server** (or `Command + K`).
3. In the address bar, type the server path using the SMB protocol, for example:
   `smb://192.168.1.10/SharedFiles`
   *(The instructor will provide the exact address for the lab).*
4. Click the `+` button to save the address to favorites, then click **Connect**.
5. Authenticate as a **Registered User**, enter the password, and check **Remember this password in my keychain** for future convenience.
6. Click **Connect**. The network drive will appear under Locations in Finder or on your Desktop.

---

## Exercise 3: Rapid Sharing (Mac Sharing Mode)

This exercise demonstrates extracting data from an Apple Silicon-based Mac while preserving FileVault encryption. 
*(Note: Because the lab is done in a production environment, avoid shutting down live computers during class unless authorized by the instructor).*

1. On the computer we wish to share ("target computer"), enter **Recovery Mode** (long-press the power button from a powered-off state until Options appear).
2. After user authentication, in the top menu bar click **Utilities** and select **Share Disk**.
3. Select the desired volume (such as `Macintosh HD`) and click **Start Sharing**.
4. Connect the data cable (Thunderbolt) between the two computers.
5. On the "host computer", open **Finder** and go to **Network**. The "target computer" will appear there as a file server!
6. Click on it, select **Connect As**, and enter the "target computer's" Admin password to decrypt it.
7. **Critical IT Note:** If you now open Disk Utility on the host computer, **you will not see the target computer's physical disk**. This mode essentially acts as an SMB server. You cannot run First Aid from the host computer on the shared computer.
8. When copying is done, perform an Eject on the host, then on the target computer click **Stop Sharing** and Restart.

---

## Bonus Exercise for IT Professionals: Terminal

1. **Discovering and Publishing Services via `dns-sd` and `sharing`**:
   To list the Share Points currently configured on the system, open Terminal and enter:
   ```bash
   sharing -l
   ```
   To search for other SMB servers announcing themselves on the local network, use the mDNS tool:
   ```bash
   dns-sd -B _smb._tcp
   ```
   *(This command runs continuously. Press `Control + C` to stop it).*

2. **Connecting to a server from the command line (mount_smbfs)**:
   You can mount network drives directly via Terminal instead of using the graphical windows:
   ```bash
   mkdir ~/Desktop/MyServer
   mount_smbfs //username@server_address/share_name ~/Desktop/MyServer
   ```
   To disconnect, simply type `umount ~/Desktop/MyServer`.
