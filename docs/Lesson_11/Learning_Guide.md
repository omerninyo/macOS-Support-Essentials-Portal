# שיעור 11: ציוד היקפי
**מדריך עזר לתלמיד**

## 🎧 סקירה (פודקאסט)

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/fd31f0d4-5f45-4a2f-acea-e9d8ba503f57/"></iframe></div>

---

## מונחי ליבה ומושגים

| מושג | רקע ומשמעות |
| :--- | :--- |
| **Accessory Security** | מנגנון אבטחה במחשבי Apple Silicon הדורש אישור מפורש של המשתמש לפני שאביזרי USB/Thunderbolt מורשים לתקשר עם המערכת (מגן מפני התקפות פיזיות). ניתן לנהל זאת דרך System Settings -> Privacy & Security או MDM. |
| **Thunderbolt vs. USB-C** | צורת החיבור הפיזית (Type-C) לעיתים זהה, אך הפרוטוקול שונה לחלוטין. כבלי ויציאות Thunderbolt 3/4 תומכים בהעברת נתונים של עד 40Gbps. Thunderbolt 5 מגדיל את קצב ההעברה עד 80Gbps ועד ל-120Gbps במצב Asymmetric. |
| **DFU Port** | יציאת USB-C ספציפית ב-Mac (בעיקר במחשבי Apple Silicon) המיועדת להכנסת המחשב למצב שחזור קושחה עמוק (Revive/Restore) באמצעות Apple Configurator (לרוב היציאה השמאלית הקרובה ביותר למשתמש). |
| **CUPS** | Common Unix Printing System. מנוע ההדפסה המובנה של macOS, המנהל את כל תורי ההדפסה, מנהלי ההתקנים (Drivers) ופרוטוקולי הרשת עבור מדפסות. |
| **PPD** | PostScript Printer Description. קובץ "שרטוט" המשמש את CUPS כדי להבין את היכולות של מדפסת ספציפית (גדלי נייר, מגשים, צבע). |
| **AirPrint** | פרוטוקול אלחוטי של Apple המאפשר הדפסה ללא צורך בהתקנת דרייברים, מבוסס על IPP ומשתמש ב-Bonjour (mDNS) לגילוי ברשת. |

!!! note "הערה טכנית (הפרעות תדרים)"
    התקני USB 3.0 עשויים לפלוט רעשי RF בתדר של 2.4 GHz. רעש זה מתנגש ישירות עם התדר של קישוריות Bluetooth ו-Wi-Fi. במידה והעכבר האלחוטי מקרטע ללא הסבר, בדקו האם קיים מתאם USB 3.0 קרוב מדי למק.

    *→ תדרי 2.4GHz והיחסים בין Wi-Fi ל-Bluetooth נלמדו בשיעור 09 (רשתות) — אותו עקרון בדיוק מסביר מדוע מתאם USB 3.0 גורם לעכבר לקרטע.*

---

## רשימת פקודות טרמינל (CLI)

!!! warning
    פקודות הניהול של מערכת ה-CUPS דורשות הרשאות (כגון `sudo` לשינויים), אך לניטור ותשאול אין צורך בהרשאות גבוהות.

### ניהול ואבחון הדפסה (CUPS)
| פקודה | תיאור |
|---|---|
| `lpstat -t` | פקודת העל לאבחון CUPS: מדפיסה את כל המידע האפשרי אודות מצב מערכת ההדפסה, המדפסות והתורים. |
| `cancel -a` | ביטול ומחיקת כל עבודות ההדפסה בכל התורים (שימושי לניקוי תור "תקוע"). |
| `cupsctl WebInterface=yes` | הפעלת ממשק הניהול הוובי הנסתר של CUPS. הגישה מתבצעת בדפדפן בכתובת `http://localhost:631` (יש להחזיר ל-no בסיום). |
| `lpinfo -v` | מציג את כל המכשירים (מדפסות המחוברות פיזית או זמינות ברשת) שמערכת CUPS מזהה. |

### כלי System Profiler לאבחון ציוד היקפי
פקודת `system_profiler` מאפשרת לשלוף מידע חומרתי ללא ה-GUI:
* `system_profiler SPUSBDataType` - מציג פירוט התקני USB.
* `system_profiler SPThunderboltDataType` - מציג פירוט על יציאות ה-Thunderbolt ומהירויות הקישור (Link Status).
* `system_profiler SPBluetoothDataType` - מציג סטטוס Bluetooth ורמות סוללה של התקנים מקושרים.

> *→ ה-CUPS רץ כ-Daemon תחת launchd — נלמד בשיעור 08 (Terminal). אפשר לעקוב אחרי `cupsd` בדיוק כמו אחרי כל Daemon אחר: דרך Console או `log stream --predicate 'process == "cupsd"'`.*

---

## Enterprise Seasoning: אבטחה ומדפסות בארגון

!!! important "Accessory Security בסביבה ארגונית"
    הגדירו ב-MDM את מדיניות ה-Accessory Security ל-"Ask for New Accessories" לפחות כדי למנוע התקפות BadUSB ("Rubber Ducky"). הגדרה "Always" מכסה תמתי מהאבטחה ולא מומלצת למקים פגישים עם ניידה באוכלוסייה.

בארגונים המנוהלים על ידי MDM ו-DDM (Declarative Device Management), מנהלי ה-IT משתמשים בפרופילים נסתרים כדי להקל על עובדים ולאבטח ציוד:
* **Storage Management:** מאפשר לחסום חיבור דיסק-און-קי לחלוטין (Disallowed) או להתיר אותו לקריאה-בלבד (Read-Only) למניעת זליגת מידע (DLP).
* **Printer Payloads:** מאפשר הפצה אוטומטית ושקטה של מדפסות הרשת המשרדיות ללא צורך בהתערבות העובד. המדפסת פשוט תופיע בחלון ההדפסה.

---

## נתיבים וקבצים רלוונטיים (Paths)

| נתיב / קובץ | תיאור |
|---|---|
| `/etc/cups/` | התיקייה המכילה את קבצי ההגדרות הפנימיים של CUPS. |
| `/Library/Printers/` | התיקייה בה מותקנים מנהלי התקנים (Drivers) וקבצי ה-PPD. |
| `/var/spool/cups/` | תיקיית התור הזמנית (Spool) בה מאוחסנים קבצים הממתינים להדפסה. |

---

## קישורים מומלצים ולקריאה נוספת

* [Troubleshoot peripheral connections on Mac](https://support.apple.com/guide/apple-platform-support/troubleshoot-peripheral-connections-aps3b8ff2373/web)
* [Allow accessories to connect to Mac](https://support.apple.com/guide/mac-help/allow-accessories-to-connect-mchlf779ae93/mac)
* [Manage printer profiles in Apple devices](https://support.apple.com/guide/apple-platform-deployment/printing-payload-settings-apdeb12df380/web)
* [Thunderbolt ports aren’t all the same](https://eclecticlight.co/2025/01/14/thunderbolt-ports-arent-all-the-same/) - סקירה טכנית על הבדלים ב-Thunderbolt.
* [A brief history of the Chooser and printer support](https://eclecticlight.co/2024/10/12/a-brief-history-of-the-chooser-and-printer-support/)

---

## 🎬 סרטון סיכום

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/Dxkv03JlXrE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

## 💡 עזרים ויזואליים להרצאה (Presentation Visuals)

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
