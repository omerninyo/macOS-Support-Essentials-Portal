# שיעור 08: טרמינל ושירותי רקע
**מדריך עזר לתלמיד (גרסת vEXP מורחבת)**

---

## מטרות השיעור

* **מבוא לטרמינל (Terminal)** - למה ה-CLI קריטי לטכנאים, קיצורי מקלדת, ויישור קו לפני עבודה מתקדמת.
* **הלב של המערכת** - תהליך `launchd` (הבדל בין LaunchDaemons, Agents ו-LaunchAngels).
* **אבחון עמוק** - קריאת זיכרון ב-Activity Monitor, וקריאה/אבחון של קבצי Plist (XML).
* **תיבול ארגוני** - איתור ה-Agent של מערכת ה-MDM, הבנת ססטוס הסנכרון שלו ומה עושים כשהוא קורס.

---

## 🎧 האזנה לסיכום — לפני או אחרי השיעור

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/d1656076-9c58-4f49-be91-863f210a4214/"></iframe></div>

---

## מושגי יסוד וטרמינולוגיה

| מושג | הסבר |
|---|---|
| **CLI / Terminal** | ממשק שורת הפקודה במק (הגיע מ-NeXTSTEP ב-2001). כלי עבודה ישיר למערכת עוקף ממשק גרפי. |
| **Zsh (Z Shell)** | המעטפת (Shell) המודרנית של מק, ברירת המחדל מ-Catalina. |
| **PID (Process ID)** | מספר זיהוי ייחודי לכל תוכנה או שירות שרצים כרגע. |
| **launchd** | מנהל התהליכים העליון (PID 1). התוכנה הראשונה שקמה. אחראי להעלות שירותים ואפליקציות. |
| **LaunchDaemon** | סוכן תשתית שרץ ברקע כ-`root` (אפילו בלי משתמש מחובר). כמו סוכני MDM או אנטיווירוס. |
| **LaunchAgent** | סוכן של משתמש ספציפי, עולה רק כשהמשתמש עושה Login. |
| **LaunchAngels (Tahoe)** | שירותי מערכת פנימיים חדשים של אפל תחת המנגנון `RunningBoard`. נעולים לגמרי ב-SSV. |
| **Plist (Property List)** | קובץ הגדרות של אפל (XML או בינארי). שומר הכל: ממיקום חלונות עד תזמון משימות למערכת. |
| **Memory Pressure** | הגרף הקריטי ב-Activity Monitor המראה את "מאמץ" הזיכרון (ירוק, צהוב, אדום). |
| **Swap** | כתיבת נתוני זיכרון מה-RAM אל הכונן הקשיח. כמות גבוהה מעידה על מחנק זיכרון וחוסר יעילות. |
| **mdmclient** | ה-Daemon המובנה של אפל האחראי על התקשורת מול ה-MDM והחלת הפרופילים. |
| **TCC & PPPC** | מנגנון שמגן על מידע רגיש. פותחים חסימות אלו עם פרופיל PPPC ארגוני. |
| **BTM (Background Task Mgt)** | מנגנון ההגנה על פריטי לוגין (Login Items). מנוהל לעומק דרך פקודת `sfltool`. |

> *→ LaunchAngels והקשר של launchd ל-Kernel (XNU) נלמדו בשיעור 13 (Boot Process) — כאן launchd הוא PID 1 שקם אחרי הקרנל ומעלה את כל השאר.*

> *→ BTM ו-sfltool נלמדים כשלב דיאגנוסטיקה גם בשיעור 15 (Diagnostics) — הוסף כאן לארגז הכלים.*

---

## חלק 1 — קיצורי מקלדת בטרמינל (Terminal Shortcuts)

| קיצור | פעולה |
|---|---|
| `Ctrl + C` | **ביטול והצלה:** עוצר מיידית ריצה של פקודה שתקעה את המסך. |
| `Ctrl + L` | **ניקוי מסך** (כמו הפקודה `clear`). מוחק את הבלגן ויורד להתחלה נקייה. |
| `Ctrl + A` | קפיצה ל**תחילת** השורה. |
| `Ctrl + E` | קפיצה ל**סוף** השורה. |
| `Tab` | **השלמה אוטומטית** של נתיבים ופקודות (הקש פעמיים להצגת אפשרויות). |

---

## חלק 2 — נתיבים קריטיים

| מה יש שם? | נתיב מלא | מי הבעלים |
|---|---|---|
| **העדפות האפליקציות של המשתמש** | `~/Library/Preferences/` | המשתמש |
| **סוכנים של המשתמש הנוכחי** | `~/Library/LaunchAgents/` | המשתמש |
| **סוכני מערכת (Daemons) של IT / צד שלישי** | `/Library/LaunchDaemons/` | מנהל (Root) |
| **ליבה של macOS (SSV - נעול)** | `/System/Library/LaunchDaemons/` | System (קריאה בלבד) |
| **ליבת Tahoe החדשה (RunningBoard)** | `/System/Library/LaunchAngels/` | System (קריאה בלבד) |

---

## נספח — פקודות מערכת חשובות

> [!NOTE]
> מומלץ לשמור פקודות אלו ב-Cheat Sheet או ב-MDM כסניפטים של קוד (Snippets) לשעת צרה.

### שליטה בסיסית ובתהליכים
```bash
# הרצת פקודה יחידה עם הרשאות מנהל
sudo [command]

# אילוץ אלים לסגירת תהליך שנתקע
kill -9 <PID>

# מד משאבים חי (במעבד) - יציאה עם 'q'
top -u

# רשימה מלאה של כלל התהליכים במערכת
ps -ax
```

### ניהול שירותים (launchctl ו-BTM)
```bash
# הצגת מצב כלל השירותים שרצים עכשיו
sudo launchctl print system

# אתחול (Load / Unload) של שירות קורס:
sudo launchctl bootout system /Library/LaunchDaemons/com.example.plist
sudo launchctl bootstrap system /Library/LaunchDaemons/com.example.plist

# שליפת מאגר ה-BTM (Background Task Management)
sudo sfltool dumpbtm > ~/Documents/btmdump.txt

# אילוץ עמוק ל-BTM (רק במקרי כשל קריטיים)
sudo sfltool resetbtm
```

> [!IMPORTANT]
> `sfltool resetbtm` מוחק את כל בסיס הנתונים של Background Task Management — כל התוכנות המותקנות שדורשות Login Item (Agents, Helper Tools) צריכות להירשם מחדש. זה כלי אחרון בתור חקירת יסודית לתקלות Login Items סשיות בלבד.

### קריאה וטיפול ב-Plists (`plutil`)
```bash
# הדפסת תוכן קובץ גם אם הוא מוצפן/בינארי
plutil -p /path/to/file.plist

# בדיקת תקינות הקובץ (Syntax Linting) - חובה לפני הטמעה
plutil -lint /path/to/file.plist

# המרת קובץ סגור לטקסט XML עריך
sudo plutil -convert xml1 /path/to/file.plist

# החזרת קובץ לפורמט בינארי וסגור
sudo plutil -convert binary1 /path/to/file.plist
```

### אבחון ה-MDM
```bash
# מעקב בזמן אמת אחרי פקודות ה-MDM הנכנסות למחשב
log stream --predicate 'process == "mdmclient"' --info

# פקודה כוחנית למשיכת מידע מה-MDM
sudo profiles renew -type enrollment
```

---

## קישורים מומלצים ולקריאה נוספת

* [Explainer: % CPU in Activity Monitor](https://eclecticlight.co/2026/02/14/explainer-cpu-in-activity-monitor/) - הסבר למה אחוזי מעבד לפעמים מטעים ואיך לקרוא אותם (Performance vs Efficiency).
* [A brief history of XML and property lists](https://eclecticlight.co/2025/08/16/a-brief-history-of-xml-and-property-lists/) - מדוע אפל נשענת כל כך חזק על קבצי Plist.
* [View Memory Usage in Activity Monitor](https://support.apple.com/guide/activity-monitor/view-memory-usage-actmntr1004/mac) - המדריך הרשמי לקריאת לחץ הזיכרון.

---

## 🎬 סרטון סיכום

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/UPIUNoYIGPo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

## עזרים ויזואליים מההרצאה

!!! tip "עזרים ויזואליים"
    תמונות אלו ממחישות את הממשק הנלמד בשיעור.

![Slide81_image94](../assets/images/Lesson_08/L08_LegacySlide_Slide81_image94.png)
![Slide81_image95](../assets/images/Lesson_08/L08_LegacySlide_Slide81_image95.png)
![Automator Tahoe](../assets/images/Lesson_08/L08_TahoeUI_26-Tahoe-Automator-scaled.png)
![Console Tahoe](../assets/images/Lesson_08/L08_TahoeUI_26-Tahoe-Console-scaled.png)
![Script Editor Tahoe](../assets/images/Lesson_08/L08_TahoeUI_26-Tahoe-Script-Editor-scaled.png)
![Shortcuts Tahoe](../assets/images/Lesson_08/L08_TahoeUI_26-Tahoe-Shortcuts-scaled.png)
