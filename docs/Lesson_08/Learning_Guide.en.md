# Lesson 08: Terminal and System Services
**Student Learning Guide**

---

## Lesson Objectives

* **Introduction to the Terminal** - Why the CLI is critical for technicians, keyboard shortcuts, and establishing a baseline before advanced operations.
* **The Heart of the System** - The `launchd` process (understanding the differences between LaunchDaemons, LaunchAgents, and LaunchAngels).
* **Deep Diagnostics** - Reading memory metrics in Activity Monitor, and reading/diagnosing Plist (XML) files.
* **Enterprise Spice** - Locating the MDM Agent, understanding its sync status, and troubleshooting when it crashes.

---

## 🎧 Audio Summary — Before or After Class

<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/d1656076-9c58-4f49-be91-863f210a4214/"></iframe></div>

---

## Core Concepts & Terminology

| Concept | Explanation |
|---|---|
| **CLI / Terminal** | The command-line interface in Mac (originated from NeXTSTEP in 2001). A direct management tool bypassing the graphical interface. |
| **Zsh (Z Shell)** | The modern shell for Mac, the default since Catalina. |
| **PID (Process ID)** | A unique identification number for any currently running software or service. |
| **launchd** | The supreme process manager (PID 1). The first software to start. Responsible for bootstrapping services and applications. |
| **LaunchDaemon** | An infrastructure agent running in the background as `root` (even without a logged-in user). Common for MDM or antivirus agents. |
| **LaunchAgent** | A user-specific agent, loaded only when the user logs in. |
| **LaunchAngels (Tahoe)** | New internal Apple system services under the `RunningBoard` framework. Completely locked within the SSV. |
| **Plist (Property List)** | Apple's configuration file format (XML or binary). Stores everything from window positions to system task scheduling. |
| **Memory Pressure** | The critical graph in Activity Monitor indicating memory "strain" (Green, Yellow, Red). |
| **Swap** | Writing memory data from RAM to the hard drive. High usage indicates memory starvation and inefficiency. |
| **mdmclient** | Apple's built-in Daemon responsible for communicating with the MDM server and enforcing profiles. |
| **TCC & PPPC** | The mechanism protecting sensitive data. We manage these restrictions using an enterprise PPPC profile. |
| **BTM (Background Task Mgt)** | The defense mechanism for Login Items. Deeply managed via the `sfltool` command. |

---

## Part 1 — Terminal Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| `Ctrl + C` | **Cancel & Rescue:** Immediately stops a running command that has frozen the screen. |
| `Ctrl + L` | **Clear Screen** (same as the `clear` command). Wipes the clutter and returns to a clean slate. |
| `Ctrl + A` | Jump to the **beginning** of the line. |
| `Ctrl + E` | Jump to the **end** of the line. |
| `Tab` | **Auto-complete** for paths and commands (press twice to display options). |

---

## Part 2 — Critical Paths

| What's there? | Full Path | Owner |
|---|---|---|
| **User Application Preferences** | `~/Library/Preferences/` | User |
| **Current User Agents** | `~/Library/LaunchAgents/` | User |
| **IT / Third-Party System Daemons** | `/Library/LaunchDaemons/` | Administrator (Root) |
| **macOS Core (SSV - Locked)** | `/System/Library/LaunchDaemons/` | System (Read-Only) |
| **New Tahoe Core (RunningBoard)** | `/System/Library/LaunchAngels/` | System (Read-Only) |

---

## Appendix — Important System Commands

> [!NOTE]
> It is highly recommended to save these commands in a Cheat Sheet or within your MDM as code snippets for troubleshooting scenarios.

### Basic Control and Process Management
```bash
# Execute a single command with administrator privileges
sudo [command]

# Forcefully kill a stuck process
kill -9 <PID>

# Live resource monitor (CPU) - press 'q' to quit
top -u

# Full list of all processes on the system
ps -ax
```

### Service Management (launchctl and BTM)
```bash
# Print the state of all currently running system services
sudo launchctl print system

# Load / Unload a failing service (bootout / bootstrap):
sudo launchctl bootout system /Library/LaunchDaemons/com.example.plist
sudo launchctl bootstrap system /Library/LaunchDaemons/com.example.plist

# Dump the BTM (Background Task Management) database
sudo sfltool dumpbtm > ~/Documents/btmdump.txt

# Deep reset for BTM (use only in critical failure scenarios)
sudo sfltool resetbtm
```

### Reading and Managing Plists (`plutil`)
```bash
# Print the file content even if encrypted/binary
plutil -p /path/to/file.plist

# Syntax linting check - mandatory before deployment
plutil -lint /path/to/file.plist

# Convert a binary file to editable XML text
sudo plutil -convert xml1 /path/to/file.plist

# Revert the file back to the closed binary format
sudo plutil -convert binary1 /path/to/file.plist
```

### MDM Diagnostics
```bash
# Real-time stream of incoming MDM commands to the Mac
log stream --predicate 'process == "mdmclient"' --info

# Forceful command to pull information from the MDM
sudo profiles renew -type enrollment
```

---

## Recommended Reading

* [Explainer: % CPU in Activity Monitor](https://eclecticlight.co/2026/02/14/explainer-cpu-in-activity-monitor/) - Understanding why CPU percentages can be misleading and how to interpret Performance vs Efficiency.
* [A brief history of XML and property lists](https://eclecticlight.co/2025/08/16/a-brief-history-of-xml-and-property-lists/) - Why Apple relies so heavily on Plist files.
* [View Memory Usage in Activity Monitor](https://support.apple.com/guide/activity-monitor/view-memory-usage-actmntr1004/mac) - The official guide to reading Memory Pressure.

---

## 🎬 Video Summary

<!-- YouTube Summary Video -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/UPIUNoYIGPo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

## 💡 Presentation Visuals

!!! tip "Presentation Visuals"
    These images illustrate the interfaces covered in this lesson.

![Slide81_image94](../assets/images/Lesson_08/L08_LegacySlide_Slide81_image94.png)
![Slide81_image95](../assets/images/Lesson_08/L08_LegacySlide_Slide81_image95.png)
![Automator Tahoe](../assets/images/Lesson_08/L08_TahoeUI_26-Tahoe-Automator-scaled.png)
![Console Tahoe](../assets/images/Lesson_08/L08_TahoeUI_26-Tahoe-Console-scaled.png)
![Script Editor Tahoe](../assets/images/Lesson_08/L08_TahoeUI_26-Tahoe-Script-Editor-scaled.png)
![Shortcuts Tahoe](../assets/images/Lesson_08/L08_TahoeUI_26-Tahoe-Shortcuts-scaled.png)
