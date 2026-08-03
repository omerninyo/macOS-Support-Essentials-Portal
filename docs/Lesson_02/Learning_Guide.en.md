# Lesson 02: User Management and Data Security
**Student Reference Guide**

## Lesson Objectives

* **Users and Directories** - Local account types, Home Folder hierarchy, and the Shared directory.
* **Secrets Management** - Evolution of passwords, Keychain, and the Passwords app from macOS Sequoia and Tahoe.
* **Passwordless Era and Security** - Passkeys, file permissions (POSIX/ACL), TCC framework, and SIP.
* **Enterprise Integration** - Working with Managed Apple Accounts (MAID) and integrating Platform SSO for seamless enterprise login.

## Overview

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/4a1fe7a9-1ab4-4499-aada-0e9c8b5d8aec/"></iframe></div>

## Key Terminology

* **Administrator:** System administrator user possessing global privileges to modify settings and install software for all users.
* **Standard User:** Regular user restricted to their home directory (`~`) and personal environment.
* **Guest User:** Guest account that deletes all contents of its directory upon logging out.
* **Sharing Only:** Account without a home directory designed exclusively for authenticating against network shares.
* **Home Folder (`/Users/username`):** The isolated home directory of the user.
* **Shared Folder (`/Users/Shared`):** Public demilitarized zone protected by a Sticky Bit.
* **Sticky Bit:** Permission flag that prevents users from deleting files belonging to other users within the same directory.
* **Keychain:** The macOS key storage infrastructure, consisting of the Login Keychain and System Keychain.
* **Passwords app:** Centralized application (introduced in macOS 15 and enhanced in macOS 26 Tahoe) for managing passwords, Passkeys, and 2FA codes.
* **Passkey:** Passwordless authentication standard (FIDO2) using a cryptographic key pair generated in the Secure Enclave.
* **POSIX:** Standard UNIX permissions model (Owner, Group, Everyone).
* **ACL (Access Control List):** Advanced, granular permission layer added on top of POSIX.
* **TCC (Transparency, Consent, and Control):** Privacy mechanism that blocks application access to personal files and hardware (such as the camera) unless explicitly approved by the user.
* **SIP (System Integrity Protection):** Protects core system files from modification, even by the root user.
* **Managed Apple Account (MAID):** Organization-owned Apple account.
* **Platform SSO:** macOS framework enabling direct authentication to a cloud Identity Provider (IdP) such as Entra ID or Okta.
* **Federated Authentication:** Configuration where entering an enterprise email redirects the user to authenticate against company identity servers without requiring an Apple password.

## Useful Commands (CLI Commands)
| Command | Description |
|---|---|
| `dscl . -list /Users` | Display list of all system users (local) |
| `dscl . -read /Users/username` | Read detailed properties of a specific user |
| `ls -la /Users` | Display file permissions, including Sticky Bit identification (`t`) |
| `ls -le /path` | Display file permissions, including ACL entry visualization (`+`) |
| `security list-keychains` | Display list of currently active keychains |
| `log show --predicate 'subsystem == "com.apple.PlatformSSO"'` | Query logs for SSO server authentication errors |

## Recommended Reading and References

* [Intro to user account types](https://support.apple.com/guide/platform-support/sup72e8c67c3/web) - Official Apple support guide.
* [About Managed Apple Accounts](https://support.apple.com/guide/deployment/depdc4ba8d82/web) - Managing MAID in the enterprise.
* [Explainer: Keychain basics](https://eclecticlight.co/2022/10/15/explainer-keychain-basics/) - In-depth article on Keychain basics.

## Summary Video

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/S1n1JS-mWTM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 💡 Presentation Visuals

> [!NOTE]
> These images can be projected in class during topic explanations or integrated into presentation decks.

!!! tip "Visual Aid (Student Reference)"
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

<!-- src_hash: 1d0afa939a651c79afc878f8fef622bf6b8187fd5cb8b2b739b3d2963cd7ee35 -->
