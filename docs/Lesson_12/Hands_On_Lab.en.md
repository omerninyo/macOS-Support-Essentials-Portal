# Lesson 12: Updates and Upgrades
**Hands-on Lab (Student Exercise)**

## Purpose of the Exercise
Practice controlling system updates and upgrades (Updates and Upgrades) using the graphical user interface (GUI), understanding the RSR (Rapid Security Response) mechanism through System Settings, and practicing the correct data migration process using Migration Assistant in an enterprise environment.

---

## Exercise 1: Managing Software Updates in the Graphical User Interface

**Scenario:**
You need to ensure the system is up-to-date, understand where minor system updates (Updates) appear versus full upgrades (Upgrades), and verify that silent security updates (Rapid Security Responses / RSR) are configured for automatic installation as required by the organization.

### Step A: Locating Available Updates

1. Open the **System Settings** application.
2. Navigate to **General** and then select **Software Update**.
3. Wait a few seconds while the system searches for updates on Apple's servers.
4. Pay attention to the division on the screen:
   * **Minor Updates (Updates):** Will appear in the upper section (e.g., moving to version 26.1).
   * **Major Upgrades (Upgrades):** May appear separately in the lower section (e.g., a recommendation to upgrade to a completely new macOS), to prevent accidental installation by the user.

### Step B: Configuring Automatic Updates and RSR

1. On the same screen, click the information button (the **i** symbol) located next to the **Automatic Updates** line.
2. Several important toggles will be displayed. Ensure the following toggle is enabled:
   **Install Security Responses and system files**

3. **Enterprise Significance:** Enabling this toggle is critical. It allows the macOS system to receive urgent security updates, which arrive as capsules (Cryptex) and are applied to the system (often without requiring a computer restart), as well as to update malicious signature lists (XProtect).
4. After checking, click **Done**.

### Step C: Downloading a Full Upgrade via Terminal

1. Sometimes we want to download the full installer file to create a USB drive for installation or to deploy it to other computers in the organization.
2. Open the **Terminal** application.
3. Run the following command to fetch the latest installer file:
   ```bash
   softwareupdate --fetch-full-installer
   ```
   *(If you want to download a specific version, you can add `--full-installer-version 26.0`)*

4. This action will download the installer file to your Applications folder as a file named `Install macOS [Name].app`. (You can stop the operation now using `Control + C` if you do not need the file).

---

## Exercise 2: Simulating Data Migration (Migration Assistant)

**Scenario:**
The user has received a new Mac, and we need to correctly transfer their data from the old Mac or a Time Machine drive, without overwriting existing local accounts or creating duplicates on the new system.

### Step A: Preparation and Tool Activation

1. Open **Migration Assistant** from the `/Applications/Utilities` folder (or simply search in Spotlight).
2. The tool will request the Admin password and close all other running applications in the background. Confirm this.
3. On the first screen, select the option **From a Mac, Time Machine backup, or startup disk** and click **Continue**.
4. *In this simulation:* If a Time Machine drive is connected to your computer, select it. If not, simply navigate through the screens and familiarize yourself with the selection options (without performing an actual migration).

### Step B: Selecting Data for Migration

1. When the tool identifies the source, it will calculate the data volume and display a list of items.
2. **Enterprise Best Practice:**
   * Expand the list of accounts using the small arrow next to the Users category.
   * Ensure you select and transfer **only** the relevant user account (Standard / Admin). Do not transfer old IT team Admin accounts if the MDM already manages them on the new Mac.
   * Examine the categories: `Applications`, `Other Files & Folders`, `System & Network`.
   * **Strong Enterprise Recommendation:** It is recommended to uncheck the `System & Network` category to prevent the transfer of old network settings or remnants from the previous Configuration Profile that might conflict. Additionally, do not transfer `Applications` to avoid transferring unsupported Kexts (especially when migrating from Intel to Apple Silicon).

### Step C: Managing Account Conflicts

1. If a local account with the same username as the one you are trying to import already exists on the new Mac, a warning will appear.
2. You will be presented with action options:
   * **Replace:** Deleting the existing account on the new Mac and overwriting it.
   * **Keep both user accounts:** The system will rename the imported account to create a distinction.
3. *In this simulation:* Select Cancel, and exit Migration Assistant gracefully.

---

## Exercise 3: Investigating the Rapid Security Response (RSR) Mechanism

**Scenario:**
As IT administrators, you will want to verify which RSR version is currently installed and how to roll it back in case of a compatibility issue with enterprise software.

1. Open **System Settings** and navigate to **General** -> **About**.
2. Check the macOS version. If a Rapid Security Response (RSR) update has been installed, you will see a letter in parentheses (e.g., `(a)`) next to the version number (such as `macOS 26.3.1 (a)`).
3. If an RSR is installed, click the information button (the **i** symbol) next to the macOS version.
4. In the screen that opens, you will find the **Remove** button, which is designed to remove that specific security update (disabling the Cryptex load on the next boot) and revert to the base system version.

<!-- src_hash: c5c5fcdb112ee1b738ab4f13b4399293b8592eb72f5007ed252fabf88ba5d25a -->
