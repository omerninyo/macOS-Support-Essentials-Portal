# Lesson 07: Backup and Restore
**Hands-On Lab (Student Practice) (vEXP)**

## Lab Objective
Understand and practice the built-in backup mechanism in macOS, including working with an external Time Machine drive and managing APFS Local Snapshots. You will configure an encrypted external backup drive, perform a simulated "disaster" recovery, and utilize the Command Line (CLI) for advanced troubleshooting.

## Prerequisites
* A Mac (Apple Silicon / Intel) running macOS.
* A user with Administrator privileges.
* **An external USB drive (Flash Drive or Portable SSD)** with at least 64GB of free space.

---

## Part 1: Setting up the USB Drive as a Time Machine Backup

1. Connect the external USB drive to the Mac.
2. To generate data for the exercise, open **Finder** and create a new folder on the Desktop named `TMLab`.
3. Open **TextEdit**, write some text (e.g., "This is highly classified enterprise data"), and save the file inside `TMLab` as `ImportantData.txt`.
4. Open **System Settings** and navigate to **General** -> **Time Machine**.
5. Click **Add Backup Disk...**
6. Select your external USB drive from the list and click **Set Up Disk**.
7. The system will ask if you want to encrypt the backup. Choose to encrypt (this is a critical enterprise security practice!) and enter a memorable password (e.g., `1234`).
8. Click **Done**. The system will format the drive as APFS (Case-sensitive) and lock it as a backup volume.

---

## Part 2: Initial Backup & Simulating Data Loss

1. In the Time Machine settings window, wait for the initial backup to begin.
2. To speed up the process, click **Options** and add the `Applications` folder and other large directories to the exclusions list, so it only backs up your user folder.
3. Wait for the backup to finish (the progress bar will complete and status will show the oldest backup time).
4. **Simulate a disaster:** Open Finder, navigate to the Desktop, move the `TMLab` folder to the Trash, and empty the Trash. The data is now "lost."

---

## Part 3: Restoring Data from the External Drive

1. Ensure the external drive is still connected.
2. Click the Time Machine icon (clock with a counter-clockwise arrow) in the top menu bar, and select **Browse Time Machine backups**.
3. The familiar Time Machine interface will open. In the background, you'll see the current Finder window.
4. On the right side, use the Timeline to go one step back in time to when the backup was made.
5. Locate the `TMLab` folder that reappeared on the Desktop in that historical view.
6. Select the folder and click the **Restore** button at the bottom of the screen.
7. The folder will return to your live Desktop. Open the file to verify the data is intact.

---

## Part 4: Local Snapshots (When Disconnected)

*What happens when the external drive is disconnected?* macOS saves small local backups called Local Snapshots.

1. Physically disconnect the USB drive from the Mac.
2. Open **Disk Utility** (from `Applications/Utilities/`).
3. In the top menu, click **View** and select **Show APFS Snapshots**.
4. Select the `Macintosh HD - Data` volume on the left.
5. At the bottom, you'll see a list of Snapshots. Note the one created just minutes ago during your Time Machine backup.
6. Repeat the "disaster simulation": Delete the `TMLab` folder and empty the Trash.
7. Without connecting the external drive, enter **Browse Time Machine backups** from the menu bar again.
8. Notice that the system still allows time travel thanks to the APFS Local Snapshot! Restore the folder just like before.

---

## Part 5: Cleaning Up and Advanced CLI Management

While you can manage snapshots via Disk Utility, System Administrators often use the Terminal for speed and automation using `tmutil`.

1. Open the **Terminal** application.
2. **View Real-Time Status:** Run `tmutil status` to see if a backup is currently running.
3. **List Local Snapshots:** Run `tmutil listlocalsnapshots /`. This prints the same list you saw in Disk Utility.
4. **Force Thinning (Free Space):** Run `tmutil thinlocalsnapshots / 10000000000 4`. This instructs the system to purge up to 10GB of snapshots with maximum urgency.
5. Plug the USB drive back in.
6. Open **Disk Utility**, select the external drive, and click **Erase** (choose ExFAT or standard APFS) to clear the Time Machine backups and return the drive to normal use.

> **End of Lab**
