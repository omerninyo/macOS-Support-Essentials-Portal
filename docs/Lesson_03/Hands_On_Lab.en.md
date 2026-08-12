# Lesson 03: Security
**Hands-On Lab (Student Exercise)**

---

### Prerequisites

- A Mac running macOS 26 (Tahoe).
- Administrator privileges.
- A third-party application (such as Google Chrome or Zoom) installed on the system.

---

## Exercise 1: Investigating the Gatekeeper Mechanism and Signature Sources via GUI

> **Objective:** Hands-on experience downloading an app from the internet and observing in real-time how the Gatekeeper mechanism blocks or approves it based on the policy configured in System Settings (Graphical User Interface).

Instead of using the command line, we will use built-in system tools to understand where each app came from and whether it's approved by Gatekeeper. We will demonstrate this by downloading the Zoom app.

#### Step 1: Elevating the Security Level (App Store Only)

1. Open **System Settings**.
2. Navigate to **Privacy & Security**.
3. Scroll down to the **Security** section.
4. Change the setting under "Allow applications downloaded from:" to the most restrictive mode: **App Store** (instead of "App Store and known developers"). This action instructs Gatekeeper to block the execution of any app that wasn't downloaded directly from Apple's App Store.

#### Step 2: Downloading and Installing Zoom

1. Open your browser (Safari) and navigate to the official Zoom website.
2. Download the installation package (`.pkg` file) for the Zoom app.
3. Launch the installation package and complete the process.
   > [!NOTE]
   > The installation itself might succeed because it is handled by the system's authorized installer process, but depending on the OS version, you might occasionally see a block even at this stage.

#### Step 3: Execution Blocked by Gatekeeper

1. Go to the **Applications** folder and attempt to launch the **Zoom** app.
2. A Gatekeeper error message will pop up, stating that the app cannot be opened because it was not downloaded from the App Store.
3. Return to **System Settings -> Privacy & Security** and revert the Security setting back to the standard mode: **App Store and known developers**.
4. Try to launch Zoom again - the app will now open successfully because it has been notarized and signed by an Identified Developer.

#### Step 4: Identifying the App's Signature Source (System Information)

1. Hold the `Option` (⌥) key on your keyboard and click the Apple menu () in the top-left corner of the screen.
2. Select **System Information** (the first option).
3. In the sidebar, scroll down to the **Software** category and click on **Applications** (loading may take a few seconds).
4. Find **Zoom** in the list. In the lower section of the window, under "Obtained from", you will see it says `Identified Developer`. This data point proves that the app was notarized and evaluated by Gatekeeper.

---

## Exercise 2: A Peek Behind the Scenes of XProtect

> **Objective:** Visual proof that the Mac indeed has an Anti-Virus, even though it's invisible. We will locate its last update time and trace its files.

The XProtect engine operates transparently to the user. We will use Finder and System Information to view its updates and the files managing it.

#### Step 1: Locating the Current XProtect Version in the System

1. Return to the **System Information** window (or reopen it via Apple menu + `Option`).
2. Under the **Software** category, click on **Installations**.
3. Click on the "Software Name" column header to sort the list alphabetically.
4. Scroll to the bottom of the list and look for the items **XProtectPlistConfigData** or **XProtectPayloads**.
5. Check the **Version** column and the Install Date to see when the system received its last silent security update from Apple.

#### Step 2: Investigating XProtect Files in Finder

1. Open a new **Finder** window.
2. In the top menu bar, click **Go** and then select **Go to Folder...** (or use the shortcut `Cmd+Shift+G`).
3. Type the following path and hit Enter:
   `/var/protected/xprotect/XProtect.bundle` 
   > [!TIP]
   > If the folder is empty after a fresh install, check the legacy path: `/Library/Apple/System/Library/CoreServices/XProtect.bundle/Contents/Resources/`

4. In the folder that opens, look for info files such as `XProtect.meta.plist` or other configuration files (depending on availability in Tahoe).
5. Select an available file and press the Spacebar to launch Quick Look and view the internal content of the security engine.

---

## Exercise 3: Managing and Resetting TCC (Transparency, Consent, and Control) Permissions

> **Objective:** Managing Camera and Microphone access requests, and how to reset TCC permissions when something goes wrong in the system.

We will use the Zoom app (downloaded in Part 1) to demonstrate how permission requests (Camera, Microphone) operate from an end-user perspective, and then learn how to reset them for Troubleshooting purposes.

#### Step 1: Requesting Permissions from an End-User Perspective

1. Open the **Zoom** app.
2. Start a **New Meeting**.
3. Immediately upon starting the meeting, Zoom will attempt to access your camera and microphone. The system (macOS) will pop up special request dialogs to approve access for the Camera and Microphone.
4. Click **Allow** on both requests.
5. Now, attempt to **Share Screen**. The system will pop up an additional request for **Screen Recording**. Follow the instructions to grant the permission (an action requiring administrative password entry and opening the Settings window).

#### Step 2: Viewing Granted Permissions in System Settings

1. Open **System Settings** and navigate to **Privacy & Security**.
2. Go into the **Camera** or **Microphone** category.
3. Here you will see the Zoom app added to the list. A toggled blue switch means access is granted (Consent), while a gray, disabled switch means access is denied.

#### Step 3: Fully Resetting Permissions via Terminal (Troubleshooting)

> [!NOTE]
> **No Need to Memorize!**
> This step uses the Terminal to reset permissions. Copy-paste the command without worrying about its syntax. We will learn how to work in the Terminal in Lesson 08.

Sometimes an app crashes or fails to recognize the permission granted to it (a common occurrence in video conferencing software). In such cases, we want to fully reset the permission from the TCC database to force the system to prompt the user again from scratch:

1. Fully close the Zoom app (**Quit**).
2. Open the **Terminal** (can be found in Applications/Utilities).
3. To reset all TCC permissions for the Zoom app in one fell swoop, type the following command and hit Enter:
   ```bash
   tccutil reset All us.zoom.xos
   ```
   *(For advanced users: You can also reset a specific permission, for example: `tccutil reset Microphone us.zoom.xos`)*
4. Now, reopen **Zoom** and start a meeting. Notice that the request dialogs for camera and microphone access reappear, exactly as if it's the first time the app is launched!

---

## Exercise 4: Enterprise Spice - Identifying PPPC Profiles

> **Objective:** How to solve issues in organizations where users accidentally deny TCC requests. Identifying the profiles that satisfy TCC on behalf of IT.

In a managed enterprise environment, IT deploys profiles that automatically grant TCC permissions (PPPC).

1. In **System Settings**, go back and then scroll down to select **Profiles** or **Device Management** (if available - if the Mac is unmanaged, this menu might be missing).
2. If profiles are installed, look for a profile containing the name **Privacy Preferences Policy Control** or **System Policy All Files**.
3. Going into the profile details will reveal which apps have been granted automatic approval.
4. If you return to Privacy & Security -> Full Disk Access, you will see that apps managed by the profile display a gray toggle switch that cannot be changed, sometimes accompanied by the text "Managed by your organization".

---

### Summary
In this lab, we practiced the fundamentals of macOS protection mechanisms through the graphical interface. We reviewed Gatekeeper settings, verified signature sources using System Information, tracked silent XProtect updates, and learned how to manage and reset TCC privacy permissions using the add and remove controls.

---

## Bonus Exercise for IT Pros: The Command Line (Terminal)

> [!NOTE]
> **"Copy-Paste" Instruction Only!**
> For advanced support professionals, here are several Terminal commands that execute the actions we saw in the GUI faster and more deeply. Again, there is no obligation to memorize them!

1. **Managing the Latest XProtect Engine:**
   Instead of searching in System Information, you can use the built-in tool to manage XProtect updates:
   ```bash
   xprotect version
   sudo xprotect update
   ```

2. **Checking Gatekeeper Status and App Assessment:**
   Instead of opening System Information, you can run a full Gatekeeper assessment on an app:
   ```bash
   spctl -a -vv /Applications/Safari.app
   ```

3. **Resetting the TCC Database:**
   Instead of clicking the minus (-) sign in settings, you can completely reset the Microphone permission system-wide in one command line:
   ```bash
   tccutil reset Microphone
   ```

4. **Investigating XProtect Remediator:**
   Instead of looking at plist files in Finder, this is how you pull the silent scan reports of XProtect from the system log of the last 24 hours (for advanced users):
   ```bash
   log show --predicate 'subsystem == "com.apple.XProtectFramework.PluginAPI"' --info --last 24h
   ```
