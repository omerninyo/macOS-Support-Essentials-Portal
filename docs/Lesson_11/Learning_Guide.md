# שיעור 11: ציוד היקפי
**מדריך עזר לתלמיד (גרסת vEXP)**


## סקירה

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/fd31f0d4-5f45-4a2f-acea-e9d8ba503f57/"></iframe></div>

## מונחי ליבה ומושגים

* **המונח Accessory Security:** מנגנון אבטחה ב-Mac עם Apple Silicon הדורש אישור מפורש של המשתמש לפני שאביזרי USB או Thunderbolt (או כרטיסי SD) מורשים לתקשר עם המערכת. ניתן לניהול דרך System Settings -> Privacy & Security או דרך פרופילי MDM.
* **המונח Thunderbolt vs. USB-C:** צורת החיבור הפיזית (Type-C) לעיתים זהה, אך הפרוטוקול שונה. כבלי ויציאות Thunderbolt 3/4 תומכים במהירויות העברת נתונים גבוהות משמעותית (עד 40Gbps) ובשרשור מכשירים (Daisy Chaining), לעומת כבלי USB סטנדרטיים. תקן Thunderbolt 5 מגדיל את קצב ההעברה עד 80Gbps ועד ל-120Gbps במצב Asymmetric.
* **המונח DFU Port:** יציאת USB-C ספציפית ב-Mac (בעיקר במחשבי Apple Silicon) המיועדת להכנסת המחשב למצב DFU לצורך שחזור קושחה (Revive/Restore) באמצעות Apple Configurator. במחשבים ניידים זו לרוב היציאה השמאלית הקרובה ביותר למשתמש.
* **המונח CUPS - Common Unix Printing System:** מנוע ההדפסה המובנה של macOS. מערכת מבוססת קוד פתוח (שפותחה במקור על ידי Apple) המנהלת את כל תורי ההדפסה, מנהלי ההתקנים, ופרוטוקולי הרשת עבור מדפסות.
* **המונח The Chooser (היסטוריה):** כלי ניהול מדפסות רשת מוקדם של אפל, שהחל את דרכו כ-Choose Printer ב-1984 והפך ל-Chooser המיתולוגי ב-1991 (System 7).
* **המונח AirPrint:** פרוטוקול אלחוטי של Apple המאפשר הדפסה ללא צורך בהתקנת מנהלי התקנים (Drivers) ייעודיים. נתמך במרבית המדפסות המודרניות.
* **המונח Printing Payload:** Payload (הגדרת תצורה) של MDM המאפשר למנהלי רשת להגדיר מדפסות, רשימות מדפסות, ומדפסות ברירת מחדל מרחוק.
* **המונח AirPrint Payload:** Payload MDM המאפשר הפצה שקטה של כתובות IP וניתוב של מדפסות התומכות ב-AirPrint למשתמשי הארגון.
* **המונח PPD - PostScript Printer Description:** קובץ הגדרות המשמש את CUPS כדי להבין את יכולות המדפסת הספציפית (גדלי נייר, מגשים, הדפסה בצבע).
* **המונח Declarative Device Management (DDM) Storage Management:** תצורת MDM הצהרתית במערכות macOS 15 ומעלה, המאפשרת ניהול קפדני של מדיניות גישה לכוננים חיצוניים ולכונני רשת (למשל חסימה מוחלטת או קריאה-בלבד).

## רשימת פקודות טרמינל (CLI)

### ניהול ואבחון הדפסה (CUPS)
מערכת ההדפסה ב-macOS ניתנת לניהול מלא ומהיר משורת הפקודה.

* `המונח lpstat -p` - הצגת רשימת כל המדפסות המותקנות במק והסטטוס הנוכחי שלהן.
* `המונח lpstat -a` - בדיקה האם המדפסות מקבלות עבודות הדפסה חדשות.
* `המונח lpstat -o` - הצגת תור עבודות ההדפסה הנוכחי.
* `המונח lpstat -t` - פקודת העל לאבחון CUPS: מדפיסה את כל המידע האפשרי אודות מצב מערכת ההדפסה, המדפסות, התורים וזמינות השירות.
* `המונח cancel -a` - ביטול ומחיקת כל עבודות ההדפסה בכל התורים (שימושי מאוד לניקוי תור "תקוע" שמונע הדפסות נוספות).
* `המונח cancel <job_id>` - ביטול עבודת הדפסה ספציפית (את ה-ID ניתן להוציא מפקודת `lpstat -o`).
* `המונח cupsctl WebInterface=yes` - הפעלת ממשק הניהול הוובי של CUPS. לאחר הפעלת פקודה זו, ניתן לגשת לממשק גרפי מתקדם דרך הדפדפן בכתובת `http://localhost:631`. (כדי לכבות יש לשנות ל-`no`).
* `המונח lpinfo -m` - הצגת כל מנהלי ההתקנים (Drivers / PPDs) הזמינים במערכת.
* `המונח lpinfo -v` - הצגת כל המכשירים (מדפסות המחוברות פיזית ב-USB או כאלו שזמינות ברשת) שמערכת CUPS מזהה כרגע.

### כלי System Profiler לאבחון ציוד היקפי
פקודת `system_profiler` מאפשרת לשלוף מידע מפורט על רכיבי חומרה ישירות בטרמינל, בדיוק כפי שמופיע באפליקציית System Information.

* `המונח system_profiler SPUSBDataType` - הצגת רשימה מפורטת של כל התקני ה-USB המחוברים כרגע למק (כולל רכזות, מקלדות, דיסקים, ומתאמים).
* `המונח system_profiler SPThunderboltDataType` - הצגת פירוט על יציאות ה-Thunderbolt במק, מהירויות הקישור (Link Status) והתקנים מחוברים. שימושי לאבחון ציוד שלא מנצל את המהירות המלאה.
* `המונח system_profiler SPPrintersDataType` - שליפת מידע מפורט על כל מדפסת שמוגדרת במערכת, כולל גרסת הדרייבר, נתיב ה-PPD המדויק, וה-URI (כתובת הרשת/החיבור) שלה.
* `המונח system_profiler SPBluetoothDataType` - הצגת סטטוס התקני Bluetooth, כולל רמות סוללה וכתובות MAC.

### רשת ושירותים

* `המונח networksetup -listallhardwareports` - הצגת כל ממשקי הרשת במק. לעיתים מדפסות רשת מוגדרות עם ממשק וירטואלי משלהן, או שחשוב לוודא שמתאם רשת חיצוני (USB to Ethernet) מזוהה כראוי על ידי המערכת ברמת החומרה.

## נתיבים וקבצים רלוונטיים (Paths)

* `/etc/cups/` - התיקייה המכילה את קבצי ההגדרות הפנימיים של מנוע ה-CUPS (למשל `cupsd.conf` ו-`printers.conf`). שינויים בקבצים אלו דורשים הרשאות root.
* `/Library/Printers/` - התיקייה בה מותקנים מנהלי התקנים (Drivers), פלאגינים וקבצי PPD של יצרניות מדפסות צד-שלישי.
* `/var/spool/cups/` - תיקיית התור הזמנית (Spool) בה מערכת CUPS מאחסנת קבצים הממתינים לביצוע הדפסה.
* `/Library/Managed Preferences/` - הנתיב בו נשמרים פרופילי התצורה (כמו Printing Payload או הגבלות Accessory Security) שנדחפו על ידי מערכת ה-MDM הארגונית.

## קישורים מומלצים ולקריאה נוספת

* [Troubleshoot peripheral connections on Mac](https://support.apple.com/guide/apple-platform-support/troubleshoot-peripheral-connections-aps3b8ff2373/web) - המדריך הרשמי למנהלי רשת לפתרון בעיות עם ציוד היקפי.
* [Allow accessories to connect to Mac](https://support.apple.com/guide/mac-help/allow-accessories-to-connect-mchlf779ae93/mac) - הסבר למשתמש על מנגנון אבטחת האביזרים החדש שחוסם חיבורי USB לא מוכרים.
* [Manage printer profiles in Apple devices](https://support.apple.com/guide/apple-platform-deployment/printing-payload-settings-apdeb12df380/web) - תיעוד ארגוני על הגדרת מדפסות מרחוק בעזרת MDM.
* [Thunderbolt ports aren’t all the same](https://eclecticlight.co/2025/01/14/thunderbolt-ports-arent-all-the-same/) - סקירת עומק טכנית על ההבדלים בין חיבורי Thunderbolt ו-USB-C השונים במחשבי מק.
* [A brief history of the Chooser and printer support](https://eclecticlight.co/2024/10/12/a-brief-history-of-the-chooser-and-printer-support/) - מאמר היסטורי על האבולוציה של הוספת מדפסות בסביבת המק מראשיתה ועד היום.

## סרטון סיכום

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/DDXfEIRgAxs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


!!! tip "המחשה ויזואלית (עזר לתלמיד)"
    תמונות אלו ממחישות את הממשק או המנגנון הרלוונטי לנושא השיעור.

![How_Thunderbolt_5_can_be_faster_or_not_p1_9](../assets/images/Lesson_11/L11_DeepDive_How_Thunderbolt_5_can_be_faster_or_not_p1_9.png)
![Slide139_image46](../assets/images/Lesson_11/L11_LegacySlide_Slide139_image46.jpg)
![Slide139_image47](../assets/images/Lesson_11/L11_LegacySlide_Slide139_image47.jpg)
![Slide140_image169](../assets/images/Lesson_11/L11_LegacySlide_Slide140_image169.png)
![Slide140_image49](../assets/images/Lesson_11/L11_LegacySlide_Slide140_image49.jpeg)
![Slide19_image29](../assets/images/Lesson_11/L11_LegacySlide_Slide19_image29.png)
![Slide19_image30](../assets/images/Lesson_11/L11_LegacySlide_Slide19_image30.png)
![Slide31_image50](../assets/images/Lesson_11/L11_LegacySlide_Slide31_image50.jpg)
![Slide31_image51](../assets/images/Lesson_11/L11_LegacySlide_Slide31_image51.jpg)
![Slide34_image52](../assets/images/Lesson_11/L11_LegacySlide_Slide34_image52.jpg)
![Slide34_image53](../assets/images/Lesson_11/L11_LegacySlide_Slide34_image53.jpg)
![Slide41_image53](../assets/images/Lesson_11/L11_LegacySlide_Slide41_image53.jpg)
![26-Tahoe-Print-scaled](../assets/images/Lesson_11/L11_TahoeUI_26-Tahoe-Print-scaled.png)
![26-Tahoe-Settings-Bluetooth-scaled](../assets/images/Lesson_11/L11_TahoeUI_26-Tahoe-Settings-Bluetooth-scaled.png)
![26-Tahoe-Settings-Printers-and-Scanners-scaled](../assets/images/Lesson_11/L11_TahoeUI_26-Tahoe-Settings-Printers-and-Scanners-scaled.png)
