# פרק 6: מערכת הקבצים והאחסון (APFS Internals) – גיליון עזר (סיכום שיעור)

## 1. נושאי השיעור

*   **1.** **מהפיכת APFS:** מבנה מערכת הקבצים, Containers וחלוקת שטח דינמית.
*   **2.** **הפרדת המערכת (SSV):** נעילת ה-System Volume והגנה קריפטוגרפית.
*   **3.** **ניהול כוננים:** תרגול ניהול Volumes דרך Disk Utility.
*   **4.** **תיבול ארגוני:** השפעת מנגנון ה-SSV על כלי ניהול ואבטחה חיצוניים.

## מושגי יסוד במערכת הקבצים
* **APFS - Apple File System:** מערכת הקבצים המודרנית של Apple. הושקה במקור ב-iOS 10.3 וב-macOS 10.13, והיא פותחה מראש תוך התאמה לכונני Flash (SSD), הצפנה, ושיתוף מקום דינמי.
* **Container:** "מכל" היושב מעל המחיצה הפיזית ומאגד בתוכו מספר Volumes של APFS. ה-Container מרכז את ניהול המקום הדינמי.
* **Volume :** מחיצה לוגית בתוך ה-Container. בניגוד למחיצות מסורתיות (Partitions), Volumes ב-APFS אינם תופסים מקום מוגדר מראש אלא משתמשים בשטח הפנוי של ה-Container לפי דרישה.
* **Sealed System Volume - SSV:** Volume המערכת החתום. Volume המוגן ברמת הקרנל וקריפטוגרפיה, המכיל את קבצי מערכת ההפעלה בלבד (מונע שינויים מצד משתמשים, אפליקציות ונוזקות). ה-SSV תמיד פועל כ-Read-Only.
* **Data Volume:** ה-Volume המכיל את הקבצים של המשתמשים, הגדרות, ואפליקציות שהותקנו (צד-שלישי). משולב יחד עם ה-SSV ליצירת תצוגה אחודה ב-Finder.
* **Firmlink:** קישור מערכתי (שפותח במיוחד עבור APFS החל מ-macOS 10.15) המגשר באופן דו-כיווני בין תיקיות ב-SSV (לקריאה בלבד) לתיקיות מקבילות ב-Data Volume, ליצירת אשליית "מחיצה אחת שלמה" (לדוגמה: גישור מ-/Users לווליום הנתונים).
* **Snapshot :** גיבוי מיידי, קפוא בזמן, ולקריאה בלבד של מצב מערכת הקבצים ברגע נתון. אינו תופס מקום ברגע היווצרותו, אך שומר עותק של בלוקים המשתנים לאחר מכן.
* **Space Sharing:** מנגנון הליבה ב-APFS שמאפשר למספר Volumes להשתמש ולחלוק את אותו שטח דיסק פנוי בתוך Container יחיד.
* **Copy-on-Write - CoW:** מנגנון ייעול; בעת שכפול קובץ, המערכת רק יוצרת מצביע לקובץ המקורי. המידע הפיזי משוכפל בדיסק רק ברגע שאחד העותקים משתנה. חוסך מקום ומאפשר "העתקה מיידית".
* **Volume Group:** קבוצה אגודה של System Volume ו-Data Volume שמחוברים יחדיו (מיוצגים כ-Macintosh HD בממשק המשתמש).

## רשימת פקודות מקיפה: `diskutil`
הכלי `diskutil` הוא כלי הליבה לניהול מערכות אחסון ב-macOS. פקודות בתוך `diskutil apfs` מתייחסות ספציפית למכולות וווליומים של APFS.

### פקודות מידע וסטטוס (Information & Verification)
* `diskutil list`
  הצגת רשימת כל הכוננים (הפיזיים והלוגיים), הקונטיינרים והווליומים המחוברים למערכת.
* `diskutil apfs list`
  הצגת רשימה מפורטת של Containers APFS בלבד, כולל שטח אחסון (Quota/Reserve) ואילו Volumes שייכים לאיזה Container.
* `diskutil info /`
  הצגת מידע מפורט על Volume יעד (במקרה זה, `/` שהוא תיקיית השורש). כולל הגדרות הצפנה, סוג מערכת הקבצים (APFS), ה-UUID המדויק ורמות הרשאה.
* `diskutil info diskX`
  קבלת מידע ספציפי על הדיסק או ה-Volume בעל המזהה `diskX`.
* `diskutil verifyVolume /`
  בדיקת תקינות מערכת הקבצים של Volume יעד (מבלי לתקן אותו).
* `diskutil repairVolume /`
  הרצת תהליך תיקון (First Aid) על Volume ספציפי דרך הטרמינל במקרה של שחיתות נתונים קלה (מומלץ לבצע ממצב התאוששות / Recovery Mode).
* `diskutil apfs listVolumeGroups`
  מציג את קבוצות הווליומים (Volume Groups), מה שמאפשר לראות איזה Volume מערכת ממופה לאיזה Volume נתונים (Data Volume).

### עבודה עם Volumes ב-APFS (הוספה ומחיקה)
בניגוד למחיצות (Partitions) ישנות, ניתן להוסיף Volumes באופן מיידי וללא אובדן נתונים.

```bash
# הוספת Volume חדש בשם "DataVault" בפורמט APFS אל תוך Container המזוהה כ-disk2
diskutil apfs addVolume disk2 APFS "DataVault"

# הוספת Volume והגבלתו (Quota) לנפח מקסימלי של 50 גיגה-בייט
diskutil apfs addVolume disk2 APFS "LimitedVol" -quota 50g

# הוספת Volume ו"שריון" (Reserve) של 20 גיגה-בייט
diskutil apfs addVolume disk2 APFS "ReservedVol" -reserve 20g

# מחיקת ה-Volume המסומן כ-disk3s5 (מוחק את כל תוכנו ומחזיר מקום לקונטיינר)
diskutil apfs deleteVolume disk3s5

# שינוי שם של Volume
diskutil rename disk3s5 "NewName"
```

### ניהול Containers וחלוקת מחיצות (Partitioning)
* `diskutil apfs resizeContainer disk2 150g`
  שינוי גודל ה-Container (נניח `disk2`) ל-150GB. יפנה מקום פיזי בדיסק לטובת מחיצות אחרות, אך יעבוד רק אם אין נתונים בחלק שנחתך. במחשבי Apple Silicon לא ניתן פשוט להקטין Container מערכת ללא שיקול, עקב פריסת ה-Recovery.
* `diskutil apfs resizeContainer disk2 0`
  הרחבת ה-Container למקסימום השטח הפנוי הזמין במחיצה הפיזית.
* `diskutil apfs create disk1s2`
  יצירת Container חדש לגמרי של APFS מתוך מחיצה ריקה.
* `diskutil apfs deleteContainer disk2`
  מחיקת Container שלם על כל הווליומים שבתוכו, והחזרת המחיצה למצב Mac OS Extended (לפני בנייה מחדש). **אזהרה: מוחק הכל!**
* `diskutil partitionDisk disk1 2 APFS "Container1" 50% APFS "Container2" 50%`
  מחיקת הדיסק הפיזי כולו (`disk1`) ויצירת 2 מחיצות נפרדות מסוג APFS בגודל 50% כל אחת.

### עבודה עם Snapshots
* `diskutil apfs listSnapshots /`
  מציג את כל ה-Snapshots השמורים ב-Volume השורש (System/Data). מאפשר לראות גיבויים קפואים ואת ה-UUID שלהם (לדוגמה, כאלו שנוצרו על ידי Time Machine או לפני עדכון מערכת).
* `diskutil apfs deleteSnapshot disk3s1 -uuid <Snapshot-UUID>`
  מחיקה ידנית של Snapshot ספציפית בעזרת מזהה ה-UUID שלה, לטובת פינוי מקום מיידי על הדיסק (במקרים שה-Snapshot שוקל הרבה בגלל שינויים).
* `tmutil localsnapshot`
  יצירה מיידית של Snapshot מקומי לגיבוי מיידי לפני שינוי קריטי במערכת ההפעלה (נפוץ בבדיקות תוכנה או IT).

---

## תיבול ארגוני: אתגרי APFS בארגון מנוהל
1. **SSV ופתרונות אבטחה (EDR/Antivirus):** מכיוון שה-SSV מוגן קריפטוגרפית (Read-Only) ולקרנל אין הרשאת כתיבה, תוכנות אבטחה ארגוניות לא צריכות ולא יכולות לסרוק את תיקיות המערכת. על כלי צד-שלישי להתקין הרחבה שמקבלת גישה בעזרת System Extension (ולא Kext) וסורקת רק את ה-Data Volume.
2. **ניהול שטח לוקאלי:** משתמשים ללא הרשאות אדמין יכולים לנהל קבצים ב-Data Volume, אך כל הוספה/מחיקה של APFS Volume חדש מצריכה הרשאות Admin. כלי MDM מסוימים יכולים לשלוט בהצפנת Volume בעזרת פרופילי FileVault (כפי שיילמד בפרק 4).
3. **Firmware ו-Apple Silicon:** על מק מבוסס Apple Silicon, ניהול המחיצות והקונטיינרים (במיוחד מחיקתם) דורש התערבות במצב התאוששות (Recovery Mode) בעזרת `Startup Security Utility` במידה והארגון דורש הגדרות בוט שונות. יצירת Containers לא רשמיים בצורה שגויה עשויה להשפיע לרעה על מחיצת ההתאוששות (1TR).

---

## קישורים מומלצים ולקריאה נוספת
* [Signed System Volume (SSV)](https://support.apple.com/guide/security/signed-system-volume-security-secd698747c9/web) - המאמר הרשמי של אפל שמסביר איך מנגנון ה-SSV נועל ומגן על קבצי המערכת.
* [Volume groups and macOS update security](https://support.apple.com/guide/security/volume-groups-and-macos-update-security-secb26c04f5e/web) - מבט לעומק על איך בנויה קבוצת הכוננים (System ו-Data).
* [Add, delete, or erase APFS volumes in Disk Utility on Mac](https://support.apple.com/guide/disk-utility/add-erase-or-delete-apfs-volumes-dskua9e6a11a/web) - מדריך בסיסי למשתמש איך להוסיף או למחוק כונני APFS.
* [What are all those Containers?](https://eclecticlight.co/2021/01/13/what-are-all-those-containers/) - מאמר טכני שחופר על תפקידו של כל קונטיינר ודיסק נסתר במק.
* [How macOS depends on firmlinks](https://eclecticlight.co/2021/01/22/how-macos-depends-on-firmlinks/) - הסבר טכני מעולה על "הקסם" שמחבר את כונן המערכת לכונן הנתונים ליצירת אשליה של כונן אחד.