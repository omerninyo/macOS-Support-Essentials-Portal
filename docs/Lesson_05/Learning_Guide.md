# שיעור 05: אפליקציות ותהליכים
**מדריך עזר לתלמיד (vEXP)**

## מטרות השיעור
* תהליכי התקנה
* ארגזי חול (Sandboxing)
* אבחון וטיפול בתקיעות
* הפצה ארגונית (VPP)
**[Image Recommendation]:** A minimalist vector icon of the App Store "A" logo and an open cardboard box representing packages.

## סקירה
<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/57c8a1df-bbc5-4e2e-9986-b6e4b0e04f4e/"></iframe></div>

## מושגי יסוד (Core Concepts)
* **App Store:** החנות הרשמית של אפל לאפליקציות. כל אפליקציה כאן עוברת ביקורת, נוטריזציה ופועלת תחת מגבלות של ארגז חול (Sandbox).
* **Package (PKG):** קובץ התקנה המכיל חבילת קבצים וסקריפטים לפיזור במערכת. משמש לרוב להתקנות תוכנות ארגוניות מורכבות.
* **Disk Image (DMG / ASIF):** כונן וירטואלי. ב-macOS 26 (Tahoe), אפל הציגה את פורמט ASIF (Apple Sparse Image Format) היעיל במיוחד.
* **Sandboxing:** מנגנון אבטחה של macOS המגביל את גישת האפליקציה למשאבי מערכת, זיכרון וקבצים בלתי קשורים. המידע נשמר בתוך "Container" מבודד.
* **Code Signing & CDHash (DeepDive):** התשתית הקריפטוגרפית של מערכת ההפעלה. המערכת מוודאת בזמן אמת כל דף זיכרון מול ה-Code Directory Hash (CDHash) כדי לוודא שלא בוצעו שינויים זדוניים.
* **App Translocation (DeepDive):** מנגנון (Gatekeeper Path Randomization) המונע מאפליקציות זדוניות שחולצו מקובץ ZIP/DMG לטעון קבצים סמוכים, על ידי הרצתן ממיקום אקראי ולקריאה-בלבד עד שיועברו לתיקיית היישומים.
* **Preemptive Multitasking & WindowServer (DeepDive):** הקרנל מנהל תהליכים בצורה כפויה. אם חוט הממשק הראשי נתקע, ה-WindowServer מציג אוטומטית את "כדור הים".
* **Force Quit:** יציאה מאולצת ואגרסיבית לאפליקציה תקועה (שליחת פקודת `SIGKILL`), שאינה מאפשרת שמירת נתונים.
* **Volume Purchase Program (VPP) / Apple Business Manager (ABM):** תוכנית הרכישה הארגונית המאפשרת לארגונים לרכוש רישיונות ולחלקם לעובדים דרך MDM ללא צורך ב-Apple ID אישי.
* **Self Service:** חנות האפליקציות הפרטית של הארגון המאפשרת למשתמשים סטנדרטיים להתקין תוכנות מאושרות ללא סיסמת Admin.

---

## פקודות טרמינל מרכזיות

### מתקינים ודיסקים (`installer` & `hdiutil`)
* **`sudo installer -pkg /path/to/package.pkg -target /`**
  התקנה שקטה של PKG לכונן הראשי. הפקודה הבסיסית לסקריפטים של MDM.

* **`hdiutil attach /path/to/image.dmg`**
  עגינת (Mount) כונן וירטואלי.

* **`hdiutil detach /Volumes/ImageName`**
  ניתוק כונן וירטואלי בצורה בטוחה.

### ניהול תהליכים ויציאה מאולצת (`killall` & `kill`)
* **`killall "App Name"`**
  סגירת אפליקציה בצורה עדינה לפי שמה (שולח `SIGTERM`).

* **`kill -9 [PID]`**
  אילוץ קריסה מיידית דרך מזהה תהליך, זהה לפעולת ה-Force Quit הגרפית (שולח `SIGKILL`).

* **`killall cfprefsd`**
  חיסול תהליך התצורה, מאלץ את המערכת לרוקן את המטמון של קבצי העדפות. קריטי בעת איפוס ארגזי חול (Sandboxes) ידני.

### הגדרות אפליקציה נסתרות (`defaults`)
* **`defaults read com.apple.Safari`**
  קורא את כלל קובץ ההגדרות (plist) עבור Safari.

* **`defaults delete com.apple.Safari`**
  מוחק את קובץ ההגדרות לחלוטין, ומחזיר את האפליקציה למצב יצרן.

### עדכוני מערכת ורוזטה (`softwareupdate`)
* **`softwareupdate --install-rosetta --agree-to-license`**
  התקנה מהירה ושקטה של סביבת התרגום רוזטה 2 במחשבי Apple Silicon.

---

## ניהול Sandboxes ואיפוס אפליקציות

**היכן אפליקציות שומרות את המידע שלהן?**

1. **העדפות (Preferences):** תחת `~/Library/Preferences/com.domain.appname.plist`
2. **Application Support:** תחת `~/Library/Application Support/AppName/`
3. **Containers:** אפליקציות מה-App Store או אפליקציות Sandbox אינן כותבות לתיקיות הכלליות. כל הגישה שלהן מנותבת אל: `~/Library/Containers/[Bundle ID]`.

**כיצד לאפס אפליקציית Sandbox (איפוס מוחלט):**

1. ודא שהאפליקציה סגורה לחלוטין (Quit או Force Quit).
2. מחק את תיקיית ה-Container של האפליקציה בנתיב: `~/Library/Containers/[Bundle ID]`.
3. מחק את הגדרות המערכת השמורות (אם קיימות מחוץ ל-Sandbox): `defaults delete [Bundle ID]`.
4. נקה את מטמון הזיכרון על ידי הרצת הפקודה `killall cfprefsd` בטרמינל.
5. פתח מחדש את האפליקציה - היא תיווצר מחדש מאפס, כאילו הופעלה לראשונה.

---

## קישורים מומלצים ולקריאה נוספת
* [Check app installation and processes on Mac](https://support.apple.com/guide/apple-platform-support/check-app-installation-and-processes-apda5f8a096c/web)
* [Learn about App Store security protections](https://support.apple.com/guide/apple-platform-support/learn-about-app-store-security-protections-apd1a7b8e19c/web)
* [Distribute content with mobile device management](https://support.apple.com/guide/deployment/distribute-content-depe210182ce/web)
* [Explainer: the app sandbox](https://eclecticlight.co/2020/09/24/explainer-the-app-sandbox/)
* [macOS Tahoe brings a new disk image format](https://eclecticlight.co/2024/09/16/macos-tahoe-brings-a-new-disk-image-format/)

## סרטון סיכום
<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/z_52E-9epcY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

!!! tip "המחשה ויזואלית (עזר לתלמיד)"
    תמונות אלו ממחישות את הממשק או המנגנון הרלוונטי לנושא השיעור.

![Slide103_image33](../assets/images/Lesson_05/L05_LegacySlide_Slide103_image33.jpg)
![Slide121_image134](../assets/images/Lesson_05/L05_LegacySlide_Slide121_image134.jpg)
![Slide66_image11](../assets/images/Lesson_05/L05_LegacySlide_Slide66_image11.jpg)
![26-Tahoe-App-Store-scaled](../assets/images/Lesson_05/L05_TahoeUI_26-Tahoe-App-Store-scaled.png)
![26-Tahoe-Force-Quit-scaled](../assets/images/Lesson_05/L05_TahoeUI_26-Tahoe-Force-Quit-scaled.png)
