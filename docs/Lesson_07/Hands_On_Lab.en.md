# Lesson 07: Backup and Restore
**Hands-On Lab**


## macOS Backup and Recovery

### Lab Objective
To understand and practice the native macOS backup mechanism, including managing external physical drives (Time Machine Backups) and manipulating local APFS Snapshots.

### Prerequisites

* A Mac computer (Apple Silicon or Intel) running macOS.
* An Administrator (Admin) user account.
* **An external USB drive (Thumb drive or Portable SSD)** with at least 64GB of free space.

### Scenario
> In this exercise, we will configure an external drive as an encrypted backup destination, execute a disaster recovery procedure (after intentionally deleting files), and explore the creation and management of Local Snapshots using both the graphical user interface (GUI) and the command line (Terminal).

---

## Step 1 — Configuring the USB Drive as a Time Machine Destination

> **Learning Outcome:** How to securely provision an external, encrypted volume as the official Time Machine backup destination in macOS.

1. Connect the external USB drive to your Mac.
2. To generate sample data for this exercise, open **Finder** and create a new folder on your **Desktop** named `TMLab`.
3. Open the **TextEdit** application, type a short string of text (e.g., "This is highly classified enterprise data"), and save the file inside the `TMLab` folder as `ImportantData.txt`.
4. Open **System Settings** and navigate to **General** -> **Time Machine**.
5. Click on **Add Backup Disk...**
6. Select your external USB drive from the list and click **Set Up Disk**.
7. The system will ask if you want to encrypt the backup. Choose to encrypt it (this is a critical IT security practice!) and enter a memorable backup password (e.g., `1234`).
8. Click **Done**. The system will now format the drive to APFS (Case-sensitive) and lock it as a dedicated backup volume.

> [!IMPORTANT]
> For this and all subsequent exercises, ensure you are ONLY utilizing the provided external USB drive for backup configurations and formatting. Never perform destructive formatting actions on your system drive!

---

## Step 2 — Initial Backup Execution and Data Loss Simulation

> **Learning Outcome:** How to monitor the initial backup progress and prepare the environment for a recovery simulation by intentionally deleting data.

1. While still in the Time Machine settings window, wait for the initial backup to commence.
2. To accelerate the process, click **Options** and add the `Applications` folder (and any other large directories) to the Exclude list, ensuring only your user directory is backed up.
3. Wait for the backup to finish (the progress bar will complete, and the status will update to "Oldest backup").
4. **Disaster Simulation:** Open **Finder**, navigate to the Desktop, delete the `TMLab` folder (move it to the Trash), and then empty the Trash. The data is now effectively "lost".

---

## Step 3 — Data Restoration from the External Drive

> **Learning Outcome:** How to recover specific files or directories using the Time Machine "Spaceship" graphical interface by traveling back in time.

1. Ensure the external drive is still connected to the Mac.
2. Click the Time Machine icon (a clock with a backward arrow) in the top **Menu Bar**, and select **Browse Time Machine backups**.
3. The familiar Time Machine interface will launch. In the background, you will see your current Finder window (the present).
4. On the right side of the screen, use the Timeline or the on-screen arrows to step back in time to the moment the backup was captured.
5. Locate the `TMLab` folder that has reappeared on the Desktop in that specific point in time.
6. Select the folder and click the **Restore** button at the bottom of the screen.
7. The folder will be instantly restored to the live system Desktop. Open the text file to verify data integrity.

---

## Step 4 — Local Snapshots

> **Learning Outcome:** Proving that macOS retains small, local backups called Local Snapshots, enabling file recovery even when the external USB drive is completely disconnected.

*What happens when the external drive is disconnected?* macOS retains lightweight, internal backups known as Local Snapshots.

1. Physically disconnect the external USB drive from the Mac.
2. Open **Disk Utility** (located in `/Applications/Utilities/`).
3. In the top menu bar, click **View** and select **Show APFS Snapshots**.
4. Select the `Macintosh HD - Data` volume from the left sidebar.
5. At the bottom of the window, observe the list of Snapshots. Note the Snapshot created just a few minutes ago during your recent backup.
6. Repeat the "Disaster Simulation" from Step 2: Delete the `TMLab` folder again and empty the Trash.
7. Without reconnecting the external drive, click **Browse Time Machine backups** from the Menu Bar once more.
8. Notice that the system still permits time travel thanks to the local APFS snapshot! Perform the restore procedure exactly as before.

> [!NOTE]
> The Local Snapshots mechanism is an integral component of the APFS architecture and the Copy-on-Write mechanism we previously covered. This is precisely why instantaneous "time travel" is possible.

---

## Step 5 — Drive Cleanup and Terminal Snapshot Management

> **Learning Outcome:** Executing advanced administrative snapshot operations via the Terminal using the `tmutil` binary, and re-provisioning the USB drive for standard use.

While we explored snapshot management via the Disk Utility GUI, System Administrators (SysAdmins) frequently leverage the command line interface (Terminal) for rapid and scriptable execution using the `tmutil` utility.

1. Open the **Terminal** application.
2. **Live Status Monitoring:** Run the following command to check if a backup process is currently active in the background:
   ```bash
   tmutil status
   ```
3. **List Snapshots:** Run the following command to output the exact same snapshot list you previously viewed in Disk Utility:
   ```bash
   tmutil listlocalsnapshots /
   ```
4. **Emergency Thinning:** Run the following command to instruct the system to forcefully purge up to ~10GB of snapshots at maximum urgency (level 4) to reclaim disk space:
   ```bash
   tmutil thinlocalsnapshots / 10000000000 4
   ```
5. Reconnect the external USB drive.
6. Open **Disk Utility**, select the external drive, and click **Erase** (choose ExFAT or standard APFS format) to purge the Time Machine volume structure and prepare it for regular usage.

> [!CAUTION]
> During this final step (formatting via Disk Utility), double-check that you are erasing the external USB drive and NOT any partition belonging to your system drive!

> **End of Lab**
