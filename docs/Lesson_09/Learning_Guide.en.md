# Lesson 09: Networking
**Student Guide (vEXP)**

## Lesson Objectives

*   **Interfaces and Priorities** - Managing Network Locations and Service Order.
*   **Diagnostic Tools** - Ping, Traceroute, and an introduction to the powerful `networksetup` command.
*   **Firewall** - The built-in macOS Firewall and how it operates.
*   **Enterprise Flavor** - Diagnosing enterprise 802.1X Wi-Fi profiles and remotely deployed VPN proxy connections.

## Overview

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/67a8f7c6-ffba-4387-824a-b30a7eeef5ae/"></iframe></div>

## Terms & Concepts

*   **Network Location:** A profile that consolidates all network settings for the Mac (active network services, IP addresses, DNS servers, and proxy settings). Multiple locations can be created to quickly switch between "Home," "Office," and other configurations.
*   **Service Order:** The sequence in which the Mac searches for and connects to available networks. Services can be dragged (e.g., Ethernet above Wi-Fi) to ensure the Mac prioritizes a wired connection when available.
*   **Firewall:** The built-in macOS Firewall operates at the Application Layer (Application Layer Firewall - ALF). It allows the user to control which applications or services are permitted to receive incoming connections from the network.
*   **Stealth Mode:** A setting within the Firewall that prevents the Mac from responding to network scan requests (such as ICMP Ping or discovery attempts), making it "invisible" to other computers.
*   **802.1X Profile:** An advanced network-level authentication mechanism. In enterprise environments, a Configuration Profile is typically provided to automatically define the credentials and certificates, enabling the Mac to securely and transparently connect to the corporate network.
*   **Proxy and VPN:** Communication tools used to route or encrypt traffic through an enterprise server. On a managed Mac (MDM), these settings are often locked and deployed remotely (e.g., Global HTTP Proxy).
*   **ifconfig vs. ip:** While the `ifconfig` command is now considered legacy in most modern Linux distributions that have transitioned to the `ip` command, in macOS, it remains a supported, fully functional, and highly effective tool for core-level network diagnostics.

---

## Advanced Terminal Commands & Tools

### The Powerful `networksetup` Command
The `networksetup` command is the "Swiss Army knife" for managing network settings on a Mac from the Terminal. Most configuration-altering commands require administrator privileges (`sudo`).

**Displaying Information (no `sudo` required):**

*   `networksetup -listallnetworkservices`
    > Lists all network services (Wi-Fi, Ethernet, etc.). A service marked with an asterisk (*) is disabled.

*   `networksetup -getinfo "Wi-Fi"`
    > Displays the current IP, Subnet, and Router settings for the specified service.

*   `networksetup -getmacaddress "Ethernet"`
    > Retrieves the physical MAC address (Hardware Address) of the specific network adapter.

*   `networksetup -getdnsservers "Wi-Fi"`
    > Shows the list of DNS servers currently manually configured for the Wi-Fi service.

*   `networksetup -listlocations`
    > Displays all existing Network Locations on the system.

*   `networksetup -getcurrentlocation`
    > Shows the currently active Network Location.

**Changing Configuration and IP/DNS Settings (requires privileges):**

*   `sudo networksetup -setdhcp "Ethernet"`
    > Configures the Ethernet adapter to automatically obtain an IP address from the DHCP server.

*   `sudo networksetup -setmanual "Ethernet" 192.168.1.100 255.255.255.0 192.168.1.1`
    > Configures a static IP address, along with the Subnet Mask and Router.

*   `sudo networksetup -setdnsservers "Wi-Fi" 8.8.8.8 8.8.4.4`
    > Manually configures DNS servers (to remove manual servers and revert to DHCP, use the value `empty`).

**Managing Services and Locations:**

*   `sudo networksetup -setnetworkserviceenabled "Bluetooth PAN" off`
    > Completely disables the specified network service.

*   `sudo networksetup -createlocation "Office" populate`
    > Creates a new network location named "Office" and automatically populates it with the Mac's existing hardware services.

*   `sudo networksetup -switchtolocation "Office"`
    > Switches the system to a different network location and immediately applies all relevant network settings for that location.

### General Diagnostic and Testing Tools (Diagnostics)

*   `ping -c 4 apple.com`
    > Sends 4 ICMP Echo Requests to a server to check its availability and response time (Latency). The command will stop automatically after 4 attempts.

*   `traceroute google.com`
    > Displays all the "hops" (routers) that data traverses to reach its destination. An excellent tool for diagnosing exactly where a network disconnection occurs.

*   `nslookup apple.com`
    > Performs a simple DNS query and shows which IP address the server resolves the domain name to.

*   `dig apple.com`
    > A more professional and detailed tool for checking DNS records, displaying server response times and precise record types.

*   `ifconfig`
    > A venerable UNIX command that displays core-level (Interface Level) information about all network adapters and virtual networks. More suited for investigating physical status or container environments.

*   `netstat -rn`
    > Displays the Mac's internal Routing Table.

*   `lsof -i :80`
    > Shows which processes and applications are currently open on the Mac and listening or connected to a specific port (in this example - port 80).

---

## Useful Paths

*   `/Library/Preferences/SystemConfiguration/preferences.plist`
    > The main configuration file containing all network interface and location settings for the Mac. Administrators sometimes delete this file to completely reset the system's network in case of severe issues.

*   `/Library/Preferences/com.apple.alf.plist`
    > The configuration file for the Application Layer Firewall (ALF).

---

## Recommended Links and Further Reading

*   [Use network locations on Mac](https://support.apple.com/en-us/105129) - Basic explanation of how to configure different network locations for quick transitions between home and office.
*   [Change Firewall settings on Mac](https://support.apple.com/guide/mac-help/change-firewall-settings-on-mac-mh34041/mac) - A simple user guide on enabling the built-in firewall.
*   [Connect to an 802.1X network on Mac](https://support.apple.com/guide/mac-help/connect-to-an-8021x-network-on-mac-mchlp1094/mac) - Guide for connecting to enterprise wireless networks that require special authentication.
*   [Deploy Wi-Fi payload settings for Apple devices](https://support.apple.com/guide/deployment/wi-fi-payload-settings-dep40eb424c/web) - An enterprise article on deploying network settings using an MDM server.

## Summary Video

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/5uY9kabOEXE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 💡 Presentation Visuals

!!! tip "Visual Illustration (Student Aid)"
    These images illustrate the interface or mechanism relevant to the lesson topic.

![Slide131_image161](../assets/images/Lesson_09/L09_LegacySlide_Slide131_image161.png)
![Slide131_image45](../assets/images/Lesson_09/L09_LegacySlide_Slide131_image45.jpg)
![Slide133_image161](../assets/images/Lesson_09/L09_LegacySlide_Slide133_image161.png)
![Slide133_image45](../assets/images/Lesson_09/L09_LegacySlide_Slide133_image45.jpg)
![Slide134_image164](../assets/images/Lesson_09/L09_LegacySlide_Slide134_image164.png)
![Slide23_image41](../assets/images/Lesson_09/L09_LegacySlide_Slide23_image41.jpg)
![Slide74_image14](../assets/images/Lesson_09/L09_LegacySlide_Slide74_image14.jpg)
![Slide74_image15](../assets/images/Lesson_09/L09_LegacySlide_Slide74_image15.jpg)
![Slide99_image103](../assets/images/Lesson_09/L09_LegacySlide_Slide99_image103.png)
![Slide99_image30](../assets/images/Lesson_09/L09_LegacySlide_Slide99_image30.jpg)
![Slide99_image31](../assets/images/Lesson_09/L09_LegacySlide_Slide99_image31.jpg)
![26-Tahoe-Finder-Connect-to-Server-scaled](../assets/images/Lesson_09/L09_TahoeUI_26-Tahoe-Finder-Connect-to-Server-scaled.png)
![26-Tahoe-Finder-Network-scaled](../assets/images/Lesson_09/L09_TahoeUI_26-Tahoe-Finder-Network-scaled.png)
![26-Tahoe-Settings-Network-scaled](../assets/images/Lesson_09/L09_TahoeUI_26-Tahoe-Settings-Network-scaled.png)
![26-Tahoe-Settings-Wi-Fi-scaled](../assets/images/Lesson_09/L09_TahoeUI_26-Tahoe-Settings-Wi-Fi-scaled.png)

<!-- src_hash: 4434d3344835e5dd1a33c5446cb8c1d22c7a23bec0fe34bf04a9c9c55f2163ea -->
