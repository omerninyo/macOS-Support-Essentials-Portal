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

## קישורים מומלצים ולקריאה נוספת

* [Explainer: Memory](https://eclecticlight.co/2026/06/20/explainer-memory/) - מאמר עומק המסביר את אופן ניהול הזיכרון במערכת ההפעלה.

## סרטון סיכום

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/DDXfEIRgAxs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 💡 עזרים ויזואליים להרצאה (Presentation Visuals)

![Explainer Memory AboutThisMac](../assets/images/Lesson_01/L01_DeepDive_Explainer_Memory_AboutThisMac.jpg)
![macOS Versions](../assets/images/Lesson_01/L01_DeepDive_macOS_Versions.png)
![Apple Silicon Architecture](../assets/images/Lesson_01/L01_LegacySlide_Apple_Silicon_Architecture.jpeg)
![M-Series Performance Comparison](../assets/images/Lesson_01/L01_LegacySlide_M-Series_Performance_Comparison.jpeg)
![Mac mini Evolution](../assets/images/Lesson_01/L01_LegacySlide_Mac_mini_Evolution.jpeg)
![Slide10 image13](../assets/images/Lesson_01/L01_LegacySlide_Slide10_image13.png)
![Slide10 image14](../assets/images/Lesson_01/L01_LegacySlide_Slide10_image14.png)
![Slide10 image15](../assets/images/Lesson_01/L01_LegacySlide_Slide10_image15.png)
![Slide10 image16](../assets/images/Lesson_01/L01_LegacySlide_Slide10_image16.png)
![Slide11 image4](../assets/images/Lesson_01/L01_LegacySlide_Slide11_image4.tif)
![Slide13 image13](../assets/images/Lesson_01/L01_LegacySlide_Slide13_image13.png)
![Slide13 image14](../assets/images/Lesson_01/L01_LegacySlide_Slide13_image14.png)
![Slide13 image17](../assets/images/Lesson_01/L01_LegacySlide_Slide13_image17.png)
![Slide14 image10](../assets/images/Lesson_01/L01_LegacySlide_Slide14_image10.jpeg)
![Slide14 image18](../assets/images/Lesson_01/L01_LegacySlide_Slide14_image18.png)
![Slide14 image19](../assets/images/Lesson_01/L01_LegacySlide_Slide14_image19.png)
![Slide14 image20](../assets/images/Lesson_01/L01_LegacySlide_Slide14_image20.png)
![Slide14 image21](../assets/images/Lesson_01/L01_LegacySlide_Slide14_image21.png)
![Slide14 image22](../assets/images/Lesson_01/L01_LegacySlide_Slide14_image22.png)
![Slide14 image23](../assets/images/Lesson_01/L01_LegacySlide_Slide14_image23.png)
![Slide14 image24](../assets/images/Lesson_01/L01_LegacySlide_Slide14_image24.png)
![Slide14 image6](../assets/images/Lesson_01/L01_LegacySlide_Slide14_image6.jpeg)
![Slide14 image7](../assets/images/Lesson_01/L01_LegacySlide_Slide14_image7.jpeg)
![Slide14 image8](../assets/images/Lesson_01/L01_LegacySlide_Slide14_image8.jpeg)
![Slide14 image9](../assets/images/Lesson_01/L01_LegacySlide_Slide14_image9.jpeg)
![Slide15 image19](../assets/images/Lesson_01/L01_LegacySlide_Slide15_image19.png)
![Slide15 image25](../assets/images/Lesson_01/L01_LegacySlide_Slide15_image25.png)
![Slide15 image26](../assets/images/Lesson_01/L01_LegacySlide_Slide15_image26.png)
![Slide15 image27](../assets/images/Lesson_01/L01_LegacySlide_Slide15_image27.png)
![Slide16 image13](../assets/images/Lesson_01/L01_LegacySlide_Slide16_image13.png)
![Slide16 image14](../assets/images/Lesson_01/L01_LegacySlide_Slide16_image14.png)
![Slide16 image15](../assets/images/Lesson_01/L01_LegacySlide_Slide16_image15.png)
![Slide20 image31](../assets/images/Lesson_01/L01_LegacySlide_Slide20_image31.png)
![Slide20 image32](../assets/images/Lesson_01/L01_LegacySlide_Slide20_image32.png)
![Slide21 image19](../assets/images/Lesson_01/L01_LegacySlide_Slide21_image19.png)
![Slide21 image33](../assets/images/Lesson_01/L01_LegacySlide_Slide21_image33.png)
![Slide21 image34](../assets/images/Lesson_01/L01_LegacySlide_Slide21_image34.png)
![Slide21 image35](../assets/images/Lesson_01/L01_LegacySlide_Slide21_image35.png)
![Slide21 image36](../assets/images/Lesson_01/L01_LegacySlide_Slide21_image36.png)
![Slide21 image37](../assets/images/Lesson_01/L01_LegacySlide_Slide21_image37.png)
![Slide21 image38](../assets/images/Lesson_01/L01_LegacySlide_Slide21_image38.png)
![Slide21 image5](../assets/images/Lesson_01/L01_LegacySlide_Slide21_image5.tif)
![Slide21 image6](../assets/images/Lesson_01/L01_LegacySlide_Slide21_image6.tif)
![Slide22 image39](../assets/images/Lesson_01/L01_LegacySlide_Slide22_image39.png)
![Slide22 image40](../assets/images/Lesson_01/L01_LegacySlide_Slide22_image40.png)
![Slide25 image11](../assets/images/Lesson_01/L01_LegacySlide_Slide25_image11.jpeg)
![Slide26 image12](../assets/images/Lesson_01/L01_LegacySlide_Slide26_image12.jpeg)
![Slide26 image43](../assets/images/Lesson_01/L01_LegacySlide_Slide26_image43.png)
![Slide27 image44](../assets/images/Lesson_01/L01_LegacySlide_Slide27_image44.png)
![Slide27 image45](../assets/images/Lesson_01/L01_LegacySlide_Slide27_image45.png)
![Slide28 image46](../assets/images/Lesson_01/L01_LegacySlide_Slide28_image46.png)
![Slide29 image47](../assets/images/Lesson_01/L01_LegacySlide_Slide29_image47.png)
![Slide30 image48](../assets/images/Lesson_01/L01_LegacySlide_Slide30_image48.png)
![Slide30 image49](../assets/images/Lesson_01/L01_LegacySlide_Slide30_image49.png)
![Slide33 image52](../assets/images/Lesson_01/L01_LegacySlide_Slide33_image52.png)
![Slide35 image13](../assets/images/Lesson_01/L01_LegacySlide_Slide35_image13.png)
![Slide35 image16](../assets/images/Lesson_01/L01_LegacySlide_Slide35_image16.png)
![Slide36 image13](../assets/images/Lesson_01/L01_LegacySlide_Slide36_image13.jpeg)
![Slide36 image14](../assets/images/Lesson_01/L01_LegacySlide_Slide36_image14.jpeg)
![Slide36 image15](../assets/images/Lesson_01/L01_LegacySlide_Slide36_image15.jpeg)
![Slide36 image16](../assets/images/Lesson_01/L01_LegacySlide_Slide36_image16.jpeg)
![Slide36 image17](../assets/images/Lesson_01/L01_LegacySlide_Slide36_image17.jpeg)
![Slide36 image18](../assets/images/Lesson_01/L01_LegacySlide_Slide36_image18.jpeg)
![Slide36 image19](../assets/images/Lesson_01/L01_LegacySlide_Slide36_image19.jpeg)
![Slide36 image20](../assets/images/Lesson_01/L01_LegacySlide_Slide36_image20.jpeg)
![Slide36 image52](../assets/images/Lesson_01/L01_LegacySlide_Slide36_image52.png)
![Slide36 image54](../assets/images/Lesson_01/L01_LegacySlide_Slide36_image54.png)
![Slide37 image21](../assets/images/Lesson_01/L01_LegacySlide_Slide37_image21.jpeg)
![Slide42 image13](../assets/images/Lesson_01/L01_LegacySlide_Slide42_image13.jpeg)
![Slide42 image14](../assets/images/Lesson_01/L01_LegacySlide_Slide42_image14.jpeg)
![Slide42 image15](../assets/images/Lesson_01/L01_LegacySlide_Slide42_image15.jpeg)
![Slide42 image16](../assets/images/Lesson_01/L01_LegacySlide_Slide42_image16.jpeg)
![Slide42 image17](../assets/images/Lesson_01/L01_LegacySlide_Slide42_image17.jpeg)
![Slide42 image18](../assets/images/Lesson_01/L01_LegacySlide_Slide42_image18.jpeg)
![Slide42 image19](../assets/images/Lesson_01/L01_LegacySlide_Slide42_image19.jpeg)
![Slide42 image20](../assets/images/Lesson_01/L01_LegacySlide_Slide42_image20.jpeg)
![Slide42 image52](../assets/images/Lesson_01/L01_LegacySlide_Slide42_image52.png)
![Slide42 image54](../assets/images/Lesson_01/L01_LegacySlide_Slide42_image54.png)
![Slide43 image56](../assets/images/Lesson_01/L01_LegacySlide_Slide43_image56.png)
![Slide43 image57](../assets/images/Lesson_01/L01_LegacySlide_Slide43_image57.png)
![Slide43 image7](../assets/images/Lesson_01/L01_LegacySlide_Slide43_image7.tif)
![Slide45 image58](../assets/images/Lesson_01/L01_LegacySlide_Slide45_image58.png)
![Slide46 image59](../assets/images/Lesson_01/L01_LegacySlide_Slide46_image59.png)
![Slide47 image60](../assets/images/Lesson_01/L01_LegacySlide_Slide47_image60.png)
![Slide49 image61](../assets/images/Lesson_01/L01_LegacySlide_Slide49_image61.png)
![Slide50 image62](../assets/images/Lesson_01/L01_LegacySlide_Slide50_image62.png)
![Slide52 image63](../assets/images/Lesson_01/L01_LegacySlide_Slide52_image63.png)
![Slide54 image68](../assets/images/Lesson_01/L01_LegacySlide_Slide54_image68.png)
![Slide55 image24](../assets/images/Lesson_01/L01_LegacySlide_Slide55_image24.jpeg)
![Slide55 image25](../assets/images/Lesson_01/L01_LegacySlide_Slide55_image25.jpeg)
![Slide55 image69](../assets/images/Lesson_01/L01_LegacySlide_Slide55_image69.png)
![Slide56 image26](../assets/images/Lesson_01/L01_LegacySlide_Slide56_image26.jpeg)
![Slide56 image27](../assets/images/Lesson_01/L01_LegacySlide_Slide56_image27.jpeg)
![Slide56 image28](../assets/images/Lesson_01/L01_LegacySlide_Slide56_image28.jpeg)
![Slide56 image69](../assets/images/Lesson_01/L01_LegacySlide_Slide56_image69.png)
![Slide56 image70](../assets/images/Lesson_01/L01_LegacySlide_Slide56_image70.png)
![Slide56 image71](../assets/images/Lesson_01/L01_LegacySlide_Slide56_image71.png)
![Slide58 image20](../assets/images/Lesson_01/L01_LegacySlide_Slide58_image20.png)
![Slide58 image30](../assets/images/Lesson_01/L01_LegacySlide_Slide58_image30.jpeg)
![Slide60 image31](../assets/images/Lesson_01/L01_LegacySlide_Slide60_image31.jpeg)
![Slide62 image74](../assets/images/Lesson_01/L01_LegacySlide_Slide62_image74.png)
![Slide63 image33](../assets/images/Lesson_01/L01_LegacySlide_Slide63_image33.jpeg)
![Slide63 image34](../assets/images/Lesson_01/L01_LegacySlide_Slide63_image34.jpeg)
![Slide63 image35](../assets/images/Lesson_01/L01_LegacySlide_Slide63_image35.jpeg)
![Slide63 image36](../assets/images/Lesson_01/L01_LegacySlide_Slide63_image36.jpeg)
![Slide63 image37](../assets/images/Lesson_01/L01_LegacySlide_Slide63_image37.jpeg)
![Slide63 image38](../assets/images/Lesson_01/L01_LegacySlide_Slide63_image38.jpeg)
![Slide63 image39](../assets/images/Lesson_01/L01_LegacySlide_Slide63_image39.jpeg)
![Slide63 image40](../assets/images/Lesson_01/L01_LegacySlide_Slide63_image40.jpeg)
![Slide63 image41](../assets/images/Lesson_01/L01_LegacySlide_Slide63_image41.jpeg)
![Slide63 image42](../assets/images/Lesson_01/L01_LegacySlide_Slide63_image42.jpeg)
![Slide63 image43](../assets/images/Lesson_01/L01_LegacySlide_Slide63_image43.jpeg)
![Slide63 image75](../assets/images/Lesson_01/L01_LegacySlide_Slide63_image75.png)
![Slide63 image76](../assets/images/Lesson_01/L01_LegacySlide_Slide63_image76.png)
![Slide63 image77](../assets/images/Lesson_01/L01_LegacySlide_Slide63_image77.png)
![Slide6 image1](../assets/images/Lesson_01/L01_LegacySlide_Slide6_image1.tif)
![Slide6 image10](../assets/images/Lesson_01/L01_LegacySlide_Slide6_image10.png)
![Slide6 image11](../assets/images/Lesson_01/L01_LegacySlide_Slide6_image11.png)
![Slide6 image8](../assets/images/Lesson_01/L01_LegacySlide_Slide6_image8.png)
![Slide6 image9](../assets/images/Lesson_01/L01_LegacySlide_Slide6_image9.png)
![Slide7 image2](../assets/images/Lesson_01/L01_LegacySlide_Slide7_image2.tif)
![Slide84 image98](../assets/images/Lesson_01/L01_LegacySlide_Slide84_image98.png)
![Slide8 image3](../assets/images/Lesson_01/L01_LegacySlide_Slide8_image3.tif)
![Slide93 image101](../assets/images/Lesson_01/L01_LegacySlide_Slide93_image101.png)
![Slide9 image12](../assets/images/Lesson_01/L01_LegacySlide_Slide9_image12.png)
![26-Tahoe-Finder-Control-Center-Edit-scaled](../assets/images/Lesson_01/L01_TahoeUI_26-Tahoe-Finder-Control-Center-Edit-scaled.png)
![26-Tahoe-Finder-Control-Center-scaled](../assets/images/Lesson_01/L01_TahoeUI_26-Tahoe-Finder-Control-Center-scaled.png)
![26-Tahoe-Finder-Copy-scaled](../assets/images/Lesson_01/L01_TahoeUI_26-Tahoe-Finder-Copy-scaled.png)
![26-Tahoe-Finder-Customize-scaled](../assets/images/Lesson_01/L01_TahoeUI_26-Tahoe-Finder-Customize-scaled.png)
![26-Tahoe-Finder-Desktop-Stacks-scaled](../assets/images/Lesson_01/L01_TahoeUI_26-Tahoe-Finder-Desktop-Stacks-scaled.png)
![26-Tahoe-Finder-Go-To-Folder-scaled](../assets/images/Lesson_01/L01_TahoeUI_26-Tahoe-Finder-Go-To-Folder-scaled.png)
![26-Tahoe-Finder-Stacks-scaled](../assets/images/Lesson_01/L01_TahoeUI_26-Tahoe-Finder-Stacks-scaled.png)
![26-Tahoe-Notification-Center-scaled](../assets/images/Lesson_01/L01_TahoeUI_26-Tahoe-Notification-Center-scaled.png)
![26-Tahoe-Settings-Battery-scaled](../assets/images/Lesson_01/L01_TahoeUI_26-Tahoe-Settings-Battery-scaled.png)
![26-Tahoe-Settings-General-scaled](../assets/images/Lesson_01/L01_TahoeUI_26-Tahoe-Settings-General-scaled.png)

!!! tip "המחשה ויזואלית (עזר לתלמיד)"
    תמונות אלו ממחישות את הממשק או המנגנון הרלוונטי לנושא השיעור.