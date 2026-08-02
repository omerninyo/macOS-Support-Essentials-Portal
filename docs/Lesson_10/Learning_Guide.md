# שיעור 10: שיתוף וגישה מרחוק
**מדריך עזר לתלמיד (Asset C)**

## סקירה

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/d4c324af-2882-4300-abb9-503dfb0683ee/"></iframe></div>

## מושגי מפתח (Key Concepts)

| מושג | רקע ומשמעות היסטורית מה-DeepDive |
| :--- | :--- |
| **AFP (Apple Filing Protocol)** | פרוטוקול שהוצג לראשונה ב-1988 והיה ברירת המחדל עד OS X 10.8. אינו נתמך רשמית כיום (Deprecated). |
| **SMB (Server Message Block)** | פותח במקור ב-IBM ואומץ ע"י מיקרוסופט. החליף את AFP ומהווה את הסטנדרט כיום, גם למקים. (שימו לב: אינו משמר חסכון במקום של קבצי Sparse ב-APFS). |
| **Chooser** | אפליקציה מיתולוגית מ-System 7 (1991) לגילוי שרתים ומדפסות (AppleShare) - מזכיר לנו כמה Zero-Configuration כיום (כמו AirDrop ו-Bonjour) הוא קסם מודרני. |
| **Mac Sharing Mode / 1TR** | מחליף את ה-Target Disk Mode ההיסטורי. ב-Apple Silicon, המק פועל כשרת SMB (קבצים) ולא כ-Block Device. מבוסס על סביבת ה-Recovery (שהופיעה רק ב-2011). |

## פרוטוקול SMB (Server Message Block)

- **הסטנדרט המוחלט:** הפרוטוקול המובנה לשיתוף קבצים ברשת כיום. מתחברים אליו ב-Finder עם הקידומת `smb://`.
- **איטיות בסביבת רשת (DS_Store):** אם חיבור ה-SMB איטי מאוד בזמן ניווט בתיקיות גדולות בשרת Windows, הדבר נובע מניסיון המק ליצור קבצי `.DS_Store`. מנהלי רשת יכולים למנוע זאת עם הפקודה בטרמינל:
  `defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE`

### פקודות דיאגנוסטיקה ואבחון רשת
- `smbutil statshares -a`: מציג את חיבורי ה-SMB הפעילים ואת רמת ההצפנה וגרסת הפרוטוקול (למשל SMB 3.1.1).
- `mount_smbfs`: לעיגון (Mount) כונני SMB ישירות מהטרמינל.
- `ping -c 5 [server]` או `netstat -an`: אבחון תעבורת רשת בסיסית.

## שירותי שיתוף (Sharing Services) וקישוריות

- **AirDrop:** שיתוף קבצים מקומי ללא ראוטר, המשתמש ב-Bluetooth לגילוי ו-Wi-Fi Direct (פרוטוקול AWDL) להעברת נתונים מהירה. במקרה של בעיות גילוי, כיבוי והדלקת ה-Wi-Fi עוזרת לאפס את ממשק ה-`awdl0`.
- **Screen Sharing:** שיתוף מסך המבוסס על מנגנון VNC עטוף באבטחה. **שימו לב:** מערכת ההפעלה (TCC) דורשת מתן הרשאת Screen Recording ליישום, אחרת תוצג שגיאה או מסך שחור.
- **Universal Control:** עבודה חלקה עם מקלדת/עכבר אחד בין כמה מחשבים/אייפדים סמוכים מאותו Apple ID (באמצעות Wi-Fi ו-Bluetooth ושירות Rapportd).

### פקודות גילוי ושיתוף
- `sharing -l`: מציג את השירותים ותיקיות השיתוף הזמינות דרך ממשק ה-CLI (מחליף ניווט ב-System Settings).
- `dns-sd -B _smb._tcp`: חיפוש והאזנה לשרתי SMB המכריזים על עצמם ברשת המקומית בטכנולוגיית Bonjour / mDNS.

## Mac Sharing Mode

- במחשבי Apple Silicon, מפעילים מצב זה דרך ה-Recovery Mode (Utilities > Share Disk).
- **תשומת לב לאנשי IT (First Aid):** בניגוד לעבר, המחשב המארח אינו יכול להריץ פקודות `fsck` או Disk Utility לתיקון הדיסק של המחשב התקול. הדיסק משותף כתיקיית רשת (SMB) ולא כבלוק חומרתי. תיקון דיסק מחייב הרצת First Aid מה-Recovery של המחשב התקול עצמו.

## Enterprise Seasoning: Single Sign-On (SSO)

- **Kerberos SSO Extension:** תוסף מובנה במערכת macOS המאפשר הזדהות פעם אחת בלבד (Passwordless) מול ה-Active Directory בעזרת TGT (Ticket-Granting Ticket).
- פקודת `klist` מציגה את הכרטיסים (Tickets) הקריפטוגרפיים שנשמרו במטמון במק. 
- **חסימות בארגון (MDM):** חשוב לדעת שארגונים יכולים להגביל שיתוף (כמו AirDrop) באמצעות טכנולוגיית Managed Open In, אשר מזהה את ה-AirDrop כסביבה "לא מנוהלת" (Unmanaged) וחוסמת העברת מסמכים רגישים אליו.

---

## קישורים מומלצים ולקריאה נוספת

* [Connect your Mac to shared computers and servers](https://support.apple.com/guide/mac-help/connect-mac-shared-computers-servers-mchlp1140/mac) 
* [Set up file sharing on Mac](https://support.apple.com/guide/mac-help/set-up-file-sharing-on-mac-mh17131/mac)
* [Intro to Kerberos Single Sign-on extension](https://support.apple.com/guide/deployment/intro-to-kerberos-single-sign-on-extension-dep0e8082f4d/web)
* [Universal Control: Use a single keyboard and mouse](https://support.apple.com/en-us/102459)

## סרטון סיכום

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/p1hW4lTaHOY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 💡 עזרים ויזואליים להרצאה (Presentation Visuals)

!!! tip "המחשה ויזואלית (עזר לתלמיד)"
    תמונות אלו ממחישות את הממשק או המנגנון הרלוונטי לנושא השיעור.

![Slide71_image86](../assets/images/Lesson_10/L10_LegacySlide_Slide71_image86.png)
![Slide71_image87](../assets/images/Lesson_10/L10_LegacySlide_Slide71_image87.png)
