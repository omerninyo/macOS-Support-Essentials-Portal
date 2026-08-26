# שיעור 12: עדכונים ושדרוגים
**מדריך עזר לתלמיד**

## 🎧 סקירה (פודקאסט)

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/d74f76f7-4640-4f79-beb9-48a4b3de0ed3/"></iframe></div>

---

**סיכום שיעור**

## נושאי השיעור
1. ארכיטקטורת העדכונים המודרנית ב-macOS 26 (FSM, Pallas, Streaming Decompression ו-UpdateBrain).
2. אבטחה והרשאות ב-Apple Silicon: הרשאות Standard Users, Volume Ownership ו-Cryptexes (BSI).
3. כלי ה-CLI softwareupdate, המלכודות ב-Migration Assistant וסולם פתרון תקלות.
4. תיבול ארגוני: Declarative Device Management (DDM), השהיות (Deferrals) ו-Bootstrap Token.

---

## מונחי ליבה ומושגים

| מושג | רקע ומשמעות ארגונית |
| :--- | :--- |
| **Update (עדכון)** | עדכון מינורי בתוך אותה משפחת גרסאות (למשל מ-26.2 ל-26.3). כולל תיקוני באגים וטלאי אבטחה. |
| **Upgrade (שדרוג)** | שדרוג דור ראשי לגרסת מערכת הפעלה חדשה (למשל מ-macOS 26 ל-27). כולל תכונות תשתיתיות חדשות. |
| **Pallas** | שרת העדכונים המרכזי של אפל (`mesu.apple.com/assets/macos/`), המספק קטלוגים מותאמים אישית לדגם המק ולקהל היעד. |
| **Content Caching (`AssetCacheServices`)** | שירות מטמון מקומי ברשת הארגונית המיירט הורדות של שרתי אפל וחוסך תעבורת WAN עצומה. |
| **UpdateBrain** | רכיב תוכנה בינארי היורד עם חבילת העדכון ואחראי לבנות את ה-SSV החדש, לעדכן את ה-RecoveryOS ולפרוס קושחה. |
| **Volume Ownership & Secure Token** | מנגנון קריפטוגרפי ב-Secure Enclave. ב-Apple Silicon, אישור עדכון דורש שיוך של בעל כרך (Volume Owner). |
| **Bootstrap Token** | מפתח הצפנה ייעודי המופקד ב-MDM בעת ה-Enrollment, ומאפשר לשרת לבצע עדכונים שקטים ואוטונומיים עבור משתמשי Standard. |
| **DDM (Declarative Management)** | מודל ניהול עצמאי שבו ה-MDM מכריז על מצב יעד ודדליין מקומי, וה-Mac מנהל ומבצע את האכיפה והאתחול בעצמו. |
| **Cryptex & BSI** | *Cryptographically Executable* — אימג' מוצפן המולבש מעל ה-SSV ומאפשר הזרקת עדכוני אבטחה ל-Safari/WebKit ללא בניית SSV מחדש. |

---

## חלק 1 — ארכיטקטורת העדכונים המודרנית ב-macOS 26

### שרשרת העדכון מקצה לקצה
ב-macOS 26, תהליך העדכון פועל כמכונת מצבים סופית (Finite State Machine) ללא כתיבה לקבצי מערכת פעילים:
1. **סריקה מול Pallas:** תהליך `softwareupdated` בודק זכאות וגרסה מול `mesu.apple.com`.
2. **חישוב שטח (`CalculatePrepareSize`):** המערכת מחשבת שטח כפול עבור ה-Snapshot, שטח ל-Cryptex (1.2x), ומפעילה את `deleted(8)` לפינוי שטח Purgeable.
3. **הזרמה וחילוץ בזמן אמת:** קובץ ה-Zip נחלץ כזרם (Stream) ישירות תוך כדי ההורדה לנתיב `/System/Library/AssetsV2/`.
4. **בנייה ע"י UpdateBrain:** שירות ה-`UpdateBrainService` יוצר Snapshot חדש, מעדכן את Rosetta ואת ה-RecoveryOS במקביל.
5. **חתימה אישית (Personalization):** אימות מול `gs.apple.com` והחלפת מצביע הבוט (SFR) באתחול.

> *← המנגנון של APFS Snapshots וחישוב שטח ה-Purgeable נלמד לעומק בשיעור 06 ובשיעור 07 — כאן רואים כיצד מערכת ההפעלה סומכת על מנגנון ה-SSV כדי לעדכן ללא זמן השבתה.*

---

## חלק 2 — אבטחה ב-Apple Silicon: הרשאות ו-Cryptexes (BSI)

### מי רשאי לעדכן?
* **בממשק הגרפי (GUI):** החל מ-macOS 12.3, כל משתמש **Standard** מקומי יכול לאשר עדכונים ושדרוגים דרך הגדרות המערכת, בתנאי שהוא מחזיק ב-Secure Token (Volume Owner).
* **בטרמינל (CLI) ומתקינים מלאים (UMA):** נדרשות הרשאות מנהל מקומי (**Local Administrator** / `sudo`).

### טכנולוגיית ה-Cryptex ו-Background Security Improvements
* **מהו Cryptex?** אימג' דיסק מוצפן המאוחסן ב-Preboot ומורכב בשכבה עליונה מעל ה-SSV הנעול.
* מאפשר להזריק עדכוני אבטחה קריטיים לאפליקציות ורכיבי מערכת ללא צורך בבנייה מחדש של ה-SSV כולו.
* **Rollback מיידי:** במידה ועדכון שבר תאימות עם כלי פנימי, ביטול ה-BSI ב-System Settings מורה ל-Bootloader לדלג על טעינת ה-Cryptex באתחול הבא.

---

## חלק 3 — כלי ה-CLI softwareupdate, ה-Migration Assistant ומדריך תקלות

### פקודות CLI מרכזיות (`softwareupdate`)

```bash
# הצגת כלל העדכונים הזמינים למכשיר
softwareupdate -l

# הורדת מתקין מלא (Universal Mac Assistant - UMA) לתיקיית Applications
softwareupdate --fetch-full-installer --full-installer-version 26.3

# התקנת כל העדכונים ואתחול אוטומטי
sudo softwareupdate -i -a -R
```

### מלכודות Migration Assistant בארגון
!!! important "מדוע להימנע מהגירה עיוורת בארגון?"
    1. **התנגשות UIDs:** יצירת אדמין זמני (UID 501) והגירת משתמש עם אותו שם גורמת לדריסה או העברה ל-`/Users/Deleted Users/`.
    2. **Dirty Migration:** גרירת Kexts ו-LaunchDaemons מיושנים מאינטל שפוגעים ביציבות המק ב-Apple Silicon.
    3. **המלצת התעשייה:** מעבר למודל **Cloud-Native Ephemeral Device** — הגדרה נקייה דרך ה-MDM וסנכרון קבצים ישירות מהענן (OneDrive / Google Drive).

### סולם פתרון התקלות המלא (Troubleshooting Ladder)
1. **שלב 1 (איפוס שירות ורשת):** `sudo killall softwareupdated` ובדיקת פורט 443 מול `gs.apple.com`.
2. **שלב 2 (פינוי שטח Purgeable):** `tmutil thinlocalsnapshots / 10000000000 4`.
3. **שלב 3 (ניקוי Staging פגום):** אתחול למצב Safe Mode.
4. **שלב 4 (פתרון הברזל):** כניסה ל-1TR Recovery ובחירה ב-**Reinstall macOS** (הורדת SSV חדש מבלי לגעת במידע המשתמש!).

---

## חלק 4 — תיבול ארגוני: DDM, השהיות ו-Bootstrap Token

### השוואה: Legacy MDM מול Declarative Device Management (DDM)

| מאפיין | Legacy MDM (העידן הישן) | Declarative Device Management (DDM מודרני) |
| :--- | :--- | :--- |
| **מנגנון תפעול** | שרת שולח פקודות בודדות (`InstallASAP`) וממתין לפולינג | שרת שולח **הכרזה (Declaration)** והמק מנהל את התהליך אוטונומית |
| **לוח זמנים ואכיפה** | שברירי; תלוי בחיבור רשת רציף וניתן לדחייה ע"י המשתמש | **דדליין מקומי קשיח** לפי שעון המחשב (למשל `18:00` מקומי בכל סניף בעולם) |
| **חוויית משתמש** | התראות פשוטות שקל להתעלם מהן | מדרג התראות מובנה: תזכורות יומיות, ספירה לאחור בשעה האחרונה, ואתחול כפוי |
| **אישור חומרה** | דרש סיסמה ממשתמשים ללא הרשאות | עושה שימוש עצמאי ב-**Bootstrap Token** לאישור שקט של ה-LocalPolicy |

### מדרג השהיות עדכונים (Software Update Deferrals - עד 90 יום)
* **Major OS Upgrade Deferral (60–90 יום):** מונע מעובדים לשדרג לגרסת macOS ראשית חדשה עד לאישור תאימות אפליקציות ארגוניות ע"י ה-IT.
* **Minor OS Update Deferral (7–14 יום):** מאפשר בדיקת טלאי מערכת נקודתיים בצוותי פיילוט.
* **Non-OS / Security Updates (0 ימי השהיה):** עדכוני Safari ו-Background Security Improvements מוחלים מיד להגנה מפני Zero-Day.
* **Content Caching בארגון (`AssetCacheServices`):** יירוט הורדות Pallas וניתובן לשרת מטמון מקומי ב-LAN לחסכון ברוחב פס.

```bash
# בדיקת סטטוס הפקדת Bootstrap Token מול ה-MDM
sudo profiles status -type bootstraptoken

# ניקוי מקומי של השהיות MDM (דורש הרשאות אדמין)
sudo softwareupdate --clear-deferrals
```

---

## קישורים מומלצים ולקריאה נוספת

* [Manage software updates in Apple Platform Deployment](https://support.apple.com/guide/deployment/manage-software-updates-depc4c80847a/web) - המדריך הרשמי לאכיפת עדכונים, DDM והשהיות.
* [Install software updates for Mac](https://support.apple.com/guide/mac-help/get-macos-updates-mchlpx1065/mac)
* [Taking manual control of macOS updates with softwareupdate](https://eclecticlight.co/2023/09/06/taking-manual-control-of-macos-updates-with-softwareupdate/) - מדריך מקצועי לשימוש ב-CLI.
* [What to do when a macOS update goes wrong](https://eclecticlight.co/2026/08/14/what-to-do-when-a-macos-update-goes-wrong-2/) - מדריך פתרון תקלות מקיף לכשלים, Boot Loops ואי-התאמות בעדכוני מערכת.

---

## 🎬 סרטון סיכום

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/RFZYlrmn08Q" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

## עזרים ויזואליים

!!! tip "המחשה ויזואלית (עזר לתלמיד)"
    תמונות אלו ממחישות את הממשק או המנגנון הרלוונטי לנושא השיעור.

![How_Software_Update_works_in_Ventura_p5_37](../assets/images/Lesson_12/L12_DeepDive_How_Software_Update_works_in_Ventura_p5_37.jpeg)
![What_should_you_do_when_an_update_goes_wrong_p1_41](../assets/images/Lesson_12/L12_DeepDive_What_should_you_do_when_an_update_goes_wrong_p1_41.jpeg)
![Slide76_image16](../assets/images/Lesson_12/L12_LegacySlide_Slide76_image16.jpg)
![Slide76_image44](../assets/images/Lesson_12/L12_LegacySlide_Slide76_image44.jpeg)
![Slide76_image90](../assets/images/Lesson_12/L12_LegacySlide_Slide76_image90.png)
![Slide76_image91](../assets/images/Lesson_12/L12_LegacySlide_Slide76_image91.png)
![Slide76_image92](../assets/images/Lesson_12/L12_LegacySlide_Slide76_image92.png)
![Slide77_image17](../assets/images/Lesson_12/L12_LegacySlide_Slide77_image17.jpg)
