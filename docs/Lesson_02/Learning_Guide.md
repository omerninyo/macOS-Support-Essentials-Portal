# שיעור 02: ניהול משתמשים ואבטחת נתונים
**מדריך עזר לתלמיד**

## מטרות השיעור

* **משתמשים ותיקיות** - סוגי חשבונות מקומיים, היררכיית ה-Home Folder ותיקיית Shared.
* **ניהול סודות** - אבולוציית הסיסמאות, Keychain, ואפליקציית Passwords החדשה.
* **העידן ללא סיסמה ואבטחה** - מבוא ל-Passkeys והרשאות קבצים (POSIX/ACL). מעבדה: יצירת Passkey באתר https://webauthn.io/.
* **תיבול ארגוני** - עבודה עם Managed Apple Accounts (MAID) ושילוב Platform SSO לכניסה שקופה בארגון.



## סקירה

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/332582b3-c603-4af5-a4a2-81be768b38a6/"></iframe></div>

## מושגי מפתח (Terminology)

* **Administrator:** משתמש מנהל המערכת, בעל הרשאות גלובליות לשנות הגדרות ולהתקין תוכנות לכולם.
* **Standard User:** משתמש רגיל, מוגבל לתיקיית הבית שלו (`~`) ולמרחב האישי שלו.
* **Guest User:** משתמש אורח, מוחק את כל תוכן התיקיה שלו בניתוק.
* **Sharing Only:** משתמש נטול תיקיית בית שנועד אך ורק להזדהות מול שיתופי רשת.
* **Home Folder (`/Users/username`):** תיקיית הבית המבודדת של המשתמש. מוגנת בהרשאות קריאה למשתמש בלבד.
* **Shared Folder (`/Users/Shared`):** אזור מפורז ציבורי. מוגן באמצעות Sticky Bit.
* **Sticky Bit:** דגל הרשאה המונע ממשתמשים למחוק קבצים השייכים למשתמשים אחרים באותה תיקיה (כמו בתיקיית Shared).
* **Keychain:** תשתית מחזיק המפתחות של macOS, מורכבת מ-Login Keychain (אישי) ו-System Keychain (מערכתי).
* **Passwords app:** האפליקציה המרכזית ב-macOS 15 לניהול סיסמאות, Passkeys, ואימות דו-שלבי.
* **Passkey (מפתח גישה):** תקן הזדהות (FIDO2) ללא סיסמה. עובד באמצעות צמד מפתחות קריפטוגרפי ומאומת מקומית ב-Secure Enclave.
* **היסטוריית ה-Keychain:** הושק ב-1993, ה-API המודרני נכתב ב-2002, והסנכרון לענן (Data Protection) הצטרף ב-2013 מ-iOS ל-Mac.
* **היסטוריית ה-Secure Enclave:** מנגנון בידוד הנתונים הוקם ב-2013 למכשירי אייפון, ונחת במחשבי ה-Mac עם שבב ה-T2 בשנת 2017.
* **POSIX:** מודל ההרשאות הסטנדרטי של UNIX (Owner, Group, Everyone).
* **ACL (Access Control List):** שכבת הרשאות מתקדמת וגרגולרית המתווספת מעל POSIX.
* **Managed Apple Account (MAID):** חשבון Apple בבעלות הארגון, המגביל שירותים מסוימים (כמו רכישות או iCloud Mail) ומאפשר אימות מול הארגון.
* **Platform SSO:** תשתית ב-macOS המאפשרת התחברות למחשב המקומי (Login Window) ישירות מול שרת זהויות ענן (IdP) כדוגמת Entra ID, ללא צורך ב-Active Directory ישן.
* **Federated Authentication:** מצב בו הזנת אימייל ארגוני מעבירה את המשתמש להזדהות מול שרת החברה, מבלי לדרוש סיסמת Apple חדשה.

## פקודות שימושיות (CLI Commands)
| פקודה | תיאור |
|---|---|
| `dscl . -list /Users` | הצגת רשימת כלל המשתמשים במערכת (לוקאליים) |
| `dscl . -read /Users/username` | קריאת מאפיינים נרחבים של משתמש ספציפי |
| `ls -la /Users` | הצגת הרשאות קבצים, כולל זיהוי ה-Sticky Bit (`t`) |
| `ls -le /path` | הצגת הרשאות קבצים, כולל תצוגת רשומות ACL (המסומנות ב-`+`) |
| `security list-keychains` | הצגת רשימת מחיזיקי המפתחות הפעילים כעת |
| `applesso` | אבחון מצב שירות ה-Platform SSO בארגון (בסביבה נתמכת) |
| `log show --predicate 'subsystem == "com.apple.PlatformSSO"'` | חיפוש שגיאות התחברות מול שרתי SSO בלוגים |

## Recommended Reading & Enrichment Links

* **Apple Platform Support: Intro to user account types**
  [https://support.apple.com/guide/platform-support/sup72e8c67c3/web](https://support.apple.com/guide/platform-support/sup72e8c67c3/web)
* **Apple Platform Deployment: About Managed Apple Accounts**
  [https://support.apple.com/guide/deployment/depdc4ba8d82/web](https://support.apple.com/guide/deployment/depdc4ba8d82/web)
* **The Eclectic Light Company: Explainer: Keychain basics**
  [https://eclecticlight.co/2022/10/15/explainer-keychain-basics/](https://eclecticlight.co/2022/10/15/explainer-keychain-basics/)
* **The Mac Security Blog: Understanding User Accounts in macOS**
  [https://www.intego.com/mac-security-blog/understanding-user-accounts-in-macos/](https://www.intego.com/mac-security-blog/understanding-user-accounts-in-macos/)

## קישורים מומלצים ולקריאה נוספת


## סרטון סיכום

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/DDXfEIRgAxs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 💡 עזרים ויזואליים להרצאה (Presentation Visuals)

!!! tip "המחשה ויזואלית (עזר לתלמיד)"
    תמונות אלו ממחישות את הממשק או המנגנון הרלוונטי לנושא השיעור.

![Tahoe UI](../assets/images/Tahoe_UI/26-Tahoe-Settings-Users-Groups-scaled.png)
![Tahoe UI](../assets/images/Tahoe_UI/26-Tahoe-Fast-User-Menu-scaled.png)
![Tahoe UI](../assets/images/Tahoe_UI/26-Tahoe-Fast-User-Lockscreen-scaled.png)
![Tahoe UI](../assets/images/Tahoe_UI/26-Tahoe-Settings-Lock-Screen-scaled.png)
![Tahoe UI](../assets/images/Tahoe_UI/26-Tahoe-Settings-Touch-ID-scaled.png)

---
<div dir="rtl" style="text-align: left;">
  <a href="../../Lesson_03/LearningGuide/" style="font-size: 0.95em; color: gray; text-decoration: none;">⏭️ דלג לאותו שלב בשיעור הבא</a>
</div>

![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide2_image3.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide48_image8.tif)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide53_image64.png)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide53_image65.png)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide53_image67.png)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide53_image66.png)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide53_image23.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide87_image22.tif)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide87_image23.tif)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide89_image24.tif)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide89_image22.tif)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide90_image23.tif)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide90_image25.tif)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide91_image27.tif)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide91_image26.tif)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide95_image28.tif)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide96_image105.png)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide96_image104.png)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide97_image107.png)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide97_image106.png)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide98_image29.tif)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide127_image151.png)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide127_image153.png)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide127_image156.png)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide127_image154.png)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide127_image155.png)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide143_image178.png)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide143_image179.png)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide143_image180.png)
![Legacy Slide](../assets/images/Legacy_Presentation/02_Users_Permissions/Slide143_image50.jpeg)
