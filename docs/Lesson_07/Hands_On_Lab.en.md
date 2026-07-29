# Lesson 07: Backup and Restore
**Hands-on Lab (Student Exercise)**

## Lab Objective
To understand and practice the built-in macOS backup mechanism, including working with an external physical drive (Time Machine Backup) and working with local snapshots (Local Snapshots) on an APFS file system. In this exercise, we will configure an external drive as an encrypted backup destination, perform a restore after a "disaster" (file deletion), and then practice creating and managing local snapshots using the graphical user interface (GUI).

## Prerequisites

*   A Mac computer (Apple Silicon / Intel) with macOS installed.
*   A user with administrator (Admin) privileges.
*   **An external USB drive (USB flash drive or portable SSD)** with at least 64GB of free space.

---

## Part 1: Configuring the USB Drive as a Time Machine Drive

1.  Connect the external USB drive to your Mac.
2.  To create data for the exercise, open **Finder** and create a new folder on your Desktop named `TMLab`.
3.  Open the **TextEdit** application, write some simple text (e.g., "This is highly classified enterprise data"), and save the file inside the `TMLab` folder as `ImportantData.txt`.
4.  Open **System Settings** and navigate to **General** -> **Time Machine**.
5.  Click on **Add Backup Disk...**
6.  Select your external USB drive from the list and click **Set Up Disk**.
7.  The system will ask if you want to Encrypt Backup. Choose to encrypt (this is a critical information security practice in organizations!) and enter a backup password you can remember (e.g., `1234`).
8.  Click **Done**. The system is now formatting the drive to APFS (Case-sensitive) and preparing it for backup.

---

## Part 2: Performing Initial Backup and Simulating Data Loss

1.  Still on the Time Machine screen, wait for the initial backup to begin.
2.  To speed up the process (as the first backup can take time), you can click **Options** and add the `Applications` folder and other large directories to the exclusion list, so it only backs up your user data.
3.  Wait for the backup to complete (the progress bar will finish, and the status will change to Oldest backup).
4.  **Simulating Disaster:** Open Finder, navigate to the Desktop, and delete the `TMLab` folder (move to Trash and empty the Trash). The data is now seemingly lost.

---

## Part 3: Restoring Data from the External Drive

1.  Ensure the external drive is still connected.
2.  Click the Time Machine icon (a clock with a backward arrow) in the top Menu Bar, and select **Browse Time Machine backups**.
3.  The familiar Time Machine interface will open. In the background, you will see the current Finder window (the present).
4.  On the right side of the screen, use the Timeline or the arrows next to the window to go back one step in time, to the point where our backup was performed.
5.  Locate the `TMLab` folder that reappeared on the Desktop at that point in time.
6.  Select the folder and click the **Restore** button at the bottom of the screen.
7.  The folder will return to the Desktop on the live system. Open the file and verify that the information inside is identical.

---

## Part 4: Local Snapshots

*What happens when the external drive is not connected?* macOS saves small local backups called Local Snapshots.

1.  Physically disconnect the USB drive from the computer.
2.  Open **Disk Utility** (from `Applications/Utilities/`).
3.  In the top menu, click **View** and select **Show APFS Snapshots**.
4.  Select the `Macintosh HD - Data` volume from the left side of the window.
5.  At the bottom of the screen, you will see a list of Snapshots. Notice that a Snapshot was created just a few minutes ago, during your last backup.
6.  Repeat the "disaster simulation" from the previous section: delete the `TMLab` folder again and empty the Trash.
7.  Without connecting the external drive, go back into **Browse Time Machine backups** from the Menu Bar.
8.  Notice: The system allows the journey through time thanks to the local APFS snapshot! Perform a restore exactly as before.

---

## Part 5: Drive Cleanup and Snapshot Management

1.  Return to the **Disk Utility** application and look at the list of Snapshots at the bottom of the window.
2.  To manually and immediately free up space, select one of the snapshots and click the minus button (`-`) (or right-click and **Delete**) to delete it.
3.  Reconnect the external USB drive.
4.  Open **Disk Utility**, select the external drive, and click **Erase** (choose ExFAT or regular APFS format) to clear it of Time Machine backups and prepare it for normal use again.

---

## Extra Exercise / Technical Iceberg Tip

Although we've seen how to manage Snapshots from Disk Utility in the GUI, system administrators (SysAdmins) often use the command line (Terminal) to perform these operations much faster or via scripts. The main tool for managing the backup engine from the command line is `tmutil`.

*   **Creating a Manual Snapshot:**

    ```bash
    sudo tmutil localsnapshot
    ```
    This command forces the system to take an immediate snapshot of the data volume (recommended before making dangerous system changes or software tests).

*   **Displaying a List of Snapshots:**

    ```bash
    tmutil listlocalsnapshots /
    ```
    Displays all existing snapshots for the main volume (exactly the same list we saw in Disk Utility).

*   **Bulk Deletion (Short Script):**

    ```bash
    for d in $(tmutil listlocalsnapshots | grep "com.apple.TimeMachine" | awk -F '.' '{print $4}'); do sudo tmutil deletelocalsnapshots $d; done
    ```
    *(Note: This command extracts the dates from the snapshot names and deletes them one by one to quickly free up disk space).*

> **End of Lab**

<!-- src_hash: d82f16cbeed6280bb2c4fde9b90f4a6d01b5d01295c427c8cfe5812551b8ebe5 -->


!!! tip "Visual Aids (Student Guide)"
    These images illustrate the relevant interface or mechanism for this lesson.

![Snapshots_aren_t_backups_p1_114](../assets/images/Lesson_07/L07_DeepDive_Snapshots_aren_t_backups_p1_114.jpeg)
![Time_Machine_backing_up_different_file_systems_p4_133](../assets/images/Lesson_07/L07_DeepDive_Time_Machine_backing_up_different_file_systems_p4_133.jpeg)
![Time_Machine_backing_up_different_file_systems_p5_133](../assets/images/Lesson_07/L07_DeepDive_Time_Machine_backing_up_different_file_systems_p5_133.jpeg)
![Slide120_image42](../assets/images/Lesson_07/L07_LegacySlide_Slide120_image42.jpg)
![Slide122_image43](../assets/images/Lesson_07/L07_LegacySlide_Slide122_image43.jpg)
![Slide122_image44](../assets/images/Lesson_07/L07_LegacySlide_Slide122_image44.jpg)
![Slide136_image168](../assets/images/Lesson_07/L07_LegacySlide_Slide136_image168.png)
![Slide67_image80](../assets/images/Lesson_07/L07_LegacySlide_Slide67_image80.png)
![26-Tahoe-Time-Machine-Menu-scaled](../assets/images/Lesson_07/L07_TahoeUI_26-Tahoe-Time-Machine-Menu-scaled.png)
![26-Tahoe-Time-Machine-scaled](../assets/images/Lesson_07/L07_TahoeUI_26-Tahoe-Time-Machine-scaled.png)
