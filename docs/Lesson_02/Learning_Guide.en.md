# Lesson 02: User Management and Data Security
**Student Learning Guide**

## Lesson Objectives

* **Users and Folders** - Local account types, Home Folder hierarchy, and the Shared folder.
* **Secrets Management** - Password evolution, Keychain, and the modern Passwords app in macOS Sequoia and Tahoe.
* **The Passwordless Era and Security** - Passkeys and file permissions (POSIX/ACL), TCC, and SIP mechanisms.
* **Enterprise Seasoning** - Working with Managed Apple Accounts (MAID) and integrating Platform SSO for seamless enterprise login.

## Overview

<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/4a1fe7a9-1ab4-4499-aada-0e9c8b5d8aec/"></iframe></div>

## Terminology (Key Concepts)

* **Administrator:** The system administrator, with global permissions to change settings and install software for everyone.
* **Standard User:** A regular user, limited to their home folder (`~`) and personal space.
* **Guest User:** A guest user whose entire folder contents are deleted upon logging out.
* **Sharing Only:** A user with no home folder intended solely for network share authentication.
* **Home Folder (`/Users/username`):** The user's isolated home directory.
* **Shared Folder (`/Users/Shared`):** A public demilitarized zone. Protected by a Sticky Bit.
* **Sticky Bit:** A permission flag preventing users from deleting files belonging to other users in the same directory.
* **Keychain:** The macOS keychain infrastructure, consisting of the Login Keychain and System Keychain.
* **Passwords app:** The central app (from macOS 15, enhanced in macOS 26 Tahoe) for managing passwords, Passkeys, and 2FA codes.
* **Passkey:** A passwordless authentication standard (FIDO2) using a cryptographic key pair in the Secure Enclave.
* **POSIX:** The standard UNIX permissions model (Owner, Group, Everyone).
* **ACL (Access Control List):** An advanced, granular permissions layer added on top of POSIX.
* **TCC (Transparency, Consent, and Control):** A privacy mechanism blocking app access to personal files and hardware (like the camera) unless explicitly approved by the user.
* **SIP (System Integrity Protection):** Protects core system files from modifications, even by the root user.
* **Managed Apple Account (MAID):** An Apple Account owned by the organization.
* **Platform SSO:** macOS infrastructure enabling Mac login directly against a cloud identity provider (IdP) like Entra ID or Okta.
* **Federated Authentication:** A state where entering an enterprise email redirects the user to authenticate against the company's server without requiring an Apple password.

## Useful CLI Commands
| Command | Description |
|---|---|
| `dscl . -list /Users` | Display a list of all system (local) users |
| `dscl . -read /Users/username` | Read extensive attributes of a specific user |
| `ls -la /Users` | View file permissions, including identifying the Sticky Bit (`t`) |
| `ls -le /path` | View file permissions, including displaying ACL records (`+`) |
| `security list-keychains` | Display a list of currently active keychains |
| `log show --predicate 'subsystem == "com.apple.PlatformSSO"'` | Search logs for SSO server connection errors |

## Recommended Reading and Links

* [Intro to user account types](https://support.apple.com/guide/platform-support/sup72e8c67c3/web) - Official Apple support guide.
* [About Managed Apple Accounts](https://support.apple.com/guide/deployment/depdc4ba8d82/web) - Managing MAIDs in the enterprise.
* [Explainer: Keychain basics](https://eclecticlight.co/2022/10/15/explainer-keychain-basics/) - In-depth article about Keychain.

## Summary Video

<!-- YouTube Summary Video -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/S1n1JS-mWTM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 💡 עזרים ויזואליים להרצאה (Presentation Visuals)

> [!NOTE]
> תמונות אלו ניתנות להקרנה בכיתה בעת הסבר על הנושא, או לשילוב במצגות.

!!! tip "המחשה ויזואלית (עזר לתלמיד)"
    תמונות אלו ממחישות את הממשק או המנגנון הרלוונטי לנושא השיעור.

![Slide87_image22](../assets/images/Lesson_02/L02_LegacySlide_Slide87_image22.jpg)
![Slide87_image23](../assets/images/Lesson_02/L02_LegacySlide_Slide87_image23.jpg)
![Slide89_image24](../assets/images/Lesson_02/L02_LegacySlide_Slide89_image24.jpg)
![Slide90_image25](../assets/images/Lesson_02/L02_LegacySlide_Slide90_image25.jpg)
![Slide91_image26](../assets/images/Lesson_02/L02_LegacySlide_Slide91_image26.jpg)
![26-Tahoe-Fast-User-Lockscreen-scaled](../assets/images/Lesson_02/L02_TahoeUI_26-Tahoe-Fast-User-Lockscreen-scaled.png)
![26-Tahoe-Settings-Lock-Screen-scaled](../assets/images/Lesson_02/L02_TahoeUI_26-Tahoe-Settings-Lock-Screen-scaled.png)
![26-Tahoe-Settings-Touch-ID-scaled](../assets/images/Lesson_02/L02_TahoeUI_26-Tahoe-Settings-Touch-ID-scaled.png)
