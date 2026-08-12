# שיעור 12: עדכונים ושדרוגים
**מדריך עזר לתלמיד (vEXP)**

## 🎧 סקירה (פודקאסט)

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/d74f76f7-4640-4f79-beb9-48a4b3de0ed3/"></iframe></div>

---

## מונחי ליבה ומושגים

| מושג | רקע ומשמעות |
| :--- | :--- |
| **עדכון (Update)** | עדכון משני (Minor Update) או טלאי לגרסה הנוכחית של המערכת (למשל, מ-macOS 26.1 ל-macOS 26.2). כולל תיקוני באגים ואבטחה. |
| **שדרוג (Upgrade)** | קפיצה לגרסה ראשית (Major Upgrade) חדשה לחלוטין (למשל, מ-macOS 25 ל-macOS 26 Tahoe). תהליך כבד הכולל שינויים תשתיתיים ב-OS. |
| **Rapid Security Response (RSR)** | נקרא גם BSI. מנגנון למענה אבטחה מהיר ומיידי של אפל להפצת תיקונים קריטיים (כמו פרצות ב-WebKit) ללא התקנת עדכון מערכת מלא. מזוהה באות בסוגריים כגון `macOS 26.3.1 (a)`. |
| **השהיית עדכונים (Deferral)** | יכולת ארגונית ב-MDM להשהות הופעה של שדרוג גדול עד 90 יום, על מנת לאפשר ל-IT לבדוק את התאימות לפני שהעובדים יעדכנו. |
| **DDM Declarative Device Management** | תשתית חדשה לניהול מכשירים. בעדכונים, מתבצעת אכיפה על ידי קביעת "הצהרה" מקומית עם דדליין, כך שה-Mac מנהל עצמאית את הכפייה וההתראות מול המשתמש. |
| **Migration Assistant** | כלי מובנה להעברת נתונים בין מקים או גיבויים. *הערה: בסביבה ארגונית קיימת המלצה מפורשת להימנע משימוש בו, כדי לא לייבא פרופילי תצורה ישנים ואפליקציות אינטל בעייתיות.* |

> [!NOTE]
> **הערה טכנית (Snapshots):** מדוע שדרוג ששוקל 5 ג'יגה דורש לעיתים 40 ג'יגה פנויים? כדי להבטיח התקנה בטוחה, ה-OS (דרך מנגנון ה-SSV) מבצע צילום מצב של הדיסק לפני העדכון. אם נופלת רשת או חשמל, המערכת חוזרת לנקודת ההתחלה מבלי שיינזק מידע! 

---

## רשימת פקודות טרמינל (CLI)

כלי ה-CLI המרכזי לניהול, הורדה, והתקנה של עדכוני מערכת הוא `softwareupdate`.

> [!WARNING]
> פקודות ההתקנה וניקוי ההשהיות (clear-deferrals) דורשות הרשאת `sudo`.

### חיפוש, הורדה והתקנה

| פקודה | תיאור |
|---|---|
| `softwareupdate -l` | מציג את רשימת כל העדכונים הזמינים למחשב הספציפי. |
| `softwareupdate -d -a` | מוריד את כל העדכונים הזמינים למטמון (Cache) אך *לא מתקין* אותם. |
| `sudo softwareupdate -i -a -R` | פקודה חזקה: מתקין את כל העדכונים ומאתחל את המחשב אוטומטית עם סיום ההתקנה. |
| `softwareupdate --fetch-full-installer` | מוריד את קובץ ההתקנה המלא (`Install macOS.app`) לתיקיית Applications. (ניתן להוסיף `--full-installer-version 26.0` לגרסה ספציפית). |

### ניהול היסטוריה ואיתור שגיאות

| פקודה | תיאור |
|---|---|
| `softwareupdate --history` | מציג את היסטוריית ההורדות וההתקנות שהתבצעו דרך המנגנון. |
| `softwareupdate --clear-deferrals` | מנקה לוקאלית את השהיות ה-MDM (שימושי לפתרון תקלות במידה וה-MDM מאפשר זאת). |
| `log show --predicate 'subsystem == "com.apple.SoftwareUpdate"'` | שליפת יומני שגיאות של תהליך העדכון (ה-`softwareupdated` וה-`UpdateBrainService`) מתוך ה-Unified Logging System למציאת סיבת הכישלון. |

---

## Enterprise Seasoning: המלצות IT להגירות (Migration Assistant)

> [!IMPORTANT]
> **מדוע לא בארגון?**
> בארגון מנוהל (MDM), כדאי מאוד לעבוד בגישת **Clean Slate**. כלומר, לתת למחשב החדש להיבנות מאפס, ולמשתמש למשוך נתונים מ-OneDrive או Google Drive.
> העברה של כלל האפליקציות וההגדרות מהמק הישן גוררת אחריה לעיתים Kexts מיושנים, אפליקציות תלויות Rosetta, ותעודות אימות MDM מתנגשות שמונעות מאנשי ה-IT לנהל את המק החדש לאחר ההגירה.

אם בכל זאת נדרש לבצע Migration Assistant ארגוני:
* סמנו **רק** את תיקיית המשתמש. הסירו את הסימון מ-`Applications` ומ-`System & Network`.
* ודאו שהחשבון המיובא אינו מתנגש בשם (UID Conflict) עם חשבון שכבר הספקתם לייצר על המק החדש.

---

## נתיבים וקבצים רלוונטיים (Paths)

| נתיב / קובץ | תיאור |
|---|---|
| `/Library/Preferences/com.apple.SoftwareUpdate.plist` | קובץ ההגדרות והמדיניות של רכיב ה-Software Update. |
| `softwareupdated` (תהליך) | תהליך הרקע המרכזי האחראי על חיפוש העדכונים ובדיקת שטח הפנוי (`CalculatePrepareSize`). |
| `UpdateBrainService` (תהליך) | שירות הפריסה עצמו (Deployment), שבונה את ה-Snapshot ופורס את החבילה בזמן האמת. |

---

## קישורים מומלצים ולקריאה נוספת

* [Manage software updates in Apple Platform Deployment](https://support.apple.com/guide/deployment/manage-software-updates-depc4c80847a/web) - המדריך למנהל: כפייה ודחייה של עדכונים בארגון מנוהל.
* [Install software updates for Mac](https://support.apple.com/guide/mac-help/get-macos-updates-mchlpx1065/mac)
* [Transfer to a new Mac with Migration Assistant](https://support.apple.com/en-us/102613)
* [Taking manual control of macOS updates with softwareupdate](https://eclecticlight.co/2023/09/06/taking-manual-control-of-macos-updates-with-softwareupdate/) - צלילת עומק לטרמינל לניהול עדכונים ידני.

---

## 🎬 סרטון סיכום

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/RFZYlrmn08Q" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

## 💡 עזרים ויזואליים להרצאה (Presentation Visuals)

!!! tip "המחשה ויזואלית (עזר לתלמיד)"
    תמונות אלו ממחישות את הממשק או המנגנון הרלוונטי לנושא השיעור.

![How_Software_Update_works_in_Ventura_p5_37](../assets/images/Lesson_12/L12_DeepDive_How_Software_Update_works_in_Ventura_p5_37.jpeg)
![What_should_you_do_when_an_update_goes_wrong_p1_41](../assets/images/Lesson_12/L12_DeepDive_What_should_you_do_when_an_update_goes_wrong_p1_41.jpeg)
![Slide1_image2](../assets/images/Lesson_12/L12_LegacySlide_Slide1_image2.jpg)
![Slide5_image5](../assets/images/Lesson_12/L12_LegacySlide_Slide5_image5.jpg)
![Slide76_image16](../assets/images/Lesson_12/L12_LegacySlide_Slide76_image16.jpg)
![Slide76_image44](../assets/images/Lesson_12/L12_LegacySlide_Slide76_image44.jpeg)
![Slide76_image90](../assets/images/Lesson_12/L12_LegacySlide_Slide76_image90.png)
![Slide76_image91](../assets/images/Lesson_12/L12_LegacySlide_Slide76_image91.png)
![Slide76_image92](../assets/images/Lesson_12/L12_LegacySlide_Slide76_image92.png)
![Slide77_image17](../assets/images/Lesson_12/L12_LegacySlide_Slide77_image17.jpg)
![Slide77_image18](../assets/images/Lesson_12/L12_LegacySlide_Slide77_image18.tif)
