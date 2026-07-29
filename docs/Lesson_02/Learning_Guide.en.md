# Lesson 02: User Management and Data Security
**Student Reference Guide**

## Lesson Objectives

* **Users and Folders** - Local account types, Home Folder hierarchy, and the Shared folder.
* **Secrets Management** - Password evolution, Keychain, and the new Passwords app.
* **The Passwordless Era and Security** - Introduction to Passkeys and file permissions (POSIX/ACL). Lab: Creating a Passkey at https://webauthn.io/.
* **Enterprise Flavor** - Working with Managed Apple Accounts (MAID) and Platform SSO integration for transparent login in the enterprise.

## Overview

<!-- NotebookLM Podcast from Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/4a1fe7a9-1ab4-4499-aada-0e9c8b5d8aec/"></iframe></div>

## Key Concepts (Terminology)

* **Administrator:** System administrator user, with global permissions to change settings and install software for everyone.
* **Standard User:** Regular user, restricted to their home folder (`~`) and personal space.
* **Guest User:** Guest user, deletes all its folder contents upon logout.
* **Sharing Only:** A user without a home folder designed solely for authenticating to network shares.
* **Home Folder (`/Users/username`):** The user's isolated home folder. Protected with read permissions for the user only.
* **Shared Folder (`/Users/Shared`):** A public demilitarized zone. Protected using the Sticky Bit.
* **Sticky Bit:** A permission flag that prevents users from deleting files belonging to other users in the same directory (like in the Shared folder).
* **Keychain:** macOS's keychain infrastructure, consisting of the Login Keychain (personal) and System Keychain (system-wide).
* **Passwords app:** The central app in macOS 15 for managing passwords, Passkeys, and two-factor authentication.
* **Passkey:** A passwordless authentication standard (FIDO2). Works using a cryptographic key pair and is verified locally in the Secure Enclave.
* **Keychain History:** Launched in 1993, the modern API was written in 2002, and cloud synchronization (Data Protection) joined in 2013 from iOS to Mac.
* **Secure Enclave History:** The data isolation mechanism was established in 2013 for iPhones, and landed on Mac computers with the T2 chip in 2017.
* **POSIX:** The standard UNIX permissions model (Owner, Group, Everyone).
* **ACL (Access Control List):** An advanced and granular permissions layer added on top of POSIX.
* **Managed Apple Account (MAID):** An Apple account owned by the organization, restricting certain services (like purchases or iCloud Mail) and allowing authentication with the organization.
* **Platform SSO:** Infrastructure in macOS allowing login to the local computer (Login Window) directly with a cloud Identity Provider (IdP) such as Entra ID, without needing legacy Active Directory.
* **Federated Authentication:** A state where entering an organizational email redirects the user to authenticate against the company's server, without requiring a new Apple password.

## Useful Commands (CLI Commands)
| Command | Description |
|---|---|
| `dscl . -list /Users` | Display the list of all users in the system (local) |
| `dscl . -read /Users/username` | Read extensive properties of a specific user |
| `ls -la /Users` | Display file permissions, including identification of the Sticky Bit (`t`) |
| `ls -le /path` | Display file permissions, including ACL records display (marked with `+`) |
| `security list-keychains` | Display the list of currently active keychains |
| `applesso` | Diagnose the status of the Platform SSO service in the organization (in a supported environment) |
| `log show --predicate 'subsystem == "com.apple.PlatformSSO"'` | Search for login errors against SSO servers in logs |

## Recommended Reading & Enrichment Links

* **Apple Platform Support: Intro to user account types**
  [https://support.apple.com/guide/platform-support/sup72e8c67c3/web](https://support.apple.com/guide/platform-support/sup72e8c67c3/web)
* **Apple Platform Deployment: About Managed Apple Accounts**
  [https://support.apple.com/guide/deployment/depdc4ba8d82/web](https://support.apple.com/guide/deployment/depdc4ba8d82/web)
* **The Eclectic Light Company: Explainer: Keychain basics**
  [https://eclecticlight.co/2022/10/15/explainer-keychain-basics/](https://eclecticlight.co/2022/10/15/explainer-keychain-basics/)
* **The Mac Security Blog: Understanding User Accounts in macOS**
  [https://www.intego.com/mac-security-blog/understanding-user-accounts-in-macos/](https://www.intego.com/mac-security-blog/understanding-user-accounts-in-macos/)

## Recommended Links and Further Reading

* [Intro to user account types](https://support.apple.com/guide/platform-support/sup72e8c67c3/web) - Official Apple Support guide to user account types and permissions in macOS.
* [About Managed Apple Accounts](https://support.apple.com/guide/deployment/depdc4ba8d82/web) - Official Apple Deployment guide for managing Managed Apple IDs in the enterprise.
* [Explainer: Keychain basics](https://eclecticlight.co/2022/10/15/explainer-keychain-basics/) - In-depth article detailing Keychains and credential storage in macOS.
* [Understanding User Accounts in macOS](https://www.intego.com/mac-security-blog/understanding-user-accounts-in-macos/) - Comprehensive review of user account types and filesystem permissions.

## Summary Video

<!-- Summary video from YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/DDXfEIRgAxs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


![Slide87 image22](../assets/images/Lesson_02/L02_LegacySlide_Slide87_image22.jpg)
![Slide87 image23](../assets/images/Lesson_02/L02_LegacySlide_Slide87_image23.jpg)
![Slide89 image24](../assets/images/Lesson_02/L02_LegacySlide_Slide89_image24.jpg)
![Slide90 image25](../assets/images/Lesson_02/L02_LegacySlide_Slide90_image25.jpg)
![Slide91 image26](../assets/images/Lesson_02/L02_LegacySlide_Slide91_image26.jpg)
![26-Tahoe-Fast-User-Lockscreen-scaled](../assets/images/Lesson_02/L02_TahoeUI_26-Tahoe-Fast-User-Lockscreen-scaled.png)
![26-Tahoe-Settings-Lock-Screen-scaled](../assets/images/Lesson_02/L02_TahoeUI_26-Tahoe-Settings-Lock-Screen-scaled.png)
![26-Tahoe-Settings-Touch-ID-scaled](../assets/images/Lesson_02/L02_TahoeUI_26-Tahoe-Settings-Touch-ID-scaled.png)



!!! tip "Visual Illustration (Student Reference)"
    These images illustrate the interface or mechanism relevant to the lesson topic.


![Slide87 image22](../assets/images/Lesson_02/L02_LegacySlide_Slide87_image22.jpg)
![Slide87 image23](../assets/images/Lesson_02/L02_LegacySlide_Slide87_image23.jpg)
![Slide89 image24](../assets/images/Lesson_02/L02_LegacySlide_Slide89_image24.jpg)
![Slide90 image25](../assets/images/Lesson_02/L02_LegacySlide_Slide90_image25.jpg)
![Slide91 image26](../assets/images/Lesson_02/L02_LegacySlide_Slide91_image26.jpg)
![26-Tahoe-Fast-User-Lockscreen-scaled](../assets/images/Lesson_02/L02_TahoeUI_26-Tahoe-Fast-User-Lockscreen-scaled.png)
![26-Tahoe-Settings-Lock-Screen-scaled](../assets/images/Lesson_02/L02_TahoeUI_26-Tahoe-Settings-Lock-Screen-scaled.png)
![26-Tahoe-Settings-Touch-ID-scaled](../assets/images/Lesson_02/L02_TahoeUI_26-Tahoe-Settings-Touch-ID-scaled.png)

<!-- src_hash: bd6527f6d1fbd66b6e94a67dc2de7e3a7fb5e602a6e7755878180387e93ede71 -->
