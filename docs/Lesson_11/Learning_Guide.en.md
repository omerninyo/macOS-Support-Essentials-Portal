# Lesson 11: Peripherals
**Student Learning Guide**


## Overview

<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/fd31f0d4-5f45-4a2f-acea-e9d8ba503f57/"></iframe></div>

## Core Terms and Concepts

* **Accessory Security:** A security mechanism in Apple Silicon Macs that requires explicit user approval before USB or Thunderbolt accessories (or SD cards) are allowed to communicate with the system. It can be managed via System Settings -> Privacy & Security or through MDM profiles.
* **Thunderbolt vs. USB-C:** The physical connector (Type-C) is often identical, but the protocol differs. Thunderbolt 3/4 cables and ports support significantly higher data transfer speeds (up to 40Gbps) and Daisy Chaining, compared to standard USB cables.
* **DFU Port:** A specific USB-C port on a Mac (primarily in Apple Silicon computers) designed to put the computer into DFU mode for firmware recovery (Revive/Restore) using Apple Configurator. On laptops, this is usually the left port closest to the user.
* **CUPS - Common Unix Printing System:** The built-in printing engine of macOS. An open-source system (originally developed by Apple) that manages all print queues, drivers, and network protocols for printers.
* **The Chooser (History):** An early Apple network printer management tool, which started as Choose Printer in 1984 and became the mythological Chooser in 1991 (System 7).
* **AirPrint:** Apple's wireless protocol that allows printing without the need to install dedicated drivers. Supported in most modern printers.
* **Printing Payload:** An MDM payload (configuration setting) that allows network administrators to remotely configure printers, printer lists, and default printers.
* **AirPrint Payload:** An MDM payload that enables the silent deployment of IP addresses and routing of AirPrint-supported printers to organization users.
* **PPD - PostScript Printer Description:** A configuration file used by CUPS to understand the capabilities of a specific printer (paper sizes, trays, color printing).

## Terminal (CLI) Commands List

### Printing Management and Diagnostics (CUPS)
The printing system in macOS can be fully and quickly managed from the command line.

* `lpstat -p` - Displays a list of all installed printers on the Mac and their current status.
* `lpstat -a` - Checks if printers are accepting new print jobs.
* `lpstat -o` - Displays the current print job queue.
* `lpstat -t` - The ultimate command for CUPS diagnostics: prints all possible information about the state of the printing system, printers, queues, and service availability.
* `cancel -a` - Cancels and deletes all print jobs in all queues (very useful for clearing a "stuck" queue that prevents further printing).
* `cancel <job_id>` - Cancels a specific print job (the ID can be obtained from the `lpstat -o` command).
* `cupsctl WebInterface=yes` - Enables the CUPS web management interface. After running this command, an advanced graphical interface can be accessed via the browser at `http://localhost:631`. (To disable, change to `no`).
* `lpinfo -m` - Displays all available drivers (PPDs) in the system.
* `lpinfo -v` - Displays all devices (physically connected via USB or available on the network) that the CUPS system currently detects.

### System Profiler Tool for Peripheral Diagnostics
The `system_profiler` command allows retrieving detailed information about hardware components directly in the terminal, exactly as it appears in the System Information app.

* `system_profiler SPUSBDataType` - Displays a detailed list of all USB devices currently connected to the Mac (including hubs, keyboards, disks, and adapters).
* `system_profiler SPThunderboltDataType` - Displays details about the Thunderbolt ports on the Mac, link speeds (Link Status), and connected devices. Useful for diagnosing equipment that isn't utilizing full speed.
* `system_profiler SPPrintersDataType` - Retrieves detailed information about every printer configured in the system, including the driver version, exact PPD path, and its URI (network/connection address).
* `system_profiler SPBluetoothDataType` - Displays the status of Bluetooth devices, including battery levels and MAC addresses.

### Network and Services

* `networksetup -listallhardwareports` - Displays all network interfaces on the Mac. Sometimes network printers are configured with their own virtual interface, or it is important to verify that an external network adapter (USB to Ethernet) is correctly detected by the system at the hardware level.

## Relevant Paths and Files

* `/etc/cups/` - The directory containing the internal configuration files of the CUPS engine (e.g., `cupsd.conf` and `printers.conf`). Changes to these files require root privileges.
* `/Library/Printers/` - The directory where third-party printer drivers, plugins, and PPD files are installed.
* `/var/spool/cups/` - The temporary spool directory where the CUPS system stores files waiting to be printed.
* `/Library/Managed Preferences/` - The path where configuration profiles (like Printing Payload or Accessory Security restrictions) pushed by the organizational MDM system are saved.

## Recommended Links and Further Reading

* [Troubleshoot peripheral connections on Mac](https://support.apple.com/guide/apple-platform-support/troubleshoot-peripheral-connections-aps3b8ff2373/web) - The official guide for network administrators to troubleshoot issues with peripherals.
* [Allow accessories to connect to Mac](https://support.apple.com/guide/mac-help/allow-accessories-to-connect-mchlf779ae93/mac) - User explanation about the new accessory security mechanism that blocks unknown USB connections.
* [Manage printer profiles in Apple devices](https://support.apple.com/guide/apple-platform-deployment/printing-payload-settings-apdeb12df380/web) - Enterprise documentation on configuring printers remotely using MDM.
* [Thunderbolt ports aren’t all the same](https://eclecticlight.co/2025/01/14/thunderbolt-ports-arent-all-the-same/) - Deep technical overview of the differences between various Thunderbolt and USB-C connections on Mac computers.
* [A brief history of the Chooser and printer support](https://eclecticlight.co/2024/10/12/a-brief-history-of-the-chooser-and-printer-support/) - Historical article on the evolution of adding printers in the Mac environment from its inception to today.

## Summary Video

<!-- Summary video from YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/DDXfEIRgAxs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>





!!! tip "Visual Aid (Student Reference)"
    These images illustrate the interface or mechanism relevant to the lesson topic.




<!-- src_hash: 3b96c95fa62fa72e644cc8df3780e8fbef016fca350fb8f4d2878ae6f809e78f -->


!!! tip "Visual Aids (Student Guide)"
    These images illustrate the relevant interface or mechanism for this lesson.

    ![How Thunderbolt 5 can be faster or not p1 9](../assets/images/Lesson_11/L11_DeepDive_How_Thunderbolt_5_can_be_faster_or_not_p1_9.png)
    ![Slide139 image46](../assets/images/Lesson_11/L11_LegacySlide_Slide139_image46.jpg)
    ![Slide139 image47](../assets/images/Lesson_11/L11_LegacySlide_Slide139_image47.jpg)
    ![Slide140 image169](../assets/images/Lesson_11/L11_LegacySlide_Slide140_image169.png)
    ![Slide140 image49](../assets/images/Lesson_11/L11_LegacySlide_Slide140_image49.jpeg)
    ![Slide19 image29](../assets/images/Lesson_11/L11_LegacySlide_Slide19_image29.png)
    ![Slide19 image30](../assets/images/Lesson_11/L11_LegacySlide_Slide19_image30.png)
    ![Slide31 image50](../assets/images/Lesson_11/L11_LegacySlide_Slide31_image50.jpg)
    ![Slide31 image51](../assets/images/Lesson_11/L11_LegacySlide_Slide31_image51.jpg)
    ![Slide34 image52](../assets/images/Lesson_11/L11_LegacySlide_Slide34_image52.jpg)
    ![Slide34 image53](../assets/images/Lesson_11/L11_LegacySlide_Slide34_image53.jpg)
    ![Slide41 image53](../assets/images/Lesson_11/L11_LegacySlide_Slide41_image53.jpg)
    ![26-Tahoe-Print-scaled](../assets/images/Lesson_11/L11_TahoeUI_26-Tahoe-Print-scaled.png)
    ![26-Tahoe-Settings-Bluetooth-scaled](../assets/images/Lesson_11/L11_TahoeUI_26-Tahoe-Settings-Bluetooth-scaled.png)
    ![26-Tahoe-Settings-Printers-and-Scanners-scaled](../assets/images/Lesson_11/L11_TahoeUI_26-Tahoe-Settings-Printers-and-Scanners-scaled.png)
