# Lesson 05: Apps and Processes
**Hands-On Lab (Student Exercise)**

> [!NOTE]
> **Lab Objective:**

> Practical exercise on deploying, installing, and diagnosing applications in macOS using the graphical user interface. During the exercise, you will experience a variety of installation methods (App Store, PKG packages, and dragging DMG files), examine how the Gatekeeper system protects the computer, and learn how to reset Sandboxed apps and manage frozen processes via Activity Monitor.

## Prerequisites

* A Mac computer installed with macOS 26 (Tahoe).
* A user with administrator privileges (Local Admin).
* A standard user for testing purposes (Standard User) – for example: `John Appleseed`.
* An active internet connection and access to an Apple ID.
* Access to the `Course_Assets_and_Demos` folder (or downloading demo apps from the internet).

---

## Exercise 5.1: Installing an App from the App Store

In this exercise, you will install an app from the official store (App Store). This is the safest and simplest way to install apps on a Mac, as all apps there have passed review and Notarization by Apple, and they operate inside a Sandbox.

**Execution Steps:**

1. Log into your standard user (e.g., `John Appleseed`).
2. Open the **App Store** app via Launchpad or the Applications folder.
3. If this is the first login, approve the Welcome screen.
4. At the bottom of the sidebar, click on **Sign In** and enter your Apple ID and password. Complete the two-factor authentication (2FA) if necessary.
5. In the top search bar, type `Apple Configurator` and press Return.
6. Locate Apple's free app and click the **Get** button (or the cloud icon if you have downloaded it before).
7. Click **Install**.
8. Wait for the download to finish, then click **Open** to verify the app opens and is functional. Accept the terms of use if a prompt appears.
9. Close the app properly using the keyboard shortcut **Command-Q**.

---

## Exercise 5.2: Installation using an Installation Package (PKG) and Examining the Graphical Signature

Enterprise software and complex tools are distributed as installation packages (Packages). These are files that require Admin privileges to place files in central system folders or install background services.

**Execution Steps:**

1. Open the installation package file (`.pkg` extension) you received from the course instructor (for example, `Zoom.pkg` or `Trust Me.pkg` from the demos folder).
2. The system's built-in Installer will open automatically and display the introduction window.
3. **Checking the security signature:** Look at the top right corner of the installation window. You should see a Lock icon.
4. Click the lock icon to open the security certificate window.
5. In the certificate window, ensure it states that the package is signed by an approved developer (Developer ID Installer) recognized by Apple.
6. **Exploring package contents:** Before you continue, click on **File** in the top Menu Bar and then on **Show Files**.
7. Review the pop-up list. Here you can see in advance which files are about to be installed and in what paths (for example, whether the software places files in `/Library/Application Support`). Close the window.
8. Click **Continue** and complete the installation. Because installing a package modifies system files, you will be required to enter an Administrator password. Enter it.
9. Navigate to the Applications folder and open the new software to verify a successful installation.

---

## Exercise 5.3: Drag-and-Drop Installation (DMG) and Challenging Gatekeeper

This is the most common installation mechanism outside the store in macOS. The DMG file (disk image) behaves like a removable virtual volume.

**Execution Steps:**

1. Open the browser (Safari) and download an installation software in DMG format (for example, the free software VLC).
2. Upon download completion, the Safari browser transparently adds a security tag named Quarantine to the file, indicating it was downloaded from the internet.
3. Open the Finder, navigate to the Downloads folder, and double-click the DMG file to mount it to the system.
4. In the window that opens, you will see the software icon next to a shortcut to the Applications folder.
5. Drag the app icon to the Applications folder shortcut to copy it to the local drive.
6. In the Finder Sidebar, under the Locations category, click the Eject icon next to the DMG name to safely unmount it.
7. Navigate to the Applications folder, locate the software you dragged, and open it.
8. **Gatekeeper protection will trigger:** A pop-up warning will appear indicating the app was downloaded from the internet and asking if you are sure you want to open it.
9. Click **Open**. This confirmation indicates you have reviewed the software and it will be removed from quarantine, so on subsequent opens, the message will not appear.

---

## Exercise 5.4: Sandboxing and Resetting App Preferences

Most modern apps in macOS run in Sandboxing mode. They cannot access every file on the computer; instead, they save their data inside a dedicated "Container" in the local user's library. Deleting the Container via Finder is the correct way to "reset" an app that is behaving abnormally.

**Execution Steps:**

1. Open the **Apple Configurator** app you installed earlier (or another simple app like Notes or Calendar).
2. Go to the software's settings (via the menu bar `App Name > Settings`) and change some setting to save information.
3. Completely close the software (Command-Q).
4. Open **Finder**. In the top menu bar, click the **Go** menu.
5. While the menu is open, press and hold the `Option` (⌥) key on the keyboard. You will notice a new folder named **Library** appears in the menu. Click on it.
6. Inside your Library folder, locate and enter the folder named `Containers`.
7. In the internal search bar (or by visual scanning), look for the folder belonging to the app (for example, `Apple Configurator` or `com.apple.configurator`).
8. Right-click on this folder and select **Move to Trash** (delete its Container). Empty the trash.
9. Relaunch the app (Apple Configurator) from the Applications folder.
10. Notice that the app now starts completely anew (reset settings or a 'Welcome' screen), because the system automatically created a new, clean Container for it.

---

## Exercise 5.5: Diagnosing and Force Quitting Frozen Processes

When an app gets stuck and doesn't respond, it receives a *(Not Responding)* status. Problematic processes can be terminated directly through system interfaces.

**Execution Steps (two main methods):**

1. Open the Safari browser and another app like Calendar for the purpose of the exercise.
2. **Method 1: The fast Force Quit mechanism**
   * Press the keyboard shortcut `Option-Command-Escape`.
   * In the "Force Quit Applications" window that pops up, select Safari and click the **Force Quit** button.
   * Confirm the warning and watch the app close immediately.
3. Relaunch Safari.
4. **Method 2: Advanced management via Activity Monitor**
   * Open the **Activity Monitor** app (located in `Applications > Utilities`).
   * Ensure you are on the CPU or Memory tab.
   * In the search bar on the top right, type `Safari`.
   * Select the Safari process in the results list, and click the `X` (Stop) button at the top of the window.
   * In the pop-up window, a choice will appear between 'Quit' (soft close) and 'Force Quit' (hard force quit without saving). Click **Force Quit**.
5. Ensure the process has completely disappeared from the Activity Monitor list.

---

## Exercise 5.6: (Demonstration and Discussion) Installing Apps in a Managed Enterprise Environment (Self Service & VPP)

In a managed organization, standard users are usually not allowed to enter an Admin password to install software or make system changes. For this, IT provides a self-service software catalog.

**Scenario Steps:**

1. The instructor will display an enterprise store app (Self Service of some MDM tool) through the demonstration station.
2. Observe how the catalog provides access only to approved software.
3. When the standard user clicks **Install**, the MDM performs the installation behind the scenes using System privileges (without bothering the user with a password prompt).
4. Apps originating from the App Store are pre-purchased silently through the VPP system and pushed to the computer, without the employee being asked to log in with a personal Apple ID.
5. **Tip:** If an enterprise app suddenly asks for an Apple ID upon launch, this may indicate a failure in assigning the managed license from the MDM.

---

## Extra Exercise / Technical Tip of the Iceberg

> [!CAUTION]
> This section is intended for advanced users who wish to see how the operations from the exercise are performed directly from the command line (Terminal). There is no need to execute them to complete the main exercise.

**Checking a PKG file signature in Terminal:**

Instead of clicking the graphical lock in the installer, you can check the PKG package's authenticity through the Terminal using the `pkgutil` command:
```bash
pkgutil --check-signature /path/to/installer.pkg
```
*(This command returns the signature status and the chain of trust certificates that approved it).*

**Checking Notarization for a .app software:**

To verify that an app successfully passed Apple's security scan (Notarization), use the `codesign` tool:
```bash
codesign --test-requirement="=notarized" --verify --verbose /Applications/BBEdit.app
```
*(If the app is approved, the output will state 'explicit requirement satisfied').*

**Fast process termination using killall:**

Instead of opening Activity Monitor, the Terminal allows quickly terminating crashing or stuck processes by their name:
```bash
killall Safari
```
*(This command performs an immediate process termination for all Safari processes running under the user).*

<!-- src_hash: 7580ecfd9bbeff886a06f6b4833547fb1f8e6b9c6e4fed2d9501d9009d2240d5 -->
