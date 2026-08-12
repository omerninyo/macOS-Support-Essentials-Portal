# שיעור 10: שיתוף וגישה מרחוק
**מדריך עזר לתלמיד (vEXP)**

## 🎧 סקירה (פודקאסט)

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/d4c324af-2882-4300-abb9-503dfb0683ee/"></iframe></div>

---

## מושגי מפתח (Key Concepts)

| מושג | רקע ומשמעות |
| :--- | :--- |
| **SMB (Server Message Block)** | הסטנדרט הנוכחי והבלעדי לשיתוף קבצים גם ב-macOS. פותח במקור ב-IBM ואומץ ע"י מיקרוסופט. החליף את פרוטוקול AFP הישן של אפל. |
| **AFP (Apple Filing Protocol)** | הפרוטוקול הישן של אפל (מ-1988). אינו נתמך רשמית כיום (Deprecated). |
| **Mac Sharing Mode / 1TR** | מחליף את ה-Target Disk Mode ההיסטורי. ב-Apple Silicon, כדי להגן על ההצפנה, המק פועל כשרת SMB מבודד (קבצים) ולא כ-Block Device, ומופעל אך ורק מתוך סביבת ה-Recovery. |
| **Bonjour / mDNS** | הטכנולוגיה של אפל לגילוי שרתים ושירותים ברשת המקומית באופן אוטומטי (Zero-Configuration). |
| **Kerberos SSO Extension** | תוסף מובנה ב-macOS שמאפשר התחברות שקופה (Passwordless) לכונני רשת ארגוניים המבוססים על Active Directory בעזרת כרטיסי TGT. |

> [!NOTE]
> **הערה טכנית:** פרוטוקול SMB אינו מודע למבנה הקבצים החסכוני של APFS (כמו קבצי Sparse או Clones), ולכן העתקת קובץ כזה לשרת SMB "תנפח" אותו לגודלו המקורי.

---

## שירותי שיתוף (Sharing Services) וקישוריות

| שירות | הסבר ואופן פעולה |
|---|---|
| **AirDrop** | שיתוף קבצים מקומי המשתמש ב-Bluetooth לגילוי, ו-Wi-Fi Direct (פרוטוקול AWDL) להעברת נתונים מהירה ללא ראוטר. במידה ו-AirDrop לא מוצא מכשירים, כיבוי והדלקת ה-Wi-Fi תאפס את ממשק ה-`awdl0`. |
| **Screen Sharing** | שיתוף מסך מובנה. מבוסס על מנגנון VNC. מחייב מתן הרשאת **Screen Recording** ב-TCC (Privacy & Security), אחרת יוצג מסך שחור או שגיאה. |
| **Universal Control** | עבודה חלקה עם מקלדת/עכבר אחד בין כמה מחשבים/אייפדים סמוכים מאותו Apple ID (פועל דרך שירות Rapportd). |

---

## עבודה עם SMB (Server Message Block)

- מתחברים לשרתים בחלון **Connect to Server** שב-Finder עם הקידומת `smb://`.
- **איטיות בסביבת רשת ארגונית:** אם חיבור ה-SMB איטי מאוד בזמן ניווט בתיקיות בשרת Windows, לרוב זה נובע מניסיון של ה-Finder ליצור קבצי `.DS_Store` נסתרים. ניתן למנוע זאת עם הפקודה הבאה בטרמינל:
  ```bash
  defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE
  ```

---

## Mac Sharing Mode

מצב שיתוף מתקדם לאבחון וחילוץ נתונים מ-Mac מבוסס Apple Silicon במקרה של כשל במערכת ההפעלה.
- מופעל דרך **Recovery Mode** תחת התפריט Utilities > Share Disk.
- המחשב המארח יראה את המחשב התקול כתיקיית רשת (SMB) תחת התפריט Network.

> [!WARNING]
> **אזהרת IT קריטית (First Aid):** בניגוד לעבר ב-Target Disk Mode, אי אפשר להריץ פקודות תיקון דיסק או Disk Utility מהמחשב המארח על המחשב התקול, מכיוון שהדיסק חשוף ברמת קובץ (SMB) ולא ברמת בלוק (Block Device). תיקון תקלות בדיסק חייב להתבצע מה-Recovery של המחשב התקול עצמו!

---

## פקודות דיאגנוסטיקה ושורת הפקודה (Terminal)

| פקודה | תיאור |
|---|---|
| `smbutil statshares -a` | מציג את חיבורי ה-SMB הפעילים, רמת ההצפנה וגרסת הפרוטוקול הנוכחית (למשל SMB 3.1.1). |
| `mount_smbfs` | פקודה לעיגון (Mount) כונני SMB ישירות משורת הפקודה. |
| `sharing -l` | מציג את כל השירותים ותיקיות השיתוף הזמינים במערכת כרגע. |
| `dns-sd -B _smb._tcp` | סורק את הרשת המקומית ב-Bonjour ומציג שרתי SMB שמכריזים על עצמם. |
| `klist` | מציג את הכרטיסים הקריפטוגרפיים (Tickets) של תוסף ה-Kerberos SSO שנשמרו במטמון במק. |

---

## Enterprise Seasoning: מגבלות MDM ושיתוף קבצים

בארגונים גדולים, מחלקת האבטחה משתמשת ב-MDM כדי להגביל יציאת מידע (DLP). תכונת ה-**Managed Open In** מאפשרת להפריד בין אפליקציות ארגוניות ופרטיות.
היות ש-AirDrop נחשב ליעד "לא מנוהל" (Unmanaged Destination), משתמשים בארגונים עשויים לגלות שהם אינם מסוגלים לשתף קבצי עבודה דרך AirDrop משום שה-MDM חוסם זאת. 

---

## קישורים מומלצים ולקריאה נוספת

* [Connect your Mac to shared computers and servers](https://support.apple.com/guide/mac-help/connect-mac-shared-computers-servers-mchlp1140/mac) 
* [Set up file sharing on Mac](https://support.apple.com/guide/mac-help/set-up-file-sharing-on-mac-mh17131/mac)
* [Intro to Kerberos Single Sign-on extension](https://support.apple.com/guide/deployment/intro-to-kerberos-single-sign-on-extension-dep0e8082f4d/web)
* [Universal Control: Use a single keyboard and mouse](https://support.apple.com/en-us/102459)

---

## 🎬 סרטון סיכום

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/p1hW4lTaHOY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

## 💡 עזרים ויזואליים להרצאה (Presentation Visuals)

!!! tip "המחשה ויזואלית (עזר לתלמיד)"
    תמונות אלו ממחישות את הממשק או המנגנון הרלוונטי לנושא השיעור.

![Slide71_image86](../assets/images/Lesson_10/L10_LegacySlide_Slide71_image86.png)
![Slide71_image87](../assets/images/Lesson_10/L10_LegacySlide_Slide71_image87.png)
