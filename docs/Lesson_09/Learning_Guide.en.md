# Lesson 09: Networking
**Student Learning Guide (vEXP)**

## Lesson Objectives

* **Interfaces and Priorities** - Managing Network Locations and Service Order.
* **Diagnostic Tools** - Ping, Traceroute, and getting to know the `networksetup` super-command.
* **Firewall** - The built-in macOS Firewall and how it works.
* **Enterprise Seasoning** - Diagnosing Network Profiles, 802.1X, Proxy and VPNs.

## Overview

<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/67a8f7c6-ffba-4387-824a-b30a7eeef5ae/"></iframe></div>

## Terms & Concepts

* **Network Location:** A profile that bundles all of the Mac's network settings (active network services, IP addresses, DNS servers, and proxy). Multiple locations can be created to quickly switch between "home", "office", and more.
* **Service Order:** The order in which the Mac searches and connects to available networks. You can drag a service (e.g. Ethernet above Wi-Fi) to ensure the Mac prefers a wired connection when available.
* **Firewall:** The built-in firewall in macOS operates at the application level (Application Layer Firewall - ALF). It allows the user to control which applications or services are allowed to receive incoming connections from the network.
* **Stealth Mode:** A state within the firewall settings that prevents the Mac from responding to network scanning requests (such as ICMP Ping or discovery attempts), making it "invisible" to other computers.
* **802.1X Profile:** An advanced Network Authentication mechanism. In enterprise environments, a Configuration Profile is usually provided that automatically configures credentials and certificates to allow the Mac to securely connect to the corporate network transparently.
* **Proxy and VPN:** Communication tools used to route or encrypt traffic through a corporate server. On a managed Mac (MDM), these settings will often be locked and deployed remotely (e.g. Global HTTP Proxy).
* **ifconfig vs. ip:** While the `ifconfig` command is now considered legacy in most modern Linux distributions that have crossed over to the `ip` command, in macOS the command remains fully supported, usable, and highly efficient for core-level network diagnostics.

---

## Terminal Commands & Tools

### The Powerful `networksetup` Command
The `networksetup` command is the "Swiss Army Knife" for network management on the Mac from the terminal. Most configuration-altering commands must be run with administrator privileges (`sudo`).

**Displaying Information (no `sudo` required):**

* `networksetup -listallnetworkservices`
  > Displays a list of all network services (Wi-Fi, Ethernet, etc.). A service with an asterisk (*) next to it is a disabled service.

* `networksetup -getinfo "Wi-Fi"`
  > Displays the current IP, Subnet, and Router settings for the specified service.

* `networksetup -getmacaddress "Ethernet"`
  > Retrieves the physical MAC address (Hardware Address) of the specified network interface.

* `networksetup -getdnsservers "Wi-Fi"`
  > Displays the list of currently manually configured DNS servers for the Wi-Fi service.

* `networksetup -listlocations`
  > Displays all Network Locations currently existing on the system.

* `networksetup -getcurrentlocation`
  > Displays the currently active network location.

**Changing Configuration and IP/DNS Settings (requires privileges):**

* `sudo networksetup -setdhcp "Ethernet"`
  > Configures the Ethernet adapter to pull an IP address automatically from the DHCP server.

* `sudo networksetup -setmanual "Ethernet" 192.168.1.100 255.255.255.0 192.168.1.1`
  > Configures a static IP address, along with Subnet Mask and Router.

* `sudo networksetup -setdnsservers "Wi-Fi" 8.8.8.8 8.8.4.4`
  > Manually configures DNS servers (to clear manual servers and revert to DHCP, use the `empty` value).

**Managing Services and Locations:**

* `sudo networksetup -setnetworkserviceenabled "Bluetooth PAN" off`
  > Completely disables the specified network service.

* `sudo networksetup -createlocation "Office" populate`
  > Creates a new network location named "Office" and automatically populates it with the hardware services existing on the Mac.

* `sudo networksetup -switchtolocation "Office"`
  > Switches the system to a different network location and applies all relevant network settings of that location immediately.

### General Diagnostic and Testing Tools (Diagnostics)

* `ping -c 4 apple.com`
  > Sends 4 ICMP Echo Requests to the server to check if it's available and what the response time (Latency) is. The command will stop automatically after 4 attempts.

* `traceroute google.com`
  > Displays all the "stations" (routers/hops) the data passes through until reaching the destination. An excellent tool for diagnosing exactly where a network disconnect occurs.

* `nslookup apple.com`
  > Performs a simple DNS query and shows which IP address the server resolves the domain name to.

* `dig apple.com`
  > A more professional and detailed tool for checking DNS records, showing response times from the server and exact record types.

* `ifconfig`
  > A veteran UNIX command displaying core-level information (Interface Level) on all network cards and virtual networks. Geared more toward investigating the physical state or Container environments.

* `netstat -rn`
  > Displays the Mac's internal Routing Table.

* `lsof -i :80`
  > Shows which processes and applications are currently open on the Mac and listening to or connected via a specific port (in this example - port 80).

---

## Useful Paths

* `/Library/Preferences/SystemConfiguration/preferences.plist`
  > The main configuration file containing all the Mac's network interfaces and locations settings. Administrators sometimes delete this file to completely reset the network on the system in case of severe issues.

* `/Library/Preferences/com.apple.alf.plist`
  > The Application Layer Firewall (ALF) configuration file.

---

## Recommended Links and Further Reading

* [Use network locations on Mac](https://support.apple.com/en-us/105129) - Basic explanation on how to configure different network locations for quick transitions between home and office.
* [Change Firewall settings on Mac](https://support.apple.com/guide/mac-help/change-firewall-settings-on-mac-mh34041/mac) - A simple user guide on enabling the built-in firewall.
* [Connect to an 802.1X network on Mac](https://support.apple.com/guide/mac-help/connect-to-an-8021x-network-on-mac-mchlp1094/mac) - Guide to connecting to corporate wireless networks requiring special authentication.
* [Deploy Wi-Fi payload settings for Apple devices](https://support.apple.com/guide/deployment/wi-fi-payload-settings-dep40eb424c/web) - Enterprise article on deploying network settings via MDM server.

## Summary Video

<!-- Summary Video from YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/DDXfEIRgAxs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 💡 עזרים ויזואליים להרצאה (Presentation Visuals)

!!! tip "המחשה ויזואלית (עזר לתלמיד)"
    תמונות אלו ממחישות את הממשק או המנגנון הרלוונטי לנושא השיעור.

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
