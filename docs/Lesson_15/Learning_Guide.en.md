# Lesson 15: Diagnostics
**Student Reference Guide**

## Overview

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/1a3db037-3234-40d2-bcb4-7bb56b307bc4/"></iframe></div>

## Core Concepts and Methodologies

*   **Isolation:** Apple's core troubleshooting strategy, aimed at dividing the problem in half at each step to isolate the source:

    *   **User vs. System:** Creating a new Test User to check if the issue exists only within a specific user profile (settings, LaunchAgents processes) or if it is a system-wide problem.
    *   **Software vs. Hardware:** Booting the computer into macOS Recovery or running Apple Diagnostics to rule out a hardware issue. If the problem does not occur in an alternative system, its origin is software-related.
    *   **Network vs. Client:** Connecting the computer to a different network (e.g., a phone hotspot) to check if the issue is related to the organizational firewall settings or the internet service provider.
*   **Apple Diagnostics:** A hardware diagnostic tool built into the firmware, designed to check physical components such as RAM, fans, battery, and sensors. On Apple Silicon Macs, it is launched from the Options menu (long-press the power button) and then pressing `Command + D`.
*   **Verbose Mode:** A boot mode (more relevant on Intel Macs with `Command + V` keys) that displays boot process text instead of the Apple logo. On Apple Silicon Macs, this is now largely replaced by deep log analysis after the system boots.
*   **Activity Monitor & Console (Brief History):** The Activity Monitor application began in 2003 (Mac OS X Panther) as a merger of the Process Viewer and CPU Monitor tools. Previously, Console worked with simple text files, but starting with macOS Sierra in 2016, the system transitioned to the Unified Logging System – a binary and unified logging system that displays thousands of events per second.

!!! tip "Deep Dive 🤿: What does Activity Monitor really measure?"
    On Apple Silicon Macs, Activity Monitor data can sometimes be misleading and does not represent absolute hardware figures:
    *   **CPU %:** Can exceed 100% (each core is counted as 100%), but the measurement does not reflect accurate load due to the asymmetric architecture (E-cores and P-cores).
    *   **Energy Impact:** This is a relative score based on an algorithm, not a physical value in Watts.
    *   **Conclusion for Support:** Use these numbers only to identify "runaway processes," not for surgical performance measurement. [Full article by Eclectic Light](https://eclecticlight.co/2026/06/29/what-does-activity-monitor-measure/)
*   **App Memory Leaks:** A condition where an application continuously consumes more and more memory without releasing it back to the system. This causes significant slowdowns on the Mac (the "Beachball" phenomenon), but usually without increased fan noise (which characterizes CPU load). The solution is to monitor memory consumption in the Memory tab of Activity Monitor and completely quit the application. In contrast, Kernel Memory Leaks are much rarer and more severe, leading to a complete system crash (Kernel Panic). [Further reading from Eclectic Light's article](https://eclecticlight.co/2026/06/19/what-can-you-do-when-an-app-uses-too-much-memory/)

## Safe Mode

Safe Mode is a powerful diagnostic tool that often resolves issues simply by booting into it, as it cleans and resets system components.

**What happens when you start your Mac in Safe Mode?**

*   **Disk Check:** The system performs a logical check and repair of the startup disk using the `fsck` (File System Consistency Check) process.
*   **Extension Disablement:** Prevents third-party Kernel Extensions (Kexts) from loading.
*   **Background Process Blocking:** Prevents third-party application LaunchDaemons and LaunchAgents from running. Only built-in system services are loaded.
*   **Login Items Blocking:** Prevents user-configured windows and applications from opening automatically.
*   **Cache Cleaning:** Temporarily deletes font caches, the Kernel cache, and System Caches, which often cause sudden software crashes.
*   **Hardware Acceleration Disablement:** Disables graphics accelerators, which may cause the screen to flicker, the mouse to stutter, or video not to play. This is normal and indicates that Safe Mode is active.

**How to enter Safe Mode?**

*   **Apple Silicon:** Shut down the Mac. Press and hold the power button until "Loading startup options" appears. Select the desired startup disk, press and hold the `Shift` key, and click "Continue in Safe Mode."
*   **Intel:** Turn on the Mac and immediately press and hold the `Shift` key until the login window appears.

## Terminal Toolkit (CLI Diagnostics)

A useful list of commands for technicians for advanced system investigation and diagnosis.

### Comprehensive System Information (`system_profiler`)
This command is the terminal version of the System Information application and allows exporting full hardware and software information.

*   `system_profiler SPSoftwareDataType` - Displays information about the macOS version, Build ID, kernel version, and uptime.
*   `system_profiler SPHardwareDataType` - Displays information about the CPU, number of cores, memory, serial number, and hardware UUID.
*   `system_profiler SPPowerDataType` - Displays battery data, including Cycle Count and battery health condition.
*   `system_profiler > ~/Desktop/MacReport.txt` - Exports the complete and full report to a text file on the desktop for submission to support.

### Advanced Network Quality Test (`networkQuality`)
A built-in command (starting from macOS Monterey) that checks not only download/upload speed but also the network's ability to remain responsive under load (Responsiveness).

*   `networkQuality` - Runs the standard test with parallel connections to Apple servers.
*   `networkQuality -v` - Runs the test with extensive detail (Verbose), including specific latency metrics.
*   `networkQuality -s` - Runs the network test sequentially rather than in parallel, a great tool for isolating data traffic issues.

### Querying the Logging System (`log show`)
The Unified Logging System in macOS replaces old text files and requires using the `log` command to retrieve accurate historical information.

*   `log show --last 10m` - Displays all logs recorded in the last 10 minutes.
*   `log show --predicate 'process == "kernel"' --last 1h` - Filters and displays only logs belonging to the central kernel process from the last hour.
*   `log show --info --debug --last 5m > ~/Desktop/logs.txt` - Extracts temporary logs at Info and Debug levels (which are not always saved to disk long-term) and exports them to a file for convenient analysis.

### Diagnosing Enterprise Identities with Kerberos (`klist`)
In Active Directory-based enterprise environments, the Kerberos system is used for transparent authentication (SSO) against network services. This command helps check if the user has indeed received a "ticket" from the server.

*   `klist` - Displays the list of active Kerberos tickets for the user. If the list is empty, the user does not have transparent permissions.
*   `klist -v` - Displays all extended (Verbose) information about the ticket, including start dates, expiration dates, and encryption type, to identify an expired ticket.

## Additional Communication Commands for Diagnosis and Isolation

*   `ping -c 4 8.8.8.8` - Sends 4 data packets to Google servers to check basic internet connectivity and response times.
*   `traceroute google.com` - Displays the packet routing path (Hops) from the Mac to the destination server, allowing identification of where communication is stuck within the enterprise network.
*   `ifconfig` - Displays low-level technical information about physical network cards (MAC Addresses).
*   `networksetup -listallhardwareports` - The easiest and most readable way to identify the physical MAC addresses for all connection types on the system.

## Enterprise Diagnostics

*   **Diagnosis with MDM Profiles:** Often, MDM security settings conflict with normal operation (e.g., USB blocking, Wi-Fi restrictions). If an issue is not resolved, an IT technician may consider temporarily removing the specific profile via System Settings > Privacy & Security > Profiles (provided it is not marked as non-removable) to isolate if it is causing the problem.
*   **Network Filtering Overrides:** In organizations using traffic filtering agents (Content Filters / Proxies), troubleshooting will often involve connecting the Mac to an external cellular network to examine whether the organizational filtering is blocking traffic to Apple.
*   **Agent Removal:** Disabling third-party security tools (such as Antivirus or DLP) that may crash and cause Kernel Panics or noticeable system slowdowns.

---

## Recommended Links and Further Reading
*   [What can you do when an app uses too much memory](https://eclecticlight.co/2026/06/19/what-can-you-do-when-an-app-uses-too-much-memory/) - A guide to diagnosing and treating applications that consume excessive memory (Memory Leaks).

*   [Start up your Mac in safe mode](https://support.apple.com/en-us/116946) - A basic user guide on how to enter Safe Mode to check for issues.
*   [Use Apple Diagnostics to test your Mac](https://support.apple.com/en-us/102550) - A user guide on how to run the built-in diagnostic tool to identify hardware issues.
*   [Unified Logging (log command line tool)](https://developer.apple.com/documentation/os/logging) - Advanced documentation on Apple's unified logging system and reading logs from the terminal.
*   [If your Mac restarts and a message appears (Kernel Panics)](https://support.apple.com/en-us/102566) - A support guide explaining why your Mac crashes and restarts and how to identify the cause.
*   [Identify your Mac hardware (System Information)](https://support.apple.com/en-us/102849) - How to use System Information to get technical data about computer components.

## Summary Video

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/DDXfEIRgAxs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>





!!! tip "Visual Illustration (Student Aid)"
    These images illustrate the interface or mechanism relevant to the lesson topic.



<!-- src_hash: c24f5df082ab2b0f02f5fe38c8ce07f52450437e5c23b790a5732bb10cb3b5d8 -->


!!! tip "Visual Aids (Student Guide)"
    These images illustrate the relevant interface or mechanism for this lesson.

![ActivityMonitor_Memory](../assets/images/Lesson_15/L15_DeepDive_ActivityMonitor_Memory.jpg)
![What_to_do_when_an_app_uses_too_much_memory_p1_41](../assets/images/Lesson_15/L15_DeepDive_What_to_do_when_an_app_uses_too_much_memory_p1_41.jpeg)
![26-Tahoe-Activity-Monitor-scaled](../assets/images/Lesson_15/L15_TahoeUI_26-Tahoe-Activity-Monitor-scaled.png)
![26-Tahoe-System-Information-scaled](../assets/images/Lesson_15/L15_TahoeUI_26-Tahoe-System-Information-scaled.png)
