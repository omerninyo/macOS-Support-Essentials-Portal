# Lesson 10: Sharing and Remote Access
**Student Learning Guide (Asset C)**

## 🎧 Podcast Overview

<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/d4c324af-2882-4300-abb9-503dfb0683ee/"></iframe></div>

---

## Key Concepts

| Concept | Background & Significance |
| :--- | :--- |
| **SMB (Server Message Block)** | The current and exclusive file sharing standard in macOS. Originally developed by IBM and adopted by Microsoft, it has entirely replaced Apple's legacy AFP protocol. |
| **AFP (Apple Filing Protocol)** | Apple's legacy file sharing protocol (dating back to 1988). It is officially deprecated and unsupported in modern environments. |
| **Mac Sharing Mode / 1TR** | The modern replacement for the historic Target Disk Mode. On Apple Silicon, to protect volume encryption, the Mac operates as an isolated SMB file server rather than a block-level device, and can only be initiated from the macOS Recovery environment. |
| **Bonjour / mDNS** | Apple's implementation of zero-configuration networking, enabling automatic discovery of servers and services on the local network. |
| **Kerberos SSO Extension** | A built-in macOS extension providing passwordless, transparent authentication to Active Directory-based enterprise network drives using Ticket Granting Tickets (TGT). |

> [!NOTE]
> **Technical Note:** The SMB protocol is not inherently aware of the storage-efficient structure of APFS (such as Sparse files or Clones). Therefore, copying an APFS-optimized file to an SMB server will "inflate" it to its full logical size.

> *→ APFS Sparse Files, Clones, and APFS storage efficiency mechanisms were covered in Lesson 06 (FileSystem) — here we see that SMB does not preserve them and inflates the file.*

---

## Sharing Services & Connectivity

| Service | Explanation & Operation |
|---|---|
| **AirDrop** | Local file sharing utilizing Bluetooth for proximity discovery and Wi-Fi Direct (AWDL protocol) for high-speed data transfer without a router. If AirDrop fails to discover devices, toggling Wi-Fi off and on resets the `awdl0` interface. |
| **Screen Sharing** | Built-in screen sharing capabilities based on the VNC framework. It requires granting **Screen Recording** permissions in TCC (Privacy & Security); otherwise, the connection will result in a black screen or an error. |
| **Universal Control** | Seamless operation across multiple nearby Macs and iPads signed into the same Apple ID using a single keyboard and mouse (powered by the Rapportd service). |

> [!IMPORTANT]
> **Screen Sharing + TCC:** If Screen Sharing is enabled but displays a black screen, the issue is almost always a missing **Screen Recording** permission in TCC. In an enterprise environment, deploy this permission via a PPPC Profile (Privacy Payload) rather than relying on end users to approve it manually.

---

## Working with SMB (Server Message Block)

- Connect to servers via the **Connect to Server** dialog in Finder using the `smb://` prefix.
- **Enterprise Network Latency:** If SMB connections suffer from severe latency when navigating folders on a Windows server, it is often due to Finder attempting to create hidden `.DS_Store` files. You can prevent this behavior using the following Terminal command:
  ```bash
  defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE
  ```

---

## Mac Sharing Mode

An advanced sharing mode used for diagnostics and data extraction from an Apple Silicon Mac experiencing an OS failure.
- Initiated via **Recovery Mode** by navigating to the **Utilities** menu > **Share Disk**.
- The host computer will recognize the failing Mac as an SMB network folder under the **Network** location.

> [!WARNING]
> **Critical IT Alert (First Aid):** Unlike the legacy Target Disk Mode, you cannot run disk repair commands or use Disk Utility from the host computer on the failing Mac. The disk is exposed at the file level (SMB) and not as a block-level device. Disk repairs must be performed directly from the Recovery environment of the failing Mac itself!

> *→ FileVault covered in Lesson 04 (Encryption) is the reason why an Admin password is required to connect in Mac Sharing Mode — the Volume Owner authorizes access via the Secure Enclave.*

---

## Diagnostics & Command Line (Terminal)

| Command | Description |
|---|---|
| `smbutil statshares -a` | Displays active SMB connections, encryption levels, and the negotiated protocol version (e.g., SMB 3.1.1). |
| `mount_smbfs` | Command to mount SMB drives directly from the CLI. |
| `sharing -l` | Lists all sharing services and share points currently available on the system. |
| `dns-sd -B _smb._tcp` | Scans the local network via Bonjour and lists SMB servers broadcasting their presence. |
| `klist` | Displays the cryptographic tickets (TGTs) cached by the Kerberos SSO extension on the Mac. |

---

## Enterprise Seasoning: MDM Restrictions & File Sharing

In large organizations, security departments utilize Mobile Device Management (MDM) to restrict data exfiltration (Data Loss Prevention - DLP). The **Managed Open In** feature enforces boundaries between corporate and personal applications.
Because AirDrop is classified as an "Unmanaged Destination," enterprise users may find themselves unable to share corporate files via AirDrop, as the MDM profile actively blocks the transfer.

---

## Recommended Links & Further Reading

* [Connect your Mac to shared computers and servers](https://support.apple.com/guide/mac-help/connect-mac-shared-computers-servers-mchlp1140/mac) 
* [Set up file sharing on Mac](https://support.apple.com/guide/mac-help/set-up-file-sharing-on-mac-mh17131/mac)
* [Intro to Kerberos Single Sign-on extension](https://support.apple.com/guide/deployment/intro-to-kerberos-single-sign-on-extension-dep0e8082f4d/web)
* [Universal Control: Use a single keyboard and mouse](https://support.apple.com/en-us/102459)

---

## 🎬 Summary Video

<!-- Summary Video from YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/p1hW4lTaHOY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

## 💡 Presentation Visuals

!!! tip "Visual Aids (Student Reference)"
    These images illustrate the relevant interfaces or mechanisms discussed in this lesson.

![Slide71_image86](../assets/images/Lesson_10/L10_LegacySlide_Slide71_image86.png)
![Slide71_image87](../assets/images/Lesson_10/L10_LegacySlide_Slide71_image87.png)
