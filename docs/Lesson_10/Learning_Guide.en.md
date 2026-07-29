# Lesson 10: Sharing and Remote Access
**Student Learning Guide**


## Overview

<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/d4c324af-2882-4300-abb9-503dfb0683ee/"></iframe></div>

## Key Concepts

| Concept | Historical Background from DeepDive |
| :--- | :--- |
| **AFP (Apple Filing Protocol)** | A protocol first introduced in 1988 and the Apple default until OS X 10.8. Not officially supported today. |
| **SMB (Server Message Block)** | Originally developed at IBM and adopted by Microsoft. Replaced AFP and is the standard today, despite limitations with APFS Sparse files. |
| **Chooser** | A historical app from System 7 (1991) used to discover servers and printers (AppleShare) before the Zero-Configuration era (like AirDrop and Bonjour). |
| **Recovery / 1TR** | The recovery partition was first introduced only in 2011. Today on Apple Silicon processors (1 True Recovery) it is a secure environment that also serves as the basis for Mac Sharing Mode. |

## SMB Protocol (Server Message Block)

- **SMB - Server Message Block:** The primary and standard protocol in macOS today for network file sharing (replaced the old AFP).
- **SMB 3.x:** The modern version offering end-to-end encryption and better support for performance and unstable networks.

### SMB Commands (smbutil)

- `smbutil statshares -a`: Displays all currently active SMB connections and their properties (including SMB protocol version and encryption level).
- `smbutil lookup <hostname>`: Performs a Name Resolution query to an IP address in a NetBIOS/SMB environment.
- `smbutil view //user@server`: Displays the list of available shared folders on a specific server for the user.

## Sharing Services

- **File Sharing:** Enables remote access to files on the Mac via the SMB protocol.
- **Screen Sharing:** Screen sharing for other users or remote access, based on an upgrade of the VNC protocol.
- **Mac Sharing Mode:** (On Apple Silicon Macs) Allows connecting one Mac to another with a data cable (USB/Thunderbolt) and treating it as an external drive on a virtual local network (replaces the historical Target Disk Mode).

### Sharing Management in the Command Line (sharing)

- `sharing -l`: Displays all currently configured shared folders on the computer (Share Points).
- `sudo sharing -a <path>`: Adds a new folder to the shared folders list (Share Point).
- `sudo sharing -r <share_point_name>`: Removes a folder from the sharing list.
- `sudo sharing -e <share_point_name> -s <flags>`: Edits permissions or specific flags for an existing shared folder.

## Network Service Discovery (Bonjour & dns-sd)

- **Bonjour / mDNS:** Apple's Zero-configuration mechanism, allowing computers and services (such as printers, shared folders) to announce themselves on the local network without the need for a central DNS server (Multicast DNS).

### mDNS / Bonjour Commands (dns-sd)

- `dns-sd -B _smb._tcp`: "Browse" all SMB servers currently announcing themselves on the local network.
- `dns-sd -B _ssh._tcp`: Browse all SSH/Remote Login devices available in the environment.
- `dns-sd -B _ipp._tcp`: Browse network printers (Internet Printing Protocol).
- `dns-sd -L <Name> _smb._tcp`: "Lookup" a specific server discovered in the browse scan to get its exact IP address and port.

## Continuity and Wireless Connectivity

- **AirDrop:** Technology for fast file sharing between Apple devices in close proximity using Bluetooth (for the "handshake" and discovery) and Wi-Fi Direct P2P (for the actual data transfer without relying on a central router).
- **Universal Control:** A feature that allows using a single keyboard and mouse from one Mac to smoothly control other nearby Macs or iPads. The devices communicate over the same Wi-Fi and Bluetooth network.

## Enterprise Seasoning: Single Sign-On (SSO)

- **Kerberos SSO Extension:** A built-in extension in macOS allowing enterprise users to authenticate only once against the Active Directory / Identity Provider server.
- **TGT - Ticket-Granting Ticket:** The cryptographic "access ticket" that the Kerberos extension receives from the server, used to authenticate against other services (like SMB drives and Intranet) transparently and automatically without the need for an additional password.
- The enterprise MDM profile currently supports an Extensible SSO payload to uniformly configure domains across company computers.

---

## Recommended Links and Further Reading

* [Connect your Mac to shared computers and servers](https://support.apple.com/guide/mac-help/connect-mac-shared-computers-servers-mchlp1140/mac) - User guide on how to connect to network folders in an organization.
* [Set up file sharing on Mac](https://support.apple.com/guide/mac-help/set-up-file-sharing-on-mac-mh17131/mac) - Simple guide on setting up file sharing from your Mac to others.
* [Intro to Kerberos Single Sign-on extension](https://support.apple.com/guide/deployment/intro-to-kerberos-single-sign-on-extension-dep0e8082f4d/web) - Technical article for IT professionals on managing smart authentication (SSO) in a Kerberos environment.
* [Use AirDrop on your Mac](https://support.apple.com/en-us/102522) - Basic user guide for fast file sharing via AirDrop.
* [Universal Control: Use a single keyboard and mouse between Mac and iPad](https://support.apple.com/en-us/102459) - Guide explaining how to work with one mouse across multiple Apple devices simultaneously.
* [Transfer files using target disk mode / Mac Sharing Mode](https://support.apple.com/guide/mac-help/transfer-files-mac-computers-target-disk-mode-mchlp1443/mac) - User guide for transferring files by connecting two computers with a cable.

## Summary Video

<!-- Summary video from YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/DDXfEIRgAxs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>





!!! tip "Visual Aid (Student Reference)"
    These images illustrate the interface or mechanism relevant to the lesson topic.



<!-- src_hash: 3d28fbdb7671d3cc9f4242c69599e411ab8050f023b37387df84c6c8a2c4d573 -->


!!! tip "Visual Aids (Student Guide)"
    These images illustrate the relevant interface or mechanism for this lesson.

    ![Slide71 image86](../assets/images/Lesson_10/L10_LegacySlide_Slide71_image86.png)
    ![Slide71 image87](../assets/images/Lesson_10/L10_LegacySlide_Slide71_image87.png)
