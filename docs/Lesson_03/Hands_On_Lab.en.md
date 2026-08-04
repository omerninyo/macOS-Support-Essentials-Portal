# Lesson 03: Security
**Hands-On Lab (Student Exercise)**

---

### Prerequisites

- A Mac computer running macOS 26 (Tahoe).
- Administrator privileges.
- Any third-party app (like Google Chrome or Zoom) installed on the system.

---

### Part 1: Investigating Gatekeeper and Signature Sources via the GUI

Instead of using the command line, we'll use built-in system tools to understand where each app came from and if it's approved by Gatekeeper.

#### Step 1: Gatekeeper Settings in System Settings

1. Open **System Settings**.
2. Navigate to **Privacy & Security** (you may need to expand to **Advanced** in some cases).
3. Scroll down to the **Security** area.
4. Ensure that under "Allow applications downloaded from:" the option "App Store and known developers" is checked. This is the recommended state indicating Gatekeeper is active.

#### Step 2: Identifying the App Signature Source (System Information)

1. Hold the `Option` (⌥) key on your keyboard, and click the Apple menu () in the top-left corner.
2. Select **System Information** (the first option).
3. In the sidebar, scroll down to the **Software** category and click on **Applications** (loading may take a few seconds).
4. Find **Safari** in the list. In the lower part of the window, under "Obtained from", you will see it says `Apple` – this is a system-signed app.
5. Now, look for an app you downloaded from the internet (e.g., Google Chrome). Look at "Obtained from" and note that it says `Identified Developer`. This proves the app was notarized and verified by Gatekeeper.

---

### Part 2: Behind the Scenes of XProtect

The XProtect engine works transparently to the user. We will use Finder and System Information to see its updates and the files that manage it.

#### Step 1: Locating the Current XProtect Version

1. Return to the **System Information** window (or reopen it via Apple menu + `Option`).
2. Under the **Software** category, click on **Installations**.
3. Click the "Software Name" column header to sort alphabetically.
4. Scroll to the bottom and look for **XProtectPlistConfigData** or **XProtectPayloads**.
5. Look at the **Version** column and the Install Date to see when the system received the last silent security update from Apple.

#### Step 2: Investigating XProtect Files in Finder

1. Open a new **Finder** window.
2. In the top menu, click **Go** and then select **Go to Folder...** (or use `Cmd+Shift+G`).
3. Type the following path and press Enter:
   `/var/protected/xprotect/XProtect.bundle`
   *(Note: If the folder is empty after a fresh install, check the fallback path: `/Library/Apple/System/Library/CoreServices/XProtect.bundle/Contents/Resources/`)*
4. In the opened folder, look for info files like `XProtect.meta.plist` or other configuration files (depending on availability in Tahoe).
5. Select an available file and press the Spacebar to activate Quick Look and view the internal content of the security engine.

---

### Part 3: Managing and Resetting TCC Permissions (Transparency, Consent, and Control)

We'll learn how to see who has access to sensitive data and how to reset a permission to force the app to ask for it again – all from the graphical interface.

#### Step 1: Viewing TCC Permissions

1. Open **System Settings** and navigate to **Privacy & Security**.
2. Enter the **Camera** or **Microphone** category.
3. Here you will see all the apps that requested access in the past. A blue toggle means access is granted (Consent), a gray toggle means access is denied.

#### Step 2: Resetting a TCC Permission for an App (Full Removal)
Sometimes an app crashes or doesn't recognize the granted permission. In this case, we want to completely remove it from the TCC database.

1. Enter the **Full Disk Access** category under Privacy & Security.
2. Select an app from the list (e.g., an IT tool or a known app).
3. Click the minus button (**-**) at the bottom of the list.
4. This completely removes the app from the TCC database for this permission. The next time the app launches and needs access, it will prompt you with a new pop-up asking for approval.
5. Now click the plus button (**+**), enter your admin password, and select the app from the Applications folder to manually add it in advance.

---

### Part 4: Enterprise Seasoning - Identifying a PPPC Profile
In a managed enterprise environment, IT installs profiles that grant TCC permissions automatically (PPPC).

1. In **System Settings**, go back and scroll down to select **Profiles** or **Device Management** (if available - if the Mac isn't managed, this menu may be missing).
2. If profiles are installed, look for one containing the name **Privacy Preferences Policy Control** or **System Policy All Files**.
3. Entering the profile details will show which apps received automatic approval.
4. If you return to Privacy & Security -> Full Disk Access, you can see that apps managed by the profile display a gray toggle that cannot be changed, often with the text "Managed by your organization".

---

### Summary
In this lab, we practiced the basics of macOS protection mechanisms via the graphical interface. We checked Gatekeeper settings, verified signature sources using System Information, tracked silent XProtect updates, and learned how to manage and reset privacy permissions in the TCC system using the add and remove buttons.

---

## Extra Exercise / Technical Tip of the Iceberg

For advanced support personnel, here are a few Terminal commands that perform the actions we saw in the GUI faster and more deeply:

1. **Managing the Modern XProtect Engine:**
   
   Instead of searching in System Information, you can use the built-in tool for managing XProtect updates:
   ```bash
   xprotect version
   sudo xprotect update
   ```

2. **Checking Gatekeeper Status and Verifying an App:**

   Instead of opening System Information, you can run a full Gatekeeper assessment on an app:
   ```bash
   spctl -a -vv /Applications/Safari.app
   ```

3. **Resetting TCC Database:**

   Instead of clicking the minus (-) sign in settings, you can completely reset the microphone permission for the entire system in one command:
   ```bash
   tccutil reset Microphone
   ```

4. **Investigating XProtect Remediator:**

   Instead of looking at plist files in Finder, this is how you extract the silent scan reports of XProtect from the system log for the last 24 hours:
   ```bash
   log show --predicate 'subsystem == "com.apple.XProtectFramework.PluginAPI"' --info --last 24h
   ```
