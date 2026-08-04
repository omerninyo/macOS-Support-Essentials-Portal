# Lesson 05: Applications & Processes
**Learning Guide (vEXP)**

## Lesson Objectives
* Installation Processes
* Sandboxing
* Troubleshooting and Freezes
* Enterprise Deployment (VPP)
**[Image Recommendation]:** A minimalist vector icon of the App Store "A" logo and an open cardboard box representing packages.

## Overview
<!-- Captivate NotebookLM Podcast -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/57c8a1df-bbc5-4e2e-9986-b6e4b0e04f4e/"></iframe></div>

## Core Concepts
* **App Store:** Apple's official app marketplace. Apps undergo App Review, Notarization, and run under strict Sandboxing.
* **Package (PKG):** An installation file containing a payload and scripts to distribute files across the system. Used for complex enterprise software.
* **Disk Image (DMG / ASIF):** A virtual disk. In macOS 26 (Tahoe), Apple introduced the highly efficient ASIF (Apple Sparse Image Format).
* **Sandboxing:** A macOS security mechanism that restricts an app's access to system resources, memory, and unrelated files. Data is stored in a isolated "Container".
* **Code Signing & CDHash (DeepDive):** The cryptographic foundation of macOS security. macOS uses lazy checking of memory pages against the Code Directory Hash (CDHash) to ensure apps haven't been tampered with.
* **App Translocation (DeepDive):** Gatekeeper Path Randomization prevents malicious apps extracted from ZIPs/DMGs from loading adjacent files by running them from a randomized, read-only location until properly moved to Applications.
* **Preemptive Multitasking & WindowServer (DeepDive):** The kernel manages threads forcefully. If an app's main UI thread hangs for a few seconds, WindowServer displays the spinning beachball cursor.
* **Force Quit:** Aggressively terminates an unresponsive app (sending a `SIGKILL` signal) without allowing it to save data.
* **Volume Purchase Program (VPP) / Apple Business Manager (ABM):** The enterprise purchase program allowing organizations to buy app licenses in bulk and distribute them via MDM without needing personal Apple IDs.
* **Self Service:** The organization's private app store, allowing standard users to install approved software without an Admin password.

---

## Key Terminal Commands

### Installers and Disks (`installer` & `hdiutil`)
* **`sudo installer -pkg /path/to/package.pkg -target /`**
  Silent installation of a PKG to the root drive. The fundamental command for MDM scripts.
* **`hdiutil attach /path/to/image.dmg`**
  Mounts a virtual disk image.
* **`hdiutil detach /Volumes/ImageName`**
  Safely unmounts a virtual disk.

### Process Management & Force Quit (`killall` & `kill`)
* **`killall "App Name"`**
  Gracefully quits an application by process name (sends `SIGTERM`).
* **`kill -9 [PID]`**
  Instantly forces a process to quit by its Process ID, identical to the graphical Force Quit (sends `SIGKILL`).
* **`killall cfprefsd`**
  Kills the configuration daemon, forcing macOS to flush the memory cache of preference files. Crucial when manually resetting app sandboxes.

### Hidden App Settings (`defaults`)
* **`defaults read com.apple.Safari`**
  Reads the entire preferences plist for Safari.
* **`defaults delete com.apple.Safari`**
  Deletes the preferences file entirely, returning the app to factory settings.

### System Updates & Rosetta (`softwareupdate`)
* **`softwareupdate --install-rosetta --agree-to-license`**
  Silently installs the Rosetta 2 translation environment for Apple Silicon Macs.

---

## Managing Sandboxes and App Resets

**Where do apps save their data?**
1. **Preferences:** Under `~/Library/Preferences/com.domain.appname.plist`
2. **Application Support:** Under `~/Library/Application Support/AppName/`
3. **Containers:** App Store apps and Sandboxed apps do not write to the general folders above. Instead, all their access is routed to: `~/Library/Containers/[Bundle ID]`.

**How to reset a Sandboxed app (Complete Reset):**
1. Ensure the app is completely closed (Quit or Force Quit).
2. Delete the app's Container folder at: `~/Library/Containers/[Bundle ID]`.
3. Clear system cached settings (if they exist outside the Sandbox): `defaults delete [Bundle ID]`.
4. Clear the memory cache by running `killall cfprefsd` in Terminal.
5. Reopen the app - it will be recreated from scratch as if launched for the first time.

---

## Recommended Reading
* [Check app installation and processes on Mac](https://support.apple.com/guide/apple-platform-support/check-app-installation-and-processes-apda5f8a096c/web)
* [Learn about App Store security protections](https://support.apple.com/guide/apple-platform-support/learn-about-app-store-security-protections-apd1a7b8e19c/web)
* [Distribute content with mobile device management](https://support.apple.com/guide/deployment/distribute-content-depe210182ce/web)
* [Explainer: the app sandbox](https://eclecticlight.co/2020/09/24/explainer-the-app-sandbox/)
* [macOS Tahoe brings a new disk image format](https://eclecticlight.co/2024/09/16/macos-tahoe-brings-a-new-disk-image-format/)

## Summary Video
<!-- YouTube Summary Video -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/z_52E-9epcY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

!!! tip "Visual Aids"
    These images illustrate the interfaces or mechanisms relevant to the lesson.

![Slide103_image33](../assets/images/Lesson_05/L05_LegacySlide_Slide103_image33.jpg)
![Slide121_image134](../assets/images/Lesson_05/L05_LegacySlide_Slide121_image134.jpg)
![Slide66_image11](../assets/images/Lesson_05/L05_LegacySlide_Slide66_image11.jpg)
![26-Tahoe-App-Store-scaled](../assets/images/Lesson_05/L05_TahoeUI_26-Tahoe-App-Store-scaled.png)
![26-Tahoe-Force-Quit-scaled](../assets/images/Lesson_05/L05_TahoeUI_26-Tahoe-Force-Quit-scaled.png)
