# שיעור 12: עדכונים ושדרוגים
**מדריך עזר לתלמיד**


## סקירה

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/d74f76f7-4640-4f79-beb9-48a4b3de0ed3/"></iframe></div>

## מושגי יסוד: טרמינולוגיה ואסטרטגיה

* **עדכון (Update):** עדכון משני (Minor Update) או טלאי תוכנה לגרסה הנוכחית של מערכת ההפעלה (למשל, מ-macOS 26.1 ל-macOS 26.2).
* **שדרוג (Upgrade):** שדרוג לגרסה ראשית (Major Upgrade) של מערכת הפעלה חדשה לחלוטין (למשל, מ-macOS 25 ל-macOS 26 Tahoe).
* **עדכון קומבו (Combo Update - היסטורי):** מונח עבר המתאר קובץ שכלל את כל השינויים מאז הגרסה המרכזית האחרונה. הוחלף כיום לחלוטין על ידי ארכיטקטורת ה-SSV וה-Cryptex.
* **Rapid Security Response - RSR (או BSI):** טלאי אבטחה קריטיים ומהירים שמולבשים על המערכת באמצעות Cryptex, ללא צורך בעדכון מערכת מלא. מזוהים באותיות בסוגריים, כגון `macOS 26.3.1 (a)`.
* **השהיית עדכונים (Deferral):** יכולת ניהולית ב-MDM להשהות הופעה של עדכוני תוכנה (עד 90 יום לשדרוג גדול) לצורך בדיקות תאימות.
* **Declarative Device Management - DDM:** התשתית המודרנית של ניהול המכשירים. אכיפת העדכונים מתבצעת על ידי שליחת "הצהרה" עם תאריך יעד (Deadline), וה-Mac מנהל לוקאלית את ההתראות והכפייה.
* **Migration Assistant:** הכלי המובנה להעברת מידע בין מקים. אינו מעתיק את מערכת ההפעלה עצמה.

---

## מאגר פקודות הטרמינל: שליטה בעדכונים (`softwareupdate`)

כלי ה-CLI המרכזי לניהול, הורדה, והתקנה של עדכוני מערכת הוא `softwareupdate`.

### חיפוש והורדה:

* **`softwareupdate -l`** או **`softwareupdate --list`**
  מציג רשימה של כל עדכוני התוכנה הזמינים.

* **`softwareupdate -d -a`**
  מוריד את כל העדכונים הזמינים למטמון אך לא מתקין אותם.

### התקנה:

* **`sudo softwareupdate -i -a`**
  מתקין את כל העדכונים.

* **`sudo softwareupdate -i -a -R`**
  מתקין ומאתחל אוטומטית.

### הורדת קבצי התקנה מלאים (Full Installers):

* **`softwareupdate --fetch-full-installer --full-installer-version 26.0`**
  מוריד את קובץ ההתקנה המלא (Install macOS.app) של הגרסה היישר לתיקיית Applications.

### ניקוי והיסטוריה:

* **`softwareupdate --clear-deferrals`**
  מנקה לוקאלית את השהיות העדכונים (אם ה-MDM מתיר זאת).

* **`softwareupdate --history`**
  מדפיס היסטוריית עדכונים שהותקנו.

* **`softwareupdate --install-rosetta --agree-to-license`**
  מתקין את סביבת ההרצה Rosetta 2 בצורה שקטה.

---

## ארכיטקטורה, תהליכי רקע ולוגים

* **`softwareupdated`**: תהליך הרקע המרכזי שאחראי על חיפוש העדכונים וחישוב שטח הדיסק הדרוש (`CalculatePrepareSize`).
* **`UpdateBrainService`**: השירות בפועל שאחראי על פריסת הקבצים ברקע ובניית ה-Snapshot וה-SSV.
* **`/Library/Preferences/com.apple.SoftwareUpdate.plist`**: קובץ התצורה ברמת המערכת.

* **חיפוש שגיאות ב-Unified Logging System:**
  ```bash
  log show --predicate 'subsystem == "com.apple.SoftwareUpdate"' --info --debug
  ```

---

## המלצות IT להגירות (Migration Assistant)

בסביבות ארגוניות, Migration Assistant עלול לייבא בעיות ממחשבים ישנים.

* **בידוד המידע להעברה:** מומלץ להעביר *רק* את חשבון המשתמש (Home Folder) ולא את `Applications`. העברת אפליקציות גוררת קבצי קונפיגורציה של MDM ישן, אפליקציות אינטל (Rosetta), והרחבות ליבה שאינן נתמכות.
* **חיבור פיזי:** ב-Apple Silicon משתמשים ב-Mac Sharing Mode (מתוך ה-Recovery) יחד עם כבל Thunderbolt להעברה מהירה.
* **חפיפת משתמשים:** אין לייבא משתמש אם כבר יצרתם משתמש בעל שם זהה ב-Mac החדש. תיווצר התנגשות UID שתחייב דריסה או יצירת כפילויות. עדיף להריץ את ה-Migration ישירות ממסך ההפעלה הראשון (OOBE).

---

## קישורים מומלצים ולקריאה נוספת

* [Manage software updates in Apple Platform Deployment](https://support.apple.com/guide/deployment/manage-software-updates-depc4c80847a/web) - המדריך הרשמי למנהלי מערכת על שליטה ועיכוב עדכונים בארגון.
* [Install software updates for Mac](https://support.apple.com/guide/mac-help/get-macos-updates-mchlpx1065/mac) - מדריך פשוט למשתמש הקצה לאיך מורידים ומתקינים עדכוני מערכת.
* [Transfer to a new Mac with Migration Assistant](https://support.apple.com/en-us/102613) - מדריך המסביר איך להעביר נתונים ומידע ממק ישן למק חדש בעזרת אשף ההגירות.
* [Taking manual control of macOS updates with softwareupdate](https://eclecticlight.co/2023/09/06/taking-manual-control-of-macos-updates-with-softwareupdate/) - צלילת עומק לטרמינל.

## סרטון סיכום

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/DDXfEIRgAxs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## 💡 עזרים ויזואליים להרצאה (Presentation Visuals)

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
