# פרק 1: התקנה, הכרה ויישור קו (Setup & Fundamentals) - סיכום שיעור (Asset C)

## 1. נושאי השיעור

*   **1.** **היסטוריה ופילוסופיה:** רקע לאבולוציה מ-OS X ל-macOS ומעבר ל-Apple Silicon.
*   **2.** **חוויית פתיחת הקופסה:** היכרות עם תהליך ההגדרה הראשוני (Setup Assistant).
*   **3.** **היכרות עם המערכת:** ניווט במערכת, Finder, System Settings ומחוות.
*   **4.** **מעבדה ראשונה:** פתיחת מחשב, זיהוי חומרה והתמצאות ראשונית.
*   **5.** **תיבול ארגוני:** היכרות עם רישום למערכות ניהול בארגון (ADE/Remote Management).

## מילון מונחים (Glossary & Concepts)
* **Apple Silicon:** ארכיטקטורת המעבדים החדשה של אפל מבוססת ARM (סדרת ה-M).
* **System on a Chip - SoC:** מערכת על שבב, המרכזת את המעבד (CPU), המאיץ הגרפי (GPU), הזיכרון (Unified Memory) וההצפנה (Secure Enclave) על פיסת סיליקון אחת.
* **Unified Memory:** זיכרון מאוחד ב-Apple Silicon המאפשר ל-CPU ול-GPU לחלוק נתונים ללא העתקה פיזית.
* **Secure Enclave:** רכיב אבטחה מבודד בחומרה האחראי על שמירת מפתחות ההצפנה וניהול ה-FileVault.
* **Setup Assistant:** Setup Assistant הראשוני (OOBE) שעולה בהפעלת מק חדש או מאופס.
* **Local Account - Admin:** החשבון המקומי הראשון שנוצר בסטאפ מקבל באופן אוטומטי הרשאות מנהל ו-Secure Token.
* **Erase All Content and Settings - EACS:** Erase All Content and Settings (EACS); תהליך המאפס את המחשב בצורה מאובטחת ומיידית.
* **Finder:** סייר הקבצים והליבה של הממשק הגרפי ב-macOS. פועל כתהליך שאינו נסגר.
* **System Settings:** מרכז ההגדרות החדש של המערכת (החליף את System Preferences), שבו מנוהלים גם פרופילי התצורה.
* **Spotlight:** מנוע חיפוש פנימי עוצמתי (מופעל לרוב ב-Cmd+Space) לאיתור אפליקציות, קבצים, וביצוע פעולות.
* **Automated Device Enrollment - ADE:** שירות Automated Device Enrollment (ADE) המאפשר לארגונים להטמיע מחשבים מרחוק וללא מגע (Zero-Touch Deployment).
* **Remote Management:** המסך שמופיע ב-Setup Assistant אם המחשב זוהה כשייך לארגון דרך שרתי אפל, ודורש מהמשתמש להזדהות ולהתקין את פרופיל הניהול.

## פקודות טרמינל שימושיות (Terminal Commands)
* `system_profiler SPHardwareDataType` - מציג את דוח החומרה הבסיסי, כולל דגם המחשב והמספר הסידורי (Serial Number).
* `system_profiler SPNetworkDataType` - מציג את תצורת הרשת, כולל כתובת ה-MAC של מתאם ה-Wi-Fi.
* `sw_vers` - מדפיס את הגרסה המדויקת של macOS המותקנת יחד עם ה-Build Number.
* `killall Finder` - הורג ומאתחל מחדש את תהליך ה-Finder במקרה של תקיעה או שינוי הגדרות מוסתרות.
* `sudo mdutil -E /` - מוחק ובונה מחדש את אינדקס החיפוש של ה-Spotlight.
* `sudo profiles renew -type enrollment` - מאלץ את המחשב לפנות לשרתי אפל כדי לבדוק מחדש אם הוא משויך לארגון (הפעלת טריגר ל-ADE).

## נתיבים חשובים (Paths & Plists)
* `/private/var/db/.AppleSetupDone` - קובץ מוסתר שאם הוא קיים, המערכת מדלגת על ה-Setup Assistant. מחיקתו תחזיר את סייען ההתקנה בהפעלה הבאה.
* `~/Library/Preferences/com.apple.finder.plist` - קובץ הגדרות המשתמש של ה-Finder.
* `/System/Library/CoreServices/Setup Assistant.app` - המיקום של אפליקציית סייען ההתקנה.

## Recommended Reading & Enrichment Links
* **Mac Setup Assistant Support:** [Set up your Mac - Apple Support](https://support.apple.com/guide/mac-help/set-up-your-new-mac-mh26966/mac)
* **Apple Silicon Fundamentals:** [Mac computers with Apple silicon - Apple Support](https://support.apple.com/en-us/HT211814)
* **Automated Device Enrollment:** [Automated Device Enrollment in Apple Business Manager](https://support.apple.com/guide/apple-business-manager/automated-device-enrollment-axm306bce837/web)
