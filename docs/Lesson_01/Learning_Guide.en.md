# Lesson 01: Installation, Orientation, and Baseline Alignment
**Student Learning Guide**

---

## Lesson Objectives

* **History and Philosophy** - The evolution from OS X to macOS, the modernized Mac lineup for enterprise environments, and the transition to Apple Silicon (including noting that macOS 26 Tahoe is the final version supporting Intel).
* **Out of Box Experience (OOBE)** - Deep dive into the Setup Assistant.
* **The System, Innovation, and Accessibility** - Navigation, Multi-Touch gestures, the Continuity ecosystem, an overview of Apple Intelligence (in Tahoe 26), screen mirroring, and accessibility (Videos: Universal Control, Continuity Camera, and "The Greatest").
* **Enterprise Spice** - What happens when the Remote Management (MDM / ADE) screen intercepts the setup process.

---

## 🎧 Audio Summary — Before or After the Lesson

<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/128517f1-2471-4e85-a0f5-7611f6c30dcb/"></iframe></div>

---

## Key Concepts

* **Apple Silicon Processors:** The modern architecture of Mac computers based on Apple's in-house design (M-Series chips in ARM configuration), delivering unprecedented performance-per-watt ratios.
* **System on a Chip (SoC):** A silicon design that integrates the Central Processing Unit (CPU), Graphics Processing Unit (GPU), memory, and security mechanisms into a single chip.
* **Unified Memory:** An innovative architecture in Apple Silicon that integrates the main memory (RAM) and video memory (VRAM) directly onto the chip package. This allows all SoC components to access the same memory pool without copying data back and forth. The architecture eliminates bottlenecks, improves performance, and saves power, but at the cost of being unable to upgrade memory after purchase (memory is soldered). [Recommended Reading by Howard Oakley](https://eclecticlight.co/2026/06/20/explainer-memory/)
* **Secure Enclave:** An isolated hardware subsystem within the SoC responsible for cryptographic operations, managing encryption keys, and verifying biometric data (Touch ID).
* **Rosetta 2:** A transparent translation environment built into macOS that allows applications compiled for Intel processors (x86) to run on Apple Silicon Macs. The translation is typically performed Ahead of Time (AoT).
* **Setup Assistant:** The initial process executed when turning on a new Mac or after an EACS (Erase All Content and Settings). Responsible for network configuration, region settings, Local Account creation, and more. In macOS 26 Tahoe, this process also securely downloads the Apple Intelligence language models.
* **Automated Device Enrollment (ADE):** A deployment and management technology (formerly DEP) that allows organizations to automatically enroll Mac computers into MDM (Zero-Touch Deployment) upon first network connection, replacing the consumer Setup Assistant with a Remote Management screen.
* **Continuity:** A suite of technologies enabling seamless workflows across Apple devices (such as Universal Control, Handoff, and Continuity Camera). It primarily relies on Bluetooth proximity detection and Peer-to-Peer Wi-Fi communication.
* **Apple Intelligence:** An artificial intelligence system built into macOS 26 Tahoe that leverages the Neural Engine in Apple Silicon to process language models locally, emphasizing privacy. It utilizes Private Cloud Compute for complex tasks.

!!! tip "Pro Tip: Language, Region, and AI Settings"
    For Apple Intelligence to function correctly, you must ensure the system language (Primary Language) exactly matches the Siri language (e.g., English US). A mismatch will result in some AI features being disabled. If you choose to use an English interface to access AI features, keep in mind that voice Dictation to Siri in other languages may be problematic due to this conflict. Additionally, if you have multiple keyboard layouts, consider disabling the language switch via the Globe key (🌐) to prevent rare scenarios of typing an incorrect password at the login screen due to an unintended keyboard layout.

* **Liquid Glass:** The new design language introduced in macOS 26 Tahoe, emphasizing transparency, depth, and a modern, reflective aesthetic that utilizes the graphical power of M-series processors.
* **Background Process:** A system process that runs in the background without a visible user window, often stored as a LaunchAgent or LaunchDaemon.

---

## Commands & Paths

!!! note "Using the Terminal (Command Line)"
    The Terminal commands demonstrated in the first lesson are listed here. There is no need to memorize their syntax right now! You can simply copy-paste them in the lab to see the result. In-depth learning of the Terminal will take place in Lesson 08, and we will cover the logging system in Lesson 16. For now, use this strictly as a quick testing tool.

| Path / Command | Description |
| :--- | :--- |
| `uname -m` | A Terminal command that returns `arm64` if the computer is running Apple Silicon, or `x86_64` for Intel processors. |
| `system_profiler SPHardwareDataType` | A command that provides full hardware specifications of the Mac, including core count and memory. |
| `sysctl -n machdep.cpu.brand_string` | A command to quickly retrieve the marketing name of the processor on the machine. |
| `Setup Assistant` | A one-way initial setup process that guides the user in configuring the system and creating the account (full reset and drive ownership will be covered in Lessons 4 and 14). |
| `sudo profiles show -type enrollment` | A command that returns the device's organizational enrollment status (whether an ADE enrollment exists via Apple Business Manager). |
| `log show --predicate 'process == "Setup Assistant"' --info` | A query for extracting specific logs from the Out of Box Experience process. |

---

## Recommended Reading and Links

* [Automated Device Enrollment](https://support.apple.com/guide/deployment/dep24b435f66/web) - Official Apple deployment guide for automatic device enrollment in an organization (ADE / ABM).
* [Boot process for a Mac with Apple silicon](https://support.apple.com/guide/security/secc7b34e5b5/web) - Official security document detailing the boot process of Apple Silicon processors.
* [Apple Intelligence Overview](https://support.apple.com/apple-intelligence) - Overview of capabilities and security of AI features in macOS.
* [Explainer: Memory](https://eclecticlight.co/2026/06/20/explainer-memory/) - An in-depth article explaining how memory is managed in the operating system.

---

## 🎬 Video Summary

<!-- YouTube Summary Video -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/oYxR-HrD0FU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

## Presentation Visuals

!!! tip "Visual Aid (Student Reference)"
    These images illustrate the interface or mechanism relevant to the lesson's topic.

![Explainer_Memory_AboutThisMac](../assets/images/Lesson_01/L01_DeepDive_Explainer_Memory_AboutThisMac.jpg)
![macOS_Versions](../assets/images/Lesson_01/L01_DeepDive_macOS_Versions.jpg)
![Slide48_image8](../assets/images/Lesson_01/L02_LegacySlide_Slide48_image8.jpg)

---

## 💡 Presentation Visuals

!!! tip "Visual Demonstration (Student Aid)"
    These images illustrate the relevant interface or mechanism for the lesson topic.

![Explainer_Memory_AboutThisMac](../assets/images/Lesson_01/L01_DeepDive_Explainer_Memory_AboutThisMac.jpg)
![macOS_Versions](../assets/images/Lesson_01/L01_DeepDive_macOS_Versions.jpg)
![26-Tahoe-Finder-Control-Center-Edit-scaled](../assets/images/Lesson_01/L01_TahoeUI_26-Tahoe-Finder-Control-Center-Edit-scaled.png)
![26-Tahoe-Finder-Control-Center-scaled](../assets/images/Lesson_01/L01_TahoeUI_26-Tahoe-Finder-Control-Center-scaled.png)
![26-Tahoe-Finder-Copy-scaled](../assets/images/Lesson_01/L01_TahoeUI_26-Tahoe-Finder-Copy-scaled.png)
![26-Tahoe-Finder-Customize-scaled](../assets/images/Lesson_01/L01_TahoeUI_26-Tahoe-Finder-Customize-scaled.png)
![26-Tahoe-Finder-Desktop-Stacks-scaled](../assets/images/Lesson_01/L01_TahoeUI_26-Tahoe-Finder-Desktop-Stacks-scaled.png)
![26-Tahoe-Finder-Go-To-Folder-scaled](../assets/images/Lesson_01/L01_TahoeUI_26-Tahoe-Finder-Go-To-Folder-scaled.png)
![26-Tahoe-Finder-Stacks-scaled](../assets/images/Lesson_01/L01_TahoeUI_26-Tahoe-Finder-Stacks-scaled.png)
![26-Tahoe-Notification-Center-scaled](../assets/images/Lesson_01/L01_TahoeUI_26-Tahoe-Notification-Center-scaled.png)
![26-Tahoe-Settings-Battery-scaled](../assets/images/Lesson_01/L01_TahoeUI_26-Tahoe-Settings-Battery-scaled.png)
![26-Tahoe-Settings-General-scaled](../assets/images/Lesson_01/L01_TahoeUI_26-Tahoe-Settings-General-scaled.png)
![Slide48_image8](../assets/images/Lesson_01/L02_LegacySlide_Slide48_image8.jpg)
![Slide67_image80](../assets/images/Lesson_01/L07_LegacySlide_Slide67_image80.png)
![Slide74_image14](../assets/images/Lesson_01/L09_LegacySlide_Slide74_image14.jpg)
