# שיעור 10: שיתוף וגישה מרחוק
**מדריך עזר לתלמיד**


## סקירה

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/332582b3-c603-4af5-a4a2-81be768b38a6/"></iframe></div>

## מושגי מפתח (Key Concepts)

| מושג | רקע היסטורי מה-DeepDive |
| :--- | :--- |
| **AFP (Apple Filing Protocol)** | פרוטוקול שהוצג לראשונה ב-1988 והיה ברירת המחדל של אפל עד OS X 10.8. אינו נתמך רשמית כיום. |
| **SMB (Server Message Block)** | פותח במקור ב-IBM ואומץ ע"י מיקרוסופט. החליף את AFP וכיום מהווה הסטנדרט, למרות מגבלות מול קבצי Sparse של APFS. |
| **Chooser** | אפליקציה היסטורית ממערכת System 7 (1991) ששימשה לגילוי שרתים ומדפסות (AppleShare) לפני עידן ה-Zero-Configuration (כמו AirDrop ו-Bonjour). |
| **Recovery / 1TR** | מחיצת ההתאוששות הוצגה לראשונה רק ב-2011. כיום במעבדי Apple Silicon (1 True Recovery) היא סביבה מאובטחת המשמשת גם בסיס ל-Mac Sharing Mode. |

## פרוטוקול SMB (Server Message Block)

- **SMB - Server Message Block:** הפרוטוקול העיקרי והסטנדרטי כיום ב-macOS לשיתוף קבצים ברשת (החליף את AFP הישן).
- **SMB 3.x:** הגרסה המודרנית המציעה הצפנה מקצה לקצה ותמיכה טובה יותר בביצועים וברשתות לא יציבות.

### פקודות SMB (smbutil)

- `smbutil statshares -a`: מציג את כל חיבורי ה-SMB הפעילים כרגע ואת המאפיינים שלהם (כולל גרסת פרוטוקול SMB ורמת ההצפנה).
- `smbutil lookup <hostname>`: ביצוע שאילתה לפתרון שם (Name Resolution) לכתובת IP בסביבת NetBIOS/SMB.
- `smbutil view //user@server`: מציג את רשימת תיקיות השיתוף הזמינות בשרת ספציפי עבור המשתמש.

## שירותי שיתוף (Sharing Services)

- **File Sharing:** מאפשר גישה מרחוק לקבצים על המק דרך פרוטוקול SMB.
- **Screen Sharing:** שיתוף מסך למשתמשים אחרים או גישה מרחוק, מבוסס על שדרוג של פרוטוקול VNC.
- **Mac Sharing Mode:** (במחשבי Apple Silicon) מאפשר לחבר מק אחד לאחר בכבל נתונים (USB/Thunderbolt) ולהתייחס אליו כאל כונן חיצוני ברשת מקומית וירטואלית (מחליף את ה-Target Disk Mode ההיסטורי).

### ניהול שיתוף בשורת הפקודה (sharing)

- `sharing -l`: מציג את כל תיקיות השיתוף שמוגדרות במחשב כרגע (Share Points).
- `sudo sharing -a <path>`: מוסיף תיקייה חדשה לרשימת התיקיות המשותפות (Share Point).
- `sudo sharing -r <share_point_name>`: מסיר תיקייה מרשימת השיתוף.
- `sudo sharing -e <share_point_name> -s <flags>`: עריכת ההרשאות או דגלים ספציפיים לתיקייה משותפת קיימת.

## גילוי שירותים ברשת (Bonjour & dns-sd)

- **Bonjour / mDNS:** מנגנון ה-Zero-configuration של אפל, המאפשר למחשבים ולשירותים (כמו מדפסות, תיקיות משותפות) להכריז על עצמם ברשת המקומית ללא צורך בשרת DNS מרכזי (Multicast DNS).

### פקודות mDNS / Bonjour (dns-sd)

- `dns-sd -B _smb._tcp`: "סריקה" (Browse) של כל שרתי ה-SMB המכריזים על עצמם כעת ברשת המקומית.
- `dns-sd -B _ssh._tcp`: סריקה של כל מכשירי ה-SSH/Remote Login הזמינים בסביבה.
- `dns-sd -B _ipp._tcp`: סריקה של מדפסות רשת (Internet Printing Protocol).
- `dns-sd -L <Name> _smb._tcp`: פתרון שם (Lookup) לשרת ספציפי שגילינו בסריקה כדי לקבל את כתובת ה-IP והפורט המדויקים שלו.

## Continuity וקישוריות אלחוטית

- **AirDrop:** טכנולוגיה לשיתוף קבצים מהיר בין מכשירי Apple בסביבה הקרובה באמצעות Bluetooth (ליצירת "לחיצת יד" ואיתור) ו-Wi-Fi Direct P2P (להעברת הנתונים עצמם ללא תלות בראוטר מרכזי).
- **Universal Control:** תכונה המאפשרת להשתמש בעכבר ומקלדת של מק אחד ולשלוט בעזרתם על מכשירי מק או אייפד אחרים סמוכים באופן חלק. המכשירים מתקשרים על גבי רשת Wi-Fi ו-Bluetooth זהים.

## Enterprise Seasoning: Single Sign-On (SSO)

- **Kerberos SSO Extension:** תוסף מובנה במערכת macOS המאפשר למשתמשים בארגון להזדהות פעם אחת בלבד מול שרת ה-Active Directory / Identity Provider.
- **TGT - Ticket-Granting Ticket:** "כרטיס הגישה" הקריפטוגרפי שהרחבת ה-Kerberos מקבלת מהשרת, ומשמש להזדהות מול שירותים אחרים (כמו כונני SMB ואינטראנט) בצורה שקופה ואוטומטית ללא צורך בהזנת סיסמה נוספת.
- פרופיל ה-MDM בארגון תומך כיום ב-Extensible SSO payload להגדרת הדומיינים באופן אחיד במחשבי החברה.

---

## קישורים מומלצים ולקריאה נוספת

* [Connect your Mac to shared computers and servers](https://support.apple.com/guide/mac-help/connect-mac-shared-computers-servers-mchlp1140/mac) - מדריך למשתמש איך להתחבר לתיקיות רשת בארגון.
* [Set up file sharing on Mac](https://support.apple.com/guide/mac-help/set-up-file-sharing-on-mac-mh17131/mac) - מדריך פשוט על הגדרת שיתוף קבצים מהמק שלך לאחרים.
* [Intro to Kerberos Single Sign-on extension](https://support.apple.com/guide/deployment/intro-to-kerberos-single-sign-on-extension-dep0e8082f4d/web) - מאמר טכני לאנשי IT על ניהול התחברות חכמה (SSO) בסביבת Kerberos.
* [Use AirDrop on your Mac](https://support.apple.com/en-us/102522) - מדריך בסיסי למשתמש לשיתוף קבצים מהיר דרך AirDrop.
* [Universal Control: Use a single keyboard and mouse between Mac and iPad](https://support.apple.com/en-us/102459) - מדריך שמסביר איך לעבוד עם עכבר אחד על כמה מכשירי אפל במקביל.
* [Transfer files using target disk mode / Mac Sharing Mode](https://support.apple.com/guide/mac-help/transfer-files-mac-computers-target-disk-mode-mchlp1443/mac) - מדריך למשתמש להעברת קבצים על ידי חיבור שני מחשבים בכבל.

## סרטון סיכום

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/DDXfEIRgAxs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


![Slide71 image86](../assets/images/Lesson_10/L10_LegacySlide_Slide71_image86.png)
![Slide71 image87](../assets/images/Lesson_10/L10_LegacySlide_Slide71_image87.png)



!!! tip "המחשה ויזואלית (עזר לתלמיד)"
    תמונות אלו ממחישות את הממשק או המנגנון הרלוונטי לנושא השיעור.


![Slide71 image86](../assets/images/Lesson_10/L10_LegacySlide_Slide71_image86.png)
![Slide71 image87](../assets/images/Lesson_10/L10_LegacySlide_Slide71_image87.png)

