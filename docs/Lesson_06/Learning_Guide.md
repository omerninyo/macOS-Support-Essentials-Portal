# שיעור 06: מערכת הקבצים (APFS)
**מדריך עזר לתלמיד**


## סקירה

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/332582b3-c603-4af5-a4a2-81be768b38a6/"></iframe></div>

## מושגי מפתח (Key Concepts)

* **APFS (Apple File System):** מערכת הקבצים המודרנית של Apple המחליפה את HFS+. בנויה לביצועים גבוהים על כונני פלאש, הצפנה, שיתוף מקום דינמי והגנה על נתונים.
* **Container (מכולה):** השכבה הראשית ב-APFS שמנהלת את כל המקום הפנוי בדיסק. מחליפה למעשה את המחיצות (Partitions) הקשיחות של העבר.
* **Volume (כרך):** יחידת אחסון לוגית בתוך ה-Container. כרכים חולקים את המקום הפנוי עם שאר הכרכים במכולה וגדלים לפי הצורך ללא צורך בהגדרה מראש (Dynamic Space Sharing).
* **Copy-on-Write (CoW):** מנגנון קריטי ב-APFS המונע שחיתות נתונים בכך שמידע חדש נכתב לבלוקים ריקים לפני שהמצביע מתעדכן. מונע מצב של חצי-כתיבה.
* **Clones (שכפולים):** תכונה בולטת של APFS המאפשרת יצירת עותקים מדויקים של קבצים ותיקיות בתוך אותו כרך באופן מיידי. עותקים אלו (Clones) חולקים את אותם הבלוקים הפיזיים ולכן **אינם תופסים מקום נוסף בדיסק** עד שאחד מהם משתנה. Finder מבצע זאת אוטומטית. ניתן לכפות זאת עם הפקודה `cp -c`.
* **SVG (System Volume Group):** שילוב לוגי של כונן המערכת וכונן המידע לקבוצה אחת שמתנהגת ככונן רגיל וקלאסי (כמו Macintosh HD).
* **SSV (Signed System Volume):** מחיצת המערכת (System) שנעולה לקריאה בלבד וחתומה קריפטוגרפית להגנה מוחלטת מפני שינויים זדוניים או שגויים.
* **Firmlinks:** קישורים אקטיביים דו-כיווניים (מעין "חורי תולעת") שמחברים ספריות בכונן ה-System לספריות בכונן ה-Data, כך שעבור המשתמש נראה שמדובר במחיצה אחת.
* **Spotlight Index:** מסד נתונים סמוי (`.Spotlight-V100`) שמכיל את התוכן של רוב הקבצים בדיסק כדי לאפשר חיפוש מיידי וגלובלי.
* **mdworker / mds / mds_stores:** התהליכים ברקע שאחראים על כריית הנתונים מהקבצים ועדכון האינדקס של Spotlight.
* **Get Info ו-Contextual Menu:** ממשק המידע והאפשרויות של ה-Finder. חלון ה-Get Info (Cmd+I) מאפשר לאבחן נתונים קריטיים על קבצים (למשל, האם הם יושבים במיקום הלוגי או הפיזי ב-Firmlinks, והרשאות מערכת). שימוש בתפריט ההקשר (קליק ימני) בשילוב מקש ה-Option במקלדת חושף אפשרויות ניהול מתקדמות (כגון חשיפת נתיבים מלאים להעתקה). [קריאה מומלצת 1](https://eclecticlight.co/2026/06/09/reading-the-finders-get-info-dialog/) | [קריאה מומלצת 2](https://eclecticlight.co/2026/06/05/get-more-from-get-info-and-the-finders-contextual-menu/)
* **User Domain:** המרחב האישי של המשתמש (Home Directory), מזוהה לרוב עם סימן הטילדה (`~`). המשתמש רשאי לשנות ולמחוק קבצים במרחב זה ללא צורך בהרשאות מנהל.
* **Local Domain:** המרחב המשותף לכלל המשתמשים במחשב (למשל תיקיית `/Applications`). שינוי קבצים כאן דורש סיסמת מנהל.
* **System Domain:** מרחב קבצי הליבה של מערכת ההפעלה. סגור לחלוטין לכתיבה.

## פקודות שימושיות (Cheat Commands)

### ניווט במרחבי המערכת (Domains Navigation)
```bash
# חזרה מהירה לתיקיית הבית (User Domain) מכל מקום במערכת
cd ~

# מעבר לתיקיית הספריה המשותפת לכלל המשתמשים (Local Domain)
cd /Library

# מעבר לתיקיית הספריה האישית המוסתרת (User Domain)
cd ~/Library
```

### אבחון APFS ו-Volumes
```bash
# הצגת רשימת הדיסקים, המכולות והכרכים במערכת
diskutil list

# הצגה מעמיקה של תצורת APFS (קבוצות כרכים, סטטוס הצפנה, תפקיד הכרך)
diskutil apfs list

# הוספת כרך חדש (Volume) בצורה דינמית מבלי לפרמט
diskutil apfs addVolume diskX APFS "NewVolumeName"

# שכפול קובץ כ-Clone באופן מיידי ללא תפיסת מקום (APFS Clone)
cp -c /path/to/original /path/to/clone

# השוואת הגודל "הלוגי" של הקבצים מול המקום "הפיזי" שהם תופסים באמת
ls -lh /path/to/clone
du -h /path/to/clone

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

## קישורים מומלצים ולקריאה נוספת

* [Reading the Finder's Get Info dialog](https://eclecticlight.co/2026/06/09/reading-the-finders-get-info-dialog/) - מדריך קריאה והבנה של חלון המידע במק.
* [Get more from Get Info and the Finder's contextual menu](https://eclecticlight.co/2026/06/05/get-more-from-get-info-and-the-finders-contextual-menu/) - מאמר המפרט על התפריטים המהירים וחלון ה-Get Info.

## סרטון סיכום

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/DDXfEIRgAxs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 💡 עזרים ויזואליים להרצאה (Presentation Visuals)

![ContextualMenu Options](../assets/images/Lesson_06/L06_DeepDive_ContextualMenu_Options.jpg)
![GetInfo Window](../assets/images/Lesson_06/L06_DeepDive_GetInfo_Window.jpg)
![How macOS depends on firmlinks p1 24](../assets/images/Lesson_06/L06_DeepDive_How_macOS_depends_on_firmlinks_p1_24.jpeg)
![How macOS depends on firmlinks p1 25](../assets/images/Lesson_06/L06_DeepDive_How_macOS_depends_on_firmlinks_p1_25.jpeg)
![Slide107 image34](../assets/images/Lesson_06/L06_LegacySlide_Slide107_image34.tif)
![Slide107 image35](../assets/images/Lesson_06/L06_LegacySlide_Slide107_image35.tif)
![Slide108 image117](../assets/images/Lesson_06/L06_LegacySlide_Slide108_image117.png)
![Slide108 image118](../assets/images/Lesson_06/L06_LegacySlide_Slide108_image118.png)
![Slide108 image35](../assets/images/Lesson_06/L06_LegacySlide_Slide108_image35.tif)
![Slide109 image36](../assets/images/Lesson_06/L06_LegacySlide_Slide109_image36.tif)
![Slide109 image37](../assets/images/Lesson_06/L06_LegacySlide_Slide109_image37.tif)
![Slide110 image119](../assets/images/Lesson_06/L06_LegacySlide_Slide110_image119.png)
![Slide111 image120](../assets/images/Lesson_06/L06_LegacySlide_Slide111_image120.png)
![Slide112 image121](../assets/images/Lesson_06/L06_LegacySlide_Slide112_image121.png)
![Slide112 image122](../assets/images/Lesson_06/L06_LegacySlide_Slide112_image122.png)
![Slide112 image45](../assets/images/Lesson_06/L06_LegacySlide_Slide112_image45.jpeg)
![Slide112 image46](../assets/images/Lesson_06/L06_LegacySlide_Slide112_image46.jpeg)
![Slide112 image47](../assets/images/Lesson_06/L06_LegacySlide_Slide112_image47.jpeg)
![Slide113 image123](../assets/images/Lesson_06/L06_LegacySlide_Slide113_image123.png)
![Slide113 image124](../assets/images/Lesson_06/L06_LegacySlide_Slide113_image124.png)
![Slide113 image125](../assets/images/Lesson_06/L06_LegacySlide_Slide113_image125.png)
![Slide113 image126](../assets/images/Lesson_06/L06_LegacySlide_Slide113_image126.png)
![Slide113 image127](../assets/images/Lesson_06/L06_LegacySlide_Slide113_image127.png)
![Slide113 image128](../assets/images/Lesson_06/L06_LegacySlide_Slide113_image128.png)
![Slide113 image129](../assets/images/Lesson_06/L06_LegacySlide_Slide113_image129.png)
![Slide115 image38](../assets/images/Lesson_06/L06_LegacySlide_Slide115_image38.tif)
![Slide115 image39](../assets/images/Lesson_06/L06_LegacySlide_Slide115_image39.tif)
![Slide116 image40](../assets/images/Lesson_06/L06_LegacySlide_Slide116_image40.tif)
![Slide116 image41](../assets/images/Lesson_06/L06_LegacySlide_Slide116_image41.tif)
![Slide118 image133](../assets/images/Lesson_06/L06_LegacySlide_Slide118_image133.png)
![Slide129 image159](../assets/images/Lesson_06/L06_LegacySlide_Slide129_image159.png)
![Slide129 image160](../assets/images/Lesson_06/L06_LegacySlide_Slide129_image160.png)
![Slide3 image4](../assets/images/Lesson_06/L06_LegacySlide_Slide3_image4.jpeg)
![Slide68 image13](../assets/images/Lesson_06/L06_LegacySlide_Slide68_image13.tif)
![Slide68 image81](../assets/images/Lesson_06/L06_LegacySlide_Slide68_image81.png)
![Slide83 image20](../assets/images/Lesson_06/L06_LegacySlide_Slide83_image20.tif)
![Slide83 image21](../assets/images/Lesson_06/L06_LegacySlide_Slide83_image21.tif)
![26-Tahoe-Disk-Utility-scaled](../assets/images/Lesson_06/L06_TahoeUI_26-Tahoe-Disk-Utility-scaled.png)
![26-Tahoe-Finder-Get-Info-scaled](../assets/images/Lesson_06/L06_TahoeUI_26-Tahoe-Finder-Get-Info-scaled.png)
![26-Tahoe-Spotlight-Action-scaled](../assets/images/Lesson_06/L06_TahoeUI_26-Tahoe-Spotlight-Action-scaled.png)
![26-Tahoe-Spotlight-scaled](../assets/images/Lesson_06/L06_TahoeUI_26-Tahoe-Spotlight-scaled.png)

!!! tip "המחשה ויזואלית (עזר לתלמיד)"
    תמונות אלו ממחישות את הממשק או המנגנון הרלוונטי לנושא השיעור.