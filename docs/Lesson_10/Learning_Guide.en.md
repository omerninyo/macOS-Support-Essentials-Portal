# Lesson 10: Sharing and Remote Access
**Student Learning Guide (Asset C)**

## Overview

<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/d4c324af-2882-4300-abb9-503dfb0683ee/"></iframe></div>

## Key Concepts

| Concept | Historical Context & Significance (DeepDive) |
| :--- | :--- |
| **AFP (Apple Filing Protocol)** | Protocol introduced in 1988 and served as default until OS X 10.8. Officially deprecated today. |
| **SMB (Server Message Block)** | Originally developed by IBM and adopted by Microsoft. Replaced AFP and serves as the current standard, even for Macs. (Note: Does not preserve space savings for APFS Sparse files). |
| **Chooser** | Mythical app from System 7 (1991) for discovering servers and printers (AppleShare)—reminding us how modern Zero-Configuration (like AirDrop and Bonjour) is modern magic. |
| **Mac Sharing Mode / 1TR** | Replaces historical Target Disk Mode. On Apple Silicon, the Mac acts as an SMB file server rather than a Block Device. Based on the Recovery environment (introduced in 2011). |

## SMB Protocol (Server Message Block)

- **The Absolute Standard:** The built-in protocol for network file sharing today. Connected in Finder using the `smb://` prefix.
- **Network Sluggishness (.DS_Store):** If SMB connection feels sluggish when browsing large directories on a Windows server, this stems from the Mac attempting to create `.DS_Store` files. Network administrators can prevent this via Terminal command:
  `defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE`

### Diagnostic and Network Troubleshooting Commands
- `smbutil statshares -a`: Displays active SMB connections, encryption levels, and protocol versions (e.g., SMB 3.1.1).
- `mount_smbfs`: For mounting SMB shares directly from Terminal.
- `ping -c 5 [server]` or `netstat -an`: Basic network traffic diagnostics.

## Sharing Services and Connectivity

- **AirDrop:** Local peer-to-peer file sharing without a router, using Bluetooth for discovery and Wi-Fi Direct (AWDL protocol) for high-speed data transfer. In case of discovery issues, toggling Wi-Fi helps reset the `awdl0` interface.
- **Screen Sharing:** Screen sharing based on VNC wrapped in security layer. **Note:** Operating system security (TCC) requires granting Screen Recording permissions to the application; otherwise, an error or black screen will occur.
- **Universal Control:** Seamless operation using a single keyboard/mouse across adjacent Macs/iPads signed into the same Apple ID (utilizing Wi-Fi, Bluetooth, and the `rapportd` service).

### Discovery and Sharing Commands
- `sharing -l`: Displays active sharing services and share points via CLI (replacing System Settings navigation).
- `dns-sd -B _smb._tcp`: Searches for and listens to SMB servers advertising themselves on the local network via Bonjour / mDNS technology.

## Mac Sharing Mode

- On Apple Silicon Macs, this mode is invoked via Recovery Mode (Utilities > Share Disk).
- **IT Pro Warning (First Aid):** Unlike legacy modes, the host computer cannot execute `fsck` or Disk Utility repair commands on the target Mac's drive. The drive is shared as a network share (SMB), not a block storage device. Disk repair requires running First Aid directly from the target Mac's own Recovery mode.

## Enterprise Seasoning: Single Sign-On (SSO)

- **Kerberos SSO Extension:** Built-in macOS extension allowing single sign-on (passwordless) authentication against Active Directory using TGT (Ticket-Granting Ticket).
- The `klist` command displays cached cryptographic tickets on the Mac.
- **Enterprise Restrictions (MDM):** It is important to note that organizations can restrict file sharing (such as AirDrop) via Managed Open In technology, which identifies AirDrop as an "Unmanaged" destination and blocks transfer of sensitive enterprise documents.

---

## Recommended Links and Further Reading

* [Connect your Mac to shared computers and servers](https://support.apple.com/guide/mac-help/connect-mac-shared-computers-servers-mchlp1140/mac) 
* [Set up file sharing on Mac](https://support.apple.com/guide/mac-help/set-up-file-sharing-on-mac-mh17131/mac)
* [Intro to Kerberos Single Sign-on extension](https://support.apple.com/guide/deployment/intro-to-kerberos-single-sign-on-extension-dep0e8082f4d/web)
* [Universal Control: Use a single keyboard and mouse](https://support.apple.com/en-us/102459)

## Summary Video

<!-- Summary Video from YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/p1hW4lTaHOY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 💡 Visual Presentation Aids (Presentation Visuals)

!!! tip "Visual Demonstration (Student Auxiliary)"
    These images illustrate the interface or mechanism relevant to the lesson topic.

![Slide71_image86](../assets/images/Lesson_10/L10_LegacySlide_Slide71_image86.png)
![Slide71_image87](../assets/images/Lesson_10/L10_LegacySlide_Slide71_image87.png)

<!-- src_hash: 5f20867470ad57b74562bac4aade57277422c3b0d02529f7200ed8bc06d5d669 -->
