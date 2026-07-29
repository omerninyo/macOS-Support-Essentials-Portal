# Lesson 01: Installation, Familiarization, and Baseline
**Hands-On Lab (vEXP)**

## Overview
This lab serves as an "equalizer" for technicians and users transitioning to macOS. The goal is to practice basic navigation, understand how the system reflects Apple Silicon hardware, and familiarize yourself with the OOBE (Out of Box Experience) from the user's perspective.

---

## Exercise 1: Configuration and Architecture Diagnostics
**Objective:** Verify computer hardware, explore the Liquid Glass UI, and differentiate between Apple and Intel (Rosetta 2) processes.

1. Go to the Apple menu (``) in the top left corner of the screen and click on **About This Mac**.
2. Notice the new "Liquid Glass" design language and verify that an Apple chip is listed (e.g., Apple M3) along with the available Unified Memory.
3. Open the **Terminal** app (use `Cmd + Space` to search with Spotlight).
4. Type the following command to quickly fetch the CPU marketing name:
   ```bash
   sysctl -n machdep.cpu.brand_string
   ```
5. Open the **Activity Monitor** app.
6. In the top bar of Activity Monitor, ensure you are on the **CPU** tab.
7. Look at the **Kind** column.
   - *Note: If the column is not visible, right-click on the column headers and check "Kind".*
8. Sort the list by clicking on the column. Identify processes running under "Apple" (architecturally written for ARM) versus "Intel" processes (currently translated in real-time by Rosetta 2).

---

## Exercise 2: Navigation, Gestures, and Workspaces (Spaces)
**Objective:** Practice seamless transition between multiple windows using the Trackpad and Multi-Touch gestures, similar to Apple's Starter Guide.

1. Open **System Settings** and navigate to the **Trackpad** menu.
2. Go through the Point & Click, Scroll & Zoom, and More Gestures tabs. Ensure the **Swipe between full-screen applications** setting is enabled (with three or four fingers).
3. Open 3 different applications (e.g., Safari, Notes, Calendar).
4. Click the green button in the top left corner of Safari to put it in Full Screen. This creates a new Space.
5. Swipe left and right with 3/4 fingers to quickly switch between the Safari window and the regular Desktop containing the other applications.
6. Swipe up with 3/4 fingers to activate **Mission Control** to see all open applications from a bird's-eye view.

---

## Exercise 3: Verifying MDM Enrollment Status in Terminal
**Objective:** Initial use of Terminal to check if the computer was managed during the Setup Assistant stage via Automated Device Enrollment.

1. Open **Terminal** (via Spotlight or at `/Applications/Utilities/Terminal.app`).
2. Type the following command and press Enter:
   ```bash
   sudo profiles show -type enrollment
   ```
3. The system will prompt you to enter your Local Account password (Admin password). Enter it (the text will not be visible on the screen) and press Enter.
4. Analyze the output:
   - If the text `Error fetching Device Enrollment configuration: (34000) Client is not DEP enabled.` appears, the computer is not registered in Apple Business Manager and is not subject to Remote Management.
   - If the output shows server details (such as a corporate MDM server URL), the computer was correctly enrolled during its initial startup.
