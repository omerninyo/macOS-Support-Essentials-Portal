# Lesson 01: יסודות macOS, חוויית משתמש והכנה לארגון
**Asset D: Hands-on Lab**

## סקירה ורקע (Overview)
מעבדה זו משמשת כ"מיישר קו" (Equalizer) לטכנאים ולמשתמשים שמבצעים מעבר ל-macOS. המטרה היא להתנסות בניווט בסיסי, להבין כיצד המערכת משקפת את חומרת ה-Apple Silicon, ולהכיר את חוויית ה-OOBE (Out of Box Experience) מנקודת המבט של המשתמש.

---

## תרגיל 1: זיהוי תצורה וארכיטקטורה (Apple Silicon Diagnostics)
**מטרה:** לאמת את חומרת המחשב ולהבדיל בין תהליכי Apple לתהליכי Intel (Rosetta 2).

1. היכנסו לתפריט התפוח (``) בחלק השמאלי העליון של המסך ולחצו על **About This Mac**.
2. ודאו כי מופיע ציון לשבב מבית אפל (למשל: Apple M3) ואת כמות ה-Unified Memory הזמינה.
3. פתחו את תוכנת ה-**Activity Monitor** (ניתן להשתמש בקיצור המקלדת `Cmd + Space` ולחפש בעזרת Spotlight).
4. בסרגל העליון של Activity Monitor, ודאו שאתם בלשונית **CPU**.
5. הסתכלו על עמודת ה-**Kind** (סוג).
   - *הערה: אם העמודה אינה מופיעה, לחצו קליק ימני על שורת הכותרת של העמודות וסמנו V ליד המילה "Kind".*
6. מיינו את הרשימה על ידי לחיצה על העמודה. זהו תהליכים שרצים תחת "Apple" (אלו תהליכים שנכתבו ארכיטקטונית ל-ARM) מול תהליכי "Intel" (שכרגע מתורגמים בזמן אמת על ידי Rosetta 2).

---

## תרגיל 2: ניווט, מחוות וסביבות עבודה (Navigation & Spaces)
**מטרה:** תרגול מעבר חלק בין חלונות מרובים בעזרת Trackpad ומחוות Multi-Touch, בדומה למסמך ה-Starter Guide של אפל.

1. פתחו את ה-**System Settings** וגשו לתפריט **Trackpad**.
2. עברו על לשוניות ה-Point & Click, Scroll & Zoom ו-More Gestures. ודאו שהגדרת **Swipe between full-screen applications** מופעלת (עם שלוש או ארבע אצבעות).
3. פתחו 3 אפליקציות שונות (למשל: Safari, Notes, Calendar).
4. לחצו על הכפתור הירוק בפינה השמאלית העליונה של Safari כדי להעביר אותו למסך מלא (Full Screen). זה יוצר Space (סביבת עבודה) חדשה.
5. החליקו עם 3/4 אצבעות שמאלה וימינה כדי לעבור במהירות בין חלון ה-Safari לבין שולחן העבודה הרגיל (Desktop) שמכיל את שאר האפליקציות.
6. החליקו למעלה עם 3/4 אצבעות להפעלת **Mission Control** כדי לראות את כל האפליקציות הפתוחות ממבט על.

---

## תרגיל 3: אימות מצב הרשמה ל-MDM בטרמינל
**מטרה:** שימוש ראשוני ב-Terminal כדי לבדוק האם המחשב נוהל במהלך שלב ה-Setup Assistant באמצעות ה-Automated Device Enrollment.

1. פתחו את ה-**Terminal** (דרך Spotlight או בנתיב `/Applications/Utilities/Terminal.app`).
2. הקלידו את הפקודה הבאה ולחצו Enter:
   ```bash
   sudo profiles show -type enrollment
   ```
3. המערכת תדרוש מכם להזין את סיסמת ה-Local Account שלכם (סיסמת מנהל). הזינו אותה (הטקסט לא ייראה על המסך) ולחצו Enter.
4. נתחו את הפלט:

   - אם מופיע הטקסט `Error fetching Device Enrollment configuration: (34000) Client is not DEP enabled.`, המחשב אינו רשום ב-Apple Business Manager ואינו כפוף ל-Remote Management.
   - אם הפלט מציג פרטים על שרת (כגון URL של שרת MDM ארגוני), המחשב נרשם כראוי בהפעלתו הראשונה.
