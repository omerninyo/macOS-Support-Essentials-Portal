# סיכום שיעור: משתמשים והרשאות (Users & Permissions)

## 1. נושאי השיעור

*   **1.** **סוגי חשבונות מקומיים:** הבנת ההבדלים בין Admin, Standard ו-Guest והשפעתם על אבטחה.
*   **2.** **היררכיית תיקיות:** ניווט בסביבת ה-Home Folder ובתיקייה המשותפת.
*   **3.** **אבטחת קבצים:** הבנת מודל ההרשאות הבסיסי ותרגול שינוי הרשאות ממשק.
*   **4.** **תיבול ארגוני:** היכרות עם Managed Apple Accounts והבדלם מחשבונות פרטיים.

## 2. מושגי מפתח

*   **Local Account:** חשבון שמוגדר אך ורק במק הספציפי. יכול להיות מסוג מנהל (Admin) עם הרשאות לשינוי System Settings, או סטנדרטי (Standard) שמוגבל לשינויים בתוך ה-Home Folder שלו בלבד.
*   **מנהל (Administrator):** משתמש בעל הרשאות מורחבות היכול להתקין אפליקציות ברמת המערכת, לשנות הגדרות ב-System Settings, ולנהל משתמשים אחרים.
*   **תיקיית משתמש (Home Folder - `~`):** המרחב הפרטי של כל משתמש במערכת (לרוב ממוקם תחת `/Users/username`). מכיל את המסמכים, ההורדות וספריית ה-Library האישית.
*   **תיקייה משותפת (`/Users/Shared`):** תיקייה ייעודית במערכת שכל המשתמשים המקומיים במק יכולים לקרוא ולכתוב אליה. משמשת להעברת קבצים בין חשבונות שונים באותו מחשב.
*   **הרשאות POSIX:** מערכת ההרשאות הבסיסית של UNIX המגדירה זכויות קריאה (Read - `r`), כתיבה (Write - `w`) והפעלה (Execute - `x`) עבור הבעלים (Owner), הקבוצה (Group) ושאר המשתמשים (Everyone).
*   **ACL (Access Control Lists):** שכבת הרשאות מתקדמת ב-macOS המאפשרת הגדרת חוקים מדויקים ופרטניים יותר (למשל, מניעת מחיקה) מעבר למגבלות של POSIX.
*   **Managed Apple Account (MAID):** בעבר נקרא Managed Apple ID. חשבון הנוצר ומנוהל על ידי הארגון דרך Apple Business Manager או Apple School Manager. בניגוד לחשבון אפל פרטי, חשבון זה נתון להגבלות ארגוניות ואינו תומך בחלק משירותי הצרכן (כמו Find My או רכישות ב-App Store).
*   **UID / GID (User ID / Group ID):** מזהה מספרי ייחודי לכל משתמש וקבוצה במערכת. משתמשים מקומיים שנוצרים מתחילים בדרך כלל מ-501.

## 3. מערך פקודות טרמינל (Terminal Commands סיכום שיעור)

### ניהול משתמשים וקבוצות (Directory Services & Accounts)
```bash
# הצגת מידע על המשתמש הנוכחי (כולל UID ו-GID)
id

# יצירת משתמש סטנדרטי חדש באמצעות sysadminctl (הדרך המודרנית והבטוחה)
sudo sysadminctl -addUser newuser -fullName "New User" -password "Password123"

# הפיכת משתמש קיים למנהל (Admin)
sudo sysadminctl -adminStatus on -user newuser

# מחיקת משתמש קיימת (זהירות! יש אפשרות לשמור או למחוק את תיקיית הבית)
sudo sysadminctl -deleteUser baduser -secure

# הצגת רשימת כל המשתמשים במערכת דרך Directory Service
dscl . -list /Users

# קריאת כל המידע הקיים ב-dscl על משתמש מסוים
dscl . -read /Users/username

# הצגת רשימת הקבוצות שהמשתמש חבר בהן
dseditgroup -o checkmember -m username admin
```

### ניהול הרשאות תצורה (POSIX & ACL)
```bash
# הצגת רשימת קבצים מפורטת כולל הרשאות POSIX (קריאה/כתיבה/הפעלה)
ls -la

# הצגת רשימת קבצים מפורטת כולל הרשאות מתקדמות (ACL) במידה וקיימות (יסומן ב-+ או @)
ls -le

# שינוי בעלים של קובץ או תיקייה (Owner:Group)
sudo chown -R username:staff /path/to/folder

# שינוי הרשאות POSIX במספרים (755 = קריאה/כתיבה/הפעלה לבעלים, קריאה/הפעלה לשאר)
sudo chmod 755 /path/to/file

# הוספת הרשאת הפעלה לקובץ (הפיכתו לסקריפט או קובץ הרצה)
sudo chmod +x /path/to/script.sh

# הוספת חוק ACL (הענקת זכות קריאה וכתיבה למשתמש ספציפי על תיקייה)
sudo chmod +a "username allow read,write" /path/to/folder

# הסרת חוק ACL ספציפי מקובץ
sudo chmod -a "username allow read,write" /path/to/folder

# איפוס הרשאות על תיקיית הבית (שימושי במקרה של תקלות הרשאות עמוקות)
diskutil resetUserPermissions / `id -u`
```

### אבטחה ומדיניות סיסמאות
```bash
# הצגת סטטוס ההצפנה ומידע על משתמשים מורשי FileVault
fdesetup list

# אילוץ המשתמש להחליף סיסמה בהתחברות הבאה
sudo pwpolicy -u username -setpolicy "newPasswordRequired=1"
```

## 4. נתיבים קריטיים וקובצי מערכת

*   `/Users/` - התיקייה בה שוכנות כל תיקיות הבית של המשתמשים במק.
*   `/Users/Shared/` - התיקייה המשותפת, פתוחה לקריאה וכתיבה לכל המשתמשים.
*   `~/Library/` - ספריית המשתמש המוסתרת (ספריית ה-Library האישית). מכילה העדפות, מטמונים (Caches), ונתוני אפליקציות פרטיים.
*   `/var/db/dslocal/nodes/Default/users/` - המיקום הפיזי בו נשמרים קובצי ה-plist שמייצגים את הגדרות החשבון המקומי של כל משתמש (תחליף מקומי ל-LDAP).
*   `/Library/Preferences/com.apple.loginwindow.plist` - קובץ העדפות הקובע הגדרות במסך ההתחברות (למשל, הסתרת רשימת משתמשים).

## 5. קריאה מומלצת והעשרה

להלן קישורים למקורות הרשמיים של Apple להעמקה נוספת, בהתבסס על תיעוד ה-Apple Platform Support ו-Apple Platform Deployment:

*   **הגדרת משתמשים וקבוצות במק (Apple Support):**
    [Set up users, guests, and groups on Mac](https://support.apple.com/guide/mac-help/set-up-other-users-on-your-mac-mtusr001/mac)
*   **ניהול הרשאות קבצים במק - POSIX ו-ACL (Apple Support):**
    [Change permissions for files, folders, or disks on Mac](https://support.apple.com/guide/mac-help/change-permissions-for-files-folders-or-disks-mchlp1203/mac)
*   **אודות חשבונות אפל מנוהלים בארגון - MAID (Apple Platform Deployment):**
    [About Managed Apple Accounts in Apple Platform Deployment](https://support.apple.com/guide/deployment/about-managed-apple-accounts-dep0db601c3/web)
*   **מדריך הטרמינל הרשמי של אפל:**
    [Apple Terminal User Guide](https://support.apple.com/guide/terminal/welcome/mac)
