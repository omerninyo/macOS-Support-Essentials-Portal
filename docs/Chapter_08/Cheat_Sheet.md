# Chapter 8: תהליכי רקע ומערכת Launchd - סיכום שיעור (Asset C)

## 1. נושאי השיעור

*   **1.** **הלב של המערכת:** היכרות עם תהליך launchd וסוגי ה-LaunchAgents וה-Daemons.
*   **2.** **Activity Monitor עמוק:** ניטור עומסי זיכרון ומעבד באבחון תקלות.
*   **3.** **קבצי Plist:** אבחון פריטי התחברות וקריאת נתוני XML במערכת.
*   **4.** **תיבול ארגוני:** איתור סוכני ה-MDM וטיפול בקריסות שלהם ברקע.

מסמך זה מרכז את מילון המושגים, הפקודות והנתיבים החשובים לניהול, ניטור ופתרון תקלות בשירותי הרקע של macOS, כולל `launchd`, קבצי `plist`, ושימוש ב-Activity Monitor.

---

## 📖 מילון מושגים ורכיבי ליבה

* **Launchd:** תהליך הליבה של macOS (התהליך הראשון שעולה – PID 1). הוא "ההורה" של כל שאר התהליכים ואחראי לטעינה, ניהול, ניטור וכיבוי של שירותים, אפליקציות ותהליכי רקע במערכת.
* **LaunchDaemon:** (LaunchDaemon) Background Process ברמת המערכת. פועל תחת משתמש ה-`root` ורץ גם אם אין משתמש מחובר למערכת. לרוב משמש כלי IT, אנטיווירוס (XProtect Remediator) וסוכני MDM.
* **LaunchAgent:** (LaunchAgent) Background Process ברמת המשתמש. מופעל רק כאשר משתמש נכנס למערכת (Login) ורץ תחת ההרשאות של אותו משתמש.
* **LaunchAngels:** רכיב חדש ומוגן ב-macOS 26 (Tahoe). אלו שירותי מערכת ייעודיים של אפל (למשל לתכונות נגישות מסוימות) שרצים תחת תנאים ספציפיים. הם מוגנים בתוך ה-Sealed System Volume (SSV) ואינם זמינים לשימוש למפתחי צד-שלישי.
* **Plist (Property List):** קובץ תצורה במבנה XML (לעיתים קרובות מקודד בינארית). בשימוש `launchd`, קובץ זה מגדיר *מה* להריץ, *מתי* להריץ (למשל בעת הפעלה מחדש או ברווחים קבועים) ואילו ארגומנטים להעביר.
* **Activity Monitor:** הכלי המובנה ב-macOS לניטור משאבי מערכת בזמן אמת, כולל מעבד (CPU), זיכרון (Memory), צריכת חשמל (Energy), כתיבה לדיסק (Disk) ופעילות רשת (Network).
* **Memory Pressure (לחץ זיכרון):** מדד ויזואלי ב-Activity Monitor המציג עד כמה המערכת מתאמצת לנהל את הזיכרון (ירוק = תקין, צהוב = בבדיקה, אדום = המערכת נאלצת להשתמש יותר מדי בכונן הקשיח לטובת Swap).
* **Swap Space:** "זיכרון וירטואלי". כאשר ה-RAM (זיכרון מאוחד ב-Apple Silicon) מתמלא, המערכת כותבת דפי זיכרון לכונן ה-SSD. עודף כתיבה/קריאה ל-Swap מאט את המערכת משמעותית.
* **MDM Agent:** ה-Daemon של פתרון ניהול המכשירים (כמו Jamf Daemon או Intune Agent) שרץ ברקע באופן קבוע ומוודא החלת Configuration Profiles ופקודות מרחוק.

---

## 🗂️ נתיבים קריטיים במערכת (System Paths)

המיקום של קובץ ה-Plist קובע אם התהליך יהיה של המערכת, של המשתמש, או ייעודי לאפל בלבד:

* **`/System/Library/LaunchDaemons/`** – שירותי מערכת פנימיים של Apple. מוגן (Read-Only) תחת SSV.
* **`/System/Library/LaunchAgents/`** – שירותי משתמש פנימיים של Apple. מוגן (Read-Only) תחת SSV.
* **`/System/Library/LaunchAngels/`** – התיקייה החדשה (מ-macOS 26) לשירותים מיוחדים מוגנים.
* **`/Library/LaunchDaemons/`** – המקום שאליו תוכנות צד שלישי (אנטיווירוס, MDM, VPN מנוהל) משליכות את התהליכים ברמת המערכת. גישה דורשת הרשאות מנהל (Admin).
* **`/Library/LaunchAgents/`** – תהליכי רקע צד שלישי שיופעלו עבור *כל* המשתמשים שיעשו Login למחשב.
* **`~/Library/LaunchAgents/`** – תהליכי רקע ייעודיים *רק למשתמש הספציפי*.

---

## 💻 מדריך פקודות טרמינל (CLI Commands)

### 1. הפקודה `launchctl` (ניהול תהליכי רקע)

> **שים לב:** התחביר הישן של `load/unload` כבר פחות מומלץ על ידי אפל, למרות שעוד עובד. התחביר המודרני משתמש ב-`bootstrap/bootout`.

**צפייה בתהליכים:**
* הצגת כל התהליכים שרצים כעת:
  ```bash
  launchctl list
  ```
* איתור תהליך ספציפי (למשל חיפוש שירות של חברת האבטחה או ה-MDM):
  ```bash
  launchctl list | grep -i mdm
  launchctl list | grep -i jamf
  ```
* קבלת מידע עמוק ומוחלט על תצורת ה-launchd כולה (טוב לשמירה לקובץ במקרה של דיאגנוסטיקה):
  ```bash
  launchctl dumpstate
  ```

**הפעלה ועצירה של שירותי מערכת (LaunchDaemons):**
* טעינת/רישום Daemon למערכת (מחייב `sudo`):
  ```bash
  sudo launchctl bootstrap system /Library/LaunchDaemons/com.example.daemon.plist
  ```
* הסרת/כיבוי Daemon מניהול המערכת:
  ```bash
  sudo launchctl bootout system /Library/LaunchDaemons/com.example.daemon.plist
  ```
* ביטול (Disable) טעינה עתידית של השירות:
  ```bash
  sudo launchctl disable system/com.example.daemon
  ```
* הפעלה כפויה (Start) של שירות קיים ללא קשר לתזמון שלו:
  ```bash
  sudo launchctl start com.example.daemon
  ```

**הפעלה ועצירה של שירותי משתמש (LaunchAgents):**
*(יש להריץ ללא sudo, ויש לציין את מזהה המשתמש - UID. ניתן למצוא את ה-UID על ידי הפקודה `id -u`)*
* טעינת Agent למשתמש:
  ```bash
  launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.example.agent.plist
  ```
* כיבוי Agent למשתמש:
  ```bash
  launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/com.example.agent.plist
  ```

### 2. הפקודה `plutil` (עבודה וקריאה של קבצי Plist)

קבצי Plist מגיעים לא פעם בתצורה בינארית שלא ניתנת לקריאה בעין בטרמינל. הפקודה `plutil` היא הכלי לעבוד איתם.

* **בדיקת תקינות סינטקס (Syntax Validation) לפני טעינה למערכת:**
  ```bash
  plutil -lint /Library/LaunchDaemons/com.example.daemon.plist
  ```
  *(הפקודה תחזיר `OK` אם הקובץ תקין, או תציין באיזו שורה יש שגיאה).*

* **המרת קובץ בינארי לקריאה כ-XML (ההדפסה תשנה את הקובץ המקורי):**
  ```bash
  sudo plutil -convert xml1 /path/to/file.plist
  ```

* **המרת הקובץ בחזרה לתצורה בינארית (חסכוני יותר במקום):**
  ```bash
  sudo plutil -convert binary1 /path/to/file.plist
  ```

* **הדפסת תוכן הקובץ בפורמט JSON קריא על המסך (מבלי לשנות את הקובץ פיזית):**
  ```bash
  plutil -p /path/to/file.plist
  ```

### 3. איתור לחץ מעבד וזיכרון דרך הטרמינל

למי שלא רוצה להשתמש ב-Activity Monitor אלא בממשק השורת פקודה:
* צפייה במשאבי המערכת בזמן אמת (מעבד וזיכרון, מתעדכן כל שניה):
  ```bash
  top -u
  ```
* הדפסת מדדי "לחץ הזיכרון" (Memory Pressure) ומצב ה-Swap:
  ```bash
  memory_pressure
  ```

---

## 🔗 Recommended Reading & Enrichment Links

להלן רשימה מאוצרת של מקורות קריאה להרחבת הידע ולהעמקה בנושאי רקע, Plists וניטור ביצועים (כולל הפניות למאמרי העומק של Apple ו-The Eclectic Light Company ששולבו בפרק):

1. **[Welcome to Tahoe’s Launch Angels (The Eclectic Light Company)](https://eclecticlight.co/)**  
   סקירה טכנית עמוקה אודות התיקייה והרכיב החדש שהוצג ב-macOS 26 Tahoe, מיקומו בתוך ה-SSV והסיבות שמפתחים חיצוניים אינם מורשים להשתמש בו.

2. **[Explainer: % CPU in Activity Monitor (The Eclectic Light Company)](https://eclecticlight.co/)**  
   מאמר המסביר מדוע מדד ה-% CPU לא תמיד משקף במדויק עומס קריטי במעבדי Apple Silicon מרובי הליבות (Performance vs. Efficiency).

3. **[Apple Activity Monitor User Guide: View Memory Usage](https://support.apple.com/guide/activity-monitor/)**  
   ההסבר הרשמי של אפל לאופן שבו מחושב מדד ה-Memory Pressure (לחץ הזיכרון) ולמה חשוב להסתכל עליו (ירוק, צהוב, אדום) במקום רק לספור כמה ג'יגה-בייט RAM פנויים נותרו.

4. **[Manage Login and Background items (The Eclectic Light Company)](https://eclecticlight.co/)**  
   צלילה לדרך שבה ה-OS מטפל בפריטי התחברות (Login Items) כחלק ממנגנון ה-LaunchAgents, ואיך מנהלי IT יכולים לעקוב אחריהם.

5. **[A brief history of XML and property lists (The Eclectic Light Company)](https://eclecticlight.co/)**  
   רקע היסטורי מצוין על הסיבה שאפל משתמשת בקבצי Plist (Property Lists) לניהול תהליכים, וכיצד אלו החליפו מנגנונים ישנים מבוססי טקסט או פורמטים קנייניים אחרים.
