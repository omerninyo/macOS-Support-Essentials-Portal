# Lesson 01: Installation, Familiarization, and Alignment
**Hands-on Lab (Student Exercise)**

## Overview
This lab serves as an "Equalizer" for technicians and users transitioning to macOS. The objective is to gain experience with basic navigation, understand how the system reflects Apple Silicon hardware, and become familiar with the Out-of-Box Experience (OOBE) from a user's perspective.

---

## Exercise 1: Configuration and Architecture Identification (Apple Silicon Diagnostics)
**Objective:** To verify the computer's hardware and differentiate between Apple processes and Intel processes (Rosetta 2).

1. Access the Apple menu (``) in the top-left corner of the screen and click **About This Mac**.
2. Verify that an Apple chip designation (e.g., Apple M3) and the amount of available Unified Memory are displayed.
3. Open the **Activity Monitor** application (you can use the keyboard shortcut `Cmd + Space` and search with Spotlight).
4. In the top bar of Activity Monitor, ensure you are on the **CPU** tab.
5. Observe the **Kind** column.
   - *Note: If the column is not visible, right-click on the column header row and check "Kind".*
6. Sort the list by clicking on the column. Identify processes running under "Apple" (these are processes architecturally written for ARM) versus "Intel" processes (which are currently being translated in real-time by Rosetta 2).

---

## Exercise 2: Navigation, Gestures, and Workspaces (Navigation & Spaces)
**Objective:** Practice seamless switching between multiple windows using the Trackpad and Multi-Touch gestures, similar to Apple's Starter Guide document.

1. Open **System Settings** and navigate to the **Trackpad** menu.
2. Review the Point & Click, Scroll & Zoom, and More Gestures tabs. Ensure the **Swipe between full-screen applications** setting is enabled (with three or four fingers).
3. Open 3 different applications (e.g., Safari, Notes, Calendar).
4. Click the green button in the top-left corner of Safari to make it full screen. This creates a new Space (workspace).
5. Swipe left and right with 3/4 fingers to quickly switch between the Safari window and the regular Desktop containing the other applications.
6. Swipe up with 3/4 fingers to activate **Mission Control** to view all open applications at a glance.

---

## Exercise 3: Verifying MDM Enrollment Status in Terminal
**Objective:** Initial use of Terminal to check if the computer was managed during the Setup Assistant phase via Automated Device Enrollment.

1. Open **Terminal** (via Spotlight or at the path `/Applications/Utilities/Terminal.app`).
2. Type the following command and press Enter:
   ```bash
   sudo profiles show -type enrollment
   ```
3. The system will prompt you to enter your Local Account password (administrator password). Enter it (the text will not be visible on the screen) and press Enter.
4. Analyze the output:

   - If the text `Error fetching Device Enrollment configuration: (34000) Client is not DEP enabled.` appears, the computer is not registered in Apple Business Manager and is not subject to Remote Management.
   - If the output displays server details (such as an organizational MDM server URL), the computer was properly enrolled during its initial setup.

<!-- src_hash: f636e65b224b5496e9857e5ac1f96036158176ef7decfa4f70c42ef8600b18c6 -->


!!! tip "Visual Aids (Student Guide)"
    These images illustrate the relevant interface or mechanism for this lesson.

![Explainer_Memory_AboutThisMac](../assets/images/Lesson_01/L01_DeepDive_Explainer_Memory_AboutThisMac.jpg)
![macOS_Versions](../assets/images/Lesson_01/L01_DeepDive_macOS_Versions.jpg)
![Slide48_image8](../assets/images/Lesson_01/L02_LegacySlide_Slide48_image8.jpg)
