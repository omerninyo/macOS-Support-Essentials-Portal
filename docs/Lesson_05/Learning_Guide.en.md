# Lesson 05 — Applications and Processes
## Student Learning Guide

---

## Lesson Objectives

- Understand the three macOS installation channels (App Store, DMG, PKG)
- Understand the Sandbox mechanism — where applications store their data
- Master tools for diagnosing and force-quitting unresponsive processes
- Understand the VPP and Self Service mechanisms in an enterprise environment

---

## 🎧 Audio Summary — Before or After Class

<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/57c8a1df-bbc5-4e2e-9986-b6e4b0e04f4e/"></iframe></div>

---

## Core Concepts

| Concept | Explanation |
|---|---|
| **App Store** | Apple's official storefront. Every app undergoes review, notarization, and operates within a strict Sandbox. |
| **DMG (Disk Image)** | A virtual drive. Double-click = Mount. Drag to Applications = Install. Eject = Mandatory after installation. |
| **PKG (Package)** | A system-level installer. It disperses files into protected paths → will always require an Admin password. |
| **Gatekeeper** | The macOS security bouncer — verifies that every application is signed and approved by Apple. |
| **Notarization** | An automated malware scanning process performed by Apple before an app is allowed to launch. |
| **Sandbox** | An isolation bubble — an app cannot access files outside of its container without explicit permission. |
| **Container** | The home directory for a Sandboxed app. Located at `~/Library/Containers/[Bundle ID]`. |
| **Force Quit** | Terminating an unresponsive process without saving (sending a `SIGKILL` signal). |
| **VPP / ABM** | Volume Purchase Program via Apple Business Manager. Licenses are owned by the organization, not the user. |
| **Self Service** | The organization's private app store — enables deployment without Admin rights or a personal Apple Account. |

---

## Part 1 — Installation Types

### Where to Find it in Finder

```text
DMG File:  Downloads → Double-click → Volume in Sidebar → Drag to Applications
PKG File:  Double-click → Installer wizard → Admin password required
App Store: Search, click Get — completely automated
```

### Important Change in Tahoe

> [!IMPORTANT]
> Unapproved applications — **Right-click → Open no longer works in Tahoe**.
> The only authorized bypass method: `System Settings → Privacy & Security → Scroll down → Open Anyway`

---

## Part 2 — Sandboxing and App Reset

### Critical Paths

*(Reminder from Lesson 2: The Library folder in your Home directory (`~/`) is the user's personal space. Traditionally, this is where apps store settings and data. We will dive deeper into system architecture domains in the next lesson).*

| What | Path |
|---|---|
| Preferences | `~/Library/Preferences/com.domain.app.plist` |
| Application Support | `~/Library/Application Support/AppName/` |
| Container (Sandbox) | `~/Library/Containers/[Bundle ID]/` |

### Proper App Reset Sequence

1. Quit completely: `Cmd+Q`
2. Open Finder → Go → Hold `Option` → **Library**
3. Navigate to `Containers/` → Find the application's folder
4. Move it to Trash and empty the Trash
5. Relaunch the app → Seeing the "Welcome" screen = Successful Reset

> [!NOTE]
> Deleting an app from `/Applications/` **does not** delete its Container!
> The Container must be deleted separately to achieve a true reset.

---

## Part 3 — Force Quit

### The Three Methods

| Method | How-to |
|---|---|
| **Fastest** | `Cmd + Option + Esc` |
| **Dock** | Right-click the app icon + Hold `Option` → Force Quit |
| **Most Detailed** | Activity Monitor → Select process → Click `X` → Force Quit |

### Quit vs. Force Quit

| Action | Signal Sent | Result |
|---|---|---|
| Standard Quit | `SIGTERM` | The app saves state and shuts down gracefully |
| Force Quit | `SIGKILL` | The kernel terminates the app instantly — **without saving** |

---

## Part 4 — VPP and Self Service

### The Enterprise Workflow

```text
Apple Business Manager (ABM)
        ↓ Licenses
    Enterprise MDM Server
        ↓ Silent Install
      Employee Mac
        ↓ 
  Self Service (Private App Catalog)
```

**The Result:** The employee clicks "Install" — MDM deploys the app silently in the background — **zero Admin prompts, zero personal Apple Account requirement.**

---

## Terminal Commands — Appendix

> [!NOTE]
> The Terminal is not required for this lesson's labs. These commands are provided as an advanced reference for IT administrators.

```bash
# Manually mount a DMG
hdiutil attach /path/to/image.dmg

# Unmount a DMG
hdiutil detach /Volumes/ImageName

# Silent PKG installation (for IT deployment scripts)
sudo installer -pkg /path/to/file.pkg -target /

# Reset app settings (Preferences only, not the full Container)
defaults delete com.apple.Safari

# Flush preferences cache (after deleting a Container)
killall cfprefsd

# Verify PKG signature
pkgutil --check-signature /path/to/file.pkg

# Silent Rosetta 2 installation
softwareupdate --install-rosetta --agree-to-license
```

---

## Links and Further Reading

- [Check app installation and processes on Mac — Apple Support](https://support.apple.com/guide/apple-platform-support/check-app-installation-and-processes-apda5f8a096c/web)
- [Learn about App Store security protections](https://support.apple.com/guide/apple-platform-support/learn-about-app-store-security-protections-apd1a7b8e19c/web)
- [Distribute content with mobile device management](https://support.apple.com/guide/deployment/distribute-content-depe210182ce/web)
- [Explainer: the app sandbox — Eclectic Light](https://eclecticlight.co/2020/09/24/explainer-the-app-sandbox/)

---

## 🎬 Summary Video

<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/z_52E-9epcY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

## Presentation Visuals

!!! tip "Presentation Visuals"
    These images illustrate the interfaces covered in the lesson.

![Installation Types Comparison](../assets/images/Lesson_05/L05_LegacySlide_Slide103_image33.jpg)
![ABM and MDM Diagram](../assets/images/Lesson_05/L05_LegacySlide_Slide121_image134.jpg)
![Self Service Interface](../assets/images/Lesson_05/L05_LegacySlide_Slide66_image11.jpg)
![App Store in Tahoe](../assets/images/Lesson_05/L05_TahoeUI_26-Tahoe-App-Store-scaled.png)
![Force Quit in Tahoe](../assets/images/Lesson_05/L05_TahoeUI_26-Tahoe-Force-Quit-scaled.png)
