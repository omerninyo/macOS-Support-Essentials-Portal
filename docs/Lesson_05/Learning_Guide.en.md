# Lesson 05: Applications & Processes
**Student Learning Guide (vEXP)**

## Lesson Objectives
* Installation Workflows
* App Sandboxing
* Diagnostics & Process Troubleshooting
* Enterprise Distribution (VPP)

## Overview
<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/57c8a1df-bbc5-4e2e-9986-b6e4b0e04f4e/"></iframe></div>

## Core Concepts
* **App Store:** Apple's official application distribution marketplace. All hosted apps undergo review, notarization, and operate strictly under App Sandbox constraints.
* **Package (PKG):** An installer package format containing payload files and post-install/pre-install scripts for system distribution. Commonly used for complex enterprise software deployments.
* **Disk Image (DMG / ASIF):** A virtual disk container. In macOS 26 (Tahoe), Apple introduced the high-efficiency ASIF (Apple Sparse Image Format).
* **Sandboxing:** macOS security technology restricting application access to system resources, memory, and unrelated file paths. Data is isolated within dedicated app Containers.
* **Code Signing & CDHash (DeepDive):** Operating system cryptographic validation layer. macOS dynamically verifies memory pages against the Code Directory Hash (CDHash) at runtime to ensure integrity.
* **App Translocation (DeepDive):** Security mechanism (Gatekeeper Path Randomization) preventing malware extracted from ZIP/DMG archives from loading malicious adjacent payloads, executing apps from random, read-only temporary paths until moved to `/Applications`.
* **Preemptive Multitasking & WindowServer (DeepDive):** Kernel preemptive scheduling. If an app's main UI thread stops responding, WindowServer automatically displays the spinning wait cursor ("spinning beach ball").
* **Force Quit:** Immediate process termination (issuing a `SIGKILL` signal) to unresponsive applications, foregoing unsaved state saving.
* **Volume Purchase Program (VPP) / Apple Business Manager (ABM):** Apple's enterprise license purchasing program, allowing organizations to acquire software licenses in volume and assign them to endpoints via MDM without requiring individual user Apple IDs.
* **Self Service:** Enterprise software catalog app enabling standard non-admin users to install approved applications without requiring local administrator credentials.

---

## Core Terminal Commands

### Installers & Disk Images (`installer` & `hdiutil`)
* **`sudo installer -pkg /path/to/package.pkg -target /`**
  Silent PKG installation to root volume. Essential baseline for MDM deployment scripts.

* **`hdiutil attach /path/to/image.dmg`**
  Mount a virtual disk image.

* **`hdiutil detach /Volumes/ImageName`**
  Safely unmount a virtual disk image.

### Process Management & Force Quit (`killall` & `kill`)
* **`killall "App Name"`**
  Gracefully terminate an application by process name (sends `SIGTERM`).

* **`kill -9 [PID]`**
  Force immediate process termination by Process ID (PID), identical to GUI Force Quit (sends `SIGKILL`).

* **`killall cfprefsd`**
  Terminates the core preferences daemon, forcing the OS to flush preference caches. Critical when manually resetting app sandboxes.

### Hidden Application Preferences (`defaults`)
* **`defaults read com.apple.Safari`**
  Reads the full preference domain (`plist`) for Safari.

* **`defaults delete com.apple.Safari`**
  Deletes the preference domain completely, resetting application settings to defaults.

### System Updates & Rosetta (`softwareupdate`)
* **`softwareupdate --install-rosetta --agree-to-license`**
  Quietly installs Rosetta 2 binary translation runtime on Apple Silicon Macs.

---

## Managing Sandboxes and App Resets

**Where do applications store data?**

1. **Preferences:** Stored in `~/Library/Preferences/com.domain.appname.plist`
2. **Application Support:** Stored in `~/Library/Application Support/AppName/`
3. **Containers:** App Store and sandboxed applications do not write directly to unmanaged user paths. All access is redirected to: `~/Library/Containers/[Bundle ID]`.

**How to perform a complete Sandbox App Reset:**

1. Ensure the application is completely quit (Quit or Force Quit).
2. Delete the application's Container folder located at: `~/Library/Containers/[Bundle ID]`.
3. Delete un-sandboxed domain preferences (if any): `defaults delete [Bundle ID]`.
4. Flush preference daemon memory cache by running `killall cfprefsd` in Terminal.
5. Relaunch the application - it will re-initialize cleanly, as if launched for the first time.

---

## Recommended Reading & Links
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

!!! tip "Visual Aid (Student Reference)"
    These images illustrate the interface or mechanism relevant to the lesson topic.

![Slide103_image33](../assets/images/Lesson_05/L05_LegacySlide_Slide103_image33.jpg)
![Slide121_image134](../assets/images/Lesson_05/L05_LegacySlide_Slide121_image134.jpg)
![Slide66_image11](../assets/images/Lesson_05/L05_LegacySlide_Slide66_image11.jpg)
![26-Tahoe-App-Store-scaled](../assets/images/Lesson_05/L05_TahoeUI_26-Tahoe-App-Store-scaled.png)
![26-Tahoe-Force-Quit-scaled](../assets/images/Lesson_05/L05_TahoeUI_26-Tahoe-Force-Quit-scaled.png)

<!-- src_hash: 80644e9d5f257f52ee6202a5ed49367118109f0cc7a0a8fd31972e8a440fe835 -->
