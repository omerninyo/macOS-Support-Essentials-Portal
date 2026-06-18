# סיכום שיעור: פרק 11 - חיבוריות וציוד היקפי (Peripherals & Printing)

## 1. נושאי השיעור

*   **1.** **ניהול ציוד חיצוני:** הבדלים בין חיבורי Thunderbolt, USB-C ו-Bluetooth.
*   **2.** **אבטחת אביזרים (Accessory Security):** מנגנוני אישור אביזרים וחיבורי USB חדשים.
*   **3.** **הדפסה ב-macOS:** ניהול והגדרת מדפסות רשת ומקומיות דרך הממשק (CUPS).
*   **4.** **תיבול ארגוני:** נעילת יציאות USB והפצת מדפסות באופן אוטומטי.

מסמך זה מרכז את כל המושגים, הפקודות והכלים החשובים לניהול ואבחון ציוד היקפי, חיבורים ומדפסות בסביבת macOS מודרנית ובסביבה ארגונית (MDM).

## מונחי ליבה ומושגים

* **Accessory Security:** מנגנון אבטחה ב-Mac עם Apple Silicon הדורש אישור מפורש של המשתמש לפני שאביזרי USB או Thunderbolt (או כרטיסי SD) מורשים לתקשר עם המערכת. ניתן לניהול דרך System Settings -> Privacy & Security או דרך פרופילי MDM.
* **Thunderbolt vs. USB-C:** צורת החיבור הפיזית (Type-C) לעיתים זהה, אך הפרוטוקול שונה. כבלי ויציאות Thunderbolt 3/4 תומכים במהירויות העברת נתונים גבוהות משמעותית (עד 40Gbps) ובשרשור מכשירים (Daisy Chaining), לעומת כבלי USB סטנדרטיים.
* **DFU Port:** יציאת USB-C ספציפית ב-Mac (בעיקר במחשבי Apple Silicon) המיועדת להכנסת המחשב למצב DFU לצורך שחזור קושחה (Revive/Restore) באמצעות Apple Configurator. במחשבים ניידים זו לרוב היציאה השמאלית הקרובה ביותר למשתמש.
* **CUPS - Common Unix Printing System:** מנוע ההדפסה המובנה של macOS. מערכת מבוססת קוד פתוח (שפותחה במקור על ידי Apple) המנהלת את כל תורי ההדפסה, מנהלי ההתקנים, ופרוטוקולי הרשת עבור מדפסות.
* **AirPrint:** פרוטוקול אלחוטי של Apple המאפשר הדפסה ללא צורך בהתקנת מנהלי התקנים (Drivers) ייעודיים. נתמך במרבית המדפסות המודרניות.
* **Printing Payload:** Payload (הגדרת תצורה) של MDM המאפשר למנהלי רשת להגדיר מדפסות, רשימות מדפסות, ומדפסות ברירת מחדל מרחוק.
* **AirPrint Payload:** Payload MDM המאפשר הפצה שקטה של כתובות IP וניתוב של מדפסות התומכות ב-AirPrint למשתמשי הארגון.
* **PPD - PostScript Printer Description:** קובץ הגדרות המשמש את CUPS כדי להבין את יכולות המדפסת הספציפית (גדלי נייר, מגשים, הדפסה בצבע).

## רשימת פקודות טרמינל (CLI)

### ניהול ואבחון הדפסה (CUPS)
מערכת ההדפסה ב-macOS ניתנת לניהול מלא ומהיר משורת הפקודה.

* `lpstat -p` - הצגת רשימת כל המדפסות המותקנות במק והסטטוס הנוכחי שלהן.
* `lpstat -a` - בדיקה האם המדפסות מקבלות עבודות הדפסה חדשות.
* `lpstat -o` - הצגת תור עבודות ההדפסה הנוכחי.
* `lpstat -t` - פקודת העל לאבחון CUPS: מדפיסה את כל המידע האפשרי אודות מצב מערכת ההדפסה, המדפסות, התורים וזמינות השירות.
* `cancel -a` - ביטול ומחיקת כל עבודות ההדפסה בכל התורים (שימושי מאוד לניקוי תור "תקוע" שמונע הדפסות נוספות).
* `cancel <job_id>` - ביטול עבודת הדפסה ספציפית (את ה-ID ניתן להוציא מפקודת `lpstat -o`).
* `cupsctl WebInterface=yes` - הפעלת ממשק הניהול הוובי של CUPS. לאחר הפעלת פקודה זו, ניתן לגשת לממשק גרפי מתקדם דרך הדפדפן בכתובת `http://localhost:631`. (כדי לכבות יש לשנות ל-`no`).
* `lpinfo -m` - הצגת כל מנהלי ההתקנים (Drivers / PPDs) הזמינים במערכת.
* `lpinfo -v` - הצגת כל המכשירים (מדפסות המחוברות פיזית ב-USB או כאלו שזמינות ברשת) שמערכת CUPS מזהה כרגע.

### כלי System Profiler לאבחון ציוד היקפי
פקודת `system_profiler` מאפשרת לשלוף מידע מפורט על רכיבי חומרה ישירות בטרמינל, בדיוק כפי שמופיע באפליקציית System Information.

* `system_profiler SPUSBDataType` - הצגת רשימה מפורטת של כל התקני ה-USB המחוברים כרגע למק (כולל רכזות, מקלדות, דיסקים, ומתאמים).
* `system_profiler SPThunderboltDataType` - הצגת פירוט על יציאות ה-Thunderbolt במק, מהירויות הקישור (Link Status) והתקנים מחוברים. שימושי לאבחון ציוד שלא מנצל את המהירות המלאה.
* `system_profiler SPPrintersDataType` - שליפת מידע מפורט על כל מדפסת שמוגדרת במערכת, כולל גרסת הדרייבר, נתיב ה-PPD המדויק, וה-URI (כתובת הרשת/החיבור) שלה.
* `system_profiler SPBluetoothDataType` - הצגת סטטוס התקני Bluetooth, כולל רמות סוללה וכתובות MAC.

### רשת ושירותים
* `networksetup -listallhardwareports` - הצגת כל ממשקי הרשת במק. לעיתים מדפסות רשת מוגדרות עם ממשק וירטואלי משלהן, או שחשוב לוודא שמתאם רשת חיצוני (USB to Ethernet) מזוהה כראוי על ידי המערכת ברמת החומרה.

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