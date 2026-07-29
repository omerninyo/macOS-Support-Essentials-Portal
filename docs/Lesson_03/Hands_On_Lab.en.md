# Lesson 03: Information Security
**Hands-On Lab (Student Exercise)**

---

### Prerequisites

- A Mac computer running macOS 26 (Tahoe).
- Administrator privileges.
- Any third-party application (like Google Chrome or Zoom) installed on the system.

---

### Part 1: Investigating the Gatekeeper Mechanism and Signature Sources via GUI

Instead of using the command line, we will use the system's built-in tools to understand where each application came from and if it is approved by Gatekeeper.

#### Step 1: Gatekeeper Settings in System Settings

1. Open **System Settings**.
2. Navigate to **Privacy & Security**.
3. Scroll down to the **Security** area.
4. Verify that under "Allow applications downloaded from:", the option "App Store and known developers" is checked. This is the normal and recommended status indicating that Gatekeeper is active.

#### Step 2: Identifying Application Signature Source (System Information)

1. Hold down the `Option` (⌥) key on the keyboard, and click the Apple menu () in the top-left corner of the screen.
2. Select **System Information** (the first option).
3. In the sidebar, scroll down to the **Software** category and click on **Applications** (loading may take a few seconds).
4. Find **Safari** in the list. At the bottom of the window, under "Obtained from", you will see it says `Apple` – this is an application signed by the system.
5. Now, search the list for an application you downloaded from the internet (e.g., Google Chrome). Look at "Obtained from" and note that it says `Identified Developer`. This datum proves that the application underwent Notarization and was checked by Gatekeeper.

---

### Part 2: A Peek Behind the Scenes of XProtect

The XProtect engine operates transparently to the user. We will use Finder and System Information to see its updates and the files that manage it.

#### Step 1: Locating the Current XProtect Version in the System

1. Return to the **System Information** window (or reopen it via the Apple menu + `Option`).
2. Under the **Software** category, click on **Installations**.
3. Click the "Software Name" column header to sort the list alphabetically.
4. Scroll to the end of the list and look for the items **XProtectPayloads** or **XProtectPlistConfigData**.
5. Look at the **Version** column and the Install Date to see when the system received the latest silent security update from Apple.

#### Step 2: Investigating XProtect Files in Finder

1. Open a new **Finder** window.
2. In the top menu, click on **Go** and then select **Go to Folder...** (or use the shortcut `Cmd+Shift+G`).
3. Type the following path and press Enter:
   `/Library/Apple/System/Library/CoreServices/XProtect.bundle/Contents/Resources/`

4. In the folder that opens, locate the `XProtect.meta.plist` file.
5. Select it and press the Spacebar to launch Quick Look. Here you can see the internal version number of the security engine in XML format.

---

### Part 3: Managing and Resetting TCC Permissions (Transparency, Consent, and Control)

We will learn how to see who has access to sensitive data, and how to reset a permission to force the application to request it again – all from the GUI.

#### Step 1: Viewing TCC Permissions

1. Open **System Settings** and navigate to **Privacy & Security**.
2. Enter the **Camera** or **Microphone** category.
3. Here you will see all the applications that have previously requested access. A toggled blue switch means access was granted (Consent), a toggled grey switch means access was denied.

#### Step 2: Resetting a TCC Permission for an App (Full Removal)
Sometimes an app crashes or doesn't recognize the permission granted to it. In such cases, we want to completely remove it from the TCC database.

1. Enter the **Full Disk Access** category under Privacy & Security.
2. Select one of the apps in the list (e.g., an IT tool or known app).
3. Click the minus button (**-**) at the bottom of the list.
4. This action completely removes the app from the TCC database for this permission. The next time the app is launched and needs access, it will show a new pop-up prompt asking for your approval.
5. Now click the plus button (**+**), enter an admin password, and select the app from the Applications folder to add it manually in advance.

---

### Part 4: Enterprise Seasoning - Identifying a PPPC Profile
In a managed enterprise environment, IT installs profiles that automatically grant TCC permissions (PPPC).

1. In **System Settings**, go back and then scroll down and select **Profiles** or **Device Management** (if it appears - if the computer is unmanaged, this menu may be absent).
2. If profiles are installed, look for a profile containing the name **Privacy Preferences Policy Control** or **System Policy All Files**.
3. Going into the profile details will show which apps received automatic approval.
4. If you return to Privacy & Security -> Full Disk Access, you can see that apps managed by the profile show a greyed-out switch that cannot be changed, sometimes with the text "Managed by your organization".

---

### Summary
In this lab, we practiced the basics of macOS protection mechanisms through the graphical interface. We checked Gatekeeper settings, verified signature sources using System Information, tracked silent XProtect updates, and learned how to manage and reset system privacy (TCC) permissions using the add and remove buttons.

---

## Extra Exercise / Technical Tip of the Iceberg

For advanced support staff, here are a few Terminal commands that perform the actions we saw in the GUI in a faster and more in-depth manner:


1. **Checking Gatekeeper status and verifying an app:**

   Instead of opening System Information, you can perform a full Gatekeeper assessment on an app:
   ```bash
   spctl --assess --verbose /Applications/Safari.app
   ```

2. **Resetting the TCC database:**

   Instead of clicking the minus sign (-) in Settings, you can completely reset the Microphone permission system-wide in one command line:
   ```bash
   tccutil reset Microphone
   ```

3. **Investigating XProtect Remediator:**

   Instead of looking at plist files in Finder, this is how you extract the silent scanning reports of XProtect from the system log over the last 24 hours:
   ```bash
   log show --predicate 'subsystem == "com.apple.XProtectFramework.PluginAPI"' --info --last 24h
   ```

<!-- src_hash: d219a474bedcf096eedd121a14f4b8c840dc3f9ed5ea32e9f010d140836a2fa1 -->

