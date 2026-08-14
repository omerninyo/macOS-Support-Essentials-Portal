# Lesson 12: Updates and Upgrades
**Student Learning Guide**

## 🎧 Overview (Podcast)

<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/d74f76f7-4640-4f79-beb9-48a4b3de0ed3/"></iframe></div>

---

## Core Terms and Concepts

| Concept | Background & Meaning |
| :--- | :--- |
| **Update** | A minor update or patch to the current version of the OS (e.g., from macOS 26.1 to macOS 26.2). Includes bug fixes and security patches. |
| **Upgrade** | A jump to a completely new major version (e.g., from macOS 25 to macOS 26 Tahoe). A heavy process involving infrastructural changes to the OS. |
| **Rapid Security Response (RSR)** | Also known as BSI. Apple's mechanism for rapid, out-of-band delivery of critical security patches (like WebKit vulnerabilities) without requiring a full system update. Identified by a letter in parentheses, such as `macOS 26.3.1 (a)`. |
| **Update Deferral** | An MDM capability allowing administrators to defer the appearance of a major upgrade for up to 90 days, enabling IT to validate compatibility before employees update. |
| **DDM (Declarative Device Management)** | A modern infrastructure for device management. For updates, enforcement is handled by applying a local "declaration" with a deadline, empowering the Mac to autonomously manage the enforcement and user notifications. |
| **Migration Assistant** | A built-in tool for transferring data between Macs or from backups. *Note: In enterprise environments, there is an explicit recommendation to avoid using it to prevent importing outdated configuration profiles and problematic Intel legacy apps.* |

!!! note "Technical Note (Snapshots)"
    Why does a 5GB upgrade sometimes demand 40GB of free space? To ensure a safe installation, the OS (via the SSV mechanism) takes a snapshot of the disk before the update. If a network drop or power failure occurs, the system reverts to the starting point with absolutely zero data loss or corruption!

---

## Terminal Commands Reference (CLI)

The primary CLI tool for managing, downloading, and installing system updates is `softwareupdate`.

!!! warning
    Installation and deferral clearing commands (`clear-deferrals`) require `sudo` privileges.

### Search, Download, and Install

| Command | Description |
|---|---|
| `softwareupdate -l` | Lists all available updates for the specific Mac. |
| `softwareupdate -d -a` | Downloads all available updates to the cache but *does not install* them. |
| `sudo softwareupdate -i -a -R` | Powerful command: Installs all updates and automatically restarts the Mac upon completion. |
| `softwareupdate --fetch-full-installer` | Downloads the full installation file (`Install macOS.app`) to the Applications folder. (You can append `--full-installer-version 26.0` for a specific version). |

### History Management and Troubleshooting

| Command | Description |
|---|---|
| `softwareupdate --history` | Displays the history of downloads and installations performed via the mechanism. |
| `softwareupdate --clear-deferrals` | Locally clears MDM deferrals (highly useful for troubleshooting if permitted by the MDM). |
| `log show --predicate 'subsystem == "com.apple.SoftwareUpdate"'` | Extracts error logs from the update process (`softwareupdated` and `UpdateBrainService`) from the Unified Logging System to determine the cause of failure. |

---

## Enterprise Seasoning: IT Recommendations for Migrations (Migration Assistant)

!!! important "Why Not in the Enterprise?"
    In a managed organization (MDM), it is highly recommended to adopt a **Clean Slate** approach. This means letting the new Mac be built from scratch, and having the user pull data directly from cloud storage (OneDrive or Google Drive).
    A full migration of applications and settings from an old Mac often drags along deprecated Kexts, legacy Rosetta-dependent apps, and conflicting MDM identity certificates that can lock IT out of managing the new Mac post-migration.

If an enterprise Migration Assistant transfer is absolutely necessary:
* Select **only** the user folder. Uncheck `Applications` and `System & Network`.
* Ensure the imported account does not cause a UID Conflict with an account already created on the new Mac.

---

## Relevant Paths and Files

| Path / File | Description |
|---|---|
| `/Library/Preferences/com.apple.SoftwareUpdate.plist` | The configuration and policy file for the Software Update component. |
| `softwareupdated` (Process) | The core background daemon responsible for searching for updates and calculating required space (`CalculatePrepareSize`). |
| `UpdateBrainService` (Process) | The actual deployment service that builds the snapshot and deploys the payload in real-time. |

---

## Recommended Reading & Deep Dives

* [Manage software updates in Apple Platform Deployment](https://support.apple.com/guide/deployment/manage-software-updates-depc4c80847a/web) - Admin Guide: Enforcing and deferring updates in a managed enterprise.
* [Install software updates for Mac](https://support.apple.com/guide/mac-help/get-macos-updates-mchlpx1065/mac)
* [Transfer to a new Mac with Migration Assistant](https://support.apple.com/en-us/102613)
* [Taking manual control of macOS updates with softwareupdate](https://eclecticlight.co/2023/09/06/taking-manual-control-of-macos-updates-with-softwareupdate/) - A deep dive into manual updates via the Terminal.

---

## 🎬 Summary Video

<!-- YouTube Summary Video -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/RFZYlrmn08Q" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

## 💡 Presentation Visuals

!!! tip "Visual Reference (Student Guide)"
    These images illustrate the interface or mechanism relevant to the lesson's topics.

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
