# Lesson 05 — Applications and Processes
## Hands-On Lab

> [!NOTE]
> **Lab Objective:**
> Practical experience deploying, installing, and diagnosing macOS applications using the native GUI.
> You will handle various installation types (PKG and DMG), navigate Gatekeeper constraints in Tahoe, perform app resets via Sandboxed Containers, and execute Force Quits.
>
> *Note: In an enterprise environment, App Store deployment is handled via MDM/VPP — see Exercise 5.*

---

## Prerequisites

- A Mac running macOS 26 (Tahoe)
- A local Administrator account
- `installer.pkg` and `.dmg` files from the Course Assets folder (provided by the instructor)

> [!TIP]
> **Missing a file?** You can download VLC from [videolan.org](https://www.videolan.org/) as a DMG, and Zoom from [zoom.us/download](https://zoom.us/download) as a PKG.

---

## Exercise 1: PKG Installation and Signature Verification

> **What you'll learn:** A PKG is a system-level installer. It will always require Admin credentials because it writes to protected system paths.

1. Open the `.pkg` file provided by the instructor (double-click).
2. The installation wizard will launch. Look at the top right corner — click the padlock icon 🔒.
3. Verify that the certificate reads **"Developer ID Installer"** (an Apple-approved developer).
4. In the menu bar, go to: **File → Show Files** — inspect the paths where files will be written.
5. Close the file list. Click **Continue** and complete the installation wizard.
6. Enter your Admin password when prompted.
7. Navigate to `/Applications/` and launch the installed application to confirm success.

> [!NOTE]
> If the installer requests a Restart, you can postpone it until the end of all lab exercises.

---

## Exercise 2: DMG Installation and Gatekeeper in Tahoe

> **What you'll learn:** A DMG is a virtual Volume. The workflow is Drag to Applications + Eject. In Tahoe, Gatekeeper enforces stricter security policies.

1. Open Safari and download a DMG file (e.g., VLC from [videolan.org](https://www.videolan.org/)).
2. Once downloaded, double-click the file in your Downloads folder.
3. The DMG window will open. Drag the application icon to the **Applications** shortcut folder.

    > 💡 You will see a copy progress window — wait for it to complete.

4. In the Finder Sidebar (under **Locations**) — click the **Eject ⏏** icon next to the DMG name.
5. Navigate to `/Applications/` and launch the application.
6. The Gatekeeper warning will appear (this is expected) → click **Open**.

**Tahoe Challenge — Unsigned Application:**

> [!IMPORTANT]
> If provided with an unsigned file for testing:
> - Try: Right-click → Open → **Notice that this option is no longer available in Tahoe.**
> - The correct method: `System Settings → Privacy & Security` → Scroll down → click **"Open Anyway"**.

---

## Exercise 3: Sandboxing and Container Reset

> **What you'll learn:** Moving an app to the Trash from `/Applications/` does not delete its settings. Resetting the Sandbox Container is required.

1. Launch a built-in macOS application (e.g., **Notes**).
2. Modify a preference (color, font, or any visible setting).
3. Quit the app completely: **`Cmd + Q`** (Do not just click the red X).

**Locating the Container:**

4. Open **Finder** → top Menu Bar → **Go**.
5. Hold the `Option (⌥)` key — the hidden **Library** folder will appear → click it.
6. Navigate into the **`Containers`** directory.
7. Locate the application's folder (e.g., `com.apple.Notes`).

    > 💡 Can't find it? Not all apps utilize Containers like Notes. Try Keynote: `com.apple.iWork.Keynote`

**The Reset Process:**

8. Right-click the Container folder → **Move to Trash**.
9. Empty the Trash (**Finder → Empty Trash**).
10. Relaunch the application → Seeing the "Welcome" screen = **The reset was successful** ✅.

> [!CAUTION]
> **Do not** run `killall cfprefsd` while other applications are open — it will affect the preference caching for all running processes.

---

## Exercise 4: Force Quit (Three Methods)

> **What you'll learn:** The spinning beachball means an app is "Not Responding". Master three ways to terminate processes rapidly depending on the situation.

Launch both **Safari** and **Calendar**.

**Method 1 — The Fastest Way:**
1. Press `Option + Command + Escape`.
2. In the Force Quit window: select **Safari** → click **Force Quit**.
3. Confirm the warning dialog.

Relaunch Safari.

**Method 2 — Via the Dock:**
1. Right-click the Safari icon in the Dock.
2. **While the menu is open** — press and hold the `Option` key.
3. Watch "Quit" transform into **"Force Quit"** → click it.

Relaunch Safari.

**Method 3 — Activity Monitor (Most Detailed):**
1. Open **Activity Monitor** (via Spotlight: `Cmd+Space` → type "Activity Monitor").
2. Search for "Safari" in the search bar.
3. Select the process → click the **`X`** button (the round icon in the top toolbar).
4. Choose **Force Quit** in the dialog prompt.

    > 💡 Pay attention to the **% CPU** column — this reveals which processes are consuming system resources.

---

## Exercise 5: (Demo & Discussion) Self Service and VPP

> **What you'll learn:** In an enterprise environment, MDM facilitates application deployments without requiring Admin credentials or personal Apple Accounts.

*This is an instructor-led demonstration from the main presentation station.*

1. The instructor will launch the organization's **Self Service** app (deployed automatically via MDM).
2. Observe the approved enterprise software catalog.
3. The instructor will click "Install" → Notice: **No Admin prompt, no Apple Account request.**
4. The application silently deploys to the `/Applications/` directory in the background.

> [!TIP]
> **Field Troubleshooting VPP:** If an enterprise-managed app suddenly prompts the user for an Apple ID, it is a primary indicator that the VPP Token has expired in Apple Business Manager. IT must renew the token in the MDM portal.

---

## Bonus Exercise — Terminal for Advanced Users

> [!CAUTION]
> Intended for advanced users only. Not required to complete the core lab.

```bash
# Verify PKG signature
pkgutil --check-signature /path/to/installer.pkg

# Validate application Notarization status
codesign --test-requirement="=notarized" --verify --verbose /Applications/VLC.app

# Flush preferences cache (useful after a Container reset)
killall cfprefsd
```
