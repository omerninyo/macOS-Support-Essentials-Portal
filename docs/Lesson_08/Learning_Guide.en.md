# Lesson 08: Terminal and System Services
**Student Learning Guide (vEXP)**

## Lesson Objectives

* **Introduction to the Terminal (CLI)** - Why the CLI is critical for technicians, keyboard shortcuts, and alignment before advanced work.
* **The Heart of the System** - The `launchd` process (difference between LaunchDaemons, Agents, and LaunchAngels).
* **Deep Diagnostics** - Reading memory in Activity Monitor, and reading/diagnosing Plist files (XML).
* **Organizational Flavor** - Locating the MDM system's Agent, understanding its sync status, and what to do when it crashes.



## Overview

<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/d1656076-9c58-4f49-be91-863f210a4214/"></iframe></div>

## Core Concepts and Terminology

* **CLI (Command Line Interface):** The direct access tool to the operating system that bypasses the Graphical User Interface (GUI). In macOS, the built-in tool is Terminal (inherited from the NeXTSTEP system in 2001).
* **Zsh (Z Shell):** A modern command shell that is the default in macOS starting with Catalina, replacing the older Bash. It provides more advanced automation and scripting capabilities.
* **Process ID (PID):** A unique process identifier (number) that the operating system assigns to every software or service running in memory at that moment.
* **launchd:** The supreme "process manager" (always receives PID 1). Responsible for booting the system, managing background services, and launching applications on demand.
* **LaunchDaemon:** A system service (Daemon) that runs in the background under the super-user privileges (`root`), independent of any logged-in user. MDM agents and enterprise antivirus software run this way.
* **LaunchAgent:** A user service that runs in the background with the permissions of the user who logged into the system. Loads only after the Login process.
* **LaunchAngel (Starting with Tahoe 26):** A new category of internal Apple system services managed directly by Apple via the `RunningBoard` mechanism. These files are locked in the SSV partition.
* **Plist (Property List):** A format for saving configuration files in macOS, based on XML or binary. Used to save app preferences and define the operations of Daemons and Agents.
* **Activity Monitor:** The built-in monitoring software displaying CPU load, memory usage, drive activity, and network traffic.
* **Memory Pressure:** The most important memory metric in Activity Monitor. It represents the system's "effort" in managing physical memory, including memory compression and Swap usage.
* **Swap:** A system mechanism where, when physical memory (RAM) runs out, the system moves less useful data to the SSD drive. Overuse of Swap causes a drastic drop in performance.
* **mdmclient:** A built-in Apple system process (Daemon) responsible for receiving MDM server commands via APNs and applying profiles in the operating system.
* **TCC (Transparency, Consent, and Control):** A security mechanism in macOS that blocks software and scripts from accessing sensitive areas without explicit permission from the user or an organizational profile (PPPC).
* **BTM (Background Task Management):** A mechanism allowing users to control which background services are allowed to run (via System Settings). It can be advanced managed using the `sfltool` command.

## Terminal Keyboard Shortcuts

* `Ctrl + C`: Stop the execution of a current command or process (Interrupt).
* `Ctrl + L`: Clear the screen (equivalent to the `clear` command).
* `Ctrl + A`: Jump to the beginning of the line.
* `Ctrl + E`: Jump to the end of the line.
* `Tab`: Auto-complete a file name, path, or command.

## Important System Commands

* `sudo`: Run a single command with network admin/Root privileges. Requires entering the admin password.
* `kill -9 <PID>`: Immediate and forceful "killing" of a stuck process by its identifier.
* `top -u`: Real-time viewing of system resource consumption sorted by CPU usage. Press `q` to exit.
* `ps -ax`: Print a list of all processes currently running in the system.

### The Master Command `launchctl`

* `launchctl list`: List of processes under the current process manager.
* `sudo launchctl print system`: Print the status of all system services (Daemons).
* `sudo launchctl bootstrap system /Library/LaunchDaemons/com.example.plist`: Load/start a system service.
* `sudo launchctl bootout system /Library/LaunchDaemons/com.example.plist`: Unload/suspend a system service.

### BTM Management (sfltool) - For Tahoe systems and above
* `sudo sfltool dumpbtm > ~/Documents/btmdump.txt`: Dump the Background Task Management database.
* `sudo sfltool resetbtm`: Reset the BTM database.

### Reading and Managing Plists (`plutil`)

* `plutil -lint /path/to/file.plist`: Syntax Check the file for syntax errors or missing tags.
* `plutil -p /path/to/file.plist`: Simple human-readable print of the content, bypassing binary files.
* `sudo plutil -convert xml1 /path/to/file.plist`: Convert a Plist file from binary to XML to allow editing.
* `sudo plutil -convert binary1 /path/to/file.plist`: Revert the file to a binary format after editing.

### MDM Diagnostics

* `log stream --predicate 'process == "mdmclient"' --info`: A command showing in real-time every action and synchronization the MDM agent communicates with the server.
* `sudo profiles renew -type enrollment`: Force an immediate synchronization with the MDM server from the client side.

## Critical Paths

* `~/Library/Preferences/`: The folder where a user's personal Plist files are saved.
* `/System/Library/LaunchDaemons/`: macOS core services directory, protected under the SSV.
* `/System/Library/LaunchAngels/`: (Starting with Tahoe) Dedicated Apple system services under RunningBoard management, locked in the SSV.
* `/Library/LaunchDaemons/`: Directory intended for third-party system agents (Daemons) (Antivirus, MDM).
* `~/Library/LaunchAgents/`: Directory intended for specific user-level agents that load upon Login.

---

## Recommended Links and Further Reading

* [Explainer: % CPU in Activity Monitor](https://eclecticlight.co/2026/02/14/explainer-cpu-in-activity-monitor/) - An in-depth explanation of why CPU percentages on the Mac are sometimes misleading and how to read them correctly.
* [A brief history of XML and property lists](https://eclecticlight.co/2025/08/16/a-brief-history-of-xml-and-property-lists/) - Interesting historical background explaining why Apple relies so heavily on XML-based Plist files and binary formats.
* [View Memory Usage in Activity Monitor](https://support.apple.com/guide/activity-monitor/view-memory-usage-actmntr1004/mac) - Apple's official guide for reading memory pressure in the Activity Monitor tool.

## Summary Video

<!-- Summary Video from YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/UPIUNoYIGPo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

!!! tip "Visual Aid (Student Reference)"
    These images illustrate the interface or mechanism relevant to the lesson topic.

![Slide81_image94](../assets/images/Lesson_08/L08_LegacySlide_Slide81_image94.png)
![Slide81_image95](../assets/images/Lesson_08/L08_LegacySlide_Slide81_image95.png)
![26-Tahoe-Automator-scaled](../assets/images/Lesson_08/L08_TahoeUI_26-Tahoe-Automator-scaled.png)
![26-Tahoe-Console-scaled](../assets/images/Lesson_08/L08_TahoeUI_26-Tahoe-Console-scaled.png)
![26-Tahoe-Script-Editor-scaled](../assets/images/Lesson_08/L08_TahoeUI_26-Tahoe-Script-Editor-scaled.png)
![26-Tahoe-Shortcuts-scaled](../assets/images/Lesson_08/L08_TahoeUI_26-Tahoe-Shortcuts-scaled.png)
