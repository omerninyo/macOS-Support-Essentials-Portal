# Lesson 05: Applications and Processes
**Hands-On Lab (Student Practice)**

> [!NOTE]
> **Lab Objective:**
> Hands-on practice deploying, installing, and diagnosing applications on macOS using the graphical user interface. During this lab, you will experience a variety of installation methods (PKG installer packages and dragging DMG files), examine how Gatekeeper protects the system (specifically in macOS Tahoe), and learn how to reset Sandboxed applications and manage unresponsive processes via Activity Monitor.
> 
> *Note regarding App Store:* In a lab and enterprise environment, students and employees do not log in with a personal Apple Account. Enterprise deployments are performed via VPP and MDM mechanisms without requiring a personal account.

## Prerequisites
* A Mac computer running macOS 26 (Tahoe).
* A user account with administrative privileges (Local Admin).
* A standard user account for testing purposes (Standard User) – e.g., `Student`.
* Access to the `Course_Assets_and_Demos` folder (or download demo applications from the internet).

---

## Exercise 1: Installing via Installer Package (PKG) and Inspecting Graphical Signature
Enterprise software is distributed as installer packages (Packages), which require Admin privileges to deploy system files.

1. Open an installer package file (`.pkg` extension) provided by your course instructor (for example, `Zoom.pkg` from the demo folder).
2. The system Installer assistant will open automatically.
3. **Checking Security Signature:** Look at the top-right corner of the installation window. You should see a Lock icon.
4. Click the lock icon to open the certificate window.
5. Verify that it states the package is signed by an approved developer (Developer ID Installer).
6. **Inspecting Package Content:** Before clicking Continue, go to the menu bar, click **File**, and then click **Show Files**.
7. Review the list to see which paths files will be installed to (for example `/Library/Application Support`). Close the window.
8. Click **Continue** and complete the installation. Enter Administrator credentials when prompted.
9. Navigate to the Applications folder (`/Applications`) and open the new application to verify installation.

---

## Exercise 2: Drag-and-Drop Installation (DMG) and Challenging Gatekeeper in Tahoe
The most common installation method outside the App Store. The DMG file behaves as a virtual volume.

1. Open Safari and download an installer application in DMG format (for example, VLC).
2. When the download completes, Safari attaches a Quarantine tag indicating the file originated from the internet.
3. In Finder, navigate to the Downloads folder and double-click the DMG file to mount it.
4. In the window that opens, drag the application icon to the Applications folder shortcut to copy it.
5. In the Sidebar under Locations, click the **Eject** icon next to the DMG name to unmount it.
6. In the Applications folder, open the application you copied.
7. **Gatekeeper Protection:** A pop-up warning will appear indicating that the application was downloaded from the internet.
8. Click **Open**.
9. **Tahoe Unique Behavior (Unsigned Application Challenge):** If you attempt to launch an unsigned application, macOS Tahoe will block it completely. Right-clicking and selecting Open will no longer work! You will need to navigate to **System Settings > Privacy & Security**, scroll down, and explicitly click **Open Anyway**.

---

## Exercise 3: Sandboxing and Resetting Application Preferences
Modern applications store their user data inside a Container. Deleting the Container performs a "factory reset" for the app.

1. Open a built-in or installed application (for example, Notes or the app you installed).
2. Access Settings/Preferences and change any setting to cause the application to write data.
3. Completely quit the application (`Command-Q`).
4. Open **Finder**. In the top menu bar, click **Go**.
5. Press and hold the `Option` key (⌥) and click the **Library** folder that appears.
6. Locate and enter the `Containers` folder.
7. Search for the application's container folder (for example, `com.apple.Notes`).
8. Right-click and select **Move to Trash**. Empty the Trash.
9. *Pro Tip (Clearing In-Memory Cache):* Open Terminal and run `killall cfprefsd` to prevent the operating system from restoring cached "zombie plists".
10. Reopen the application. It will launch as if freshly installed, because a new Container is automatically generated.

---

## Exercise 4: Diagnosing and Force-Quitting Unresponsive Processes
When an application hangs (Not Responding), we must force-quit it.

1. Open Safari and Calendar.
2. **Method 1: Quick Force Quit Mechanism**
   * Press `Option-Command-Escape`.
   * In the "Force Quit Applications" window, select Safari and click **Force Quit**.
   * Confirm the warning and observe the application closing immediately.
3. Reopen Safari.
4. **Method 2: Advanced Management via Activity Monitor**
   * Open **Activity Monitor** (located in `Applications > Utilities`).
   * Ensure you are on the CPU or Memory tab.
   * Search for `Safari` in the search bar.
   * Select the process and click the `X` (Stop) button at the top of the window.
   * Select **Force Quit** in the confirmation pop-up.
5. Verify that the process has been completely terminated.

---

## Exercise 5: (Demo & Discussion) Installing Applications in a Managed Enterprise Environment (Self Service & VPP)
In an enterprise environment, IT provides an installation catalog without requiring Admin privileges.

1. The instructor will demonstrate a Self Service application (such as Jamf Self Service) from the demo station.
2. Standard users can browse the catalog of approved software.
3. Upon clicking **Install**, the MDM agent installs the software in the background using System privileges without requesting credentials.
4. Licenses (VPP) are pushed transparently without requiring a personal Apple ID.
5. **Tip:** If an enterprise application prompts for an Apple ID, the MDM VPP license likely failed or expired.

---

## IT Pro Bonus Exercise: Command Line (Terminal)

> [!CAUTION]
> For advanced users who want to see terminal commands. Optional for the main lab.

**Verifying PKG Signature:**
```bash
pkgutil --check-signature /path/to/installer.pkg
```
**Verifying Application Notarization:**
```bash
codesign --test-requirement="=notarized" --verify --verbose /Applications/BBEdit.app
```
**Terminating Process and Clearing Cache (for Sandbox Reset):**
```bash
killall Safari
killall cfprefsd
```

<!-- src_hash: 9481ca676c9d8d3a4606418a5b07f4e4be2e724919b786c67cc01c4421072af7 -->
