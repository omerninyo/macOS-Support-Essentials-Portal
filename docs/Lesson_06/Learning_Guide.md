# שיעור 06: מערכת הקבצים (APFS)
**מדריך עזר לתלמיד**

---

## מטרות השיעור

* APFS Architecture & Dynamic Space Sharing
* System Volume Group (SVG) & Orphaned Volumes
* Firmlinks
* Spotlight Indexing & Live Text

---

## 🎧 האזנה לסיכום — לפני או אחרי השיעור

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/9f334406-f88d-4a75-9797-47bfdc6a6767/"></iframe></div>

---

## מושגי מפתח

| מושג | הסבר |
|---|---|
| **APFS** | מערכת הקבצים המודרנית של Apple. בנויה לביצועים גבוהים, חלוקת מקום דינמית, והגנה על נתונים. |
| **Container (מכולה)** | מאגר האחסון הראשי ב-APFS שמנהל את השטח הפנוי עבור כל הכרכים שבתוכו. מחליף מחיצות קשיחות. |
| **Volume (כרך)** | יחידת אחסון לוגית. כרכים חולקים מקום פנוי באופן דינמי ללא צורך להגדיר גודל מראש (Dynamic Space Sharing). |
| **Copy-on-Write (CoW)** | מנגנון המונע שחיתות נתונים על ידי כתיבת שינויים לבלוקים חדשים לפני עדכון המצביע למידע. |
| **Clones (שכפולים)** | יצירת עותקים מדויקים באותו כרך בשבריר שנייה **ללא תפיסת מקום נוסף** (Zero-storage overhead) עד לביצוע שינוי. Finder מבצע זאת אוטומטית. |
| **SVG (System Volume Group)** | מעטפת המאחדת את כונן המערכת וכונן המידע לקבוצה אחת שמוצגת ככונן אחיד למשתמש. |
| **SSV (Signed System Volume)** | מחיצת ה-System הנעולה והחתומה קריפטוגרפית. המערכת עולה מתוך Snapshot מאומת. שום תוכנה או Admin לא יכולים לשנות בה קבצים. |
| **Firmlinks** | "חורי תולעת" — קישורים דו-כיווניים המחברים ספריות מה-System אל ה-Data לחוויית שימוש רציפה. |
| **Orphaned Data Volume** | מקרה קצה בו נוצר נתק בין ה-System ל-Data (לעיתים לאחר שחזור לקוי), ומשאיר כונן `Macintosh HD - Data` שמבזבז מקום. |
| **Spotlight Index & Live Text** | מסד נתונים סמוי (`.Spotlight-V100`) לחיפוש גלובלי. בגרסאות עדכניות, התהליך כולל אנליזת תמונות (OCR), מה שעשוי לגרום לעיבוד ממושך ברקע (Runaway Indexing). |
| **User / Local / Network / System Domains** | חלוקת המערכת למרחבים שמגדירים מיקום נתונים והרשאות. חיונית לפתרון תקלות הגדרות ומשאבים בסביבה מרובת משתמשים. |
| **אבטחה ארגונית (Enterprise Security)** | לאור ה-SSV, אין צורך שתוכנות AV יסרקו את כונן המערכת. חשוב להחריג נתיבי מערכת כדי למנוע לולאות Firmlink שעלולות לגרום לקריסות. |

---

## חלק 1 — APFS: Container, Volume, Clone

### מבנה APFS בפועל

```
Physical Disk
└── Container (disk3) ← הבריכה הגדולה
    ├── Volume: Macintosh HD (System) ← Read-Only, חתום
    ├── Volume: Macintosh HD - Data   ← Read-Write, נתוני משתמש
    ├── Volume: Preboot
    ├── Volume: Recovery
    └── Volume: VM (Swap)
```

!!! important
    כל הכרכים ב-Container חולקים את **אותו מקום פנוי**. אין צורך להגדיר גודל מראש לכל כרך — המערכת מנהלת את זה דינמית.

### חישוב שטח אחסון ודילמת ה-Purgeable Space

ב-macOS, חישוב נפח האחסון הכולל מתבצע לפי הנוסחה:
$$\text{Capacity} = \text{Available} + (\text{Used} - \text{Purgeable})$$

* **מהו Purgeable Space?** מקום שכרגע שמורים בו קבצים זמניים (מטמונים, קבצי לוגים ו-Local Snapshots) ש-macOS רשאית למחוק אוטומטית באמצעות תהליך הרקע `deleted(8)` כאשר המערכת זקוקה לשטח פנוי נוסף.
* **המלכוד של Finder מול Disk Utility:** ב-macOS 26 Tahoe, ה-Finder וחלון האחסון בהגדרות המערכת נוטים לעיתים להחסיר את נתוני ה-Purgeable Space שנתפסים ע"י Snapshots ולהציגם כשטח תפוס לחלוטין (`Used`). כתוצאה מכך, המערכת עלולה לחסום העתקת קבצים חדשים עם שגיאת "אין מספיק מקום פנוי", למרות שב-Disk Utility ניתן לראות בבירור שהשטח מוגדר כ-Purgeable וניתן לפינוי מיידי.

### פקודות אבחון

```bash
# הצגת היררכיית APFS
diskutil list
diskutil apfs list

# הוספת כרך עם Quota
diskutil apfs addVolume diskX APFS "NewVolumeName" -quota 50g

# יצירת Clone ידני (ללא תפיסת מקום)
cp -c /path/to/original /path/to/clone
```

---

## חלק 2 — SSV ו-Firmlinks

### מבנה ה-System Volume Group

```
"Macintosh HD" (מה שה-Finder מציג)
        ↕ Firmlinks (תפרים דו-כיווניים)
┌─────────────────────┐    ┌─────────────────────┐
│   System Volume      │    │    Data Volume       │
│   (Read-Only)        │    │    (Read-Write)      │
│   חתום קריפטוגרפית  │    │   נתוני משתמש        │
└─────────────────────┘    └─────────────────────┘
```

!!! note
    הפקודה `sudo touch /System/test.txt` תחזיר **"Read-only file system"** — זו לא שגיאה, זו ההגנה של SSV בפעולה.

### פקודות SSV ו-Firmlinks

```bash
# אימות שה-SSV חתום וסגור (חשוב לפני פריסת AV ארגוני)
csrutil authenticated-root status

# הצגת ה-Firmlinks (התפרים בין System ל-Data)
cat /usr/share/firmlinks

# הצגת נקודות ה-Mount (הראה את read-only)
mount
```

---

## חלק 3 — File System Domains

### ארבעת המרחבים

| Domain | נתיב | גישה | שימוש |
|---|---|---|---|
| **User** | `~/Library/` | משתמש בלבד | העדפות, Containers, Caches אישיים |
| **Local** | `/Library/` | כל המשתמשים (Admin לשינוי) | פונטים משותפים, Daemons, Frameworks |
| **Network** | `/Network/Library/` | רשת ארגונית | משאבים ממשרד ה-IT |
| **System** | `/System/Library/` | נעול (SSV) | קבצי מערכת — אין כניסה |

!!! tip "תרחיש נפוץ בשטח"
    משתמש מתקין פונט ורק הוא רואה אותו → הפונט הותקן ב-User Domain (`~/Library/Fonts`). כדי שיהיה זמין לכולם: להעביר ל-`/Library/Fonts` (דורש Admin).

### גישה ל-User Library ב-Finder

1. פתח Finder → תפריט `Go` בשורת התפריטים
2. החזק מקש `Option (⌥)` → **Library** תופיע ברשימה
3. לחץ עליה → זוהי ה-`~/Library` שלך

---

## חלק 4 — Spotlight

### איך Spotlight עובד

```
קובץ חדש נוצר / משתנה
        ↓
mdworker (תהליך רקע)
        ↓
mdimporter plugin (מותאם לסוג הקובץ)
        ↓
.Spotlight-V100 (מסד הנתונים)
        ↓
Spotlight Search / Finder / "About This Mac"
```

### פתרון תקלות Spotlight

```bash
# בדיקת סטטוס אינדקס
sudo mdutil -s /

# איפוס ובניה מחדש (לבעיית "System Data" מוגזם)
sudo mdutil -E /

# בדיקת מטא-דאטה של קובץ ספציפי
mdimport -t -d3 /path/to/file.pdf
```

!!! note
    לאחר `mdutil -E /` תראה את תהליכי `mds_stores` ו-`photoanalysisd` קופצים ב-Activity Monitor. זה תקין — המערכת בונה מחדש. עשוי לקחת שעות עד ימים.

---

## חלק 5 — אבטחה ארגונית (Enterprise)

### מה אנשי IT צריכים לדעת

!!! important "לפני פריסת AV/DLP ארגוני על Mac"
    1. הרץ `csrutil authenticated-root status` — אם `enabled`, כונן המערכת **חתום ומוגן**. אין צורך לסרוק אותו.
    2. הגדר Exclusions לנתיבי מערכת: `/System/`, `/usr/bin/`, `/usr/lib/`
    3. השתמש ב-`/usr/local/` (נגיש לכתיבה) לסקריפטים — לא ב-`/usr/bin/` (נעול)

!!! caution
    כלי AV ישן שסורק ללא Exclusions על Mac עם Firmlinks — עלול להיכנס ללולאה אינסופית ולגרום ל-**Kernel Panic**. תמיד לעדכן סוכני אבטחה לגרסה התומכת ב-Tahoe/Sequoia.

---

## קישורים ולקריאה נוספת

* [Use Disk Utility to repair a storage device](https://support.apple.com/en-il/guide/platform-support/sup9e89abfd4/web) — מדריך רשמי
* [How macOS depends on firmlinks](https://eclecticlight.co/2023/07/22/how-macos-depends-on-firmlinks/) — מאמר עומק על Firmlinks
* [Aren't snapshots purgeable?](https://eclecticlight.co/2026/08/24/arent-snapshots-purgeable/) — תחקיר מעמיק על ניהול שטח פנוי ו-Purgeable Snapshots ב-macOS 26 Tahoe
* [Using and troubleshooting Spotlight in Sequoia](https://eclecticlight.co/2024/11/29/using-and-troubleshooting-spotlight-in-sequoia-summary/) — פתרון תקלות Spotlight

---

## 🎬 סרטון סיכום

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/cBSnmMtt9ho" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

## עזרים ויזואליים

!!! tip "המחשה ויזואלית (עזר לתלמיד)"
    תמונות אלו ממחישות את הממשק או המנגנון הרלוונטי לנושא השיעור.

![GetInfo_Window](../assets/images/Lesson_06/L06_DeepDive_GetInfo_Window.jpg)
![How_macOS_depends_on_firmlinks_p1_24](../assets/images/Lesson_06/L06_DeepDive_How_macOS_depends_on_firmlinks_p1_24.jpeg)
![How_macOS_depends_on_firmlinks_p1_25](../assets/images/Lesson_06/L06_DeepDive_How_macOS_depends_on_firmlinks_p1_25.jpeg)
![Slide107_image35](../assets/images/Lesson_06/L06_LegacySlide_Slide107_image35.jpg)
![Slide115_image38](../assets/images/Lesson_06/L06_LegacySlide_Slide115_image38.jpg)
![Slide115_image39](../assets/images/Lesson_06/L06_LegacySlide_Slide115_image39.jpg)
![Slide116_image40](../assets/images/Lesson_06/L06_LegacySlide_Slide116_image40.jpg)
![Slide116_image41](../assets/images/Lesson_06/L06_LegacySlide_Slide116_image41.jpg)
![Slide3_image4](../assets/images/Lesson_06/L06_LegacySlide_Slide3_image4.jpeg)
![26-Tahoe-Disk-Utility-scaled](../assets/images/Lesson_06/L06_TahoeUI_26-Tahoe-Disk-Utility-scaled.png)
![26-Tahoe-Finder-Get-Info-scaled](../assets/images/Lesson_06/L06_TahoeUI_26-Tahoe-Finder-Get-Info-scaled.png)
![26-Tahoe-Spotlight-Action-scaled](../assets/images/Lesson_06/L06_TahoeUI_26-Tahoe-Spotlight-Action-scaled.png)
![26-Tahoe-Spotlight-scaled](../assets/images/Lesson_06/L06_TahoeUI_26-Tahoe-Spotlight-scaled.png)
