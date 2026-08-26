# Lesson 12: Software Updates & Upgrades
**Practical Hands-On Lab**

## Objective
Master software updates and upgrades via GUI, inspect Background Security Improvements (BSI) and Cryptex architecture, verify Bootstrap Token status on Apple Silicon, and explore Migration Assistant workflows in managed enterprise environments.

---

## Exercise 1: Managing Software Updates in GUI

> **Learning Goal:** Distinguish between minor Updates and major Upgrades in GUI, configure automatic updates and BSI, and understand why macOS requires substantial snapshot overhead space.

**Scenario:** Verify that the system is up to date, identify where point updates vs. major upgrades appear, and ensure Background Security Improvements are enabled.

### Step A: Check for Available Updates

1. Open **System Settings**.
2. Navigate to **General > Software Update**.
3. Allow the system to query Apple's servers (Pallas).
4. Observe the interface separation:
   * **Minor Updates:** Displayed in the primary update card (e.g., 26.2 to 26.3).
   * **Major Upgrades:** Displayed in a separate bottom section to prevent accidental upgrades.

### Step B: Configure Automatic Updates & BSI

1. Click the info icon (s) next to **Automatic Updates**.
2. Ensure **Install Security Responses and system files** is turned ON.
3. Click **Done**.

---

## Exercise 2: Inspecting Cryptex & BSI Rollback

> **Learning Goal:** Identify live Cryptex security overlays and understand the instant rollback mechanism if a security patch introduces enterprise app incompatibilities.

**Scenario:** An internal business application crashes following a silent security patch. Learn how to verify Cryptex state and trigger immediate rollback.

1. Open **System Settings > General > About**.
2. Click the info icon next to the macOS version string.
3. View the exact build and active security overlay details.
4. If an active overlay is present, clicking **Remove & Restart** instructs the bootloader to omit mounting the Cryptex on the next boot, reverting immediately to the clean baseline SSV.

---

## Exercise 3: Simulating Migration Assistant & Enterprise Pitfalls

> **Learning Goal:** Understand Migration Assistant mechanics, high-risk data categories, and why Cloud-Native Ephemeral device workflows are preferred in Zero-Trust environments.

**Scenario:** A user receives a new Mac. Learn how to avoid UID collisions and dirty migrations when transferring user profiles.

### Step A: Launch and Inspect Options

1. Launch **Migration Assistant** from `/Applications/Utilities`.
2. Authenticate with admin credentials.
3. Select **From a Mac, Time Machine backup, or startup disk** and click **Continue**.
4. *(Do not execute full migration during this simulation).*

### Step B: Enterprise Best Practices

1. When sources are detected, 4 categories appear: `Users`, `Applications`, `Other Files & Folders`, `System & Network`.
2. **Critical Rules:**
   * Select **only** the designated user account.
   * Deselect **System & Network** (prevents network and MDM profile conflicts).
   * Deselect **Applications** (prevents copying obsolete Intel Kexts and incompatible daemons).
3. **UID Collision:** If an account with the same short name exists on the target Mac, selecting Keep Both appends numbers and breaks paths, while Replace wipes data.
4. Exit the assistant cleanly (**Quit**).

---

## Exercise 4: Verifying Bootstrap Token & Terminal CLI Tools

> **Learning Goal:** Verify Bootstrap Token escrow status for silent MDM updates on Apple Silicon, scan updates via Terminal, and simulate full installer downloads.

**Scenario:** As an IT administrator, verify that the Mac can accept silent DDM update enforcements without user password prompts.

### Step A: Verify Bootstrap Token Status

1. Open **Terminal**.
2. Run the following command:
   ```bash
   sudo profiles status -type bootstraptoken
   ```
3. **Verify Output:** Confirm that `Bootstrap token is escrowed to server: YES` is displayed.

### Step B: Scan and Query Updates in CLI

1. Scan for available updates:
   ```bash
   softwareupdate -l
   ```
2. Simulate full installer download:
   ```bash
   softwareupdate --fetch-full-installer
   ```
   *(Press `Control + C` at any time to cancel the large download).*
