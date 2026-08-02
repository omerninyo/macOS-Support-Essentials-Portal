# Lesson 07: Backup and Recovery
**Student Reference Guide (vEXP)**

## Lesson Objectives

*   Snapshots
*   Time Machine Backup
*   File Restoration and Recovery
*   Backup in an Enterprise Environment
**[Image Recommendation]:** A minimalist vector clock face rotating backwards with a hard drive symbol in the background.

## Overview

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/5ae70462-ee1b-458a-b1f0-967157554d1f/"></iframe></div>

## Core Concepts

**Comparison: The Evolution of Time Machine Backup**
| Feature | Classic Time Machine (HFS+) | Modern Time Machine (APFS) |
| :--- | :--- | :--- |
| **Technological Basis** | Directory Hard Links (creating the illusion of a full backup) | Synthetic APFS Snapshots |
| **Target File System** | HFS+ | APFS |
| **Copy Efficiency** | Creation of millions of hard links for unchanged files | Relies on block-level Delta-copying (fast and space-saving) |
| **Long-Term Reliability** | Frequent crashes under hard link load | High stability due to native system snapshots |

*   **Time Machine:** macOS's built-in backup mechanism. It saves historical copies of files, allowing restoration of individual files or an entire system.
*   **APFS Snapshots:** A freeze of the file system state at a specific point in time within APFS. Enables immediate rollback without the need for lengthy data copying.
*   **Local Snapshots:** Snapshots stored on the local drive itself (the Data Volume). Created automatically as an interim backup or before system updates. They are automatically deleted when disk space runs low.
*   **Synthetic Snapshots:** Snapshots built at the end of the backup process on the external drive, as a combination of changed blocks.
*   **Migration Assistant:** A utility for transferring data, user accounts, and settings from an old Mac, a Time Machine backup (using a Synthetic Snapshot), or a PC.
*   **FileProvider Framework:** The system mechanism (API) that allows cloud services like OneDrive to display files that exist only in the cloud ("Dataless files") and download them only when needed.

## Advanced Terminal Commands (`tmutil`)

The `tmutil` (Time Machine Utility) command-line tool is a powerful way to manage, diagnose, and control Time Machine backups and APFS snapshots. *(Note: Some commands require `sudo` permissions)*.

### Basic Management and Status
*   `tmutil status`: Displays the current real-time backup status.
*   `tmutil startbackup --block`: Immediately starts a backup and blocks the terminal until its completion.
*   `tmutil listbackups`: Prints an organized list of all existing backups known to the system at the destination.
*   `tmutil destinationinfo`: Displays information and data about the currently configured destination drives.

### Exclusions from Backup
*   `tmutil addexclusion /path/to/folder_or_file`: Permanently excludes a file or folder from backup.
*   `tmutil removeexclusion /path/to/folder_or_file`: Removes the exclusion tag so the file will be backed up again.

### Local Snapshots
*   `tmutil listlocalsnapshots /`: Displays a list of all Local Snapshots saved on the current system drive.
*   `tmutil localsnapshot`: Immediately creates a local Snapshot (useful before a significant system change).
*   `tmutil thinlocalsnapshots / 10000000000 4`: Forces the system to thin Snapshots to free up disk space (this example frees about 10GB with the fastest urgency of 4).

### Diagnostics
*   `log show --predicate 'subsystem == "com.apple.TimeMachine"' --info --last 4h`: Extracts precise logs to understand delays like Deep Traversal Scans.

## Relevant System Daemons & Tools

*   `backupd`: The main Time Machine background process that manages delta copies and backups.
*   `diskutil apfs listSnapshots /`: A `diskutil` command used for APFS-level diagnostics to display low-level Snapshots.
*   **System Settings -> General -> Time Machine**: The graphical user interface for configuring backups.

## Enterprise Seasoning

*   **Ephemeral Device:** In modern organizations under Zero-Trust, portable drives are avoided, and there's a complete shift to cloud synchronization services (OneDrive, Google Drive). The approach is cloud backup and remote installation (Zero-Touch) if the computer is destroyed.
*   **FileProvider Clash:** Cloud files (Dataless) can create critical load if Time Machine tries to back them up, forcing the Mac to download terabytes of data from the cloud.
*   **MDM Restrictions:** Network administrators often deploy a profile with the `restrictTimeMachine` value to disable local backup capability, or alternatively, enforce `forceEncryptedTimeMachineBackups` so that backups are performed with encryption only for heavy users who require them.

## Recommended Links & Further Reading

*   [Back up your Mac with Time Machine](https://support.apple.com/en-us/HT201250)
*   [Restore your Mac from a backup](https://support.apple.com/en-us/HT203981)
*   [About Time Machine local snapshots](https://support.apple.com/en-us/HT204015)
*   [Mac backups (Apple Platform Support)](https://support.apple.com/guide/platform-support/mac-backups-supc05405716/web)
*   [Erase Apple devices](https://support.apple.com/guide/deployment/erase-apple-devices-dep8bb2f3590/web)
*   [A brief history of Time Machine](https://eclecticlight.co/2021/04/19/a-brief-history-of-time-machine/)

## Summary Video

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/OXYBpCK91Lg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

!!! tip "Visual Illustration (Student Aid)"
    These images illustrate the interface or mechanism relevant to the lesson topic.

![Snapshots_aren_t_backups_p1_114](../assets/images/Lesson_07/L07_DeepDive_Snapshots_aren_t_backups_p1_114.jpeg)
![Time_Machine_backing_up_different_file_systems_p4_133](../assets/images/Lesson_07/L07_DeepDive_Time_Machine_backing_up_different_file_systems_p4_133.jpeg)
![Time_Machine_backing_up_different_file_systems_p5_133](../assets/images/Lesson_07/L07_DeepDive_Time_Machine_backing_up_different_file_systems_p5_133.jpeg)
![Slide120_image42](../assets/images/Lesson_07/L07_LegacySlide_Slide120_image42.jpg)
![Slide122_image43](../assets/images/Lesson_07/L07_LegacySlide_Slide122_image43.jpg)
![Slide122_image44](../assets/images/Lesson_07/L07_LegacySlide_Slide122_image44.jpg)
![Slide136_image168](../assets/images/Lesson_07/L07_LegacySlide_Slide136_image168.png)
![Slide67_image80](../assets/images/Lesson_07/L07_LegacySlide_Slide67_image80.png)
![26-Tahoe-Time-Machine-Menu-scaled](../assets/images/Lesson_07/L07_TahoeUI_26-Tahoe-Time-Machine-Menu-scaled.png)
![26-Tahoe-Time-Machine-scaled](../assets/images/Lesson_07/L07_TahoeUI_26-Tahoe-Time-Machine-scaled.png)

<!-- src_hash: eeccb985c5d6546c96a8809aa6f56381358b733e5d96977a795d06523cf3a4ba -->
