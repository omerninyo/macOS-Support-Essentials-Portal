# Lesson 10: Sharing and Remote Access
**Student Learning Guide (Asset C)**

## Overview

<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/d4c324af-2882-4300-abb9-503dfb0683ee/"></iframe></div>

## Key Concepts

| Concept | Historical Background & Meaning from DeepDive |
| :--- | :--- |
| **AFP (Apple Filing Protocol)** | Protocol first introduced in 1988 and the default until OS X 10.8. Officially deprecated today. |
| **SMB (Server Message Block)** | Originally developed by IBM and adopted by Microsoft. Replaced AFP as the standard today, even for Macs. (Note: does not preserve APFS Sparse file space savings). |
| **Chooser** | A mythological app from System 7 (1991) for discovering servers and printers (AppleShare) - reminding us how Zero-Configuration (like AirDrop and Bonjour) is modern magic. |
| **Mac Sharing Mode / 1TR** | Replaces the historical Target Disk Mode. On Apple Silicon, the Mac acts as an SMB (file) server rather than a Block Device. Based on the Recovery environment (which only appeared in 2011). |

## SMB Protocol (Server Message Block)

- **The Absolute Standard:** The built-in protocol for network file sharing today. Connect via Finder using the `smb://` prefix.
- **Network Environment Sluggishness (DS_Store):** If SMB connection is very slow while navigating large folders on a Windows server, it stems from the Mac attempting to create `.DS_Store` files. Network admins can prevent this with a Terminal command:
  `defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE`

### Network Diagnostic Commands
- `smbutil statshares -a`: Displays active SMB connections, their encryption level, and protocol version (e.g., SMB 3.1.1).
- `mount_smbfs`: To mount SMB drives directly from the Terminal.
- `ping -c 5 [server]` or `netstat -an`: Basic network traffic diagnostics.

## Sharing Services & Connectivity

- **AirDrop:** Local file sharing without a router, using Bluetooth for discovery and Wi-Fi Direct (AWDL protocol) for high-speed data transfer. If discovery fails, turning Wi-Fi off and on helps reset the `awdl0` interface.
- **Screen Sharing:** Screen sharing based on an encrypted VNC mechanism. **Note:** The operating system (TCC) requires giving Screen Recording permission to the application, otherwise it shows an error or a black screen.
- **Universal Control:** Seamlessly use one keyboard/mouse across multiple nearby Macs or iPads on the same Apple ID (using Wi-Fi, Bluetooth, and the Rapportd service).

### Discovery & Sharing Commands
- `sharing -l`: Shows services and shared folders available via CLI (replacing System Settings navigation).
- `dns-sd -B _smb._tcp`: Browse and listen for SMB servers announcing themselves on the local network via Bonjour / mDNS technology.

## Mac Sharing Mode

- On Apple Silicon computers, activate this mode via Recovery Mode (Utilities > Share Disk).
- **IT Attention (First Aid):** Unlike in the past, the host computer cannot run `fsck` or Disk Utility to repair the faulty computer's drive. The disk is shared as a network folder (SMB) rather than a hardware block. Disk repair requires running First Aid from the faulty computer's own Recovery.

## Enterprise Seasoning: Single Sign-On (SSO)

- **Kerberos SSO Extension:** A built-in macOS extension allowing passwordless authentication against the Active Directory using a TGT (Ticket-Granting Ticket).
- The `klist` command displays the cryptographic tickets cached on the Mac.
- **Enterprise Restrictions (MDM):** It's important to know organizations can restrict sharing (like AirDrop) via Managed Open In technology, which recognizes AirDrop as an "Unmanaged" environment and blocks sensitive documents from transferring there.

---

## Recommended Links and Further Reading

* [Connect your Mac to shared computers and servers](https://support.apple.com/guide/mac-help/connect-mac-shared-computers-servers-mchlp1140/mac) 
* [Set up file sharing on Mac](https://support.apple.com/guide/mac-help/set-up-file-sharing-on-mac-mh17131/mac)
* [Intro to Kerberos Single Sign-on extension](https://support.apple.com/guide/deployment/intro-to-kerberos-single-sign-on-extension-dep0e8082f4d/web)
* [Universal Control: Use a single keyboard and mouse](https://support.apple.com/en-us/102459)

## Summary Video

<!-- Summary Video from YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/DDXfEIRgAxs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 💡 Presentation Visuals

!!! tip "Visual Aid (Student Aid)"
    These images illustrate the interface or mechanism relevant to the lesson topic.

![Slide71_image86](../assets/images/Lesson_10/L10_LegacySlide_Slide71_image86.png)
![Slide71_image87](../assets/images/Lesson_10/L10_LegacySlide_Slide71_image87.png)
