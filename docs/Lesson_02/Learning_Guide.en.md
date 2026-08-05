# Lesson 02: User Management and Data Security
**Student Learning Guide**

## Lesson Objectives

* **Users and Folders** - Local account types, Home Folder hierarchy, and the Shared folder.
* **Secrets Management** - Password evolution, Keychain, and the Passwords app in macOS Sequoia and Tahoe.
* **The Passwordless Era and Security** - Passkeys, file permissions (POSIX/ACL), TCC framework, and SIP.
* **Enterprise Integration** - Working with Managed Apple Accounts (MAID) and integrating Platform SSO for seamless enterprise login.

## Overview

<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/4a1fe7a9-1ab4-4499-aada-0e9c8b5d8aec/"></iframe></div>

## Terminology (Key Concepts)

* **Administrator:** The system administrator, with global permissions to modify settings and install software for all users.
* **Standard User:** A regular user, limited to their home directory (`~`) and personal space.
* **Guest User:** A guest user whose home folder contents are completely erased upon logout.
* **Sharing Only:** A user account without a home directory, designed solely for network share authentication.
* **Home Folder (`/Users/username`):** The user's isolated home directory.
* **Shared Folder (`/Users/Shared`):** A public demilitarized zone. Protected via a Sticky Bit.
* **Sticky Bit:** A permission flag preventing users from deleting files belonging to other users within the same directory.
* **Keychain:** The macOS keychain infrastructure, consisting of the Login Keychain and System Keychain.
* **Passwords app:** The centralized application (introduced in macOS 15 and enhanced in macOS 26 Tahoe) for managing passwords, Passkeys, and 2FA codes.
* **Passkey:** A passwordless authentication standard (FIDO2) utilizing a cryptographic key pair generated within the Secure Enclave.

!!! info "5-Stage Enterprise Passkeys Deployment Model (Enterprise Passkeys Framework)"
    When an organization transitions from traditional passwords to secure passwordless authentication (Passkeys), deployment follows 5 structured stages:
    
    1. **Assessment & Planning:** Mapping IT systems, organizational security, and compliance requirements.
    2. **Solution Selection:** Selecting a password manager / Identity Provider (IdP) supporting FIDO2/WebAuthn standards.
    3. **Pilot & Testing:** Controlled trial with a selected group of IT staff and end users.
    4. **Full Deployment:** Expanding deployment to all enterprise employees and enforcing policies via MDM.
    5. **Monitoring & Optimization:** Auditing logs, phasing out text passwords, and reducing phishing incidents.

* **POSIX:** The standard UNIX permissions model (Owner, Group, Everyone).
* **ACL (Access Control List):** An advanced, granular permissions layer layered on top of POSIX.
* **TCC (Transparency, Consent, and Control):** A privacy framework that blocks application access to personal files and hardware peripherals (such as the camera) unless explicitly approved by the user.
* **SIP (System Integrity Protection):** Safeguards system core files against modifications, even by the root user.
* **Managed Apple Account (MAID):** An organizationally owned Apple Account.
* **Platform SSO:** A macOS infrastructure framework enabling Mac login authentication directly against a cloud Identity Provider (IdP) such as Entra ID or Okta.
* **Federated Authentication:** A configuration where entering an enterprise email redirects the user to authenticate against the company's identity server, bypassing the requirement for a separate Apple password.

## Useful CLI Commands
| Command | Description |
|---|---|
| `dscl . -list /Users` | Display a list of all local system users |
| `dscl . -read /Users/username` | Inspect detailed attributes of a specific user account |
| `ls -la /Users` | Display file permissions, including identifying the Sticky Bit (`t`) |
| `ls -le /path` | Display file permissions, including ACL entries (`+`) |
| `security list-keychains` | Display the list of currently active keychains |
| `log show --predicate 'subsystem == "com.apple.PlatformSSO"'` | Query system logs for Platform SSO authentication errors |

## Recommended Reading and Links

* [Intro to user account types](https://support.apple.com/guide/platform-support/sup72e8c67c3/web) - Official Apple Support guide.
* [About Managed Apple Accounts](https://support.apple.com/guide/deployment/depdc4ba8d82/web) - Enterprise MAID management.
* [Explainer: Keychain basics](https://eclecticlight.co/2022/10/15/explainer-keychain-basics/) - In-depth article on Keychain architecture.

## Summary Video

<!-- YouTube Summary Video -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/S1n1JS-mWTM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 💡 Presentation Visuals

> [!NOTE]
> These images can be projected in class during lecture discussions or incorporated into presentation decks.

!!! tip "Visual Demonstration (Student Reference)"
    These images illustrate the interface or mechanism relevant to the lesson topic.

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

<!-- src_hash: 4a9f8712568197e9f35b1cbd8c846c374280b4d19ae8cf5e165c68c33999af5a -->
