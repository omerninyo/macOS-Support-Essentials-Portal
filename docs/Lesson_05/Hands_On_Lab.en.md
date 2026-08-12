# Lesson 05 — Applications and Processes
## Hands-On Lab

> [!NOTE]
> **Objective:**
> Hands-on practice with deploying, installing, and diagnosing macOS applications using a GUI-first approach.
> You will experiment with installation packages (PKG and DMG), challenge Gatekeeper's strict policies in Tahoe, reset sandboxed applications by manipulating their Containers, and execute forceful process terminations.
>
> *Note: In Enterprise environments, App Store distributions are centrally managed via MDM/VPP — see Exercise 5.*

---

## Prerequisites

- A Mac running macOS 26 (Tahoe)
- A local user account with Admin privileges
- `installer.pkg` and `.dmg` files from the Course Assets folder (provided by your instructor)

> [!TIP]
> **Missing a file?** You can download VLC from [videolan.org](https://www.videolan.org/) as a DMG, and Zoom from [zoom.us/download](https://zoom.us/download) as a PKG.

---

## Exercise 1 — PKG Installation and Signature Validation

> **Learning Goal:** PKG = System Installer. Always requires Admin credentials because it writes to protected system paths.

1. Open the `.pkg` file provided by your instructor (double-click).
2. The installation wizard will launch. Look at the top right corner for a padlock icon 🔒.
3. Click the padlock → Verify that the certificate reads **"Developer ID Installer"** (an approved Apple Developer).
4. In the menu bar: Select **File → Show Files** — observe which system paths the payload will be extracted to.
5. Close the file list. Click **Continue** and complete the installation wizard.
6. Enter your Admin password when prompted.
7. Navigate to `/Applications/` and launch the application to confirm a successful installation.

> [!NOTE]
> If the installer prompts for a Restart — you may postpone it until all lab exercises are completed.

---

## Exercise 2 — DMG Installation and Challenging Gatekeeper in Tahoe

> **Learning Goal:** DMG = Virtual Volume. Drag to Applications + Eject. In macOS Tahoe, Gatekeeper enforces stricter security policies.

1. Open Safari and download a DMG file (e.g., VLC from [videolan.org](https://www.videolan.org/)).
2. Once downloaded, double-click the file in your Downloads folder.
3. The DMG window will open. Drag the application icon to the **Applications** folder shortcut.

    > 💡 A copy progress window will appear — wait until it completes.

4. In the Finder sidebar (under **Locations**) — click the **Eject ⏏** icon next to the DMG name.
5. Go to `/Applications/` and open the newly installed application.
6. A standard Gatekeeper warning will appear (this is expected) → click **Open**.

**The Tahoe Challenge — Unsigned Applications:**

> [!IMPORTANT]
> If you are given an unsigned file for testing:
> - Try: Right-click → Open → **Notice this bypass option has been removed in Tahoe.**
> - The Enterprise Path: Go to `System Settings → Privacy & Security` → Scroll down → click **"Open Anyway"**.

---

## Exercise 3 — Sandboxing and Container Reset

> **Learning Goal:** Deleting an application from the Applications folder does not remove its configuration data. Targeting the Container is the correct procedure for sandboxed apps.

1. Open a built-in application (e.g., **Notes**).
2. Modify a setting or preference (color, font, or any visible change).
3. Quit the application entirely: Press **`Cmd + Q`** (do not just click the X button).

**Locating the Container:**

4. Open **Finder** → Go to the top menu bar → Select **Go**.
5. Hold down the `Option (⌥)` key — **Library** will magically appear in the list → click it.
6. Navigate into the **`Containers`** folder.
7. Locate the application's container folder (e.g., `com.apple.Notes`).

    > 💡 Can't find it? Notes doesn't always populate a Container immediately. Try Keynote instead: `com.apple.iWork.Keynote`.

**The Reset Procedure:**

8. Right-click the Container folder → select **Move to Trash**.
9. Empty the Trash (**Finder → Empty Trash**).
10. Relaunch the application → Seeing the "Welcome" screen confirms **the reset was successful** ✅.

> [!CAUTION]
> **Do not run** `killall cfprefsd` while other applications are open — it will abruptly flush the preference cache for all active processes.

---

## Exercise 4 — Force Quit: The Three Methods

> **Learning Goal:** Spinning Beachball = Application Not Responding. Master three ways to terminate a hung process—choosing the fastest method based on the scenario.

Launch both **Safari** and **Calendar**.

**Method 1 — The Fastest (Keyboard):**
1. Press `Option + Command + Escape`.
2. In the Force Quit Applications window: Select **Safari** → click **Force Quit**.
3. Confirm the warning dialog.

Relaunch Safari.

**Method 2 — Via the Dock:**
1. Right-click the Safari icon in the Dock.
2. **While the context menu is open** — hold down the `Option` key.
3. Watch "Quit" dynamically change to **"Force Quit"** → click it.

Relaunch Safari.

**Method 3 — Activity Monitor (Detailed Diagnostics):**
1. Open **Activity Monitor** (via Spotlight: `Cmd+Space` → type "Activity Monitor").
2. Search for "Safari" using the search bar at the top right.
3. Select the Safari process → click the **`X`** (the Stop button in the top toolbar).
4. Choose **Force Quit** in the confirmation dialog.

    > 💡 Pay attention to the **% CPU** column — it provides visibility into which process is consuming excessive resources.

---

## Exercise 5 — (Demo & Discussion) Self Service and VPP

> **Learning Goal:** In an Enterprise environment, the MDM facilitates zero-touch deployment—no Admin credentials, no personal Apple IDs required.

This is a demonstration exercise — your instructor will project this from the master console.

1. The instructor will launch the **Self Service** application (automatically deployed by the MDM).
2. Review the catalog of corporate-approved software.
3. The instructor will click "Install" → Notice: **No Admin prompt, no Apple ID request.**
4. The application seamlessly installs directly into `/Applications/` in the background.

> [!TIP]
> **VPP Troubleshooting in the Field:** If a corporate application deployed via MDM unexpectedly prompts for a personal Apple ID, this is the classic symptom of an expired VPP Token in ABM. The token must be renewed in the MDM portal.

---

## Bonus Exercise — Terminal for Advanced Users

> [!CAUTION]
> For advanced power users only. This is not required for the core lab exercises.

```bash
# Verify a PKG signature
pkgutil --check-signature /path/to/installer.pkg

# Validate an application's notarization ticket
codesign --test-requirement="=notarized" --verify --verbose /Applications/VLC.app

# Flush the preference cache (typically executed after a Container reset via CLI)
killall cfprefsd
```
