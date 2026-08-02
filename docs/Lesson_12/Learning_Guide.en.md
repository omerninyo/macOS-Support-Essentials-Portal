# Lesson 12: Updates and Upgrades
**Student Learning Guide**

## Overview

<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/d74f76f7-4640-4f79-beb9-48a4b3de0ed3/"></iframe></div>

## Core Concepts: Terminology & Strategy

* **Update:** A minor update or software patch released by Apple for the current operating system version (e.g., macOS 26.1 to macOS 26.2).
* **Upgrade:** A major upgrade to a completely new operating system (e.g., macOS 25 to macOS 26).
* **Combo Update (Historical):** A term from the past (prior to Big Sur) describing a large update file containing all changes from the base version. Replaced today by the SSV (Signed System Volume) mechanism.
* **Rapid Security Response (RSR / BSI):** A mechanism for distributing critical security patches without requiring a full system update, utilizing Cryptex architecture. Identified by a letter in parentheses, e.g., `macOS 26.3.1 (a)`.
* **Deferral:** An administrative capability (via MDM Configuration Profile) to delay the appearance of software updates or upgrades for users for up to 90 days for compatibility testing.
* **Declarative Device Management (DDM):** The modern device management generation. Instead of sending a forced MDM command to update, IT defines a "Declaration" with a target deadline, and the OS manages preparations, alerts, and timing autonomously.
* **Migration Assistant:** macOS's built-in tool for transferring user profiles, data, and settings between Macs. Does not copy the OS itself.

---

## Terminal Command Repository: Managing Updates (`softwareupdate`)

The primary CLI tool in macOS for managing, downloading, and installing system updates is `softwareupdate`.

### Search and Download:

* **`softwareupdate -l`** or **`softwareupdate --list`**
  Scans and displays a list of all currently available software updates.

* **`softwareupdate -d -a`** or **`softwareupdate --download --all`**
  Downloads all available updates to the system cache but does **not** install them.

* **`softwareupdate -d "Name of Update"`**
  Downloads a specific update by its exact label.

### Installation:

* **`sudo softwareupdate -i -a`**
  Installs all available system updates.
  
* **`sudo softwareupdate -i -a -R`**
  Installs all updates and automatically Restarts the computer upon completion.

### Downloading Full Installers:

* **`softwareupdate --fetch-full-installer --full-installer-version 26.0`**
  Downloads the full installer app for a specific macOS version directly to the `/Applications` folder.

### Cleanup and History:

* **`softwareupdate --clear-deferrals`**
  Clears local MDM update deferrals (if permitted).

* **`softwareupdate --history`**
  Prints a neat table with the history of all updates installed on the computer.

* **`softwareupdate --install-rosetta --agree-to-license`**
  Silently installs the Rosetta 2 translation environment.

---

## Architecture, Background Processes, and Logs

* **`softwareupdated`**: The main background daemon responsible for searching, verifying with Apple servers, and installing updates. Runs `CalculatePrepareSize` to check for required space.
* **`UpdateBrainService`**: The service that takes over the actual streaming decompression, snapshot building, and sealing.
* **`/Library/Preferences/com.apple.SoftwareUpdate.plist`**: The system-level configuration file storing update behaviors.

* **Searching for Update Errors in Unified Logging:**
  ```bash
  log show --predicate 'subsystem == "com.apple.SoftwareUpdate"' --info --debug
  ```

---

## IT Recommendations for Migrations (Migration Assistant)

Using Migration Assistant in enterprise environments can carry over past issues.

* **Isolate Data to Transfer:** It is highly recommended *not* to transfer `Applications` or `Other files and folders`, but only the User Account (Home Folder). Transferring apps drags old MDM configs and unsupported Kexts (especially moving from Intel to Apple Silicon).
* **Physical Connection:** For fastest performance on Apple Silicon, use Mac Sharing Mode via Recovery with a Thunderbolt cable.
* **Account Overlap (UID Conflict):** Do not import a user to a new Mac if you've already created a local account with the exact same name. Migration Assistant will demand you either rename or replace the existing account.

---

## Recommended Links & Further Reading

* [Manage software updates in Apple Platform Deployment](https://support.apple.com/guide/deployment/manage-software-updates-depc4c80847a/web) - The official guide for system administrators.
* [Install software updates for Mac](https://support.apple.com/guide/mac-help/get-macos-updates-mchlpx1065/mac) - A simple guide for end users.
* [Transfer to a new Mac with Migration Assistant](https://support.apple.com/en-us/102613) - Guide explaining data transfer.
* [Taking manual control of macOS updates with softwareupdate](https://eclecticlight.co/2023/09/06/taking-manual-control-of-macos-updates-with-softwareupdate/) - A deep dive into CLI updates management.

## Summary Video

<!-- Summary Video from YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/DDXfEIRgAxs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
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
