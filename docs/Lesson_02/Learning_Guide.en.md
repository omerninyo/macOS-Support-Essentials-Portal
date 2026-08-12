# Lesson 02: User Management & Data Security
**Learning Guide (Student Reference)**

---

## Lesson Objectives

* **Users & Directories** - Local account types, Home Folder hierarchy, and the Shared folder.
* **Secrets Management** - The evolution of passwords, Keychain infrastructure, and the Passwords app from macOS Sequoia through Tahoe.
* **The Passwordless Era & Security Architecture** - Passkeys, POSIX/ACL file permissions, TCC frameworks, and System Integrity Protection (SIP).
* **Enterprise Spice** - Deploying Managed Apple Accounts (MAIDs) and integrating Platform SSO for seamless organizational authentication.

---

## 🎧 Audio Summary — Pre/Post Lesson

<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/4a1fe7a9-1ab4-4499-aada-0e9c8b5d8aec/"></iframe></div>

---

## Terminology

* **Administrator:** The system administrator account, possessing global permissions to modify system-wide settings and install software for all users.
* **Standard User:** A restricted account, sandboxed primarily to its designated Home Folder (`~`) and personal workspace.
* **Guest User:** A temporary account that automatically purges its entire Home Folder upon logout.
* **Sharing Only:** A lightweight, headless account with no Home Folder, utilized strictly for authenticating against network file shares.
* **Home Folder (`/Users/username`):** The isolated, primary storage directory for an individual user.
* **Shared Folder (`/Users/Shared`):** A public demilitarized zone (DMZ) for local file exchange, protected by the Sticky Bit.
* **Sticky Bit:** A permission flag preventing users from deleting files owned by other users within a shared directory.
* **Keychain:** The native macOS credential management infrastructure, primarily divided into the user's Login Keychain and the global System Keychain.
* **Passwords App:** The centralized macOS 15+ (and enhanced in macOS 26 Tahoe) GUI application for managing passwords, Passkeys, and 2FA tokens.
* **Passkey:** A modern, passwordless authentication standard (FIDO2) utilizing cryptographic key pairs securely stored within the Secure Enclave.

> [!TIP]
> **Enterprise Passkeys Framework (5-Stage Model)**
> Transitioning an organization from legacy passwords to secure passwordless authentication (Passkeys) requires a structured approach:
> 1. **Assessment & Planning:** Audit existing IT infrastructure and security requirements.
> 2. **Solution Selection:** Choose an Identity Provider (IdP) or password manager with full FIDO2 support.
> 3. **Testing:** Conduct a controlled deployment with the IT team.
> 4. **Full Deployment:** Push Passkey policies globally via Mobile Device Management (MDM).
> 5. **Monitoring & Optimization:** Review authentication logs and systematically deprecate legacy passwords.

* **POSIX:** The standard UNIX permission model (Owner, Group, Everyone).
* **ACL (Access Control List):** An advanced, granular permission layer overlaid on top of POSIX.
* **TCC (Transparency, Consent, and Control):** The macOS privacy framework that blocks application access to personal data and hardware (e.g., Camera, Microphone) without explicit user consent.
* **SIP (System Integrity Protection):** A kernel-level defense mechanism locking down core system files and directories, preventing modification even by the `root` user.
* **Managed Apple Account (MAID):** An Apple Account owned, created, and managed by the organization.
* **Platform SSO:** A macOS framework enabling seamless desktop login directly against cloud Identity Providers (IdPs) like Entra ID or Okta.
* **Federated Authentication:** A workflow where entering a corporate email seamlessly redirects the user to their organizational IdP for authentication, eliminating the need for a separate Apple password.

---

## CLI Commands

> [!NOTE]
> **Terminal Usage**
> The CLI commands listed here are for demonstration purposes. There is no need to memorize their syntax at this stage! You can simply copy-paste them during the lab to observe the output. We will dive deep into Terminal workflows in Lesson 08, and explore the unified logging system in Lesson 16. For now, treat the Terminal purely as a quick diagnostic tool.

| Command | Description |
|---|---|
| `dscl . -list /Users` | List all local user accounts on the system |
| `dscl . -read /Users/username` | Read extended properties and attributes of a specific user |
| `ls -la /Users` | Display file permissions, including identifying the Sticky Bit (`t`) |
| `ls -le /path` | Display file permissions, including ACL records (`+`) |
| `security list-keychains` | Display the list of currently active Keychains |
| `log show --predicate 'subsystem == "com.apple.PlatformSSO"'` | Search for Platform SSO authentication errors within system logs |

---

## Recommended Reading

* [Intro to user account types](https://support.apple.com/guide/platform-support/sup72e8c67c3/web) - Official Apple Platform Support guide.
* [About Managed Apple Accounts](https://support.apple.com/guide/deployment/depdc4ba8d82/web) - Managing MAIDs in the enterprise.
* [Explainer: Keychain basics](https://eclecticlight.co/2022/10/15/explainer-keychain-basics/) - An in-depth architectural look at Keychain.

---

## 🎬 Video Summary

<!-- YouTube Video Summary -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/S1n1JS-mWTM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

## 💡 Presentation Visuals

> [!NOTE]
> These images can be projected in the classroom during explanations or integrated into presentations.

!!! tip "Visual Reference (Student Aid)"
    These screenshots illustrate the GUI or mechanisms relevant to the lesson's core concepts.

![Slide87_image22](../assets/images/Lesson_02/L02_LegacySlide_Slide87_image22.jpg)
![Slide87_image23](../assets/images/Lesson_02/L02_LegacySlide_Slide87_image23.jpg)
![Slide89_image24](../assets/images/Lesson_02/L02_LegacySlide_Slide89_image24.jpg)
![Slide90_image25](../assets/images/Lesson_02/L02_LegacySlide_Slide90_image25.jpg)
![Slide91_image26](../assets/images/Lesson_02/L02_LegacySlide_Slide91_image26.jpg)
![26-Tahoe-Fast-User-Lockscreen-scaled](../assets/images/Lesson_02/L02_TahoeUI_26-Tahoe-Fast-User-Lockscreen-scaled.png)
![26-Tahoe-Settings-Lock-Screen-scaled](../assets/images/Lesson_02/L02_TahoeUI_26-Tahoe-Settings-Lock-Screen-scaled.png)
![26-Tahoe-Settings-Touch-ID-scaled](../assets/images/Lesson_02/L02_TahoeUI_26-Tahoe-Settings-Touch-ID-scaled.png)
![Slide96_image104](../assets/images/Lesson_02/L02_LegacySlide_Slide96_image104.png)
![Slide96_image105](../assets/images/Lesson_02/L02_LegacySlide_Slide96_image105.png)
![Slide97_image106](../assets/images/Lesson_02/L02_LegacySlide_Slide97_image106.png)
![Slide97_image107](../assets/images/Lesson_02/L02_LegacySlide_Slide97_image107.png)
