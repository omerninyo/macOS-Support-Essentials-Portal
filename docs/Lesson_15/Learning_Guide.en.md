# Lesson 15: Diagnostics
**Student Learning Guide**

## Overview

<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/1a3db037-3234-40d2-bcb4-7bb56b307bc4/"></iframe></div>

## Core Concepts & Methodologies

* **Isolation:** Apple's core troubleshooting strategy, which aims to cut the problem in half at every step to isolate the root cause:
  * **User vs. System:** Creating a new Test User to check whether the issue exists only within a specific user's profile (their settings, their LaunchAgents) or if it is a System-wide issue.
  * **Software vs. Hardware:** Booting the Mac into macOS Recovery or running Apple Diagnostics to rule out hardware failure. If the issue doesn't occur in an alternate operating system environment, the root cause is software-related.
  * **Network vs. Client:** Connecting the Mac to a different network (e.g., a cellular Hotspot) to check if the issue is related to the corporate Firewall settings or the local ISP.

> *→ LaunchAgents and LaunchDaemons covered in Lesson 08 (Terminal) are critical for understanding the User vs. System isolation phase—a process running from the user's Library folder is an Agent, whereas a process running from the shared /Library is a Daemon.*
* **Apple Diagnostics:** A hardware diagnostic tool built directly into the device's firmware, designed to test physical components such as RAM, fans, battery, and sensors. On Apple Silicon Macs, you invoke it from the Startup Options menu (press and hold the power button) and then press `Command + D`.
* **Verbose Mode:** A boot mode (more relevant on Intel Macs using `Command + V`) that displays the boot process text instead of the Apple logo. Today, on Apple Silicon, this is mostly replaced by deep log analysis after the OS boots.
* **Activity Monitor & Console (Brief History):** The Activity Monitor app debuted in 2003 (Mac OS X Panther) as a merger of Process Viewer and CPU Monitor. In the past, the Console app parsed simple text files, but starting with macOS Sierra in 2016, Apple transitioned to the Unified Logging System—a binary-based, centralized logging architecture capable of handling thousands of events per second.

!!! tip "Deep Dive 🤿: What Does Activity Monitor Actually Measure?"
    On Apple Silicon Macs, the metrics in Activity Monitor can sometimes be misleading and do not represent absolute hardware data:

    * **CPU %:** Can exceed 100% (each core counts as 100%), but this measurement does not reflect exact load due to the asymmetric architecture (E-cores and P-cores).
    * **Energy Impact:** This is a relative algorithm-based Score, not a physical measurement in Watts.
    * **Takeaway for IT Support:** Use these numbers solely to identify "Runaway Processes," rather than for surgical performance benchmarking. [Read the full Eclectic Light article](https://eclecticlight.co/2026/06/29/what-does-activity-monitor-measure/)
* **App Memory Leaks:** A condition where an application continuously consumes more RAM without releasing it back to the system. This causes severe system sluggishness (the dreaded Beachball), but usually without increased fan noise (which typically indicates CPU load). The solution is to monitor memory consumption in the Memory tab of Activity Monitor and Force Quit the application. Conversely, Kernel Memory Leaks are rare and far more severe, leading to a complete system crash (Kernel Panic). [Read more from Eclectic Light](https://eclecticlight.co/2026/06/19/what-can-you-do-when-an-app-uses-too-much-memory/)

## Safe Mode

> *→ Safe Mode was mentioned in Lesson 11 (Peripherals) as a solution for Bluetooth and general peripheral issues—here we uncover what happens behind the scenes.*

Safe Mode is a powerful diagnostic tool that often resolves issues simply by being invoked, as it flushes caches and resets system components.

**What happens when booting a Mac in Safe Mode?**

* **Directory Check:** The system runs a logical check and repair of the startup volume using the `fsck` (File System Consistency Check) process.

!!! important
    `fsck_apfs` runs automatically during a Safe Boot. If the SSD is corrupted, the Mac might appear to hang during boot for a long time without any visual progress indicator. Wait at least 10 minutes before assuming the Mac is permanently stuck.

* **Disables Extensions:** Prevents the loading of third-party Kernel Extensions (Kexts).
* **Blocks Background Processes:** Prevents third-party LaunchDaemons and LaunchAgents from executing. Only built-in system services are loaded.
* **Blocks Login Items:** Prevents user-configured applications and windows from launching automatically at login.
* **Clears Caches:** Temporarily deletes font caches, the Kernel cache, and System Caches, which are often the culprits behind sudden application crashes.
* **Disables Hardware Acceleration:** Disables graphics accelerators, which may cause the screen to flicker, the mouse to lag, or video playback to fail. This is expected behavior and proves that Safe Mode is active.

**How to enter Safe Mode:**

* **Apple Silicon:** Shut down the Mac. Press and hold the power button until "Loading startup options" appears. Select the startup disk, press and hold the `Shift` key, and click "Continue in Safe Mode".
* **Intel:** Power on the Mac and immediately press and hold the `Shift` key until the login window appears.

## The Terminal Toolkit (CLI Diagnostics)

A list of essential commands for IT technicians for advanced system investigation and diagnostics.

### Comprehensive System Information (`system_profiler`)
This command is the CLI counterpart to the System Information app, allowing you to export complete hardware and software data.

* `system_profiler SPSoftwareDataType` - Displays macOS version, Build ID, Kernel version, and system Uptime.
* `system_profiler SPHardwareDataType` - Displays CPU info, core count, memory, Serial Number, and Hardware UUID.
* `system_profiler SPPowerDataType` - Displays battery metrics, including Cycle Count and battery health Condition.
* `system_profiler > ~/Desktop/MacReport.txt` - Exports the complete, full system report to a text file on the desktop to send to an escalation tier.

### Advanced Network Quality Testing (`networkQuality`)
A built-in utility (starting from macOS Monterey) that tests not only download/upload speeds but also the network's Responsiveness under load.

* `networkQuality` - Runs the standard test utilizing parallel connections to Apple's servers.
* `networkQuality -v` - Runs the test with verbose output, detailing specific Latency metrics.
* `networkQuality -s` - Runs the network test sequentially rather than in parallel; an excellent tool for isolating data throughput issues.

### Querying the Logging System (`log show`)
The Unified Logging System in macOS replaced legacy plain-text files and requires the `log` command to extract precise historical data.

* `log show --last 10m` - Displays all logs recorded in the last 10 minutes.
* `log show --predicate 'process == "kernel"' --last 1h` - Filters and displays only logs generated by the core kernel process from the last hour.
* `log show --info --debug --last 5m > ~/Desktop/logs.txt` - Extracts transient Info and Debug level logs (which aren't always persisted to disk) and exports them to a file for comfortable parsing.

### Enterprise Identity Diagnostics via Kerberos (`klist`)
In Active Directory-based enterprise environments, Kerberos is utilized for Single Sign-On (SSO) to network services. This command helps verify if the user successfully acquired a Ticket from the server.

* `klist` - Lists the user's active Kerberos tickets. If the list is empty, the user lacks SSO privileges.
* `klist -v` - Displays verbose information about the ticket, including start times, expiration dates, and encryption types, to spot an expired validity.

## Additional Networking Commands for Isolation

* `ping -c 4 8.8.8.8` - Sends 4 ICMP packets to Google's servers to test basic internet connectivity and response times.
* `traceroute google.com` - Displays the network routing path (Hops) from the Mac to the destination server, enabling you to pinpoint where traffic is dropping inside the corporate network.
* `ifconfig` - Displays low-level technical information about physical network interfaces (MAC Addresses).
* `networksetup -listallhardwareports` - The most readable and straightforward way to identify physical MAC addresses for all network connection types on the system.

## Enterprise Seasoning (Enterprise Diagnostics)

* **Diagnostics with MDM Profiles:** Frequently, MDM security configurations clash with standard operations (e.g., USB blocking, Wi-Fi restrictions). If an issue persists, an IT technician will consider temporarily removing the specific configuration profile via System Settings > Privacy & Security > Profiles (provided it wasn't deployed as non-removable) to isolate if the MDM payload is the culprit.
* **Bypassing Network Filtering:** In organizations utilizing Content Filters or Proxies, isolating an issue will often involve connecting the Mac to an external cellular hotspot to verify if the corporate web filter is blocking traffic to Apple domains.
* **Removing Agents:** Disabling third-party endpoint security tools (such as Antivirus, EDR, or DLP solutions) that might be crashing and triggering Kernel Panics or noticeable system throttling.

---

## Recommended Reading & Links
* [What can you do when an app uses too much memory](https://eclecticlight.co/2026/06/19/what-can-you-do-when-an-app-uses-too-much-memory/) - Guide on diagnosing and resolving Memory Leaks.

* [Start up your Mac in safe mode](https://support.apple.com/en-us/116946) - Basic user guide on how to boot into Safe Mode for troubleshooting.
* [Use Apple Diagnostics to test your Mac](https://support.apple.com/en-us/102550) - User guide on invoking the built-in diagnostic tool to identify hardware failures.
* [Unified Logging (log command line tool)](https://developer.apple.com/documentation/os/logging) - Advanced documentation on Apple's unified logging system and CLI querying.
* [If your Mac restarts and a message appears (Kernel Panics)](https://support.apple.com/en-us/102566) - Support article explaining Kernel Panics and identifying root causes.
* [Identify your Mac hardware (System Information)](https://support.apple.com/en-us/102849) - How to utilize System Information to gather hardware telemetry.

## Summary Video

<!-- Summary Video from YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/HdTN25vs7Oo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

!!! tip "Visual Aids (Student Reference)"
    You can refer to the following images from the course workbook (Asset A) while studying this topic:
    * `L15_DeepDive_ActivityMonitor_Memory.jpg`
    * `L15_DeepDive_What_to_do_when_an_app_uses_too_much_memory_p1_41.jpeg`
    * `L15_TahoeUI_26-Tahoe-Activity-Monitor-scaled.png`
    * `L15_TahoeUI_26-Tahoe-System-Information-scaled.png`

---

## 💡 Presentation Visuals

!!! tip "Visual Demonstration (Student Aid)"
    These images illustrate the relevant interface or mechanism for the lesson topic.

![ActivityMonitor_Memory](../assets/images/Lesson_15/L15_DeepDive_ActivityMonitor_Memory.jpg)
![What_to_do_when_an_app_uses_too_much_memory_p1_41](../assets/images/Lesson_15/L15_DeepDive_What_to_do_when_an_app_uses_too_much_memory_p1_41.jpeg)
![26-Tahoe-Activity-Monitor-scaled](../assets/images/Lesson_15/L15_TahoeUI_26-Tahoe-Activity-Monitor-scaled.png)
![26-Tahoe-System-Information-scaled](../assets/images/Lesson_15/L15_TahoeUI_26-Tahoe-System-Information-scaled.png)
