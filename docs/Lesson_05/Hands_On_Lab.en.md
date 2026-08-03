# Lesson 05: Applications and Processes
**Hands-On Lab (Student Exercise) (vEXP)**

> [!NOTE]
> **Lab Objective:**
> Practical exercise in deploying, installing, and diagnosing applications on macOS using the Graphical User Interface (GUI). During this lab, you will experience various installation methods (App Store, PKG packages, and dragging DMG files), examine how the Gatekeeper mechanism protects the Mac (especially in macOS Tahoe), and learn how to reset Sandboxed applications and manage hung processes via Activity Monitor.

## Prerequisites
* A Mac running macOS 26 (Tahoe).
* A user account with Administrative privileges (Local Admin).
* A Standard User account for testing purposes – e.g., `John Appleseed`.
* Active Internet connection and access to an Apple ID.
* Access to the `Course_Assets_and_Demos` folder (or downloading demo applications from the Internet).

---

## Exercise 5.1: Installing an Application from the App Store
Installing from the official store is the safest method on Mac, as all applications run within a Sandbox and have undergone review (Notarization).

**Execution Steps:**

1. Log in to your Standard User account (e.g., `John Appleseed`).
2. Open the **App Store** app via Launchpad or the Applications folder.
3. If this is your first sign-in, confirm the Welcome screen.
4. At the bottom of the sidebar, click **Sign In** and enter your Apple ID and password. Complete two-factor authentication (2FA) if prompted.
5. In the top search bar, type `Apple Configurator` and press Return.
6. Locate the free app and click the **Get** button (or the cloud icon).
7. Click **Install**.
8. Wait for the download to complete, then click **Open** to verify the app opens and functions properly. Accept terms of service if displayed.
9. Gracefully close the app using the keyboard shortcut **Command-Q**.

---

## Exercise 5.2: Installing via Installer Package (PKG) and Examining Graphical Signatures
Enterprise software is distributed as installer packages (Packages), which require Admin privileges to deploy system files.

**Execution Steps:**

1. Open an installer package file (`.pkg` extension) provided by your instructor (e.g., `Zoom.pkg` or `Trust Me.pkg` from the demo folder).
2. The system Installer application will open automatically.
3. **Checking Security Signatures:** Look at the top right corner of the installer window. You should see a Lock icon.
4. Click the lock icon to open the certificate inspector window.
5. Verify that it states the package is signed by an approved developer (Developer ID Installer).
6. **Inspecting Package Content:** Before clicking Continue, navigate to the Menu Bar, click **File**, and then **Show Files**.
7. Review the file list to see the target installation paths (e.g., `/Library/Application Support`). Close the window.
8. Click **Continue** and complete the installation. Enter Administrator credentials when prompted.
9. Navigate to the Applications folder and open the newly installed application to verify installation.

---

## Exercise 5.3: Drag-and-Drop Installation (DMG) and Challenging Gatekeeper in Tahoe
The most common installation method outside the App Store. The DMG file acts as a virtual volume.

**Execution Steps:**

1. Open Safari and download an installer in DMG format (e.g., VLC).
2. Upon download completion, Safari attaches a Quarantine attribute indicating the file originated from the Internet.
3. In Finder, navigate to the Downloads folder and double-click the DMG file to mount it.
4. In the window that opens, drag the application icon to the Applications folder shortcut to copy it.
5. In the Sidebar under Locations, click the **Eject** icon next to the DMG name to unmount it.
6. In the Applications folder, open the copied application.
7. **Gatekeeper Protection:** A pop-up warning will appear stating that the app was downloaded from the Internet.
8. Click **Open**.
9. **The Tahoe Twist (Challenging an Unsigned App):** If you attempt to launch an unsigned app, macOS Tahoe will block it completely. Right-clicking and selecting Open will no longer work! You will need to go to **System Settings > Privacy & Security**, scroll down, and explicitly click **Open Anyway**.

---

## Exercise 5.4: Sandboxing and Resetting Application Preferences
Modern applications store their data inside a Container. Deleting the Container constitutes a "Factory Reset".

**Execution Steps:**

1. Open **Apple Configurator** (or a simple app like Notes).
2. Go to settings and change any setting to force the application to save data.
3. Completely quit the application (Command-Q).
4. Open **Finder**. In the top Menu Bar, click **Go**.
5. Hold down the `Option` (⌥) key and click the **Library** folder that appears.
6. Locate and enter the `Containers` folder.
7. Search for the application's folder (e.g., `Apple Configurator` or `com.apple.configurator`).
8. Right-click and select **Move to Trash**. Empty the Trash.
9. *Pro Tip (Flushing Memory Cache):* Open Terminal and run `killall cfprefsd` to prevent the OS from restoring "zombie plists".
10. Relaunch the application. It will launch as if newly installed, as a new Container is automatically generated.

---

## Exercise 5.5: Diagnosing and Force Quitting Unresponsive Processes
When an application hangs (Not Responding), we must terminate it forcibly.

**Execution Steps:**

1. Open Safari and Calendar.
2. **Method 1: Quick Force Quit Mechanism**
   * Press `Option-Command-Escape`.
   * In the "Force Quit Applications" window, select Safari and click **Force Quit**.
   * Confirm the warning and observe the app closing immediately.
3. Relaunch Safari.
4. **Method 2: Advanced Management via Activity Monitor**
   * Open **Activity Monitor** (located in `Applications > Utilities`).
   * Ensure you are on the CPU or Memory tab.
   * Search for `Safari` in the search bar.
   * Select the process and click the `X` (Stop) button at the top of the window.
   * Select **Force Quit** in the pop-up dialog.
5. Verify the process is completely removed.

---

## Exercise 5.6: (Demonstration & Discussion) Installing Apps in a Managed Enterprise Environment (Self Service & VPP)
In an enterprise environment, IT provides a catalog for installations without requiring Admin privileges.

**Scenario Steps:**

1. The instructor will display a Self Service application (e.g., Jamf Self Service) on the demonstration station.
2. The standard user can browse the approved software catalog.
3. Upon clicking **Install**, the MDM agent installs the software in the background using System privileges without prompting for credentials.
4. Licenses (VPP) are pushed transparently without requiring a personal Apple ID.
5. **Tip:** If an app prompts for an Apple ID in an enterprise environment, the VPP license from MDM likely failed or expired.

---

## IT Pro Bonus Exercise: Command Line (Terminal)

> [!CAUTION]
> For advanced users wanting to explore command-line utilities. Optional for the main lab.

**Checking PKG Signature:**
```bash
pkgutil --check-signature /path/to/installer.pkg
```
**Verifying Application Notarization:**
```bash
codesign --test-requirement="=notarized" --verify --verbose /Applications/BBEdit.app
```
**Process Termination & Cache Flush (for Sandbox Reset):**
```bash
killall Safari
killall cfprefsd
```

<!-- src_hash: 871e9419ea2fa0470c8efd25fcc538132f2d0affac4b8fac523e89b753f56d1e -->
