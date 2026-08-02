# Lesson 07: Backup and Restore
**Hands-on Lab (Student Exercise) (vEXP)**

## Lab Objective
To understand and practice the built-in macOS backup mechanism, including working with an external physical drive (Time Machine Backup) and working with Local Snapshots in the APFS file system. In this exercise, we will configure an external drive as an encrypted backup destination, perform a restore after a "disaster" (file deletion), and then practice creating and managing local Snapshots using the graphical user interface (GUI) and the command line (Terminal).

## Prerequisites

*   Mac computer (Apple Silicon / Intel) with macOS installed.
*   User with administrator (Admin) privileges.
*   **External USB drive (USB flash drive or portable SSD)** with at least 64GB of free space.

---

## Exercise 1: Configuring the USB Drive as a Time Machine Drive

1.  Connect the external USB drive to your Mac.
2.  To create data for practice, open **Finder** and create a new folder on the Desktop named `TMLab`.
3.  Open the **TextEdit** application, write some simple text (e.g., "This is highly classified enterprise data"), and save the file inside the `TMLab` folder as `ImportantData.txt`.
4.  Open **System Settings** and navigate to **General** -> **Time Machine**.
5.  Click **Add Backup Disk...**
6.  Select your external USB drive from the list and click **Set Up Disk**.
7.  The system will ask if you want to encrypt the backup (Encrypt Backup). Choose to encrypt (this is critical information security practice in organizations!) and enter a backup password you can remember (e.g., `1234`).
8.  Click **Done**. The system is now formatting the drive as APFS (Case-sensitive) and locking it as a backup drive.

---

## Exercise 2: Performing an Initial Backup and Simulating Data Loss

1.  While still on the Time Machine screen, wait for the initial backup to begin.
2.  To speed up the process, you can click **Options** and add the `Applications` folder and other large directories to the exclusion list (Exclude), so it only backs up your user data.
3.  Wait for the backup to complete (the progress bar will finish, and the status will change to Oldest backup).
4.  **Disaster Simulation:** Open Finder, navigate to the Desktop, and delete the `TMLab` folder (move to Trash and empty the Trash). The data is presumably lost.

---

## Exercise 3: Restoring Data from the External Drive

1.  Ensure the external drive is still connected.
2.  Click the Time Machine icon (a clock with a backward arrow) in the top Menu Bar, and select **Browse Time Machine backups**.
3.  The familiar Time Machine interface will open. In the background, you will see the current Finder window (the present).
4.  On the right side of the screen, use the Timeline or the arrows to go back one step in time, to the point where our backup was performed.
5.  Locate the `TMLab` folder that reappeared on the Desktop at that point in time.
6.  Select the folder and click the **Restore** button at the bottom of the screen.
7.  The folder will return to the Desktop in the live system. Open the file and verify that the information inside is identical.

---

## Exercise 4: Local Snapshots

*What happens when the external drive is not connected?* macOS saves small local backups called Local Snapshots.

1.  Physically disconnect the USB drive from the computer.
2.  Open **Disk Utility** (from `Applications/Utilities/`).
3.  In the top menu, click **View** and select **Show APFS Snapshots**.
4.  Select the `Macintosh HD - Data` volume from the left side of the window.
5.  At the bottom of the screen, you will see a list of Snapshots. Note that a Snapshot was created just a few minutes ago, during your last backup.
6.  Repeat the "disaster simulation" from the previous section: delete the `TMLab` folder again and empty the Trash.
7.  Without connecting the external drive, re-enter **Browse Time Machine backups** from the Menu Bar.
8.  Note: The system allows time travel thanks to the local APFS snapshot! Perform a restore exactly as before.

---

## Exercise 5: Cleaning the Drive and Managing Snapshots in Terminal

Although we've seen how to manage Snapshots from Disk Utility in the GUI, System Administrators (SysAdmins) often use the command line (Terminal) to perform these operations quickly and efficiently with the `tmutil` tool.

1.  Open the **Terminal** application.
2.  **View Live Status:** Run `tmutil status` to see if a backup is running in the background.
3.  **Display Snapshot List:** Run `tmutil listlocalsnapshots /`. This will print the same list you saw in Disk Utility.
4.  **Urgent Space Reclamation (Thinning):** Run the command `tmutil thinlocalsnapshots / 10000000000 4`. This instructs the system to urgently delete up to approximately 10GB of snapshots to free up space on your drive.
5.  Reconnect the external USB drive.
6.  Open **Disk Utility**, select the external drive, and click **Erase** (choose ExFAT or regular APFS format) to clear it of Time Machine backups and prepare it for normal use again.

> **End of Lab**

<!-- src_hash: 6c635e61743565f5b38ec74b0bec41d723c77cc039fcdf75a0ef434a6a108ad1 -->
