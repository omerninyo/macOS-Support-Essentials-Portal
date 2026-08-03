# Lesson 05: Applications and Processes
**Student Learning Guide (vEXP)**

## Lesson Objectives
* Installation Processes
* Sandboxing
* Diagnosing and Troubleshooting Unresponsive Apps
* Enterprise Deployment (VPP)
**[Image Recommendation]:** A minimalist vector icon of the App Store "A" logo and an open cardboard box representing packages.

## Overview
<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/57c8a1df-bbc5-4e2e-9986-b6e4b0e04f4e/"></iframe></div>

## Core Concepts
* **App Store:** Apple's official application store. Every application here undergoes review, notarization, and operates within Sandbox constraints.
* **Package (PKG):** An installer file containing a collection of files and scripts to be distributed across the system. Primarily used for complex enterprise software installations.
* **Disk Image (DMG / ASIF):** A virtual disk volume. In macOS 26 (Tahoe), Apple introduced the highly efficient ASIF (Apple Sparse Image Format).
* **Sandboxing:** A macOS security mechanism that restricts an application's access to system resources, memory, and unrelated files. Data is stored inside an isolated "Container".
* **Code Signing & CDHash (DeepDive):** The operating system's cryptographic infrastructure. The system validates every memory page in real time against the Code Directory Hash (CDHash) to ensure no malicious modifications occurred.
* **App Translocation (DeepDive):** A mechanism (Gatekeeper Path Randomization) that prevents malicious applications extracted from a ZIP/DMG file from loading adjacent files, by executing them from a randomized, read-only location until moved to the Applications folder.
* **Preemptive Multitasking & WindowServer (DeepDive):** The kernel manages processes preemptively. If the main user interface thread hangs, WindowServer automatically displays the spinning wait cursor ("spinning beachball").
* **Force Quit:** An aggressive forced termination of an unresponsive application (sending a `SIGKILL` command), which does not allow data saving.
* **Volume Purchase Program (VPP) / Apple Business Manager (ABM):** The enterprise purchasing program allowing organizations to acquire licenses and distribute them to employees via MDM without requiring personal Apple IDs.
* **Self Service:** The organization's private app store allowing standard users to install approved software without administrator credentials.

---

## Key Terminal Commands

### Installers and Disks (`installer` & `hdiutil`)
* **`sudo installer -pkg /path/to/package.pkg -target /`**
  Silent installation of a PKG to the target root volume. The baseline command for MDM scripts.

* **`hdiutil attach /path/to/image.dmg`**
  Mounting a virtual disk image.

* **`hdiutil detach /Volumes/ImageName`**
  Safely unmounting a virtual disk image.

### Process Management and Forced Termination (`killall` & `kill`)
* **`killall "App Name"`**
  Gracefully terminating an application by name (sends `SIGTERM`).

* **`kill -9 [PID]`**
  Forcing an immediate crash via process ID, identical to the graphical Force Quit operation (sends `SIGKILL`).

* **`killall cfprefsd`**
  Terminating the configuration process, forcing the system to flush the preference file cache. Critical during manual sandbox resets.

### Hidden Application Settings (`defaults`)
* **`defaults read com.apple.Safari`**
  Reads the entire preference file (plist) for Safari.

* **`defaults delete com.apple.Safari`**
  Deletes the preference file entirely, restoring the application to factory default state.

### System Updates and Rosetta (`softwareupdate`)
* **`softwareupdate --install-rosetta --agree-to-license`**
  Silent and rapid installation of the Rosetta 2 translation environment on Apple Silicon Macs.

---

## Managing Sandboxes and Application Resets

**Where do applications store their data?**

1. **Preferences:** Under `~/Library/Preferences/com.domain.appname.plist`
2. **Application Support:** Under `~/Library/Application Support/AppName/`
3. **Containers:** App Store applications or sandboxed applications do not write to general directories. All access is redirected to: `~/Library/Containers/[Bundle ID]`.

**How to reset a Sandboxed application (Complete Reset):**

1. Ensure the application is completely closed (Quit or Force Quit).
2. Delete the application's Container directory at: `~/Library/Containers/[Bundle ID]`.
3. Delete saved system preferences (if any exist outside the sandbox): `defaults delete [Bundle ID]`.
4. Flush the memory cache by executing `killall cfprefsd` in Terminal.
5. Relaunch the application—it will be recreated from scratch as if launched for the first time.

---

## Recommended Links and Further Reading
* [Check app installation and processes on Mac](https://support.apple.com/guide/apple-platform-support/check-app-installation-and-processes-apda5f8a096c/web)
* [Learn about App Store security protections](https://support.apple.com/guide/apple-platform-support/learn-about-app-store-security-protections-apd1a7b8e19c/web)
* [Distribute content with mobile device management](https://support.apple.com/guide/deployment/distribute-content-depe210182ce/web)
* [Explainer: the app sandbox](https://eclecticlight.co/2020/09/24/explainer-the-app-sandbox/)
* [macOS Tahoe brings a new disk image format](https://eclecticlight.co/2024/09/16/macos-tahoe-brings-a-new-disk-image-format/)

## Summary Video
<!-- Summary Video from YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/z_52E-9epcY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

!!! tip "Visual Demonstration (Student Auxiliary)"
    These images illustrate the interface or mechanism relevant to the lesson topic.

![Slide103_image33](../assets/images/Lesson_05/L05_LegacySlide_Slide103_image33.jpg)
![Slide121_image134](../assets/images/Lesson_05/L05_LegacySlide_Slide121_image134.jpg)
![Slide66_image11](../assets/images/Lesson_05/L05_LegacySlide_Slide66_image11.jpg)
![26-Tahoe-App-Store-scaled](../assets/images/Lesson_05/L05_TahoeUI_26-Tahoe-App-Store-scaled.png)
![26-Tahoe-Force-Quit-scaled](../assets/images/Lesson_05/L05_TahoeUI_26-Tahoe-Force-Quit-scaled.png)

<!-- src_hash: c595259ce1cc201b26cb418a255e279fa679901c69c91d8860b490651ec24ec9 -->
