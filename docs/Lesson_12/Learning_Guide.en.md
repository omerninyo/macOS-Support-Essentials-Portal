# Lesson 12: Updates and Upgrades
**Student Reference Guide**

## Overview

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/d74f76f7-4640-4f79-beb9-48a4b3de0ed3/"></iframe></div>

## Core Concepts: Terminology and Strategy

*   **Update:** A minor update or software patch for the current operating system version (e.g., from macOS 26.1 to macOS 26.2).
*   **Upgrade:** A major upgrade to an entirely new operating system version (e.g., from macOS 25 to macOS 26 Tahoe).
*   **Combo Update (Historical):** An older term describing a file that included all changes since the last major version. It has now been completely replaced by the SSV and Cryptex architecture.
*   **Rapid Security Response - RSR (or BSI):** Critical and rapid security patches applied to the system via Cryptex, without requiring a full system update. Identified by letters in parentheses, such as `macOS 26.3.1 (a)`.
*   **Deferral:** A management capability in MDM to defer the appearance of software updates (up to 90 days for a major upgrade) for compatibility testing.
*   **Declarative Device Management - DDM:** The modern infrastructure for device management. Update enforcement is performed by sending a "declaration" with a deadline, and the Mac locally manages notifications and enforcement.
*   **Migration Assistant:** The built-in tool for transferring information between Macs. It does not copy the operating system itself.

---

## Terminal Command Repository: Controlling Updates (`softwareupdate`)

The primary CLI tool for managing, downloading, and installing system updates is `softwareupdate`.

### Search and Download:

*   **`softwareupdate -l`** or **`softwareupdate --list`**
    Lists all available software updates.

*   **`softwareupdate -d -a`**
    Downloads all available updates to the cache but does not install them.

### Installation:

*   **`sudo softwareupdate -i -a`**
    Installs all updates.

*   **`sudo softwareupdate -i -a -R`**
    Installs and automatically restarts.

### Downloading Full Installers:

*   **`softwareupdate --fetch-full-installer --full-installer-version 26.0`**
    Downloads the full installer file (Install macOS.app) of the specified version directly to the Applications folder.

### Cleanup and History:

*   **`softwareupdate --clear-deferrals`**
    Locally clears update deferrals (if allowed by the MDM).

*   **`softwareupdate --history`**
    Prints a history of installed updates.

*   **`softwareupdate --install-rosetta --agree-to-license`**
    Installs the Rosetta 2 runtime environment silently.

---

## Architecture, Background Processes, and Logs

*   **`softwareupdated`**: The main background process responsible for checking for updates and calculating required disk space (`CalculatePrepareSize`).
*   **`UpdateBrainService`**: The actual service responsible for deploying files in the background and building the Snapshot and SSV.
*   **`/Library/Preferences/com.apple.SoftwareUpdate.plist`**: The system-level configuration file.

*   **Searching for errors in the Unified Logging System:**
    ```bash
    log show --predicate 'subsystem == "com.apple.SoftwareUpdate"' --info --debug
    ```

---

## IT Recommendations for Migrations (Migration Assistant)

In enterprise environments, Migration Assistant can import issues from older computers.

*   **Isolating Data for Transfer:** It is recommended to transfer *only* the user account (Home Folder) and not `Applications`. Transferring applications can bring old MDM configuration files, Intel applications (Rosetta), and unsupported kernel extensions.
*   **Physical Connection:** On Apple Silicon, use Mac Sharing Mode (from Recovery) with a Thunderbolt cable for fast transfer.
*   **User Overlap:** Do not import a user if you have already created a user with the same name on the new Mac. This will create a UID conflict requiring an overwrite or duplication. It is preferable to run Migration directly from the Out-Of-Box Experience (OOBE) screen.

---

## Recommended Links and Further Reading

*   [Manage software updates in Apple Platform Deployment](https://support.apple.com/guide/deployment/manage-software-updates-depc4c80847a/web) - The official guide for system administrators on controlling and deferring updates in an organization.
*   [Install software updates for Mac](https://support.apple.com/guide/mac-help/get-macos-updates-mchlpx1065/mac) - A simple guide for end-users on how to download and install system updates.
*   [Transfer to a new Mac with Migration Assistant](https://support.apple.com/en-us/102613) - A guide explaining how to transfer data and information from an old Mac to a new Mac using Migration Assistant.
*   [Taking manual control of macOS updates with softwareupdate](https://eclecticlight.co/2023/09/06/taking-manual-control-of-macos-updates-with-softwareupdate/) - A deep dive into the terminal.

## Summary Video

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/RFZYlrmn08Q" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 💡 Presentation Visuals

![How_Software_Update_works_in_Ventura_p5_37](../assets/images/Lesson_12/L12_DeepDive_How_Software_Update_works_in_Ventura_p5_37.jpeg)
![What_should_you_do_when_an_update_goes_wrong_p1_41](../assets/images/Lesson_12/L12_DeepDive_What_should_you_do_when_an_update_goes_wrong_p1_41.jpeg)
![Slide1_image2](../assets/images/Lesson_12/L12_LegacySlide_Slide1_image2.jpg)
![Slide5_image5](../assets/images/Lesson_12/L12_LegacySlide_Slide5_image5.jpg)
![Slide76_image16](../assets/images/Lesson_12/L12_LegacySlide_Slide76_image16.jpg)
![Slide76_image44](../assets/images/Lesson_12/L12_LegacySlide_Slide76_image44.jpeg)
![Slide76_image90](../assets/images/Lesson_12/L12_LegacySlide_Slide76_image90.png)
![Slide76_image91](../assets/images/Lesson_12/L12_LegacySlide_Slide76_image91.png)
![Slide76_image92](../assets/images/Lesson_12/L12_LegacySlide_Slide76_image92.png)
![Slide77_image17](../assets/images/Lesson_12/L12_LegacySlide_Slide77_image17.jpg)
![Slide77_image18](../assets/images/Lesson_12/L12_LegacySlide_Slide77_image18.tif)

<!-- src_hash: 1227eac81664e86205b25732d417832d45fc961e7bc54aa08e6df4b44af2ea3d -->
