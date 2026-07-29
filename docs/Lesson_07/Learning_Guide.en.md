# Lesson 07: Backup and Recovery
**Student Reference Guide**


## Lesson Objectives

* Snapshots
* Time Machine Backup
* File Restoration and Recovery
* Backup in an Enterprise Environment
**[Image Recommendation]:** A minimalist vector clock face rotating backwards with a hard drive symbol in the background.


## Overview

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/5ae70462-ee1b-458a-b1f0-967157554d1f/"></iframe></div>

## Core Concepts

**Comparison: The Evolution of Time Machine Backup**
| Feature | Classic Time Machine (HFS+) | Modern Time Machine (APFS) |
| :--- | :--- | :--- |
| **Technological Basis** | Directory Hard Links (creating the illusion of a full backup) | Synthetic APFS Snapshots |
| **Destination File System** | HFS+ | APFS |
| **Copy Efficiency** | Creation of millions of hard links for unchanged files | Relies on block-level Delta-copying (fast and space-saving) |
| **Long-term Reliability** | Frequent crashes under hard link load | High stability due to native system snapshots |

*   **Time Machine:** macOS's built-in backup mechanism. Stores historical copies of files, allowing restoration of individual files or an entire system.
*   **APFS Snapshots:** A freeze of the file system state at a specific point in time within APFS. Enables immediate rollback without the need for lengthy data copying.
*   **Local Snapshots:** Snapshots stored on the local drive itself (the Data Volume). Created automatically as an interim backup or before system updates. They are automatically deleted when disk space runs low.
*   **Backup Destination:** The external drive (USB, Thunderbolt, NAS, or Time Machine-compatible SMB server) configured to store the backup. Starting with macOS Big Sur, backup destinations are automatically formatted to the APFS file system.
*   **Mobile Time Machine:** Behavior where the Mac continues to create and save Local Snapshots even when the external drive is disconnected, to maintain a historical sequence that it will synchronize with the destination drive once connected.
*   **Rollback:** The action of reverting to a previous Snapshot. In an APFS system, this action occurs almost instantaneously due to the system's block-sharing (Copy-on-Write) features.
*   **Migration Assistant:** A utility for transferring data, user accounts, and settings from an old Mac, a Time Machine backup, or a PC (during OOBE or afterward).
*   **Erase Assistant / Erase All Content and Settings (EACS):** A built-in tool in System Settings (under General -> Transfer or Reset) that allows quickly erasing the Data Volume and cryptographic keys to return the Mac to factory settings – without needing to reinstall the OS.

## Advanced Terminal Commands (`tmutil`)

The `tmutil` (Time Machine Utility) command-line tool is a powerful way to manage, diagnose, and control Time Machine backups and APFS snapshots.
*(Note: Some commands that make changes require `sudo` permissions)*.

### Basic Management and Status

*   `tmutil status`
    *   Displays the current real-time backup status (shows if a backup is currently running, progress percentage, and destination path).
*   `tmutil startbackup`
    *   Immediately starts a Time Machine backup to the configured destination. Adding the `--block` flag will run the backup in the foreground, and the command will only complete when the backup is finished. The `--auto` flag simulates an automatic system initiation (which also includes thinning Snapshots as needed).
*   `tmutil stopbackup`
    *   Stops a backup that is currently in progress.
*   `tmutil listbackups`
    *   Prints an organized list of all existing and recognized backups (stored at the backup destination).
*   `tmutil latestbackup`
    *   Prints the full path of the last successfully completed backup.
*   `tmutil destinationinfo`
    *   Displays information and data about all destination drives currently configured for Time Machine backup (including destination identifiers).

### Exclusions from Backup

*   `tmutil addexclusion /path/to/folder_or_file`
    *   Permanently excludes a file or folder from backup. The command embeds an Extended Attribute that tells `backupd` to skip this path. (To exclude system files, `sudo` must be used).
*   `tmutil removeexclusion /path/to/folder_or_file`
    *   Removes the exclusion tag from the file or folder, so they will be backed up again in the next backup.
*   `tmutil isexcluded /path/to/folder_or_file`
    *   Checks and returns output indicating whether a specific path is currently excluded from backup.

### Local Snapshots

*   `tmutil listlocalsnapshots /`
    *   Displays a list of all Local Snapshots stored on the current system drive (the Root - `/`).
*   `tmutil localsnapshot`
    *   Immediately creates a local Snapshot (useful as a safety net before making significant system changes).
*   `sudo tmutil deletelocalsnapshots <date>`
    *   Deletes a specific Snapshot based on the date obtained from the list command (e.g., `2026-05-10-153020`).
*   `tmutil thinlocalsnapshots / <purge_amount_bytes> <urgency_1_to_4>`
    *   Forces the system to thin Snapshots to free up disk space (urgency 4 is the fastest for stopping related processes).

### Diagnostics & Analysis

*   `tmutil calculatedrift /path/to/backup1 /path/to/backup2`
    *   Calculates what has changed (added, removed, modified) between two different backups to understand why a recent backup is taking up a lot of space.
*   `tmutil compare`
    *   Performs a full comparison between the current state of the system (disk) and the last backup performed.

## Relevant System Tools & Processes (Daemons & Tools)

*   `backupd`: The core internal Time Machine background process that manages copying and administration operations with backup destinations.
*   `diskutil apfs listSnapshots /`: The `diskutil` command used as an APFS-level diagnostic tool to display snapshots on the disk at the deepest technical level.
*   `System Settings -> General -> Time Machine`: The graphical user interface (GUI) for setting frequency, adding exclusions, and managing drives in a simple organization.

## Enterprise Seasoning

*   **Avoidance of Local Backups:** In modern organizations, there is a tendency to forgo Time Machine for end-users due to hardware costs and the difficulty of securing portable drives that may be lost or stolen.
*   **Cloud Backup as an Alternative (Cloud Storage):** The use of synchronization-based services such as OneDrive, Google Drive, or Box is preferred and supervised via MDM profiles, where data is always synchronized, and restoration to a replacement computer occurs as soon as an MAID account is connected.
*   **Profile Restrictions via MDM:** MDM can be used to restrict users from performing restorations, control Erase Assistant capabilities to prevent computers from being erased before being handed over to the IT department, or force the system not to exclude sensitive paths that the network administrator definitely wants to back up if Time Machine or network drives are still being used for backup.

## Recommended Links & Further Reading

*   [Back up your Mac with Time Machine](https://support.apple.com/en-us/HT201250) - Basic user guide on enabling the Time Machine backup system.
*   [Restore your Mac from a backup](https://support.apple.com/en-us/HT203981) - User guide on how to restore files from a previous backup.
*   [About Time Machine local snapshots](https://support.apple.com/en-us/HT204015) - A brief explanation of the local snapshots mechanism when the backup drive is not connected.
*   [Mac backups (Apple Platform Support)](https://support.apple.com/guide/platform-support/mac-backups-supc05405716/web) - Article for system administrators on backup policy in an organization.
*   [Erase Apple devices](https://support.apple.com/guide/deployment/erase-apple-devices-dep8bb2f3590/web) - Enterprise documentation on remote secure erasure and reset of computers.
*   [A brief history of Time Machine](https://eclecticlight.co/2021/04/19/a-brief-history-of-time-machine/) - Historical overview of Time Machine's evolution over the years.
*   [Snapshots aren't backups](https://eclecticlight.co/2021/02/16/snapshots-arent-backups/) - A technical opinion piece explaining why snapshots should not be relied upon as a substitute for a true backup.
*   [Understand and check Time Machine backups to APFS](https://eclecticlight.co/2021/03/25/understand-and-check-time-machine-backups-to-apfs/) - In-depth technical article on how Time Machine leverages APFS mechanisms for fast backups.

## Summary Video

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/DDXfEIRgAxs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>





!!! tip "Visual Illustration (Student Aid)"
    These images illustrate the interface or mechanism relevant to the lesson topic.



<!-- src_hash: c6ae134b9f7e311fb4cc92a72a4ebf4cfb2571f2a463f754a50cace131665f8f -->


!!! tip "Visual Aids (Student Guide)"
    These images illustrate the relevant interface or mechanism for this lesson.

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
