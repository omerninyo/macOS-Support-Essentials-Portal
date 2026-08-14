# Lesson 05 — Applications and Processes
## Hands-On Lab

!!! note "Lab Objective"
    Practical experience in deploying, installing, and diagnosing macOS applications via the graphical user interface.
    You will experience different installation types (PKG and DMG), navigate Gatekeeper restrictions in Tahoe, reset applications via their Container, and execute Force Quits.

    *Note: In an enterprise environment, App Store deployment is managed via MDM/VPP — see Exercise 5.*

---

## Prerequisites

- A Mac running macOS 26 (Tahoe)
- A user account with local Admin privileges
- `installer.pkg` and `.dmg` files from the Course Assets folder (provided by the instructor)

!!! tip
    **Missing a file?** You can download VLC from [videolan.org](https://www.videolan.org/) as a DMG, and Zoom from [zoom.us/download](https://zoom.us/download) as a PKG.

---

## Exercise 1 — PKG Installation and Signature Verification

> **What we're learning:** PKG = System-level installer. It will always require Admin rights because it writes to protected system paths.

1. Double-click the `.pkg` file provided by your instructor.
2. The installation wizard will launch. Look at the top right corner — the padlock icon 🔒.
3. Click the padlock → Verify that it states **"Developer ID Installer"** (an approved developer).
4. In the menu bar: **File → Show Files** — review which paths the files will be written to.
5. Close the file list. Click **Continue** and complete the installation.
6. Enter your Admin password when prompted.
7. Navigate to `/Applications/` and launch the software to verify it works.

!!! note
    If the installer prompts for a Restart — you can postpone this until the end of all exercises.

---

## Exercise 2 — DMG Installation and Challenging Gatekeeper in Tahoe

> **What we're learning:** DMG = Virtual Volume. Drag to Applications + Eject. In Tahoe, Gatekeeper is far stricter.

1. Open Safari and download a DMG file (e.g., VLC from [videolan.org](https://www.videolan.org/)).
2. Once downloaded, double-click the file in Downloads.
3. The DMG window will open. Drag the application icon to the **Applications** shortcut.

    > 💡 You will see a copy progress window — wait until it completes.

4. In the Finder sidebar (under **Locations**) — click the **Eject ⏏** icon next to the DMG name.
5. Navigate to `/Applications/` and launch the application.
6. A Gatekeeper warning will appear (this is expected) → click **Open**.

**The Tahoe Challenge — Unsigned Application:**

!!! important
    If you are provided with an unsigned file for testing:
    - Try this: Right-click → Open → **Notice that this option no longer exists in Tahoe.**
    - The correct method: `System Settings → Privacy & Security` → Scroll down → Click **"Open Anyway"**

---

## Exercise 3 — Sandboxing and Container Reset

> **What we're learning:** Deleting an application from Applications does not delete its settings. The Container is the actual target.

1. Launch a built-in application (e.g., **Notes**).
2. Change a setting (color, font, any configuration change you prefer).
3. Quit completely: **`Cmd + Q`** (Do not just click the X).

**Locating the Container:**

4. Open **Finder** → Top menu bar → **Go**.
5. Hold the `Option (⌥)` key — **Library** will appear in the list → Click it.
6. Navigate into the **`Containers`** directory.
7. Locate the application's folder (e.g., `com.apple.Notes`).

    > 💡 Can't find it? Notes doesn't always show a straightforward Container. Try Keynote: `com.apple.iWork.Keynote`

**The Reset:**

8. Right-click the Container folder → **Move to Trash**.
9. Empty the Trash (**Finder → Empty Trash**).
10. Relaunch the application → Seeing the "Welcome" screen indicates **the reset was successful** ✅.

!!! caution
    **Do not execute** `killall cfprefsd` while other applications are running — it will affect the preferences of all active processes.

---

## Exercise 4 — Force Quit: The Three Methods

> **What we're learning:** The spinning beachball = Not Responding. Three ways to terminate — choose the fastest one for your scenario.

Open **Safari** and **Calendar**.

**Method 1 — The Fastest:**
1. Press `Option + Command + Escape`.
2. In the window that appears: Select **Safari** → Click **Force Quit**.
3. Confirm the warning dialog.

Relaunch Safari.

**Method 2 — Via the Dock:**
1. Right-click the Safari icon in the Dock.
2. **While the menu is open** — hold `Option`.
3. Watch how "Quit" transforms into **"Force Quit"** → Click it.

Relaunch Safari.

**Method 3 — Activity Monitor (The most detailed):**
1. Launch **Activity Monitor** (via Spotlight: `Cmd+Space` → "Activity Monitor").
2. Search for "Safari" in the search bar.
3. Select the process → Click the **`X`** (the circular button in the top toolbar).
4. Select **Force Quit** in the dialog.

    > 💡 Pay attention to the **% CPU** column — this reveals what is consuming system resources.

---

## Exercise 5 — (Demo and Discussion) Self Service and VPP

> **What we're learning:** In an enterprise environment — MDM enables installations without Admin privileges and without personal Apple IDs.

This is a demonstration exercise — the instructor will present from the main console.

1. The instructor will launch **Self Service** (automatically deployed by the MDM).
2. Review the catalog of approved enterprise software.
3. The instructor will click "Install" → Notice: **No Admin prompt, no Apple ID prompt.**
4. The application is installed directly to `/Applications/` in the background.

!!! tip "A sign of a VPP issue in the field"
    If an enterprise application prompts for an Apple ID → This is a sign that the VPP Token has expired in ABM. It must be renewed in the portal.

---

## Bonus Exercise — Terminal for Advanced Users

!!! caution
    For advanced users only. Not required for the core exercise.

```bash
# Verify PKG signature
pkgutil --check-signature /path/to/installer.pkg

# Validate application notarization
codesign --test-requirement="=notarized" --verify --verbose /Applications/VLC.app

# Flush preferences cache (after a Container reset)
killall cfprefsd
```
