# Lesson 01: Installation, Orientation, and Baseline Alignment
**Hands-On Lab (Student Exercise)**

---

## Overview
This lab serves as an "Equalizer" for technicians and users transitioning to macOS. The goal is to experience basic navigation, understand how the system reflects Apple Silicon hardware, and explore the OOBE (Out of Box Experience) from the user's perspective.

---

## Exercise 1: Configuration and Architecture Identification (Apple Silicon Diagnostics)

> **Objective:** Verify the computer's hardware (which processor is installed), explore the new Liquid Glass interface, and differentiate between native Apple core processes and legacy Intel processes that are translated in real-time by Rosetta 2.

1. Click the Apple menu (``) in the top-left corner of the screen and select **About This Mac**.
2. Notice the new "Liquid Glass" design language, and ensure an Apple chip is listed (e.g., Apple M3) along with the available Unified Memory.
3. Open the **Terminal** application (you can use the keyboard shortcut `Cmd + Space` and search using Spotlight).
4. Type the following command to quickly retrieve the processor's marketing name on the machine:
   ```bash
   sysctl -n machdep.cpu.brand_string
   ```

5. Open the **Activity Monitor** application.
6. In the top toolbar of Activity Monitor, ensure you are on the **CPU** tab.
7. Look at the **Kind** column.
   
> [!TIP]
> If the column is not visible, right-click on the column headers and check the box next to "Kind".

8. Sort the list by clicking on the column header. Identify processes running under "Apple" (these are natively compiled for ARM architecture) versus "Intel" processes (which are currently being translated in real-time by Rosetta 2).

---

## Exercise 2: Navigation, Gestures, and Workspaces (Navigation & Spaces)

> **Objective:** Practice seamlessly switching between multiple windows using the Trackpad and Multi-Touch gestures, enabling efficient workflows aligned with Apple's design philosophy.

1. Open **System Settings** and navigate to the **Trackpad** menu.
2. Review the Point & Click, Scroll & Zoom, and More Gestures tabs. Ensure the **Swipe between full-screen applications** setting is enabled (with three or four fingers).
3. Open 3 different applications (e.g., Safari, Notes, Calendar).
4. Click the green button in the top-left corner of Safari to switch it to Full Screen mode. This creates a new Space.
5. Swipe left and right with 3 or 4 fingers to quickly switch between the Safari window and the regular Desktop containing the other applications.
6. Swipe up with 3 or 4 fingers to invoke **Mission Control** and see a bird's-eye view of all open applications.

---

## Exercise 3: Verifying MDM Enrollment Status in Terminal

> **Objective:** An initial use of Terminal to check whether our computer was "managed" (became an enterprise device) during the Setup Assistant phase via the Automated Device Enrollment mechanism.

> [!NOTE]
> **Copy-Paste Only!**
> In this exercise, we are using the Terminal strictly to verify an organizational setting. There is no need to memorize the command or understand its entire syntax right now. Structured learning of the Terminal will begin in Lesson 08. Simply copy the command, paste it, and review the output.

1. Open **Terminal** (via Spotlight or at the path `/Applications/Utilities/Terminal.app`).
2. Type (or paste) the following command and press Enter:
   ```bash
   sudo profiles show -type enrollment
   ```

3. The system will prompt you for your Local Account password (administrator password). Enter it (note that the text does not appear on screen for privacy protection) and press Enter.
4. Analyze the output:
   * If the text `Error fetching Device Enrollment configuration: (34000) Client is not DEP enabled.` appears, the computer is not enrolled in Apple Business Manager and is not subject to remote organizational management.
   * If the output displays server details (such as an enterprise MDM server URL), the computer was successfully enrolled during its initial setup and will receive organizational profiles.
