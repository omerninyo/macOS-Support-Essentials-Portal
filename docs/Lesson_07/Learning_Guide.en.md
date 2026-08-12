# Lesson 07: Backup and Restore
**Student Learning Guide (vEXP)**

## Lesson Objectives

* Snapshots
* Time Machine Backup
* File Restoration and Recovery
* Backup in an Enterprise Environment
**[Image Recommendation]:** A minimalist vector clock face rotating backwards with a hard drive symbol in the background.

## Overview

<!-- Captivate NotebookLM Podcast -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/5ae70462-ee1b-458a-b1f0-967157554d1f/"></iframe></div>

## Core Concepts

**Comparison: Time Machine Evolution**
| Feature | Classic Time Machine (HFS+) | Modern Time Machine (APFS) |
| :--- | :--- | :--- |
| **Technology Base** | Directory Hard Links (creating illusion of full backup) | Synthetic APFS Snapshots |
| **Destination Filesystem** | HFS+ | APFS |
| **Copy Efficiency** | Creating millions of hard links for unchanged files | Block-level Delta-copying (extremely fast) |
| **Long-Term Reliability** | Frequent corruption under Hard Link load | High stability due to native system snapshots |

* **Time Machine:** macOS's built-in backup mechanism. Keeps historical copies of files, allowing single-file or full system restoration.
* **APFS Snapshots:** A freeze of the filesystem state at a specific point in time in APFS. Allows instant restoration (Rollback) without lengthy data copying.
* **Local Snapshots:** Snapshots saved on the local drive (Data Volume). Created automatically as intermediate backups or before system updates. Deleted automatically when disk space is low.
* **Synthetic Snapshots:** The snapshots compiled on the external Time Machine drive, merging delta blocks to form a complete backup state.
* **Migration Assistant:** A utility for transferring data, user accounts, and settings from an old Mac, a Time Machine backup, or a PC.
* **FileProvider Framework:** The API used by modern Cloud Sync apps (OneDrive, Google Drive) to present "dataless" files that only download on demand.

## Advanced Terminal Commands (`tmutil`)

The `tmutil` (Time Machine Utility) command-line tool is a powerful way to manage backups and APFS snapshots. *(Note: some commands require `sudo`)*.

### Basic Management & Status
* `tmutil status`: Displays real-time backup status.
* `tmutil startbackup --block`: Starts a backup immediately and blocks the terminal until it completes.
* `tmutil listbackups`: Prints a list of all existing backups on the destination.
* `tmutil destinationinfo`: Shows information about configured Time Machine destinations.

### Exclusions
* `tmutil addexclusion /path/to/folder_or_file`: Permanently excludes an item from backup.
* `tmutil removeexclusion /path/to/folder_or_file`: Removes the exclusion tag.

### Local Snapshots
* `tmutil listlocalsnapshots /`: Lists all Local Snapshots on the root drive.
* `tmutil localsnapshot`: Creates an immediate Local Snapshot.
* `tmutil thinlocalsnapshots / 10000000000 4`: Forces the system to thin snapshots to free up space (e.g., 10GB with urgency level 4).

### Diagnostics
* `log show --predicate 'subsystem == "com.apple.TimeMachine"' --info --last 4h`: Extracts granular Time Machine logs to troubleshoot issues like Deep Traversal Scans.

## Daemons & Tools

* `backupd`: The central background daemon managing Time Machine operations.
* `diskutil apfs listSnapshots /`: Low-level APFS command to view snapshots.
* **System Settings -> General -> Time Machine**: The GUI for configuring backups.

## Enterprise Seasoning

* **The Ephemeral Device:** In modern Zero-Trust environments, IT prefers using Cloud Sync (OneDrive, Box) instead of Time Machine. If a Mac breaks, a new one is provisioned via Zero-Touch deployment, and files sync from the cloud.
* **The FileProvider Clash:** Cloud "dataless" files conflict with Time Machine's block-level copying, which can trigger mass downloads and flood the network.
* **MDM Restrictions:** IT admins often deploy an MDM profile setting `restrictTimeMachine` to true, completely disabling local backups to force cloud adoption, or they use `forceEncryptedTimeMachineBackups` to mandate encryption for users who still need it.

## Recommended Reading & Links

* [Back up your Mac with Time Machine](https://support.apple.com/en-us/HT201250)
* [Restore your Mac from a backup](https://support.apple.com/en-us/HT203981)
* [About Time Machine local snapshots](https://support.apple.com/en-us/HT204015)
* [Mac backups (Apple Platform Support)](https://support.apple.com/guide/platform-support/mac-backups-supc05405716/web)
* [Erase Apple devices](https://support.apple.com/guide/deployment/erase-apple-devices-dep8bb2f3590/web)
* [A brief history of Time Machine](https://eclecticlight.co/2021/04/19/a-brief-history-of-time-machine/)

## Summary Video

<!-- YouTube Summary Video -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/OXYBpCK91Lg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

!!! tip "Presentation Visuals"
    These images illustrate the relevant interface or mechanism for the lesson.

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
