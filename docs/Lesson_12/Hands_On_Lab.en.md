# Lesson 12: Updates and Upgrades
**Hands-On Lab**

## Objective
Practice managing system updates (Updates and Upgrades) via the graphical user interface (GUI), understand the RSR (Rapid Security Response) mechanism through System Settings, and practice the correct data transfer process using Migration Assistant in an enterprise environment.

---

## Lab 1: Managing Software Updates in the GUI

**Scenario:**
You need to ensure the system is up-to-date, understand where minor updates (Updates) appear versus full upgrades (Upgrades), and verify that Rapid Security Responses (RSR / BSI) are set to install automatically as required in the organization.

### Step 1: Locating Available Updates

1. Open the **System Settings** app.
2. Navigate to **General** and then select **Software Update**.
3. Wait a few seconds while the system checks with Apple's servers.
4. Notice the screen layout:
   * **Minor Updates (Updates):** Appear at the top (e.g., updating to 26.1).
   * **Major Upgrades (Upgrades):** May appear separately at the bottom (e.g., a recommendation to upgrade to a completely new macOS), preventing accidental installation by the user.

### Step 2: Configuring Automatic Updates and RSR

1. On the same screen, click the Info icon (**i**) located next to the **Automatic Updates** row.
2. You will see several important toggles. Ensure the following toggle is ON:
   **Install Security Responses and system files**
3. **Enterprise Significance:** Enabling this is critical. It allows macOS to receive urgent Rapid Security Responses, which arrive as Cryptex capsules and are applied to the system (often without requiring a restart), as well as updating malware signature lists (XProtect).
4. When finished checking, click **Done**.

### Step 3: Downloading a Full Upgrade via Terminal

1. Often we want to download the full Installer app to create a bootable USB drive or deploy it to other Macs.
2. Open the **Terminal** app.
3. Type the following command to fetch the latest full installer:
   ```bash
   softwareupdate --fetch-full-installer
   ```
   *To download a specific version (e.g., 26.0), you would append `--full-installer-version 26.0`.*
4. This command will download the installer directly to your `/Applications` folder as an app named `Install macOS [Name].app`. (You can cancel the process with `Control + C` if you don't need it right now).

---

## Lab 2: Simulating Data Migration (Migration Assistant)

**Scenario:**
The user received a new Mac, and we must transfer their data correctly from the old Mac or a Time Machine drive, without overwriting Local Accounts or creating conflicts on the new system.

### Step 1: Preparations and Launching the Tool

1. Open **Migration Assistant** from the `/Applications/Utilities` folder (or search in Spotlight).
2. The tool will prompt for the Admin password and will close all other background applications. Approve this.
3. On the first screen, select **From a Mac, Time Machine backup, or startup disk** and click **Continue**.
4. *In this simulation:* If you have a Time Machine drive connected, select it. If not, simply review the screens and get familiar with the choices (without actually performing a transfer).

### Step 2: Selecting Data to Transfer

1. Once the tool identifies the source, it calculates the data size and displays a list of items.
2. **Enterprise Best Practice:**
   * Expand the Accounts list using the small arrow next to the Users category.
   * Ensure you check and transfer **only** the relevant User Account (Standard / Admin). Do not transfer old IT admin accounts if your MDM or Zero-Touch Deployment already handles them on the new Mac.
   * Review the categories: `Applications`, `Other Files & Folders`, `System & Network`.
   * **Strong Enterprise Recommendation:** Uncheck the `System & Network` category to avoid transferring old network settings, old VPN connections, or remnants of a previous Configuration Profile that might conflict with the new MDM Enrollment process. Also, avoid transferring `Applications` to prevent incompatible Kexts or Rosetta dependencies.

### Step 3: Managing Account Conflicts

1. If the new Mac already has an account with the exact same username as the one you're trying to import, a warning will pop up.
2. You will be presented with options:
   * **Replace:** Deletes the existing account on the new Mac and overwrites it. (An option may appear to keep a copy of the overwritten data in the `Deleted Users` folder).
   * **Keep both user accounts:** The system will rename the imported account, so both live side-by-side without overwriting.
3. *In this simulation:* Choose Cancel, and exit Migration Assistant cleanly, as we do not want to overwrite or copy data during this lab.

---

## Lab 3: Investigating Rapid Security Response (RSR)

**Scenario:**
As IT admins, you want to verify which RSR version is currently installed (if any) and how it can be removed in case it causes compatibility issues with internal corporate software.

1. Open **System Settings** and navigate to **General** -> **About**.
2. Check the displayed macOS version. If a rapid RSR update was installed, you will see a letter in parentheses (e.g., `(a)`) next to the version number (such as `macOS 26.3.1 (a)`).
3. If an RSR is installed, you can click the Info button (**i**) next to the macOS version.
4. In the window that opens, if you need to perform a "Rollback" due to a compatibility issue, you will find the **Remove** button designed to remove that specific security update (unmounting the Cryptex) and revert to the base version upon restart.
