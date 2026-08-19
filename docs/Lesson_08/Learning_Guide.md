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

> *← LaunchAngels והקשר של launchd ל-Kernel (XNU) נלמדו בשיעור 13 (Boot Process) — כאן launchd הוא PID 1 שקם אחרי הקרנל ומעלה את כל השאר.*

> *← BTM ו-sfltool נלמדים כשלב דיאגנוסטיקה גם בשיעור 15 (Diagnostics) — הוסף כאן לארגז הכלים.*

---

## חלק 1 — יסודות הטרמינל ולוח פקודות חיוני (Terminal Essentials Cheat Sheet)

### ⌨️ קיצורי מקלדת וטיפים קריטיים לעבודה מהירה

| קיצור / פעולה | הסבר ושימוש מעשי |
|---|---|
| `Tab` | **השלמה אוטומטית (Auto-completion)** של פקודות ונתיבים. הקישו פעמיים להצגת כל האפשרויות. |
| `Ctrl + C` | **ביטול והצלה:** עוצר מיידית ריצה של פקודה תקועה (SIGINT) ומחזיר את שורת הפקודה. |
| `Ctrl + L` | **ניקוי מסך** (שווה ערך לפקודה `clear`). מנקה את התצוגה ומתחיל משורה עליונה נקייה. |
| `Ctrl + A` / `Ctrl + E` | קפיצה מהירה ל**תחילת** השורה (`Ctrl+A`) או ל**סוף** השורה (`Ctrl+E`). |
| חצים `↑` / `↓` | **גלילה בהיסטוריה:** דפדוף אחורה וקדימה בכל הפקודות שהורצו לאחרונה. |
| **גרירת קובץ (Drag & Drop)** | גרירת כל קובץ או תיקייה מחלון ה-Finder לתוך שורת הטרמינל מדביקה אוטומטית את הנתיב המלא שלו (כולל טיפול מדויק ברווחים). |
| `open .` | **הטיפ ההפוך (מטרמינל ל-Finder):** הפקודה `open .` (פתח רווח נקודה) פותחת מיידית חלון Finder בתיקייה שבה אתם נמצאים כרגע בטרמינל! ניתן גם לפתוח קובץ ספציפי: `open filename.pdf`. |

---

### 📂 1. ניווט והתמצאות במערכת הקבצים (Navigation & Location)

| פקודה | תיאור ודגלים חשובים |
|---|---|
| `pwd` | **Print Working Directory** — מדפיס את הנתיב המלא של התיקייה שבה אתם עומדים כרגע. |
| `cd <path>` | **Change Directory** — מעבר לתיקייה המבוקשת. |
| `cd ~` או `cd` | חזרה מיידית לתיקיית הבית של המשתמש הנוכחי (`/Users/username`). |
| `cd ..` | עלייה תיקייה אחת למעלה בהיררכיית התיקיות. |
| `cd -` | חזרה לתיקייה הקודמת שבה הייתם (כמו כפתור Back). |
| `cd /` | מעבר לשורש הכונן הראשי (Root filesystem). |
| `ls` | **List** — הצגת שמות הקבצים והתיקיות במיקום הנוכחי. |
| `ls -l` | רשימה מפורטת (Long listing) הכוללת הרשאות, בעלים, גודל ותאריך שינוי. |
| `ls -a` | הצגת **כל** הקבצים, כולל קבצים נסתרים המתחילים בנקודה (`.zshrc`, `.DS_Store`). |
| `ls -lh` | רשימה מפורטת עם גדלי קבצים קריאים לאדם (**Human Readable** — ב-KB, MB, GB). |
| `ls -le` / `ls -l@` | הצגת רשימות בקרת גישה (ACLs) ותכונות מורחבות (Extended Attributes כמו תגית בידוד Quarantine). |

---

### 🛠️ 2. יצירה, ניהול ומחיקת קבצים (File & Directory Management)

| פקודה | תיאור ודגלים חשובים |
|---|---|
| `mkdir <dir>` | **Make Directory** — יצירת תיקייה חדשה. |
| `mkdir -p a/b/c` | יצירת היררכיית תיקיות מקוננות שלמה בפקודה יחידה. |
| `touch <file>` | יצירת קובץ טקסט ריק חדש, או עדכון חותמת הזמן של קובץ קיים. |
| `cp <source> <target>` | **Copy** — העתקת קובץ ממקור ליעד. |
| `cp -R <src> <dst>` | העתקת תיקייה שלמה על כל תוכנה באופן רקורסיבי. |
| `mv <source> <target>` | **Move / Rename** — העברת קובץ/תיקייה ליעד אחר ו/או שינוי שמו. |
| `rm <file>` | **Remove** — מחיקת קובץ לצמיתות (**שימו לב:** עוקף את פח האשפה ולא ניתן לשחזור מה-Trash!). |
| `rm -r <dir>` | מחיקת תיקייה שלמה ותוכנה באופן רקורסיבי. |
| `rm -rf <dir>` | מחיקה מאולצת וללא שאלות. *(אזהרה חמורה: אין להריץ `sudo rm -rf` על נתיב שאינכם בטוחים בו במאה אחוז!)* |

---

### 📄 3. צפייה, קריאה ועריכת קבצים (Viewing & Editing)

| פקודה | תיאור ודגלים חשובים |
|---|---|
| `cat <file>` | שפיכת כל תוכן הקובץ ברצף למסך (מתאים לקבצים קצרים בלבד). |
| `less <file>` | קריאה ודפדוף נוח בקבצים ארוכים (גלילה בחצים/רווח, חיפוש טקסט עם `/`, יציאה חזרה לטרמינל עם `q`). |
| `head -n 20 <file>` | הצגת 20 השורות הראשונות של הקובץ בלבד. |
| `tail -n 20 <file>` | הצגת 20 השורות האחרונות של הקובץ בלבד. |
| `tail -f <logfile>` | **Follow Mode** — עקיבה חיה בזמן אמת אחרי שורות חדשות שנכתבות לקובץ לוג (עצירה עם `Ctrl+C`). |
| `nano <file>` | עורך טקסט פשוט וידידותי בתוך הטרמינל (שמירה: `Ctrl+O`, יציאה: `Ctrl+X`). |

---

### 🔍 4. זהות, עזרה ומידע מערכת (Help, Identity & Environment)

| פקודה | תיאור ודגלים חשובים |
|---|---|
| `man <command>` | **Manual** — ספר ההוראות המלא והרשמי של כל פקודה (גלילה בחצים, יציאה עם `q`). |
| `which <command>` | הצגת הנתיב המדויק שבו שמור קובץ הפקודה (למשל `/usr/bin/python3`). |
| `whoami` | מציג את שם המשתמש הנוכחי שמחובר לטרמינל. |
| `sw_vers` | מציג את גרסת ה-macOS המדויקת ואת מספר ה-Build. |
| `uname -m` | מציג את ארכיטקטורת המעבד (`arm64` עבור Apple Silicon מול `x86_64` עבור Intel). |
| `sudo <command>` | **Superuser Do** — הרצת פקודה בודדת בהרשאות מנהל-על (`root`). |

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

!!! note
    מומלץ לשמור פקודות אלו ב-Cheat Sheet או ב-MDM כסניפטים של קוד (Snippets) לשעת צרה.

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

!!! important
    `sfltool resetbtm` מוחק את כל בסיס הנתונים של Background Task Management — כל התוכנות המותקנות שדורשות Login Item (Agents, Helper Tools) צריכות להירשם מחדש. זה כלי אחרון בתור חקירת יסודית לתקלות Login Items סשיות בלבד.

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

* [Terminal User Guide for Mac (Apple Support)](https://support.apple.com/guide/terminal/welcome/mac) — מדריך המשתמש הרשמי של אפל לאפליקציית הטרמינל.
* [Complete Mac Terminal Commands Cheat Sheet (GeeksforGeeks)](https://www.geeksforgeeks.org/linux-unix/complete-mac-terminal-commands-cheat-sheet/) — לוח עזר מקיף לפקודות טרמינל במק.
* [Use zsh as the default shell on your Mac (Apple Support)](https://support.apple.com/en-us/102360) — הסבר על מעטפת Zsh וקובצי הפרופיל והאתחול שלה.
* [Command-line management in macOS (Apple Platform Deployment)](https://support.apple.com/guide/deployment/command-line-management-dep3d526a457/web) — מדריך הניהול הרשמי של אפל לאנשי IT באמצעות שורת הפקודה.
* [View Memory Usage in Activity Monitor (Apple Support)](https://support.apple.com/guide/activity-monitor/view-memory-usage-actmntr1004/mac) — המדריך הרשמי לקריאת לחץ הזיכרון (Memory Pressure).
* [Explainer: % CPU in Activity Monitor (The Eclectic Light Company)](https://eclecticlight.co/2026/02/14/explainer-cpu-in-activity-monitor/) — הסבר למה אחוזי מעבד לפעמים מטעים ואיך לקרוא אותם (ליבות P מול E).
* [A brief history of XML and property lists (The Eclectic Light Company)](https://eclecticlight.co/2025/08/16/a-brief-history-of-xml-and-property-lists/) — מדוע אפל נשענת כל כך חזק על קבצי Plist.

---

## 🎬 סרטון סיכום

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/UPIUNoYIGPo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

## עזרים ויזואליים

!!! tip "המחשה ויזואלית (עזר לתלמיד)"
    תמונות אלו ממחישות את הממשק או המנגנון הרלוונטי לנושא השיעור.

![Slide81_image94](../assets/images/Lesson_08/L08_LegacySlide_Slide81_image94.png)
![Slide81_image95](../assets/images/Lesson_08/L08_LegacySlide_Slide81_image95.png)
![26-Tahoe-Automator-scaled](../assets/images/Lesson_08/L08_TahoeUI_26-Tahoe-Automator-scaled.png)
![26-Tahoe-Console-scaled](../assets/images/Lesson_08/L08_TahoeUI_26-Tahoe-Console-scaled.png)
![26-Tahoe-Script-Editor-scaled](../assets/images/Lesson_08/L08_TahoeUI_26-Tahoe-Script-Editor-scaled.png)
![26-Tahoe-Shortcuts-scaled](../assets/images/Lesson_08/L08_TahoeUI_26-Tahoe-Shortcuts-scaled.png)
