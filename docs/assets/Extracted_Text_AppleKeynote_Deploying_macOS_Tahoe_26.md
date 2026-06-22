# Extracted Text: AppleKeynote_Deploying_macOS_Tahoe_26

## Slide 1
- Presenter Name
- Title
- Date
- Deploying macOS Tahoe

## Slide 2

## Slide 3

## Slide 4
- Powerful ways to get more done

## Slide 5
- Spotlight experience
- Search enhancements
- System and app actions
- Quick Keys

## Slide 6
- Intelligent actions in Shortcuts

## Slide 7
- iPhone Continuity
- Phone app
- Live Translation
- Live Activities

## Slide 8
- Apple School & Business Manager
- Deployment options
- Platform changes
- Upgrading to macOS Tahoe 26
- Summary
- Resources

## Slide 9
- Apple School & Business Manager

## Slide 10
- Integrates with device management solutions
- Enables zero-touch deployment
- Volume purchasing of Apps and Books
- Create Managed Apple Accounts
- Apple Push Notification service
- Apple School & Business Manager

## Slide 11
- Managed Apple Accounts

## Slide 12
- Managed Apple Accounts
- Connect to your identity provider
- Sign in with federated authentication
- Verify your domain for accounts
- Manage access to Apple services
- Limit sign-in to Managed Apple Accounts only

## Slide 13

## Slide 14
- Download list of users for account transfer

## Slide 15
- Restrict personal Apple Accounts on managed devices

## Slide 16
- Prevent personal Apple Account sign-in
- Download list of users for account transfer
- Access to App Notarisation service
- New Managed Apple Account features

## Slide 17
- Device inventory
- and assignments

## Slide 18
- IMEI and EID
- Released devices information
- Wi-Fi and Bluetooth MAC address
- AppleCare coverage details
- Device inventory data

## Slide 19
- New inventory
- data
- AppleCare
- coverage information

## Slide 20
- Manually add devices to your organisation

## Slide 21
- Apple School and Business Manager APIs

## Slide 22
- Apple Business Manager access
- Automate device management tasks
- Administrators can create API accounts
- List servers, devices, inventory and more
- Assign to device management services
- Apple School and Business Manager API

## Slide 23
- Supported API endpoints
- Name
- Endpoint
- List of device management services
- GET /v1/mdmServers
- List all devices
- GET /v1/orgDevices
- Get device information
- GET /v1/orgDevices/{id}
- Get device management service information for a device
- GET /v1/orgDevices/{id}/relationships/assignedServer
- Get all devices assigned to device management service
- GET /v1/mdmServers/{id}/relationships/devices
- Assign or unassign devices from device management service
- POST /v1/orgDeviceActivities
- Get batch action activity status
- GET /v1/orgDeviceActivities/{id}

## Slide 24
- Generate and download API key

## Slide 25
- Generate and download API key

## Slide 26
- Generate and download API key
- Generate Private Key

## Slide 27
- Manage API keys

## Slide 28
- Manage API keys

## Slide 29
- Apple School & Business Manager
- Authorisation service
- Private key
- Public key
- Generate client assertion
- Authenticate & obtain access token
- Apple School and Business Manager API

## Slide 30
- Device management migration

## Slide 31
- Seamlessly migrate between services
- No device erase required
- Notifications guides users
- Admins can set enrolment deadline
- Requires macOS, iOS, iPadOS 26 or later
- Device management migration

## Slide 32
- Add new device management service

## Slide 33
- Transfer app licenses to new management service

## Slide 34
- Set new management service
- Enforce by deadline

## Slide 35
- Filter by eligibility

## Slide 36
- Migration status

## Slide 37
- User notification

## Slide 38
- Managed apps that are running

## Slide 39
- Full screen enforcement after deadline

## Slide 40

## Slide 41

## Slide 42
- Old configurations and apps are removed. New ones are installed.

## Slide 43
- Has Managed User – Signed in
- Has Managed User – Not signed in
- No Managed User
- macOS Managed Users

## Slide 44
- Personal Recovery Key (PRK) stays valid
- Install
- FDERecoveryKeyEscrow
- payload to rotate PRK
- macOS FileVault

## Slide 45
- Build your best new device enrolment
- Establish a device provisioning network
- Provide matching configurations
- Use
- await_device_configured = true
- Rotate Personal Recovery Key
- Preserve apps
- Admin best practices

## Slide 46
- Deployment options

## Slide 47
- Organisation-owned devices

## Slide 48
- Automated Device Enrolment
- Device
- Enrolment

## Slide 49
- Designed for new or refreshed devices
- Automatically enrol into management
- Customise setup for users:
- Skip setup screens
- Customise enrolment
- Require a minimum version of macOS
- Enforce FileVault in Setup Assistant
- Register with Platform SSO
- Automated Device Enrolment

## Slide 50

## Slide 51
- Automatically enrolled in MDM

## Slide 52
- Enrolment customisation with IdP login

## Slide 53
- Security key support

## Slide 54
- Platform SSO registration in
- Setup Assistant

## Slide 55
- Managed Apple Account federation

## Slide 56
- User name and profile photo provided from IdP

## Slide 57
- Enforce software updates in
- Setup Assistant

## Slide 58
- Enforce software updates in
- Setup Assistant

## Slide 59

## Slide 60
- Enforce FileVault in
- Setup Assistant

## Slide 61

## Slide 62
- Zero trust with
- Managed Device Attestation

## Slide 63
- Automated Device Enrolment
- Device
- Enrolment

## Slide 64
- Designed for devices already in use
- Manual enrolment into management
- Account-driven enrolment process:
- Sign in with Managed Apple Account
- Personal and work data separated
- Device Enrolment

## Slide 65
- Account-driven Device Enrolment

## Slide 66
- Sign in with Managed Apple Account

## Slide 67
- Sign in with Managed Apple Account

## Slide 68
- Federated authentication

## Slide 69
- Federated authentication

## Slide 70

## Slide 71
- Transparent management details for users

## Slide 72
- Personal Apple Account
- Managed Apple Account signed in
- Management details

## Slide 73
- Management and security frameworks

## Slide 74
- Device management capabilities
- Configure email accounts
- Organise apps in the Dock
- Install apps
- Remote wipe
- Restrict settings
- Manage preferences
- Enforce FileVault
- Configure enterprise Wi-Fi and VPN
- Enforce passcode
- Hide system apps
- Restrict data flow
- Apply restrictions
- Manage local user account

## Slide 75
- Device management capabilities
- Configurations
- Commands
- Device Status
- Restrictions

## Slide 76
- Apps and Books deployment
- Purchase Apps and
- Books in volume
- Assign licenses
- with your management service
- Deploy directly
- to devices

## Slide 77
- macOS Security Compliance Project
- pages.nist.gov/macos_security/
- NIST 800-53 Rev 5
- NIST 800-171 Rev 2
- CNSSI 1253
- DISA STIG
- CIS Level 1
- CIS Level 2

## Slide 78
- Endpoint Security for Mac
- Monitor authentication activity
- Monitor external drive mount activity
- Monitor XProtect and Gatekeeper notifications
- Monitor login and logout activity
- Monitor process executions and forking

## Slide 79
- MDM and Endpoint Security solutions
- MDM solutions
- Endpoint Security solutions

## Slide 80
- Use Face ID to sign in to apps and websites
- Sign in once in
- Mac login window
- Single sign-on integrations

## Slide 81
- Platform SSO for
- 1:1 deployments

## Slide 82
- Enables single sign-on at Mac login window
- Touch ID and Unlock with Apple Watch
- Automatically sign in to apps and websites
- Authentication methods:
- Password synchronisation
- Secure Enclave–backed key
- Smart card
- Platform SSO

## Slide 83
- Platform SSO
- Single sign-on
- extension
- Identity
- provider
- Native app
- and Safari

## Slide 84
- Platform SSO registration in
- Setup Assistant
- for new devices

## Slide 85
- Platform SSO registration for devices in use

## Slide 86
- Use Touch ID,
- use Unlock with
- Apple Watch or enter password

## Slide 87
- Automatically signed in to apps and websites

## Slide 88
- Platform SSO in System Settings

## Slide 89
- Monitor for malicious activity
- with Endpoint Security
- Set baselines and manage security with MDM
- Integrate with your identity provider for single sign-on

## Slide 90
- Shared organisation owned devices

## Slide 91
- Shared Mac identity options
- Local user accounts
- Third-party login tools
- Platform SSO
- AD binding

## Slide 92
- Platform SSO for Shared Mac

## Slide 93
- Designed for Shared Mac deployments
- Log in to Mac with account credentials from IdP
- Sign in to apps and websites
- User data is erased after logout
- Auto Advance streamlines setup process
- Authenticated Guest Mode

## Slide 94
- Authenticated Guest Mode

## Slide 95
- User logs in with
- IdP credentials

## Slide 96
- Automatically signed in to apps and websites

## Slide 97
- Files are deleted after logout

## Slide 98
- Ready for new user

## Slide 99
- Option for faster login
- Deletes only Documents, Desktop, Downloads and a few other areas
- All Guest Sessions erased every 8 hours
- Ideal for high-frequency and short sessions
- Authenticated Guest Mode — Quick Login

## Slide 100

## Slide 101
- Works with Authenticated Guest Mode
- NFC Access Key in Apple Wallet
- Express mode support
- Requires an external NFC reader for Mac
- Tap to Login to Mac

## Slide 102
- Tap to Login to Mac

## Slide 103
- Identity Provider
- Tap to Login to Mac
- Authenticate
- App

## Slide 104
- Apple Access Platform
- App
- Wallet Pass
- 6d646d5650506465704142
- 4d61736d4144456d64614
- 4444d6d6166457253534f
- Tap to Login to Mac

## Slide 105
- Tap to Login to Mac
- Wallet Pass
- 6d646d5650506465704142
- 4d61736d4144456d64614
- 4444d6d6166457253534f
- Identity Provider

## Slide 106

## Slide 107

## Slide 108
- User-owned devices

## Slide 109
- Designed for personal devices
- Curated BYOD management capabilities
- Account-driven enrolment process:
- Sign in with Managed Apple Account
- Personal and work data separated
- Enrolment SSO support on iOS and iPadOS
- User Enrolment

## Slide 110
- User Enrolment
- Transparent management details for users

## Slide 111
- Curated BYOD management capabilities
- Configure accounts
- Access personal information
- Configure Per-app VPN
- Access inventory of personal apps
- Install and configure apps
- Remove any personal data
- Require a passcode on iPhone or iPad
- Collect any logs on the device
- Enforce certain restrictions
- Take over personal apps
- Access inventory of work apps
- Require a complex iPhone and iPad passcode
- Remove work data only
- Remotely wipe the entire device
- Disable ChatGPT Integration
- Access device location

## Slide 112
- Platform changes

## Slide 113
- App management
- Safari extensions
- Apple Intelligence
- Management updates

## Slide 114
- Manage app update behaviour per app
- Enforce or disable automatic updates
- Pin specific app versions
- Monitor update progress with status channel
- App update management

## Slide 115
- Manage App Store apps and package installers
- Declarative features of app management
- Required or optional install
- Status channel
- ManagedAppDistribution framework
- macOS app management

## Slide 116
- New API to configure managed apps
- Supports passwords, certificates and identities
- Streamlines user authentication
- Configuring managed apps

## Slide 117
- App management
- Safari extensions
- Apple Intelligence
- Management updates

## Slide 118
- New privacy-preserving filtering API
- Filters systemwide URL requests
- Apple Private Information Retrieval (PIR)
- HTTP Relay hosted by Apple for privacy
- Content filtering

## Slide 119
- App management
- Safari extensions
- Apple Intelligence
- Management updates

## Slide 120

## Slide 121
- Manage Safari extensions
- Manage bookmarks
- Configure home page
- Consolidated Safari configuration
- Safari management

## Slide 122
- Safari management
- Feature Name
- Key
- Platform
- Whether users can clear the Safari history
- AllowHistoryClearing
- iOS, iPadOS, macOS, visionOS
- Whether users can use Private Browsing
- AllowPrivateBrowsing
- iOS, iPadOS, macOS, visionOS
- Summarisation of content in Safari
- AllowSummary
- iOS, iPadOS, macOS, visionOS
- JavaScript execution
- AllowJavaScript
- iOS, iPadOS
- Prevent pop-ups
- AllowPopups
- iOS, iPadOS
- Cookie handling
- AcceptCookies
- iOS, iPadOS
- Fraud warnings
- AllowDisablingFraudWarning
- iOS, iPadOS

## Slide 123
- App management
- Safari extensions
- Apple Intelligence
- Management updates

## Slide 124

## Slide 125
- Your data is never stored
- Used only for your requests
- Verifiable privacy promise
- Private Cloud Compute

## Slide 126
- Apple Intelligence management
- Feature Name
- Restriction
- Siri
- allowAssistant
- Writing Tools
- allowWritingTools
- Safari Summary
- allowSafariSummary
- Mail Summary
- allowMailSummary
- Mail Smart Replies
- allowMailSmartReplies
- Notes Transcription Summary
- allowNotesTranscriptionSummary
- Image Playground
- allowImagePlayground
- Image Wand
- allowImageWand
- Genmoji
- allowGenmoji
- Visual Intelligence Summary
- allowVisualIntelligenceSummary
- Apple Intelligence Report
- allowAppleIntelligenceReport
- ChatGPT
- allowExternalIntelligenceIntegrations
- allowExternalIntelligenceIntegrationsSignIn
- allowedExternalIntelligenceWorkspaceIDs

## Slide 127
- Private Cloud Compute security resources
- security.apple.com

## Slide 128
- Upgrading to macOS Tahoe

## Slide 129
- https://support.apple.com/100100
- “Keeping your software up to date is one of the most important things you can do to maintain your Apple product’s security.”

## Slide 130
- New declarative model for updates
- Manage deferrals and notifications
- Enforce updates by specific date and time
- Older software update management
- is deprecated
- Managed software updates

## Slide 131
- Deferring software updates

## Slide 132
- Test software updates

## Slide 133
- Beta
- Release
- Admin testing

## Slide 134
- Beta
- Release
- Ready to deploy
- Admin testing

## Slide 135
- Beta
- Release
- Ready to deploy
- Admin testing
- Admin deferral

## Slide 136
- 90-day deferral window
- Separate major, minor and non-OS deferrals
- Deferred updates are hidden in Settings
- Deferral does not limit admin installation
- Defer beta updates
- Defer software updates

## Slide 137
- Updates deferred up to 90 days

## Slide 138
- Enforcing software updates

## Slide 139
- Beta
- Release
- Ready to deploy
- Admin testing
- Admin deferral
- Admin install

## Slide 140
- Enforce updates by specific date and time
- Major or minor updates
- Notify users when updates will occur
- Leverages the bootstrap token
- Installation status reporting
- Install software updates

## Slide 141
- Managed Update
- An update to macOS is past due. You can install it now or it will be installed automatically within the next hour.

## Slide 142
- Software update enforce notification experience
- 30 days
- 14 days
- 24 hours
- Settings UI
- 1 hour
- Notification
- Settings UI
- Notification
- Notification
- Update available
- Update is managed and available to “Update Now” or “Update Later” and will be installed on the scheduled date and time.

## Slide 143
- 30 days
- 14 days
- 24 hours
- Settings UI
- 1 hour
- Notification
- Settings UI
- Notification
- Notification
- Update available
- Update is managed and available to “Update Now” or “Update Later” and will be installed on the scheduled date and time.
- Software update enforce notification experience
- Daily notifications
- A managed update is available, can “Update Now” or “Update Later” and will be installed on the scheduled date and time.

## Slide 144
- 30 days
- 14 days
- 24 hours
- Settings UI
- 1 hour
- Notification
- Settings UI
- Notification
- Notification
- Update available
- Update is managed and available to “Update Now” or “Update Later” and will be installed on the scheduled date and time.
- Daily notifications
- A managed update is available, can “Update Now” or “Update Later” and will be installed on the scheduled date and time.
- Software update enforce notification experience
- Update available
- Hourly notifications
- Update is managed and available and can “Update Now” or will be installed on the scheduled date.
- A managed update is available, can “Update Now” or will be installed on the scheduled date and time.

## Slide 145
- Software update enforce notification experience
- Managed install pending
- 60m remaining
- 30m remaining
- 10m remaining
- 60s remaining
- 30 days
- 14 days
- 24 hours
- Settings UI
- 1 hour
- Notification
- Settings UI
- Notification
- Notification
- Update available
- Update is managed and available to “Update Now” or “Update Later” and will be installed on the scheduled date and time.
- Daily notifications
- A managed update is available, can “Update Now” or “Update Later” and will be installed on the scheduled date and time.
- Update available
- Hourly notifications
- Update is managed and available and can “Update Now” or will be installed on the scheduled date.
- A managed update is available, can “Update Now” or will be installed on the scheduled date and time.

## Slide 146
- Missed “specific enforcement” deadline
- Is the update prepared?
- Download
- Apply the update
- Missed “Install by” date
- Missed
- No
- Yes
- Schedule +60m from now
- Prepare

## Slide 147
- Summary

## Slide 148
- Use Automated Device Enrolment for new devices
- Set a minimum OS version
- Enforce FileVault during enrolment
- Starting your deployment
- Use Device Enrolment for existing devices
- Use User Enrolment for BYOD
- Improve the user experience with account-driven flows

## Slide 149
- Ongoing management and security
- Establish a baseline of configurations
- Set Gatekeeper policies and use restrictions as needed
- Deploy critical apps and leverage self-service portals
- Keep systems up to date by enforcing updates
- Utilise Endpoint Security solutions as needed
- Monitor for compliance and automate remediation

## Slide 150
- Go further with identity integrations
- Investigate SSO integration with your IdP
- Use Platform SSO where possible
- Explore passkey use for your organisation
- Begin adopting Managed Apple Accounts
- Connect to your IdP for federated authentication
- Choose which Apple services are allowed

## Slide 151
- Early Testing
- New feature discovery
- Test plan evaluation
- Infrastructure Readiness
- Management testing
- Networking updates
- OS Validation
- Final testing
- App readiness
- Beta Release
- Public Release

## Slide 152
- Submit feedback to Apple
- Collaborate on team-owned feedback
- File Feedback in Feedback Assistant app
- Reproduce issue, noting time
- List steps to reproduce
- Included on Beta installs
- Always available in Safari via applefeedback://
- Feedback Assistant

## Slide 153
- Establish a baseline for your Mac deployment
- Align your organisation to best practices
- Test new management features
- Available on AppleSeed for IT
- Mac Evaluation Utility

## Slide 154
- Account-driven
- enrolments
- Best for IT
- Apple Intelligence management
- Add Vision Pro to
- your organisation
- AppleCare and
- device inventory data
- Managed Apple Accounts
- Prevent unmanaged accounts
- List users for domain capture
- Tap to Login
- on Mac
- APIs for
- Apple Business Manager
- Platform SSO
- in Setup Assistant
- App update management
- Return to Service for Vision Pro
- Device management migration

## Slide 155
- Resources

## Slide 156
- AppleSeed for IT
- beta.apple.com/en-GB/for-it

## Slide 157
- Apple Platform
- Deployment
- support.apple.com/guide/deployment

## Slide 158
- Apple Platform Security
- support.apple.com/guide/security

## Slide 159
- IDC White Paper:
- The Business Imperative of Secure Endpoints
- apple.com/uk/business/enterprise/resources

## Slide 160
- Apple Security Research
- security.apple.com

## Slide 161
- Apple Platform Certifications
- support.apple.com/guide/certifications
- FIPS 140-2
- FIPS 140-3
- COMMON CRITERIA

## Slide 162
- Apple Business Manager User Guide
- support.apple.com/guide/apple-business-manager

## Slide 163
- Apple School Manager User Guide
- support.apple.com/guide/apple-school-manager

## Slide 164

