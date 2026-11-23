# Lesson 01: Installation, Orientation and Baseline
**Hands-On Lab (Student Practice)**

---

## Overview
This lab serves as an equalizer for IT technicians and administrators transitioning to macOS. You will practice GUI-first system navigation, verify how macOS surfaces Apple Silicon hardware versus translated Intel processes, and check whether a Mac is enrolled in enterprise management (MDM).

---

## Exercise 1: Configuration and Architecture Identification via GUI (Apple Silicon Diagnostics)

> **What You Will Learn:** Verify Mac hardware specifications in the GUI, explore the Liquid Glass design language, and distinguish native Apple Silicon processes from Intel processes translated in real time by Rosetta 2.

1. Click the Apple menu (``) in the upper-left corner of the screen and select **About This Mac**.
2. Observe the **Liquid Glass** visual interface, and verify the Apple chip model (e.g., `Apple M3` or `Apple M4`) and the amount of **Unified Memory**.
3. Click **More Info...** to open `System Settings -> General -> About`, then scroll down and click **System Report...** to inspect full hardware details in **System Information**.
4. Open **Activity Monitor** (via Spotlight using `Cmd + Space`).
5. Ensure the **CPU** tab is selected in the top toolbar and locate the **Kind** column.

!!! tip
    If the `Kind` column is not visible, right-click the column header bar and check **Kind**.

6. Click the **Kind** column header to sort processes. Identify native **Apple** (ARM64) processes versus **Intel** processes (translated on the fly by Rosetta 2, if any are installed).

---

## Exercise 2: Navigation, Gestures, and Workspaces (Navigation & Spaces)

> **What You Will Learn:** Smoothly switch between windows and full-screen workspaces using Trackpad Multi-Touch gestures.

1. Open **System Settings** and select **Trackpad**.
2. Review the **Point & Click**, **Scroll & Zoom**, and **More Gestures** tabs, ensuring **Swipe between full-screen applications** is enabled.
3. Launch 3 built-in applications (e.g., Safari, Notes, Calendar).
4. Hover over the green button in the top-left corner of Safari: inspect the built-in Window Tiling options, then click **Enter Full Screen** to create a dedicated **Space**.
5. Swipe left and right with 3 or 4 fingers on the Trackpad to switch between full-screen Safari and the standard Desktop.
6. Swipe up with 3 or 4 fingers to open **Mission Control** for a bird's-eye view of all open windows and Spaces.

---

## Exercise 3: Checking Enterprise Management (Device Management) in the GUI

> **What You Will Learn:** Locate enterprise MDM enrollment and Configuration Profiles directly in System Settings.

1. Open **System Settings** and navigate to **General -> Device Management**.
2. Inspect the current state:
   * On an unmanaged standalone classroom Mac, no MDM enrollment or profiles will be listed.
   * On a corporate Mac enrolled via **Automated Device Enrollment (ADE)** during Setup Assistant, the primary MDM profile, organization details, and enforced configuration payloads appear here.

---

## IT Bonus Exercise: The Command Line (Terminal)

> **What You Will Learn:** Query exact CPU branding and Apple Business Manager (ADE/DEP) enrollment status via Terminal.

!!! note "Copy-and-Paste Only"
    Formal Terminal training begins in Lesson 08. Copy and paste these commands for quick inspection only.

1. Open **Terminal** (`Cmd + Space` -> `Terminal`) and query the exact CPU brand string:
   ```bash
   sysctl -n machdep.cpu.brand_string
   ```

2. Check whether this Mac's serial number is assigned to an MDM server in Apple Business Manager (ADE):
   ```bash
   sudo profiles show -type enrollment
   ```
   *(Enter your local admin password when prompted; `Client is not DEP enabled` confirms a standalone Mac).*

<!-- src_hash: 6c10b8b2112f26c74df0353c867a84e36bda3870dff6ee456e9ebd5d93cf2da1 -->
