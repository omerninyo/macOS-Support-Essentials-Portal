# Lesson 01: Installation, Familiarization, and Baseline
**Learning Guide (vEXP)**

## Lesson Objectives

* **History & Philosophy** - Evolution from OS X to macOS, the updated Mac lineup for enterprise, and the transition to Apple Silicon (noting macOS 26 Tahoe is the final release supporting Intel).
* **Out of Box Experience (OOBE)** - Deep dive into the Setup Assistant.
* **System, Innovation & Accessibility** - Navigation, Multi-Touch gestures, Continuity ecosystem, overview of Apple Intelligence (macOS 26 Tahoe), screen mirroring, and accessibility features (videos: Universal Control, Continuity Camera, and "The Greatest").
* **Enterprise Flavoring** - What happens when the Remote Management screen (MDM / ADE) interrupts the setup process.

## Overview

<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/128517f1-2471-4e85-a0f5-7611f6c30dcb/"></iframe></div>

## Key Concepts

* **Apple Silicon:** The modern architecture of Mac computers based on Apple's internal development (M-Series processors with ARM architecture), providing an unprecedented performance-to-power ratio.
* **System on a Chip (SoC):** A silicon design that integrates the central processing unit (CPU), graphics processing unit (GPU), memory, and security mechanisms onto a single chip.
* **Unified Memory:** An innovative architecture in Apple Silicon that integrates main memory (RAM) and video memory (VRAM) into the chip package itself. This allows all SoC components to access the same memory pool without copying data back and forth. It eliminates bottlenecks, improves performance, and saves power, but at the cost of not being able to upgrade memory after purchase (it is soldered). [Read more by Howard Oakley](https://eclecticlight.co/2026/06/20/explainer-memory/)
* **Secure Enclave:** An isolated hardware subsystem within the SoC responsible for cryptographic operations, managing encryption keys, and verifying biometric data (Touch ID).
* **Rosetta 2:** A transparent translation environment built into macOS that allows applications written for Intel (x86) processors to run on Apple Silicon Macs. The translation is mostly done Ahead of Time (AOT).
* **Setup Assistant:** The initial process that runs when booting a new Mac or after EACS. Responsible for network settings, region, creating the Local Account, and more. macOS 26 Tahoe also uses this stage to securely download Apple Intelligence models.
* **Automated Device Enrollment (ADE):** Deployment and management technology (formerly DEP) that allows organizations to automatically connect Macs to an MDM (Zero-Touch Deployment) from the first network connection, replacing the consumer Setup Assistant with a Remote Management screen.
* **Continuity:** A collection of technologies allowing a seamless workflow across Apple devices (like Universal Control, Handoff, Continuity Camera). Mostly relies on Bluetooth proximity detection and Peer-to-Peer Wi-Fi.
* **Apple Intelligence:** An AI system built into macOS 26 Tahoe that utilizes the Neural Engine in Apple Silicon for local language model processing with a strong emphasis on privacy. Uses Private Cloud Compute for complex tasks.
> [!TIP]
> **Pro Tip: Language, Locale, and AI in Israel**
> For Apple Intelligence to function properly, the system's Primary Language must match Siri's language (e.g., English US). A mismatch will disable some AI features. If you use an English interface to access AI features, note that voice Dictation to Siri in Hebrew will be problematic due to this collision. Additionally, if you have multiple keyboard languages, consider disabling language switching via the Globe key (🌐) to prevent rare password typing issues at the login screen due to an incorrect layout.

* **Liquid Glass:** The new design language introduced in macOS 26 Tahoe, emphasizing transparency, depth, and a modern, reflective aesthetic that leverages M-series GPUs.
* **Background Process:** A system process that runs in the background without a visible user window, often stored as a LaunchAgent or LaunchDaemon.

## Commands & Paths

| Path / Command | Description |
| :--- | :--- |
| `uname -m` | Terminal command that returns `arm64` if the Mac is running Apple Silicon, or `x86_64` for Intel processors. |
| `system_profiler SPHardwareDataType` | Command that provides full hardware details of the Mac, including core count and memory. |
| `sysctl -n machdep.cpu.brand_string` | Command to quickly fetch the CPU marketing name. |
| `Setup Assistant` | One-way initial startup process guiding the user through system setup and account creation. |
| `sudo profiles show -type enrollment` | Command that returns the device's organizational enrollment status (whether an ADE enrollment exists via Apple Business Manager). |
| `log show --predicate 'process == "Setup Assistant"' --info` | Query to retrieve specific logs from the Out of Box Experience process. |

## Recommended Reading & Links

* [Automated Device Enrollment](https://support.apple.com/guide/deployment/dep24b435f66/web) - Official Apple deployment guide for automatic device enrollment in organizations (ADE / ABM).
* [Boot process for a Mac with Apple silicon](https://support.apple.com/guide/security/secc7b34e5b5/web) - Official security document detailing the boot process for Apple Silicon.
* [Apple Intelligence Overview](https://support.apple.com/apple-intelligence) - Overview of AI capabilities and security in macOS.
* [Explainer: Memory](https://eclecticlight.co/2026/06/20/explainer-memory/) - In-depth article explaining how memory management works in the operating system.

## Summary Video

<!-- Summary Video from YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/oYxR-HrD0FU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

!!! tip "Visual Aid (Student Reference)"
    These images illustrate the interface or mechanism relevant to the lesson topic.

![Explainer_Memory_AboutThisMac](../assets/images/Lesson_01/L01_DeepDive_Explainer_Memory_AboutThisMac.jpg)
![macOS_Versions](../assets/images/Lesson_01/L01_DeepDive_macOS_Versions.jpg)
![Slide48_image8](../assets/images/Lesson_01/L02_LegacySlide_Slide48_image8.jpg)
