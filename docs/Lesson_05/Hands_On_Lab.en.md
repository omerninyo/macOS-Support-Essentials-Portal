# Lesson 05: Applications & Processes
**Hands-On Lab (vEXP)**

> [!NOTE]
> **Lab Objective:**
> Practical exercise in deploying, installing, and troubleshooting macOS applications using the Graphical User Interface. You will experience various installation methods (App Store, PKG, DMG), test Gatekeeper's strict Tahoe policies, and learn how to reset Sandboxed apps and manage stuck processes via Activity Monitor.

## Prerequisites
* A Mac running macOS 26 (Tahoe).
* A user with Administrator rights (Local Admin).
* A Standard User for testing – e.g., `John Appleseed`.
* Active internet connection and Apple ID.
* Access to `Course_Assets_and_Demos` folder.

---

## Exercise 5.1: Installing from the App Store
Installing from the App Store is the safest method, as apps are Sandboxed, Notarized, and reviewed by Apple.

**Steps:**
1. Log in to your Standard User account (`John Appleseed`).
2. Open the **App Store** from Launchpad or Applications.
3. If it's the first time, accept the Welcome screen.
4. Click **Sign In** at the bottom left and enter your Apple ID and password. Complete 2FA if prompted.
5. Search for `Apple Configurator` and press Return.
6. Click **Get** (or the cloud icon).
7. Click **Install**.
8. Wait for the download, then click **Open** to ensure the app works. Accept terms if prompted.
9. Quit the app gracefully using **Command-Q**.

---

## Exercise 5.2: Installing via PKG and Checking Security Signatures
Enterprise software is distributed as PKG files, requiring Admin permissions to install system-wide files.

**Steps:**
1. Open a `.pkg` file provided by the instructor (e.g., `Zoom.pkg` or `Trust Me.pkg` from the demos folder).
2. The Installer opens automatically.
3. **Check the Security Signature:** Look at the top right corner of the Installer window for a Lock icon.
4. Click the Lock to view the security certificate.
5. Ensure the package is signed by an approved "Developer ID Installer".
6. **Inspect Package Contents:** Before clicking continue, go to the Menu Bar, click **File** > **Show Files**.
7. Review the list of files to be installed and their target paths (e.g., `/Library/Application Support`). Close the window.
8. Click **Continue** and complete the installation. Enter the Administrator password when prompted.
9. Navigate to the Applications folder and launch the new software to verify.

---

## Exercise 5.3: DMG Drag-and-Drop and the Tahoe Gatekeeper Challenge
This is the most common installation method outside the App Store. The DMG acts as a virtual removable volume.

**Steps:**
1. Open Safari and download a DMG installer (e.g., VLC).
2. Once downloaded, Safari transparently applies a Quarantine flag indicating it came from the internet.
3. Open Finder, go to Downloads, and double-click the DMG to Mount it.
4. In the new window, drag the app icon to the Applications shortcut to copy it.
5. In the Finder Sidebar under Locations, click the **Eject** symbol next to the DMG name.
6. Go to the Applications folder and open the app you just copied.
7. **Gatekeeper Intervention:** A warning appears stating the app was downloaded from the internet.
8. Click **Open**. (Note: If this was an unsigned app, the "Open" button would not exist, and Right-Click > Open no longer bypasses Gatekeeper in macOS Tahoe).
9. **Tahoe Specific (Unsigned App Challenge):** If you attempt to open an unsigned test app, macOS Tahoe will flatly refuse. You must go to **System Settings > Privacy & Security**, scroll down to Security, and explicitly click **Open Anyway**.

---

## Exercise 5.4: Sandboxing and Resetting App Preferences
Modern macOS apps run Sandboxed. They save their data in a specific "Container". Deleting this Container via Finder is the proper way to "factory reset" a malfunctioning app.

**Steps:**
1. Open **Apple Configurator** (or another simple app like Notes).
2. Go to the app's Settings and change any preference so it saves data.
3. Completely quit the app (Command-Q).
4. Open **Finder**. In the top menu bar, click **Go**.
5. Hold the `Option` (⌥) key on the keyboard. A hidden **Library** folder will appear. Click it.
6. Locate and enter the `Containers` folder.
7. Find the folder for your app (e.g., `Apple Configurator` or `com.apple.configurator`).
8. Right-click this folder and select **Move to Trash**. Empty the trash.
9. *Pro Tip (To clear memory cache):* Open Terminal and run `killall cfprefsd` to prevent the system from restoring zombie plists.
10. Reopen the app from the Applications folder. It will launch as if it's the very first time (Welcome screen/reset settings) because a fresh Container was automatically generated.

---

## Exercise 5.5: Troubleshooting and Force Quitting Stuck Processes
When an app hangs, it enters a *(Not Responding)* state. You can terminate problematic processes via the GUI.

**Steps:**
1. Open Safari and Calendar for this exercise.
2. **Method 1: Quick Force Quit Mechanism**
   * Press `Option-Command-Escape`.
   * In the "Force Quit Applications" window, select Safari and click **Force Quit**.
   * Confirm the warning. Watch the app instantly close.
3. Reopen Safari.
4. **Method 2: Advanced Management via Activity Monitor**
   * Open **Activity Monitor** (in `Applications > Utilities`).
   * Ensure you are in the CPU or Memory tab.
   * Search for `Safari` in the top right.
   * Select the Safari process and click the `X` (Stop) button at the top.
   * Choose between 'Quit' (soft close) and 'Force Quit' (hard kill). Click **Force Quit**.
5. Verify the process is completely removed from the list.

---

## Exercise 5.6: (Demo & Discussion) Enterprise VPP and Self Service
In a managed organization, standard users cannot enter Admin passwords. IT provides a Self Service catalog.

**Scenario Steps:**
1. The instructor will display an enterprise store app (e.g., Jamf Self Service) on the demo station.
2. Observe how the catalog provides approved software.
3. When the user clicks **Install**, the MDM executes the installation in the background with System privileges (no password prompt).
4. App Store apps are pre-purchased via VPP and pushed seamlessly without requiring a personal Apple ID.
5. **Tip:** If an enterprise app suddenly prompts for an Apple ID, it often indicates the MDM's VPP license assignment failed or the token expired.

---

## Extra / Technical Tip
> [!CAUTION]
> For advanced users who want to see terminal equivalents. Not required for the core lab.

**Check PKG Signature:**
```bash
pkgutil --check-signature /path/to/installer.pkg
```
**Verify App Notarization:**
```bash
codesign --test-requirement="=notarized" --verify --verbose /Applications/BBEdit.app
```
**Kill App and Flush Plist Cache:**
```bash
killall Safari
killall cfprefsd
```
