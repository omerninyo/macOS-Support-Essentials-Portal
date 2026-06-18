# Chapter 08: Launchd & Background Processes - Hands-On Lab

## תרחיש התרגול (Lab Scenario)
במעבדה זו נחקור לעומק את מנגנון ה-`launchd` של macOS ואת תהליכי הרקע, תוך שימוש בכלים גרפיים מובנים של המערכת. נשתמש ב-Activity Monitor כדי לנתח צריכת משאבים וניהול זיכרון, נבחן קבצי תצורה מסוג Plist בעזרת Finder ו-TextEdit, וניצור סוכן רקע (LaunchAgent) משלנו. לבסוף, נשתמש ב-System Settings כדי לנהל אותו, ובאפליקציית ה-Console לאיתור תהליכי ה-MDM שרצים ברקע.

## דרישות קדם (Prerequisites)
- מחשב עם macOS 26 (Tahoe).
- Local Account עם הרשאות מנהל (Local Admin).
- היכרות בסיסית עם עורך הטקסט TextEdit ואפליקציית Activity Monitor.
- (אופציונלי אך מומלץ לחלק 4) חיבור שריר למערכת MDM או סוכן EDR מותקן.

---

## חלק 1: ניתוח עמוק עם Activity Monitor
**מטרה:** זיהוי משאבים, תהליכים והבנת ההיררכיה במערכת ההפעלה דרך עיניו של משתמש IT.

1. פתח את **Activity Monitor** (ניתן למצוא תחת תיקיית `Applications/Utilities/` או דרך חיפוש ב-Spotlight).
2. עבור ללשונית **CPU** ובחר בתפריט העליון בשורת התפריטים: `View > All Processes, Hierarchically`.
   - תצוגה זו תסדר את התהליכים בתצורת עץ, כך שתוכל לראות איזה תהליך אב הוליד איזה תהליך בן.
3. אתר את התהליך השורשי. גלול למעלה או חפש ושים לב שתהליך `kernel_task` מקבל תמיד PID 0.
4. מתחתיו, חפש את התהליך `launchd` אשר תמיד מקבל PID 1. הוא אחראי על טעינת רוב שאר התהליכים במערכת.
5. לחץ פעמיים על תהליך `launchd` לחקירת הלשוניות:
   - **Memory:** בדוק כמה זיכרון תהליך האב צורך באופן שוטף.
   - **Open Files and Ports:** גלול ברשימה וראה את כמות הקבצים והספריות שהתהליך ניגש אליהם (כולל ספריות עמוקות בתוך המערכת).
6. סגור את חלון המידע של `launchd` ועבור ללשונית הכללית של **Memory** באפליקציה.
7. בחן את תרשים ה-**Memory Pressure** בתחתית המסך:
   - **ירוק:** יש מספיק זיכרון פיזי (RAM) זמין לכלל התהליכים.
   - **צהוב:** מנגנון ניהול הזיכרון מתחיל לדחוס נתונים (Memory Compression) או להשתמש ב-Swap כדי לפנות מקום.
   - **אדום:** המערכת משתמשת באופן אינטנסיבי בדיסק כזיכרון וירטואלי (Swap), מה שמוביל להאטה מורגשת בביצועים.
8. **תרגול Force Quit:** 
   - פתח את אפליקציית המחשבון (`Calculator`).
   - אתר אותה ברשימה ב-Activity Monitor.
   - בחר את התהליך ולחץ על לחצן ה-**X** (Stop) בסרגל הכלים העליון של החלון.
   - בחר באופציה **Force Quit**. המערכת שולחת פקודת `SIGKILL` לתהליך וסוגרת אותו באופן מיידי ומאולץ.

---

## חלק 2: יצירת LaunchAgent וניהולו דרך System Settings
**מטרה:** הבנת המבנה של קובץ XML מסוג Plist והפעלת Background Process ברמת המשתמש (LaunchAgent) ללא צורך בהרשאות Root, וכיבוי מבוקר דרך הממשק הגרפי.

1. פתח את אפליקציית **TextEdit**.
2. ודא שאתה במצב Plain Text (בתפריט העליון: `Format > Make Plain Text`, אם זה לא מופיע, אתה כבר במצב המתאים).
3. העתק והדבק פנימה את קוד ה-XML הבא:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>Label</key>
       <string>com.example.hello</string>
       <key>ProgramArguments</key>
       <array>
           <string>/bin/echo</string>
           <string>Hello from LaunchAgent!</string>
       </array>
       <key>StandardOutPath</key>
       <string>/tmp/hello_agent.log</string>
       <key>StartInterval</key>
       <integer>10</integer>
   </dict>
   </plist>
   ```
4. בתפריט העליון לחץ על `File > Save`. נשמור את הקובץ ישירות לתיקיית סוכני הרקע של המשתמש:
   - בחלון השמירה, הקש על קיצור המקלדת `Cmd+Shift+G` (כדי לפתוח את חלונית "Go to Folder").
   - הקלד את הנתיב: `~/Library/LaunchAgents` ולחץ על ה-Enter (אם התיקייה אינה קיימת, צור אותה תחילה דרך ה-Finder בנתיב הבית שלך).
   - בשדה שם הקובץ (Save As), הקלד: `com.example.hello.plist`. 
   - הורד את הסימון מ- "If no extension is provided, use .txt" ולחץ על **Save**.
5. כדי לטעון את ה-LaunchAgent ללא שימוש בטרמינל, בצע **Log Out** מחשבון המשתמש שלך דרך תפריט התפוח (` > Log Out`).
6. התחבר בחזרה למשתמש (Log In). תהליך ה-`launchd` מזהה את הקובץ החדש בספרייה שלך ומפעיל אותו.
7. כעת נבדוק אם הסוכן רץ. פתח את **Finder**, לחץ על `Go > Go to Folder` והקלד `/tmp`.
8. חפש את הקובץ `hello_agent.log` ופתח אותו (על ידי לחיצה כפולה, הוא ייפתח ב-Console או TextEdit). אתה אמור לראות שהשורה "Hello from LaunchAgent!" מודפסת כל 10 שניות. (אם לא, המתן דקה ופתח שוב).
9. **כיבוי מבוקר (Disable Override):** 
   - פתח את **System Settings**.
   - נווט אל **General > Login Items & Extensions**.
   - תחת הקטגוריה `Allow in the Background`, חפש פריט המזוהה כ- `com.example.hello` או "Unknown Developer".
   - כבה את המתג לצידו. פעולה זו עוצרת את הסוכן ורושמת במערכת ה-BTM (Background Task Management) שיש להתעלם ממנו בהפעלות הבאות, גם אם הקובץ עצמו נשאר בתיקייה!

---

## חלק 3: חקירת LaunchDaemons מובנים של המערכת
**מטרה:** להבחין בהבדל המהותי בין סוכן הקיים בתיקיית המשתמש לבין שירותי ליבה של macOS בספריית ה-System.

1. פתח חלון **Finder** חדש.
2. לחץ על צירוף המקשים `Cmd+Shift+G` והקלד את הנתיב: `/System/Library/LaunchDaemons`.
   *(זוהי ספריה המוגנת הרמטית על ידי מנגנון ה-SSV של אפל, ולא ניתנת לשינוי, אך קריאה שלה מותרת).*

3. ברשימת הקבצים, חפש פריטים הקשורים לשירותי רשת. גלול למטה עד שתמצא את הקובץ `com.apple.mDNSResponder.plist`.
4. בחר את הקובץ ולחץ על מקש הרווח (**Spacebar**) כדי לפתוח אותו בתצוגה המקדימה (Quick Look).
5. עיין בתוכן ה-XML:
   - חפש את המפתח `ProgramArguments`. שים לב כיצד הוא מכיל את הנתיב המדויק לקובץ ההפעלה (`/usr/sbin/mDNSResponder`).
   - חפש את המפתח `KeepAlive` ושים לב לערכים שלו. אלו ההנחיות המגדירות ל-`launchd` לדאוג שהתהליך תמיד יפעל עבור שירותי גילוי הרשת (Bonjour).

---

## חלק 4: חקירת תהליכי MDM עם אפליקציית ה-Console
**מטרה:** איתור תהליך ה-MDM ברקע, הבנת ההיררכיה שלו, ומעקב אחר פעילות הסנכרון בעזרת אפליקציית ה-Console החזותית.

1. פתח שוב את **Activity Monitor**.
2. ודא כי התצוגה היא `All Processes` רגיל.
3. בשורת החיפוש בפינה הימנית העליונה, הקלד את המונח `mdmclient`.
   - *תהליך ה-`mdmclient` הוא ה-Daemon המובנה של macOS שמקשיב לתקשורת מפלטפורמת ה-MDM.*
   - *(הערה: אם הארגון שלכם משתמש ב-Agent צד-שלישי כמו של Jamf או Kandji, תוכל לחפש גם את שמם).*
4. בחר את התהליך `mdmclient` ולחץ על לחצן ה-**i** (Information) בסרגל העליון (או לחץ פעמיים על השורה).
5. עבור ללשונית **Open Files and Ports**.
6. גלול ברשימה וחפש נתיבים המצביעים לתיקיית `/var/db/ConfigurationProfiles`. זהו המקום שבו המערכת שומרת Configuration Profiles קריטיים שה-Daemon מנהל.
7. כעת, נראה את הפעילות בזמן אמת: פתח את אפליקציית **Console** (נמצאת תחת `/Applications/Utilities/`).
8. בצד שמאל, תחת `Devices`, בחר את המחשב המקומי שלך.
9. בשורת החיפוש בפינה הימנית העליונה של ה-Console, הקלד `mdmclient` ולחץ Enter.
10. לחץ על כפתור ה-**Start** (אם הוא לא לחוץ כבר) בחלק העליון כדי להתחיל לתפוס אירועים בזמן אמת.
11. תוכל לפתוח את **System Settings > Privacy & Security > Profiles** וללחוץ על פרופיל (אם קיים) כדי לגרום למערכת לייצר קצת לוגים, ולצפות כיצד הם מופיעים בצורה ויזואלית ב-Console בחתך של `mdmclient`.

---

## תרגיל אקסטרה / קצה קרחון טכני

כדי לנהל תהליכי רקע בצורה מהירה דרך שורת הפקודה, מנהלי מערכת נוהגים להשתמש בכלי ה-`launchctl`. הכלי מונע את הצורך בביצוע יציאה/כניסה של המשתמש. כמו כן, מפתחים משתמשים בפקודת `log stream` לתצוגת לוגים בזמן אמת במקום להשתמש באפליקציית ה-Console.

1. **טעינה (Load) של LaunchAgent ללא ניתוק:**
   ```bash
   launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.example.hello.plist
   ```
   *(פקודה זו מחליפה את הדרך הישנה `launchctl load` ומנחה את המערכת להפעיל את הקובץ עבור המשתמש הנוכחי).*

2. **מעקב אחרי ה-MDM בלייב בטרמינל:**
   ```bash
   log stream --predicate 'process == "mdmclient"' --info
   ```
   *(זהו המקביל המדויק לחיפוש `mdmclient` באפליקציית ה-Console, אך מסנן מידע שולי בצורה אפקטיבית יותר).*
