# שיעור 05: אפליקציות ותהליכים
**מדריך עזר (מדריך עזר לתלמיד)**


## סקירה

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/332582b3-c603-4af5-a4a2-81be768b38a6/"></iframe></div>

## מושגי יסוד (Core Concepts)

* **App Store:** החנות הרשמית של אפל לאפליקציות. כל אפליקציה כאן עוברת ביקורת (App Review), חתימה קריפטוגרפית ונוטריון (Notarization), ופועלת תחת מגבלות של "Sandbox" (Sandboxing).
* **Package - PKG:** קובץ התקנה המכיל אוגדן של קבצים והוראות (Scripts) לפיזורם במערכת הקבצים. משמש לרוב להתקנות מורכבות של תוכנות ארגוניות ולכלי שורת הפקודה.
* **Disk Image - DMG / ASIF:** "תמונת דיסק" וירטואלית. בגרסאות קודמות נפוצו קבצי UDZO/UDSP, וב-macOS 26 (Tahoe) אפל הציגה את פורמט ה-ASIF (Apple Sparse Image Format) היעיל במיוחד.
* **Sandboxing - Sandbox:** מנגנון אבטחה של macOS המגביל את הגישה של אפליקציה (בעיקר צד-שלישי ו-App Store) למשאבי מערכת, זיכרון וקבצים שאינם שייכים לה. המידע נשמר בתוך "Container" .
* **Group Containers (DeepDive):** תיקייה ייעודית (תחת `~/Library/Group Containers`) המשמשת לאפליקציות שונות מאותו מפתח (לדוגמה: תוכנות חבילת Office) כדי לשתף מידע בארגז החול ביניהן.
* **Packages vs Bundles (DeepDive):** היסטורית ישנה הבחנה דקה: Bundle הוא לרוב אפליקציה שמכילה קוד הרצה, בעוד Package היא תיקייה שמוצגת כקובץ יחיד אך אינה מכילה בהכרח קוד (כמו מסמך RTFD או Pages).
* **App Translocation - Gatekeeper Path Randomization:** מנגנון המונע מאפליקציות זדוניות שחולצו מקובץ ZIP למשל, לרוץ מתוך תיקיית ההורדות תוך פנייה לקבצים סמוכים. המערכת מריצה את האפליקציה ממיקום אקראי (Read-Only) בזיכרון.
* **Force Quit:** Force Quit - סגירה אגרסיבית של אפליקציה שאינה מגיבה (Not Responding) מבלי לאפשר לה לשמור נתונים.
* **Volume Purchase Program - VPP / Apple Business Manager (ABM):** תוכנית הרכישה הארגונית המאפשרת לארגונים לרכוש רישיונות לאפליקציות באופן מרוכז ולחלק אותן למשתמשים דרך ה-MDM.
* **Self Service:** Self Service, דמוי App Store פרטי של הארגון. משתמשים יכולים להתקין תוכנות ופרופילים המאושרים על ידי הארגון ללא צורך בסיסמת מנהל (Admin).

---

## פקודות טרמינל מרכזיות (Terminal Commands)

### כלי התקנות ודיסקים (installer & hdiutil)

* **`sudo installer -pkg /path/to/package.pkg -target /`**
  התקנת חבילת PKG במצב "שקט" (Silent) ישירות לשורש הכונן. הפקודה הבסיסית ביותר להתקנת תוכנות ארגוניות מהטרמינל או דרך סקריפטים של ה-MDM.

* **`hdiutil attach /path/to/image.dmg`**
  עגינת (Mount) תמונת דיסק וירטואלית. מחזיר את נתיב הכונן החדש שנוצר (לרוב תחת `/Volumes/Name`).

* **`hdiutil detach /Volumes/ImageName`**
  ניתוק (Unmount) בטוח של תמונת דיסק או כונן חיצוני.

* **`hdiutil info`**
  הצגת רשימה של כלל הדיסקים הווירטואליים שמעוגנים כרגע במערכת.

* **`diskutil image create blank --format ASIF --size 100G --volumeName myVolume imagePath`**
  יצירת תמונת דיסק ריקה בפורמט החדש של Tahoe - ASIF.

### ניהול תהליכים ויציאה מאולצת (killall & kill)

* **`killall "App Name"`**
  סגירת אפליקציה (שליחת פקודת Termination עדינה) לפי שם התהליך. לדוגמה: `killall Safari`.

* **`kill -9 [PID]`**
  Force Quit מיידית ואלימה (Force Quit) של תהליך באמצעות מספר מזהה (Process ID). הפקודה עוקפת כל מנגנון שמירה רגיל של האפליקציה וזהה לחלוטין לכפתור ה-Force Quit ב-Activity Monitor.

* **`top`**
  הצגת נתונים בזמן אמת של כל התהליכים הרצים במערכת והמשאבים שהם דורשים (CPU/RAM). לחיצה על `q` תצא מהתצוגה.

### הגדרות אפליקציה מוסתרות (defaults)

* **`defaults read com.apple.Safari`**
  קריאת כלל קובץ ההגדרות (Plist) של אפליקציית ספארי השמור בתיקיית ה-Preferences.

* **`defaults write com.apple.screencapture type -string "png"`**
  כתיבת הגדרה ידנית (לדוגמה: שינוי פורמט צילומי המסך ל-PNG).

* **`defaults delete com.apple.Safari`**
  מחיקת קובץ ההגדרות לחלוטין. פעולה זו מחזירה את הגדרות האפליקציה למצב יצרן (שלב קריטי באיפוס אפליקציה מלא).

### עדכוני מערכת וכלים (softwareupdate)

* **`softwareupdate --install-rosetta --agree-to-license`**
  התקנה מהירה ושקטה של סביבת התרגום Rosetta 2 למחשבי Apple Silicon (נדרש רבות עבור תוכנות התקנה ישנות).

---

## ניהול Sandbox ואיפוס אפליקציות (Sandboxing & App Reset)

**איפה אפליקציות שומרות את המידע שלהן?**

1. **Preferences:** תחת `~/Library/Preferences/com.domain.appname.plist`
2. **Application Support:** תחת `~/Library/Application Support/AppName/`
3. **Containers:** אפליקציות מתוך ה-App Store או אפליקציות שמוגדרות מראש כאפליקציות Sandbox (Sandboxed), לא כותבות לתיקיות הכלליות שלמעלה. במקום זאת, כל הגישה שלהן מנותבת אל: `~/Library/Containers/[Bundle ID]`.

**כיצד לאפס אפליקציית Sandbox (איפוס מוחלט):**

1. ודא שהאפליקציה סגורה לחלוטין (`killall` או Force Quit).
2. מחק את תיקיית ה-Container של האפליקציה בנתיב: `~/Library/Containers/[Bundle ID]`.
3. מחק את הגדרות המערכת השמורות (אם קיימות מחוץ ל-Sandbox): `defaults delete [Bundle ID]`.
4. הפעל את האפליקציה מחדש - היא תיווצר מחדש מאפס, כאילו הופעלה לראשונה.

---

## קישורים מומלצים ולקריאה נוספת

* [Check app installation and processes on Mac](https://support.apple.com/guide/apple-platform-support/check-app-installation-and-processes-apda5f8a096c/web) - מדריך של אפל שמסביר איך לבדוק אילו תהליכים ותוכנות רצים ברקע.
* [Learn about App Store security protections](https://support.apple.com/guide/apple-platform-support/learn-about-app-store-security-protections-apd1a7b8e19c/web) - מאמר על מנגנוני האבטחה וה-Sandbox של חנות האפליקציות.
* [Distribute content with mobile device management](https://support.apple.com/guide/deployment/distribute-content-depe210182ce/web) - מאמר למנהלים על הפצת תוכנות מרחוק באמצעות MDM.
* [Explainer: the app sandbox](https://eclecticlight.co/2020/09/24/explainer-the-app-sandbox/) - מאמר טכני מעמיק מבלוג חיצון על איך עובד ארגז החול (Sandbox) שמבודד אפליקציות.
* [Explainer: Disk images](https://eclecticlight.co/2021/11/17/explainer-disk-images/) - סקירה על ההיסטוריה והמבנה של קובצי DMG.
* [macOS Tahoe brings a new disk image format](https://eclecticlight.co/2024/09/16/macos-tahoe-brings-a-new-disk-image-format/) - מאמר טכני שמסביר על הפורמט החדש של קובצי התקנה ב-macOS 26.

## סרטון סיכום

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/DDXfEIRgAxs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 💡 עזרים ויזואליים להרצאה (Presentation Visuals)

!!! tip "המחשה ויזואלית (עזר לתלמיד)"
    תמונות אלו ממחישות את הממשק או המנגנון הרלוונטי לנושא השיעור.

![Tahoe UI](../assets/images/Tahoe_UI/26-Tahoe-App-Store-scaled.png)
![Tahoe UI](../assets/images/Tahoe_UI/26-Tahoe-Force-Quit-scaled.png)

---
<div dir="rtl" style="text-align: left;">
  <a href="../../Lesson_06/LearningGuide/" style="font-size: 0.95em; color: gray; text-decoration: none;">⏭️ דלג לאותו שלב בשיעור הבא</a>
</div>
