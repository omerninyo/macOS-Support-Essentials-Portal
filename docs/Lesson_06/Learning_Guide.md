
# שיעור 06: מערכת הקבצים (APFS)
**מדריך עזר לתלמיד**


## מטרות השיעור

* APFS Architecture & Dynamic Space Sharing
* System Volume Group (SVG) & Orphaned Volumes
* Firmlinks
* Spotlight Indexing & Live Text
**[Image Recommendation]:** A super minimalist abstract vector diagram showing a glowing data core (representing APFS) splitting into two interconnected hemispheres (System and Data).


## סקירה

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/9f334406-f88d-4a75-9797-47bfdc6a6767/"></iframe></div>

## מושגי מפתח (Key Concepts)

* **APFS (Apple File System):** מערכת הקבצים המודרנית של Apple. בנויה לביצועים גבוהים, חלוקת מקום דינמית, והגנה על נתונים.
* **Container (מכולה):** מאגר האחסון הראשי ב-APFS שמנהל את השטח הפנוי עבור כל הכרכים שבתוכו (מחליף מחיצות קשיחות).
* **Volume (כרך):** יחידת אחסון לוגית. כרכים חולקים מקום פנוי באופן דינמי ללא צורך להגדיר גודל מראש (Dynamic Space Sharing).
* **Copy-on-Write (CoW):** מנגנון המונע שחיתות נתונים על ידי כתיבת שינויים לבלוקים חדשים לפני עדכון המצביע למידע.
* **Clones (שכפולים):** יצירת עותקים מדויקים באותו כרך בשבריר שנייה **ללא תפיסת מקום נוסף** (Zero-storage overhead) עד לביצוע שינוי. Finder מבצע זאת אוטומטית.
* **SVG (System Volume Group):** מעטפת המאחדת את כונן המערכת וכונן המידע לקבוצה אחת שמוצגת ככונן אחיד למשתמש.
* **SSV (Signed System Volume):** מחיצת ה-System הנעולה והחתומה קריפטוגרפית. המערכת עולה מתוך Snapshot מאומת. שום תוכנה או אדמין לא יכולים לשנות בה קבצים.
* **Firmlinks:** "חורי תולעת" (קישורים דו-כיווניים) המחברים ספריות מה-System אל ה-Data לחוויית שימוש רציפה.
* **Orphaned Data Volume:** מקרה קצה בו נוצר נתק בין ה-System ל-Data (לעיתים לאחר שחזור לקוי), ומשאיר כונן `Macintosh HD - Data` שמבזבז מקום.
* **Spotlight Index & Live Text:** מסד נתונים סמוי (`.Spotlight-V100`) לחיפוש גלובלי. בגרסאות עדכניות, התהליך כולל אנליזת תמונות מורכבת (OCR באמצעות `photoanalysisd`), מה שעשוי לגרום לעיבוד ממושך ברקע (Runaway Indexing).
* **User, Local, Network, System Domains:** חלוקת המערכת למרחבים שמגדירים מיקום נתונים והרשאות. הבנתם חיונית לפתרון תקלות של הגדרות ומשאבים (כמו פונטים) בסביבה מרובת משתמשים.
* **אבטחה ארגונית (Enterprise Security):** לאור ה-SSV, אין צורך שתוכנות אנטי-וירוס יסרקו את כונן המערכת (הוא גם כך מוגן). חשוב להחריג נתיבי מערכת כדי למנוע לולאות אינסופיות עקב Firmlinks, מה שעלול לגרום לקריסות במק.

## פקודות שימושיות (Cheat Commands)

### אבחון APFS ו-Volumes
```bash
# הצגת היררכיית APFS במערכת
diskutil list
diskutil apfs list

# הוספת כרך חדש עם מכסה (Quota) לתוך Container
diskutil apfs addVolume diskX APFS "NewVolumeName" -quota 50g

# יצירת Clone ידני ללא תפיסת מקום
cp -c /path/to/original /path/to/clone
```

### ניווט ואימות מערכת
```bash
# הצגת ה-Firmlinks במערכת
cat /usr/share/firmlinks

# אימות שה-SSV מוגן וחתום קריפטוגרפית (חשוב ל-IT)
csrutil authenticated-root status

# ניווט מהיר ל-User Domain לעומת ה-Local Domain
cd ~/Library
cd /Library
```

### פתרון תקלות ב-Spotlight
```bash
# בדיקת סטטוס והפעלה של אינדקס
sudo mdutil -s /

# איפוס ובנייה מחדש של אינדקס למקרה של נתוני שטח פנוי פגומים
sudo mdutil -E /

# בדיקת מטא-דאטה לקובץ ספציפי
mdimport -t -d3 /path/to/file.pdf
```

## קישורים מומלצים ולקריאה נוספת

* [Use Disk Utility to repair a storage device](https://support.apple.com/en-il/guide/platform-support/sup9e89abfd4/web) - מדריך רשמי לבדיקה ותיקון.
* [How macOS depends on firmlinks](https://eclecticlight.co/2023/07/22/how-macos-depends-on-firmlinks/) - מאמר עומק על Firmlinks.
* [Using and troubleshooting Spotlight in Sequoia: summary](https://eclecticlight.co/2024/11/29/using-and-troubleshooting-spotlight-in-sequoia-summary/) - סיכום פתרון תקלות ב-Spotlight.

## סרטון סיכום

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/cBSnmMtt9ho" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 💡 עזרים ויזואליים להרצאה (Presentation Visuals)

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
![26-Tahoe-Disk-Utility-scaled](../assets/images/Lesson_06/L06_TahoeUI_26-Tahoe-Disk-Utility-scaled.png)
![26-Tahoe-Finder-Get-Info-scaled](../assets/images/Lesson_06/L06_TahoeUI_26-Tahoe-Finder-Get-Info-scaled.png)
![26-Tahoe-Spotlight-Action-scaled](../assets/images/Lesson_06/L06_TahoeUI_26-Tahoe-Spotlight-Action-scaled.png)
![26-Tahoe-Spotlight-scaled](../assets/images/Lesson_06/L06_TahoeUI_26-Tahoe-Spotlight-scaled.png)

