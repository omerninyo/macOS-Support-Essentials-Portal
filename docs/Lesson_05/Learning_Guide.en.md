# Lesson 05 — Applications and Processes
## Learning Guide (Student Summary)

---

## Objective

- Understand the three macOS installation channels (App Store, DMG, PKG).
- Comprehend the Sandbox mechanism — where applications store their data.
- Master GUI tools for diagnosing and force-quitting hung processes.
- Learn the Enterprise VPP (Volume Purchase Program) and Self Service deployment flow.

---

## 🎧 Audio Summary — Listen Before or After Class

<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/57c8a1df-bbc5-4e2e-9986-b6e4b0e04f4e/"></iframe></div>

---

## Core Concepts

| Term | Explanation |
|---|---|
| **App Store** | Apple's official storefront. Every application passes strict review, notarization, and operates within a strict Sandbox. |
| **DMG (Disk Image)** | A virtual drive. Double-click to Mount. Drag the app to Applications to install. Ejecting when done is mandatory. |
| **PKG (Package)** | A system-level installer. Scatters files to protected paths → always requires an Admin password. |
| **Gatekeeper** | The macOS security enforcer — verifies that every application is signed and approved by Apple. |
| **Notarization** | Apple's automated malware scanning process for apps before they are allowed to run. |
| **Sandbox** | An isolation bubble — sandboxed apps cannot access files outside their container without explicit user permission. |
| **Container** | The home directory for a Sandboxed application. Located at `~/Library/Containers/[Bundle ID]`. |
| **Force Quit** | Terminating a hung process without saving state (sending a `SIGKILL` signal). |
| **VPP / ABM** | Enterprise licensing mechanism (Volume Purchase Program via Apple Business Manager). The license belongs to the organization, not the user. |
| **Self Service** | The organization's private App Store — enables seamless installation without Admin rights or personal Apple IDs. |

---

## Part 1 — Installation Types

### Locating in Finder

```text
DMG File:  Downloads folder → Double-click → Volume appears in Sidebar → Drag to Applications
PKG File:  Double-click → Installation Wizard launches → Admin credentials required
App Store: Search, click Download — Everything is handled automatically
```

### Crucial Change in macOS Tahoe

> [!IMPORTANT]
> Unapproved Applications — **Right-click → Open is deprecated in Tahoe**.
> The only valid GUI path: `System Settings → Privacy & Security → Scroll down → Open Anyway`.

---

## Part 2 — Sandbox and App Reset

### Important Paths

*(Reminder from Lesson 2: The `Library` folder in your Home directory (`~/`) is your personal space. Traditionally, this is where apps save their configurations and data. We will dive deeper into macOS filesystem architecture in the next lesson).*

| What | Path |
|---|---|
| Preferences | `~/Library/Preferences/com.domain.app.plist` |
| Application Support | `~/Library/Application Support/AppName/` |
| Container (Sandbox) | `~/Library/Containers/[Bundle ID]/` |

### Correct Sequence for App Reset

1. Fully quit the app: `Cmd+Q`
2. Open Finder → Click **Go** in the menu bar → Hold `Option` → Select **Library**
3. Navigate to `Containers/` → Locate the application's folder
4. Move the folder to Trash and empty it
5. Relaunch the app → Seeing the "Welcome" screen confirms a successful reset

> [!NOTE]
> Deleting an application from `/Applications/` **does not** delete its Container!
> The Container must be explicitly deleted to perform a reset.

---

## Part 3 — Force Quit

### 4 Methods

| Method | How |
|---|---|
| **Fastest (Keyboard)** | `Cmd + Option + Esc` |
| **Dock** | Right-click the icon + Hold `Option` → Force Quit |
| **Diagnostic (GUI First)** | Activity Monitor → Review CPU/RAM usage and Open Files before clicking the `X` button |
| **Terminal (CLI)** | `killall AppName` to instantly kill remotely or when the GUI is completely frozen |

### Quit vs. Force Quit

| Action | Signal Sent | Result |
|---|---|---|
| Standard Quit | `SIGTERM` | The app saves data and terminates gracefully |
| Force Quit | `SIGKILL` | The kernel kills the process immediately — **no data is saved** |

---

## Part 4 — VPP and Self Service

### The Enterprise Workflow

```text
Apple Business Manager (ABM)
        ↓ Licenses
   Corporate MDM Server
        ↓ Silent Install
    Employee's Mac
        ↓ 
  Self Service (Private Corporate Catalog)
```

**The Outcome:** The employee clicks "Install" — the MDM installs it silently in the background — **without Admin rights, and without a personal Apple ID.**

---

## Terminal Commands — Appendix

> [!NOTE]
> The Terminal is not required for the lab exercises. These commands are provided as an Enterprise IT extension for those interested.

```bash
# Manually mount a DMG
hdiutil attach /path/to/image.dmg

# Eject a DMG
hdiutil detach /Volumes/ImageName

# Silent PKG installation (Standard IT Scripting)
sudo installer -pkg /path/to/file.pkg -target /

# Reset App Preferences (Preferences only, ignores Sandbox Containers)
defaults delete com.apple.Safari

# Clear Preferences Cache (Run after deleting a Container)
killall cfprefsd

# Verify PKG signature
pkgutil --check-signature /path/to/file.pkg

# Silent Rosetta 2 installation for Apple Silicon
softwareupdate --install-rosetta --agree-to-license
```

---

## Links and Further Reading

- [Check app installation and processes on Mac — Apple Support](https://support.apple.com/guide/apple-platform-support/check-app-installation-and-processes-apda5f8a096c/web)
- [Learn about App Store security protections](https://support.apple.com/guide/apple-platform-support/learn-about-app-store-security-protections-apd1a7b8e19c/web)
- [Distribute content with mobile device management](https://support.apple.com/guide/deployment/distribute-content-depe210182ce/web)
- [Explainer: the app sandbox — Eclectic Light](https://eclecticlight.co/2020/09/24/explainer-the-app-sandbox/)

---

## 🎬 Video Summary

<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/z_52E-9epcY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

## 💡 Presentation Visuals

!!! tip "Visual Aids"
    These images illustrate the interfaces discussed in this lesson.

![Installation Types Comparison](../assets/images/Lesson_05/L05_LegacySlide_Slide103_image33.jpg)
![ABM and MDM Diagram](../assets/images/Lesson_05/L05_LegacySlide_Slide121_image134.jpg)
![Self Service Interface](../assets/images/Lesson_05/L05_LegacySlide_Slide66_image11.jpg)
![App Store in Tahoe](../assets/images/Lesson_05/L05_TahoeUI_26-Tahoe-App-Store-scaled.png)
![Force Quit in Tahoe](../assets/images/Lesson_05/L05_TahoeUI_26-Tahoe-Force-Quit-scaled.png)
