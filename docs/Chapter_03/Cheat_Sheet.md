# Asset C: סיכום שיעור - פרק 3 (Security & TCC)

## 1. נושאי השיעור

*   **1.** **הגן הסגור (Gatekeeper):** הבנה כיצד macOS מוודאת שתוכנות בטוחות להפעלה (Notarization).
*   **2.** **האנטי-וירוס השקט (XProtect):** היכרות עם סורק הקוד הזדוני המובנה במערכת.
*   **3.** **ניהול פרטיות (TCC):** הבנת המנגנון שמגביל גישת אפליקציות למצלמה ולמידע רגיש.
*   **4.** **תיבול ארגוני:** ניהול TCC ומתן אישורים אוטומטיים דרך פרופילים של ה-IT.

מסמך זה מרכז את כל הפקודות, המושגים, הנתיבים וכלי האבחון שנלמדו בפרק השלישי, העוסק באבטחת המערכת, מנגנוני הגנה מובנים (Gatekeeper, XProtect) ומערכת ה-TCC.

## 2. מושגי יסוד (Terminology)

* **Gatekeeper:** מנגנון האבטחה של macOS שמוודא שרק תוכנות ממקור מהימן (App Store או מפתחים מזוהים) מורשות לרוץ על המק. הוא בודק את חתימת המפתח ואת ה-Notarization.
* **Notarization:** תהליך אוטומטי של Apple שבו אפליקציות נסרקות לאיתור קוד זדוני ידוע לפני הפצתן, עוד בטרם הגיעו למשתמש. Gatekeeper דורש אישור זה עבור כל תוכנה המורדת מהאינטרנט.
* **XProtect:** מערכת ה-Anti-Virus השקטה והמובנית של macOS. פועלת ברקע, מבוססת חתימות (YARA) וחוסמת הפעלה של תוכנות זדוניות מוכרות בעת ניסיון ההרצה הראשון.
* **XProtect Remediator:** מנגנון סריקה אקטיבי שרץ ברקע (על ידי LaunchDaemons) ומבצע סריקות תקופתיות לאיתור והסרת נוזקות שכבר הצליחו לחדור למערכת.
* **Transparency, Consent, and Control (TCC):** מנגנון הפרטיות של macOS, הדורש מהמשתמש לאשר באופן אקטיבי בקשות גישה של אפליקציות למשאבים רגישים (כגון מצלמה, מיקרופון, מיקום, תיקיית מסמכים או דיסק מלא).
* **Privacy Preferences Policy Control - PPPC:** Configuration Profile (Payload) ארגוני המופץ על ידי מערכת ה-MDM ומאפשר למנהלי ה-IT להעניק מראש (או למנוע) הרשאות TCC עבור אפליקציות, ובכך למנוע מהמשתמשים לקבל חלוניות קופצות (Pop-ups) הדורשות אישור מנהל.
* **System Integrity Protection - SIP:** מנגנון אבטחה ב-macOS המונע אפילו ממשתמש root לשנות קבצי מערכת רגישים, כולל את מסדי הנתונים של ה-TCC.
* **Quarantine:** תגית (Extended Attribute) המוצמדת לקבצים שהורדו מהאינטרנט על ידי אפליקציות כמו ספארי, דואר או תוכנות מסרים. תגית זו מפעילה את הבדיקה של Gatekeeper עם פתיחת הקובץ.

---

## 3. פקודות טרמינל (CLI Commands)

### חקירה וניהול של Gatekeeper (`spctl`)
הכלי `spctl` (SecAssessment system policy security) משמש לניהול ובדיקת מערכת ה-Gatekeeper.

* **בדיקת הסטטוס של Gatekeeper (האם הוא פעיל):**
  ```bash
  spctl --status
  ```
* **בדיקת אפליקציה - הערכת Gatekeeper (האם היא מאושרת ותרוץ):**
  ```bash
  spctl -a -vv /Applications/AppName.app
  ```
  *(הדגל `-a` מבצע Assessment, `-vv` מציג פלט מפורט כולל מידע על ה-Notarization וזהות המפתח).*

* **עקיפה נקודתית של Gatekeeper עבור אפליקציה ספציפית:**
  ```bash
  sudo spctl --add /path/to/AppName.app
  ```

* **הסרת תגית ההסגר (Quarantine) מקובץ שהורד מהאינטרנט (עוקף את אזהרת ההפעלה הראשונית):**
  ```bash
  xattr -d com.apple.quarantine /path/to/AppName.app
  ```

### ניהול ואיפוס הרשאות TCC (`tccutil`)
הכלי `tccutil` מאפשר לאפס הרשאות פרטיות שהוענקו, מה שמכריח את המערכת לבקש אותן שוב בפעם הבאה שהאפליקציה תיפתח. (שים לב: לא ניתן להעניק הרשאות דרך `tccutil`, אלא רק לאפס אותן לאחור).

* **איפוס כל הרשאות ה-TCC עבור כל האפליקציות (חזרה למצב "מפעל" מבחינת פרטיות):**
  ```bash
  tccutil reset All
  ```
* **איפוס הרשאת מצלמה בלבד (לכל האפליקציות שביקשו עד כה):**
  ```bash
  tccutil reset Camera
  ```
* **איפוס הרשאת מיקרופון בלבד:**
  ```bash
  tccutil reset Microphone
  ```
* **איפוס הרשאת גישה לכל הדיסק (Full Disk Access):**
  ```bash
  tccutil reset SystemPolicyAllFiles
  ```
* **איפוס הרשאת צפייה במסך (Screen Recording):**
  ```bash
  tccutil reset ScreenCapture
  ```
* **איפוס הרשאת מצלמה עבור אפליקציה ספציפית (לדוגמה, Terminal או Zoom), על ידי Bundle ID:**
  ```bash
  tccutil reset Camera com.apple.Terminal
  tccutil reset Camera us.zoom.xos
  ```

---

## 4. נתיבים קריטיים, לוגים ומסדי נתונים (Paths & Plists)

### מיקומי מסדי הנתונים של TCC
מערכת ה-TCC שומרת את ההרשאות בתוך מסדי נתונים מסוג SQLite. מסדים אלו מוגנים על ידי System Integrity Protection (SIP) ולא ניתן לערוך או למחוק אותם ידנית, אלא אם מבטלים SIP.

* **מסד הנתונים ברמת המשתמש (ניהול הרשאות כמו מצלמה, מיקרופון, אנשי קשר ותיקיות מקומיות):**
  ```text
  ~/Library/Application Support/com.apple.TCC/TCC.db
  ```
* **מסד הנתונים ברמת המערכת (ניהול הרשאות קריטיות כמו Full Disk Access):**
  ```text
  /Library/Application Support/com.apple.TCC/TCC.db
  ```

### XProtect & Remediator
מיקומי קבצי החתימות וכלי הסריקה של המנגנון השקט:

* **קובץ החתימות המסורתי של XProtect (רשימת ה-YARA/Blocklist שמתעדכנת ברקע):**
  ```text
  /Library/Apple/System/Library/CoreServices/XProtect.bundle/Contents/Resources/XProtect.plist
  ```
* **האפליקציה המריצה את ה-XProtect Remediator (כלי הסריקות התקופתיות והרמדיאציה):**
  ```text
  /Library/Apple/System/Library/CoreServices/XProtect.app
  ```

### שאילתות לוגים (Unified Logging) דרך הטרמינל
למעקב אחר פעילות של המנגנונים בסביבת הטרמינל:

* **מעקב אחר פעילות Gatekeeper (חקירת חסימות אפליקציות):**
  ```bash
  log show --predicate 'subsystem == "com.apple.syspolicy"' --info --last 1h
  ```
* **מעקב אחר חסימות של מערכת ה-TCC (מי ניסה לגשת למה ומתי נחסם):**
  ```bash
  log show --predicate 'subsystem == "com.apple.TCC"' --info --last 1h
  ```
* **צפייה בתוצאות הסריקה של XProtect Remediator (האם זוהתה נוזקה במערכת):**
  ```bash
  log show --predicate 'subsystem == "com.apple.XProtectFramework.PluginAPI"' --info
  ```

---

## 5. Recommended Reading & Enrichment Links

להלן רשימה של קישורים למאמרי התמיכה והתיעוד הרשמיים של Apple בנושאי אבטחה, TCC ו-Gatekeeper, לחיזוק והרחבת הלמידה:

* **Gatekeeper and runtime protection in macOS:**  
  [https://support.apple.com/guide/security/gatekeeper-and-runtime-protection-secbd103561c/web](https://support.apple.com/guide/security/gatekeeper-and-runtime-protection-secbd103561c/web)

* **Protecting against malware in macOS - XProtect & XProtect Remediator:**  
  [https://support.apple.com/guide/security/protecting-against-malware-sec469d47bd8/web](https://support.apple.com/guide/security/protecting-against-malware-sec469d47bd8/web)

* **Control access to your camera on Mac - TCC Privacy basics:**  
  [https://support.apple.com/guide/mac-help/control-access-to-the-camera-mchlf6d108da/mac](https://support.apple.com/guide/mac-help/control-access-to-the-camera-mchlf6d108da/mac)

* **Safely open apps on your Mac - Overview of App Security:**  
  [https://support.apple.com/en-us/HT202491](https://support.apple.com/en-us/HT202491)

* **Privacy Preferences Policy Control - PPPC payloads for MDM:**  
  [https://support.apple.com/guide/deployment/privacy-preferences-policy-control-payloads-dep38df53c2a/web](https://support.apple.com/guide/deployment/privacy-preferences-policy-control-payloads-dep38df53c2a/web)
