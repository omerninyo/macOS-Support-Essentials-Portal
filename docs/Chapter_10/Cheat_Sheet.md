# סיכום שיעור: שיתוף קבצים ושירותי רשת (Chapter 10)

## 1. נושאי השיעור

*   **1.** **חיבור לשרתים:** שימוש בפרוטוקול SMB לגישה לתיקיות רשת.
*   **2.** **שיתוף מקומי:** העברת מידע מהירה עם AirDrop, Screen Sharing ו-Universal Control.
*   **3.** **שכפול מהיר (Mac Sharing Mode):** ניהול העברות נתונים במצב שיתוף דיסק.
*   **4.** **תיבול ארגוני:** התממשקות ל-Single Sign-On ליצירת חיבור אוטומטי לשרתים.

## 2. פרוטוקול SMB (Server Message Block)
- **SMB - Server Message Block:** הפרוטוקול העיקרי והסטנדרטי כיום ב-macOS לשיתוף קבצים ברשת (החליף את AFP הישן).
- **SMB 3.x:** הגרסה המודרנית המציעה הצפנה מקצה לקצה ותמיכה טובה יותר בביצועים וברשתות לא יציבות.

### פקודות SMB (smbutil)
- `smbutil statshares -a`: מציג את כל חיבורי ה-SMB הפעילים כרגע ואת המאפיינים שלהם (כולל גרסת פרוטוקול SMB ורמת ההצפנה).
- `smbutil lookup <hostname>`: ביצוע שאילתה לפתרון שם (Name Resolution) לכתובת IP בסביבת NetBIOS/SMB.
- `smbutil view //user@server`: מציג את רשימת תיקיות השיתוף הזמינות בשרת ספציפי עבור המשתמש.

## 3. שירותי שיתוף (Sharing Services)
- **File Sharing:** מאפשר גישה מרחוק לקבצים על המק דרך פרוטוקול SMB.
- **Screen Sharing:** שיתוף מסך למשתמשים אחרים או גישה מרחוק, מבוסס על שדרוג של פרוטוקול VNC.
- **Mac Sharing Mode:** (במחשבי Apple Silicon) מאפשר לחבר מק אחד לאחר בכבל נתונים (USB/Thunderbolt) ולהתייחס אליו כאל כונן חיצוני ברשת מקומית וירטואלית (מחליף את ה-Target Disk Mode ההיסטורי).

### ניהול שיתוף בשורת הפקודה (sharing)
- `sharing -l`: מציג את כל תיקיות השיתוף שמוגדרות במחשב כרגע (Share Points).
- `sudo sharing -a <path>`: מוסיף תיקייה חדשה לרשימת התיקיות המשותפות (Share Point).
- `sudo sharing -r <share_point_name>`: מסיר תיקייה מרשימת השיתוף.
- `sudo sharing -e <share_point_name> -s <flags>`: עריכת ההרשאות או דגלים ספציפיים לתיקייה משותפת קיימת.

## 4. גילוי שירותים ברשת (Bonjour & dns-sd)
- **Bonjour / mDNS:** מנגנון ה-Zero-configuration של אפל, המאפשר למחשבים ולשירותים (כמו מדפסות, תיקיות משותפות) להכריז על עצמם ברשת המקומית ללא צורך בשרת DNS מרכזי (Multicast DNS).

### פקודות mDNS / Bonjour (dns-sd)
- `dns-sd -B _smb._tcp`: "סריקה" (Browse) של כל שרתי ה-SMB המכריזים על עצמם כעת ברשת המקומית.
- `dns-sd -B _ssh._tcp`: סריקה של כל מכשירי ה-SSH/Remote Login הזמינים בסביבה.
- `dns-sd -B _ipp._tcp`: סריקה של מדפסות רשת (Internet Printing Protocol).
- `dns-sd -L <Name> _smb._tcp`: פתרון שם (Lookup) לשרת ספציפי שגילינו בסריקה כדי לקבל את כתובת ה-IP והפורט המדויקים שלו.

## 5. Continuity וקישוריות אלחוטית
- **AirDrop:** טכנולוגיה לשיתוף קבצים מהיר בין מכשירי Apple בסביבה הקרובה באמצעות Bluetooth (ליצירת "לחיצת יד" ואיתור) ו-Wi-Fi Direct P2P (להעברת הנתונים עצמם ללא תלות בראוטר מרכזי).
- **Universal Control:** תכונה המאפשרת להשתמש בעכבר ומקלדת של מק אחד ולשלוט בעזרתם על מכשירי מק או אייפד אחרים סמוכים באופן חלק. המכשירים מתקשרים על גבי רשת Wi-Fi ו-Bluetooth זהים.

## 6. Enterprise Seasoning: Single Sign-On (SSO)
- **Kerberos SSO Extension:** תוסף מובנה במערכת macOS המאפשר למשתמשים בארגון להזדהות פעם אחת בלבד מול שרת ה-Active Directory / Identity Provider.
- **TGT - Ticket-Granting Ticket:** "כרטיס הגישה" הקריפטוגרפי שהרחבת ה-Kerberos מקבלת מהשרת, ומשמש להזדהות מול שירותים אחרים (כמו כונני SMB ואינטראנט) בצורה שקופה ואוטומטית ללא צורך בהזנת סיסמה נוספת.
- פרופיל ה-MDM בארגון תומך כיום ב-Extensible SSO payload להגדרת הדומיינים באופן אחיד במחשבי החברה.

---

## Recommended Reading & Enrichment Links
* **Connect your Mac to shared computers and servers:** [Apple Support (macOS User Guide)](https://support.apple.com/guide/mac-help/connect-mac-shared-computers-servers-mchlp1140/mac)
* **Set up file sharing on Mac:** [Apple Support (macOS User Guide)](https://support.apple.com/guide/mac-help/set-up-file-sharing-on-mac-mh17131/mac)
* **Intro to Kerberos Single Sign-on extension:** [Apple Platform Deployment](https://support.apple.com/guide/deployment/intro-to-kerberos-single-sign-on-extension-dep0e8082f4d/web)
* **Use AirDrop on your Mac:** [Apple Support](https://support.apple.com/en-us/102522)
* **Universal Control: Use a single keyboard and mouse between Mac and iPad:** [Apple Support](https://support.apple.com/en-us/102459)
* **Transfer files between two Mac computers using target disk mode - Mac Sharing Mode:** [Apple Support](https://support.apple.com/guide/mac-help/transfer-files-mac-computers-target-disk-mode-mchlp1443/mac)
