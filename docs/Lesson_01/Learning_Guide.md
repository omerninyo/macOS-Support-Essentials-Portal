# שיעור 01: התקנה, הכרה ויישור קו
**מדריך עזר לתלמיד**

## מטרות השיעור

* **היסטוריה ופילוסופיה** - אבולוציה מ-OS X ל-macOS, ליין ה-Mac המעודכן לחברות, והמעבר ל-Apple Silicon.
* **חוויית פתיחת הקופסה (OOBE)** - צלילה ל-Setup Assistant.
* **המערכת, חדשנות ונגישות** - ניווט, מחוות Multi-Touch, אקוסיסטם ה-Continuity, סקירת Apple Intelligence, שקוף מסך, ונגישות (סרטונים: Universal Control, Continuity Camera, ו-"The Greatest").
* **תיבול ארגוני** - מה קורה כשמסך ה-Remote Management (MDM / ADE) קוטע את תהליך ההגדרה.



## סקירה

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/332582b3-c603-4af5-a4a2-81be768b38a6/"></iframe></div>

## מושגי מפתח (Key Concepts)

* **Apple Silicon:** הארכיטקטורה המודרנית של מחשבי ה-Mac המבוססת על פיתוח פנימי של אפל (מעבדי M-Series בתצורת ARM), המספקת יחס ביצועים לצריכת חשמל חסר תקדים.
* **System on a Chip (SoC):** תכנון סיליקון שמאגד את המעבד הראשי (CPU), המעבד הגרפי (GPU), זיכרון, ומנגנוני אבטחה לשבב בודד.
* **Unified Memory:** זיכרון מאוחד. ארכיטקטורה חדשנית ב-Apple Silicon המשלבת את הזיכרון הראשי (RAM) וזיכרון המסך (VRAM) אל תוך תושבת השבב עצמה. הדבר מאפשר לכל רכיבי ה-SoC לגשת לאותו מאגר זיכרון ללא צורך בהעתקת נתונים הלוך ושוב. הארכיטקטורה מבטלת צווארי בקבוק, משפרת ביצועים וחוסכת חשמל, אך במחיר של חוסר יכולת לשדרג את הזיכרון לאחר הרכישה (הזיכרון מולחם). [לקריאה נוספת מאת Howard Oakley](https://eclecticlight.co/2026/06/20/explainer-memory/)
* **Secure Enclave:** תת-מערכת חומרתית מבודדת בתוך ה-SoC האחראית על פעולות קריפטוגרפיות, שמירת מפתחות הצפנה ואימות נתונים ביומטריים (Touch ID).
* **Rosetta 2:** סביבת תרגום שקופה המובנית ב-macOS המאפשרת לאפליקציות שנכתבו עבור מעבדי Intel (x86) לרוץ על מחשבי Apple Silicon. התרגום מבוצע לרוב מראש (Ahead of Time).
* **Setup Assistant:** התהליך הראשוני שמתבצע בהפעלת מק חדש או אחרי EACS. אחראי על הגדרות רשת, אזור, יצירת Local Account, ועוד.
* **Automated Device Enrollment (ADE):** טכנולוגיית פריסה וניהול (לשעבר DEP) המאפשרת לארגונים לחבר מחשבי Mac ל-MDM באופן אוטומטי (Zero-Touch Deployment) מרגע החיבור הראשון לרשת, ולהחליף את ה-Setup Assistant הצרכני במסך Remote Management.
* **Continuity:** אוסף טכנולוגיות המאפשרות רצף עבודה בין מכשירי אפל (כמו Universal Control, Handoff, Continuity Camera). עובד לרוב על בסיס זיהוי קרבה ב-Bluetooth ותקשורת Peer-to-Peer Wi-Fi.
* **Apple Intelligence:** מערכת בינה מלאכותית המובנית ב-macOS המנצלת את ה-Neural Engine שב-Apple Silicon לעיבוד מודלי שפה באופן מקומי, מתוך דגש על פרטיות.
* **Background Process:** תהליך מערכת שרץ ברקע ללא חלון משתמש גלוי, לעיתים קרובות מאוחסן כ-LaunchAgent או LaunchDaemon.

## פקודות ונתיבים רלוונטיים (Commands & Paths)

| נתיב / פקודה | תיאור |
| :--- | :--- |
| `uname -m` | פקודת טרמינל המחזירה `arm64` אם המחשב מריץ Apple Silicon, או `x86_64` למעבדי Intel. |
| `system_profiler SPHardwareDataType` | פקודה המספקת פירוט חומרה מלא של ה-Mac, כולל מספר הליבות והזיכרון. |
| `/var/db/.AppleSetupDone` | קובץ דגל (Flag). כאשר הוא קיים, מערכת ההפעלה "יודעת" ששלב ה-Setup Assistant הושלם, ומדלגת עליו בהדלקות הבאות. |
| `sudo profiles show -type enrollment` | פקודה המחזירה את סטטוס ההרשמה של המכשיר לארגון (האם קיימת הרשמת ADE דרך Apple Business Manager). |
| `log show --predicate 'process == "Setup Assistant"' --info` | שאילתה לשליפת לוגים ספציפיים מתוך התהליך של פתיחת הקופסה. |

## Recommended Reading & Enrichment Links

* **Apple Platform Deployment - Automated Device Enrollment:**

  [https://support.apple.com/guide/deployment/dep24b435f66/web](https://support.apple.com/guide/deployment/dep24b435f66/web)
* **Apple Platform Security - Boot process for a Mac with Apple silicon:**

  [https://support.apple.com/guide/security/secc7b34e5b5/web](https://support.apple.com/guide/security/secc7b34e5b5/web)
* **Apple Support - Apple Intelligence Overview:**

  [https://support.apple.com/apple-intelligence](https://support.apple.com/apple-intelligence)

## סרטון סיכום

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/DDXfEIRgAxs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 💡 עזרים ויזואליים להרצאה (Presentation Visuals)

!!! tip "המחשה ויזואלית (עזר לתלמיד)"
    תמונות אלו ממחישות את הממשק או המנגנון הרלוונטי לנושא השיעור.

![Tahoe UI](../assets/images/Tahoe_UI/26-Tahoe-Settings-General-scaled.png)
![Tahoe UI](../assets/images/Tahoe_UI/26-Tahoe-Finder-Control-Center-scaled.png)
![Tahoe UI](../assets/images/Tahoe_UI/26-Tahoe-Finder-Control-Center-Edit-scaled.png)
![Tahoe UI](../assets/images/Tahoe_UI/26-Tahoe-Finder-Customize-scaled.png)
![Tahoe UI](../assets/images/Tahoe_UI/26-Tahoe-Finder-Desktop-Stacks-scaled.png)
![Tahoe UI](../assets/images/Tahoe_UI/26-Tahoe-Finder-Stacks-scaled.png)
![Tahoe UI](../assets/images/Tahoe_UI/26-Tahoe-Notification-Center-scaled.png)
![Tahoe UI](../assets/images/Tahoe_UI/26-Tahoe-Settings-Battery-scaled.png)
![Tahoe UI](../assets/images/Tahoe_UI/26-Tahoe-Finder-Copy-scaled.png)
![Tahoe UI](../assets/images/Tahoe_UI/26-Tahoe-Finder-Go-To-Folder-scaled.png)
![DeepDive Diagram](../assets/images/DeepDive/macOS Versions.png)
![M-Series Performance Comparison](../assets/images/Evolution_Keynote/image17.jpeg)
![Mac mini Evolution](../assets/images/Evolution_Keynote/Slide2_image3.jpeg)
![Apple Silicon Architecture](../assets/images/Evolution_Keynote/Slide3_image4.jpeg)

---
<div dir="rtl" style="text-align: left;">
  <a href="../../Lesson_02/LearningGuide/" style="font-size: 0.95em; color: gray; text-decoration: none;">⏭️ דלג לאותו שלב בשיעור הבא</a>
</div>

![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide6_image11.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide6_image1.tif)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide6_image10.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide6_image8.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide6_image9.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide7_image2.tif)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide8_image3.tif)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide9_image12.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide10_image13.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide10_image16.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide10_image15.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide10_image14.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide11_image4.tif)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide13_image14.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide13_image17.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide13_image13.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide14_image7.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide14_image6.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide14_image18.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide14_image24.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide14_image9.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide14_image19.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide14_image22.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide14_image23.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide14_image21.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide14_image8.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide14_image20.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide14_image10.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide15_image26.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide15_image27.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide15_image19.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide15_image25.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide16_image13.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide16_image14.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide16_image15.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide20_image31.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide20_image32.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide21_image34.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide21_image35.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide21_image37.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide21_image36.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide21_image33.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide21_image19.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide21_image5.tif)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide21_image6.tif)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide21_image38.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide22_image40.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide22_image39.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide25_image11.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide26_image12.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide26_image43.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide27_image44.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide27_image45.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide28_image46.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide29_image47.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide30_image49.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide30_image48.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide33_image52.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide35_image13.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide35_image16.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide36_image13.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide36_image19.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide36_image15.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide36_image14.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide36_image18.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide36_image17.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide36_image16.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide36_image20.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide36_image54.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide36_image52.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide37_image21.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide42_image54.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide42_image20.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide42_image16.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide42_image52.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide42_image17.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide42_image18.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide42_image14.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide42_image15.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide42_image19.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide42_image13.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide43_image7.tif)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide43_image56.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide43_image57.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide45_image58.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide46_image59.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide47_image60.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide49_image61.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide50_image62.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide52_image63.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide54_image68.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide55_image25.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide55_image24.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide55_image69.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide56_image27.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide56_image70.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide56_image71.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide56_image26.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide56_image28.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide56_image69.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide58_image20.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide58_image30.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide60_image31.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide62_image74.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide63_image33.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide63_image35.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide63_image42.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide63_image39.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide63_image38.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide63_image43.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide63_image34.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide63_image37.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide63_image40.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide63_image41.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide63_image36.jpeg)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide63_image77.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide63_image76.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide63_image75.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide84_image98.png)
![Legacy Slide](../assets/images/Legacy_Presentation/01_Evolution/Slide93_image101.png)
![DeepDive Screenshot](../assets/images/DeepDive/DeepDive_Explainer_Memory_AboutThisMac.jpg)
