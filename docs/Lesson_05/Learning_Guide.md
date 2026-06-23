# שיעור 05: אפליקציות ותהליכים
**מדריך עזר לתלמיד**


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

![Slide102 image113](../assets/images/Lesson_05/L05_LegacySlide_Slide102_image113.png)
![Slide102 image32](../assets/images/Lesson_05/L05_LegacySlide_Slide102_image32.tif)
![Slide103 image114](../assets/images/Lesson_05/L05_LegacySlide_Slide103_image114.png)
![Slide103 image115](../assets/images/Lesson_05/L05_LegacySlide_Slide103_image115.png)
![Slide103 image33](../assets/images/Lesson_05/L05_LegacySlide_Slide103_image33.tif)
![Slide104 image116](../assets/images/Lesson_05/L05_LegacySlide_Slide104_image116.png)
![Slide105 image96](../assets/images/Lesson_05/L05_LegacySlide_Slide105_image96.png)
![Slide105 image97](../assets/images/Lesson_05/L05_LegacySlide_Slide105_image97.png)
![Slide117 image130](../assets/images/Lesson_05/L05_LegacySlide_Slide117_image130.png)
![Slide117 image131](../assets/images/Lesson_05/L05_LegacySlide_Slide117_image131.png)
![Slide117 image132](../assets/images/Lesson_05/L05_LegacySlide_Slide117_image132.png)
![Slide121 image134](../assets/images/Lesson_05/L05_LegacySlide_Slide121_image134.png)
![Slide121 image135](../assets/images/Lesson_05/L05_LegacySlide_Slide121_image135.png)
![Slide123 image136](../assets/images/Lesson_05/L05_LegacySlide_Slide123_image136.png)
![Slide123 image137](../assets/images/Lesson_05/L05_LegacySlide_Slide123_image137.png)
![Slide123 image138](../assets/images/Lesson_05/L05_LegacySlide_Slide123_image138.png)
![Slide123 image139](../assets/images/Lesson_05/L05_LegacySlide_Slide123_image139.png)
![Slide123 image140](../assets/images/Lesson_05/L05_LegacySlide_Slide123_image140.png)
![Slide124 image141](../assets/images/Lesson_05/L05_LegacySlide_Slide124_image141.png)
![Slide124 image142](../assets/images/Lesson_05/L05_LegacySlide_Slide124_image142.png)
![Slide124 image143](../assets/images/Lesson_05/L05_LegacySlide_Slide124_image143.png)
![Slide124 image144](../assets/images/Lesson_05/L05_LegacySlide_Slide124_image144.png)
![Slide124 image145](../assets/images/Lesson_05/L05_LegacySlide_Slide124_image145.png)
![Slide124 image146](../assets/images/Lesson_05/L05_LegacySlide_Slide124_image146.png)
![Slide124 image147](../assets/images/Lesson_05/L05_LegacySlide_Slide124_image147.png)
![Slide124 image148](../assets/images/Lesson_05/L05_LegacySlide_Slide124_image148.png)
![Slide125 image149](../assets/images/Lesson_05/L05_LegacySlide_Slide125_image149.png)
![Slide125 image150](../assets/images/Lesson_05/L05_LegacySlide_Slide125_image150.png)
![Slide125 image48](../assets/images/Lesson_05/L05_LegacySlide_Slide125_image48.jpeg)
![Slide126 image151](../assets/images/Lesson_05/L05_LegacySlide_Slide126_image151.png)
![Slide126 image152](../assets/images/Lesson_05/L05_LegacySlide_Slide126_image152.png)
![Slide128 image157](../assets/images/Lesson_05/L05_LegacySlide_Slide128_image157.png)
![Slide128 image158](../assets/images/Lesson_05/L05_LegacySlide_Slide128_image158.png)
![Slide12 image13](../assets/images/Lesson_05/L05_LegacySlide_Slide12_image13.png)
![Slide12 image14](../assets/images/Lesson_05/L05_LegacySlide_Slide12_image14.png)
![Slide12 image17](../assets/images/Lesson_05/L05_LegacySlide_Slide12_image17.png)
![Slide144 image181](../assets/images/Lesson_05/L05_LegacySlide_Slide144_image181.png)
![Slide144 image182](../assets/images/Lesson_05/L05_LegacySlide_Slide144_image182.png)
![Slide145 image96](../assets/images/Lesson_05/L05_LegacySlide_Slide145_image96.png)
![Slide145 image97](../assets/images/Lesson_05/L05_LegacySlide_Slide145_image97.png)
![Slide146 image183](../assets/images/Lesson_05/L05_LegacySlide_Slide146_image183.png)
![Slide146 image184](../assets/images/Lesson_05/L05_LegacySlide_Slide146_image184.png)
![Slide146 image185](../assets/images/Lesson_05/L05_LegacySlide_Slide146_image185.png)
![Slide146 image186](../assets/images/Lesson_05/L05_LegacySlide_Slide146_image186.png)
![Slide146 image187](../assets/images/Lesson_05/L05_LegacySlide_Slide146_image187.png)
![Slide146 image97](../assets/images/Lesson_05/L05_LegacySlide_Slide146_image97.png)
![Slide147 image51](../assets/images/Lesson_05/L05_LegacySlide_Slide147_image51.jpeg)
![Slide24 image42](../assets/images/Lesson_05/L05_LegacySlide_Slide24_image42.png)
![Slide32 image51](../assets/images/Lesson_05/L05_LegacySlide_Slide32_image51.png)
![Slide39 image22](../assets/images/Lesson_05/L05_LegacySlide_Slide39_image22.jpeg)
![Slide39 image52](../assets/images/Lesson_05/L05_LegacySlide_Slide39_image52.png)
![Slide39 image55](../assets/images/Lesson_05/L05_LegacySlide_Slide39_image55.png)
![Slide51 image9](../assets/images/Lesson_05/L05_LegacySlide_Slide51_image9.tif)
![Slide57 image29](../assets/images/Lesson_05/L05_LegacySlide_Slide57_image29.jpeg)
![Slide57 image69](../assets/images/Lesson_05/L05_LegacySlide_Slide57_image69.png)
![Slide59 image10](../assets/images/Lesson_05/L05_LegacySlide_Slide59_image10.tif)
![Slide59 image20](../assets/images/Lesson_05/L05_LegacySlide_Slide59_image20.png)
![Slide59 image72](../assets/images/Lesson_05/L05_LegacySlide_Slide59_image72.png)
![Slide59 image73](../assets/images/Lesson_05/L05_LegacySlide_Slide59_image73.png)
![Slide61 image32](../assets/images/Lesson_05/L05_LegacySlide_Slide61_image32.jpeg)
![Slide61 image69](../assets/images/Lesson_05/L05_LegacySlide_Slide61_image69.png)
![Slide65 image78](../assets/images/Lesson_05/L05_LegacySlide_Slide65_image78.png)
![Slide65 image79](../assets/images/Lesson_05/L05_LegacySlide_Slide65_image79.png)
![Slide66 image11](../assets/images/Lesson_05/L05_LegacySlide_Slide66_image11.tif)
![Slide66 image12](../assets/images/Lesson_05/L05_LegacySlide_Slide66_image12.tif)
![Slide75 image88](../assets/images/Lesson_05/L05_LegacySlide_Slide75_image88.png)
![Slide75 image89](../assets/images/Lesson_05/L05_LegacySlide_Slide75_image89.png)
![Slide82 image96](../assets/images/Lesson_05/L05_LegacySlide_Slide82_image96.png)
![Slide82 image97](../assets/images/Lesson_05/L05_LegacySlide_Slide82_image97.png)
![26-Tahoe-App-Store-scaled](../assets/images/Lesson_05/L05_TahoeUI_26-Tahoe-App-Store-scaled.png)
![26-Tahoe-Force-Quit-scaled](../assets/images/Lesson_05/L05_TahoeUI_26-Tahoe-Force-Quit-scaled.png)

!!! tip "המחשה ויזואלית (עזר לתלמיד)"
    תמונות אלו ממחישות את הממשק או המנגנון הרלוונטי לנושא השיעור.