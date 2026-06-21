# Chapter 06 - Asset C: Cheat Sheet

## מושגי מפתח (Key Concepts)
* **APFS (Apple File System):** מערכת הקבצים המודרנית של Apple המחליפה את HFS+. בנויה לביצועים גבוהים על כונני פלאש, הצפנה, שיתוף מקום דינמי והגנה על נתונים.
* **Container (מכולה):** השכבה הראשית ב-APFS שמנהלת את כל המקום הפנוי בדיסק. מחליפה למעשה את המחיצות (Partitions) הקשיחות של העבר.
* **Volume (כרך):** יחידת אחסון לוגית בתוך ה-Container. כרכים חולקים את המקום הפנוי עם שאר הכרכים במכולה וגדלים לפי הצורך ללא צורך בהגדרה מראש (Dynamic Space Sharing).
* **Copy-on-Write (CoW):** מנגנון קריטי ב-APFS המונע שחיתות נתונים בכך שמידע חדש נכתב לבלוקים ריקים לפני שהמצביע מתעדכן. חוסך גם מקום בעת יצירת Clones.
* **SVG (System Volume Group):** שילוב לוגי של כונן המערכת וכונן המידע לקבוצה אחת שמתנהגת ככונן רגיל וקלאסי (כמו Macintosh HD).
* **SSV (Signed System Volume):** מחיצת המערכת (System) שנעולה לקריאה בלבד וחתומה קריפטוגרפית להגנה מוחלטת מפני שינויים זדוניים או שגויים.
* **Firmlinks:** קישורים אקטיביים דו-כיווניים (מעין "חורי תולעת") שמחברים ספריות בכונן ה-System לספריות בכונן ה-Data, כך שעבור המשתמש נראה שמדובר במחיצה אחת.
* **Spotlight Index:** מסד נתונים סמוי (`.Spotlight-V100`) שמכיל את התוכן של רוב הקבצים בדיסק כדי לאפשר חיפוש מיידי וגלובלי.
* **mdworker / mds / mds_stores:** התהליכים ברקע שאחראים על כריית הנתונים מהקבצים ועדכון האינדקס של Spotlight.

## פקודות שימושיות (Cheat Commands)

### אבחון APFS ו-Volumes
```bash
# הצגת רשימת הדיסקים, המכולות והכרכים במערכת
diskutil list

# הצגה מעמיקה של תצורת APFS (קבוצות כרכים, סטטוס הצפנה, תפקיד הכרך)
diskutil apfs list

# הוספת כרך חדש (Volume) בצורה דינמית מבלי לפרמט
diskutil apfs addVolume diskX APFS "NewVolumeName"

# הצגת נתיבי ה-Firmlinks במערכת
cat /usr/share/firmlinks

# בדיקת סטאטוס חתימת מחיצת המערכת המאומתת
csrutil authenticated-root status
```

### ניהול ואבחון Spotlight
```bash
# בדיקה האם Spotlight מופעל על כונן ה-Root
sudo mdutil -s /

# מחיקה ובנייה מחדש של אינדקס ה-Spotlight (לפתרון תקלות "System Data" חריג)
sudo mdutil -E /

# רשימת כל הפלאגינים (MDImporters) המותקנים במערכת
mdimport -L

# סריקה ופליטת נתוני המטא-דאטה של קובץ ספציפי (לאיתור באגים בחיפוש)
mdimport -t -d3 /path/to/specific/file.pdf
```

## Recommended Reading & Enrichment Links
* **Apple Platform Support:** Use Disk Utility - [Link](https://support.apple.com/en-il/guide/platform-support/sup9e89abfd4/web)
* **The Eclectic Light Company:** A brief history of APFS in honour of its fifth birthday - [Link](https://eclecticlight.co/2022/04/01/a-brief-history-of-apfs-in-honour-of-its-fifth-birthday/)
* **The Eclectic Light Company:** How macOS depends on firmlinks - [Link](https://eclecticlight.co/2023/07/22/how-macos-depends-on-firmlinks/)
* **The Eclectic Light Company:** Using and troubleshooting Spotlight in Sequoia: summary - [Link](https://eclecticlight.co/2024/11/29/using-and-troubleshooting-spotlight-in-sequoia-summary/)
