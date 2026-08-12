# שיעור 05 — אפליקציות ותהליכים
## מדריך עזר לתלמיד

---

## מטרות השיעור

- הכרת שלושת ערוצי ההתקנה ב-macOS (App Store, DMG, PKG)
- הבנת מנגנון ה-Sandbox — היכן אפליקציות שומרות מידע

- שליטה בכלים לאבחון ואילוץ סגירה של תהליכים תקועים
- הכרת מנגנון VPP ו-Self Service בסביבה ארגונית

---

## 🎧 האזנה לסיכום — לפני או אחרי השיעור

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/57c8a1df-bbc5-4e2e-9986-b6e4b0e04f4e/"></iframe></div>

---

## מושגי יסוד

| מושג | הסבר |
|---|---|
| **App Store** | החנות הרשמית של אפל. כל אפליקציה עוברת ביקורת, נוטריזציה ופועלת תחת Sandbox |
| **DMG (Disk Image)** | כונן וירטואלי. לחיצה כפולה = Mount. גרירה ל-Applications = התקנה. Eject = חובה בסוף |
| **PKG (Package)** | מתקין מערכתי. מפזר קבצים לנתיבים מוגנים → תמיד ידרוש סיסמת Admin |
| **Gatekeeper** | שוטר הכניסה של macOS — בודק שכל אפליקציה חתומה ואושרה על ידי אפל |
| **Notarization** | סריקת אפליקציה אוטומטית על ידי אפל לפני שמותר לה לרוץ |
| **Sandbox** | בועת בידוד — אפליקציה לא יכולה לגשת לקבצים מחוץ לה ללא אישור |
| **Container** | תיקיית הבית של אפליקציית Sandbox. נמצא ב-`~/Library/Containers/[Bundle ID]` |
| **Force Quit** | סגירת תהליך תקוע ללא שמירה (שליחת `SIGKILL`) |
| **VPP / ABM** | מנגנון רכישת רישיונות ארגוני. הרישיון שייך לארגון, לא למשתמש |
| **Self Service** | חנות אפליקציות פרטית של הארגון — התקנה ללא Admin וללא Apple ID אישי |

---

## חלק 1 — סוגי התקנה

### איפה זה ב-Finder

```
קובץ DMG:  הורדות (Downloads) → לחיצה כפולה → Volume ב-Sidebar → גרור ל-Applications
קובץ PKG:  לחיצה כפולה → אשף התקנה → Admin נדרש
App Store:  לחפש, ללחוץ הורד — הכל אוטומטי
```

### שינוי חשוב ב-Tahoe

> [!IMPORTANT]
> אפליקציה שלא מאושרת — **קליק ימני → Open לא עובד יותר ב-Tahoe**.
> הדרך היחידה: `System Settings → Privacy & Security → גלול מטה → Open Anyway`

---

## חלק 2 — Sandbox ואיפוס אפליקציות

### נתיבים חשובים

*(תזכורת משיעור 2: תיקיית ה-Library בתיקיית הבית שלכם (`~/`) היא המרחב האישי של המשתמש. באופן מסורתי, כאן האפליקציות שומרות את ההגדרות והמידע שלכן. אנו נלמד לעומק על ארכיטקטורת המרחבים במערכת בשיעור הבא).*

| מה | נתיב |
|---|---|
| הגדרות (Preferences) | `~/Library/Preferences/com.domain.app.plist` |
| Application Support | `~/Library/Application Support/AppName/` |
| Container (Sandbox) | `~/Library/Containers/[Bundle ID]/` |

### סדר נכון לאיפוס אפליקציה

1. סגור לחלוטין: `Cmd+Q`
2. פתח Finder → Go → החזק `Option` → **Library**
3. היכנס ל-`Containers/` → מצא את תיקיית האפליקציה
4. העבר לאשפה (Trash) ורוקן
5. פתח מחדש → מסך "ברוכים הבאים" = האיפוס הצליח

> [!NOTE]
> אפליקציה שנמחקה מ-`/Applications/` **אינה** מוחקת את ה-Container!
> ה-Container חייב להימחק בנפרד.

---

## חלק 3 — Force Quit

### 4 הדרכים

| דרך | איך |
|---|---|
| **הכי מהיר** | `Cmd + Option + Esc` |
| **Dock** | קליק ימני על האייקון + החזק `Option` → Force Quit |
| **אבחון וסגירה** | Activity Monitor → בדיקת משאבי CPU/RAM ו-Open Files לפני לחיצה על `X` |
| **טרמינל (CLI)** | פקודת `killall AppName` לסגירה מיידית מרחוק או כשהעכבר קפוא |

### Quit מול Force Quit

| פעולה | מה נשלח | תוצאה |
|---|---|---|
| Quit רגיל | `SIGTERM` | אפליקציה שומרת ומתרוקנת בסדר |
| Force Quit | `SIGKILL` | הקרנל רוצח מיידית — **ללא שמירה** |

---

## חלק 4 — VPP ו-Self Service

### הזרימה הארגונית

```
Apple Business Manager (ABM)
        ↓ רישיונות
   שרת MDM ארגוני
        ↓ Silent Install
    מחשב העובד
        ↓ 
  Self Service (קטלוג פרטי לעובד)
```

**התוצאה:** עובד לוחץ "התקן" — MDM מתקין ברקע — **ללא Admin, ללא Apple ID אישי**

---

## פקודות Terminal — נספח

> [!NOTE]
> ה-Terminal לא נדרש לתרגילי השיעור. פקודות אלו הן הרחבה למי שמעוניין.

```bash
# עגינת DMG ידנית
hdiutil attach /path/to/image.dmg

# ניתוק DMG
hdiutil detach /Volumes/ImageName

# התקנת PKG שקטה (לסקריפטים של IT)
sudo installer -pkg /path/to/file.pkg -target /

# איפוס הגדרות אפליקציה (Preferences בלבד, לא Container)
defaults delete com.apple.Safari

# ריקון מטמון הגדרות (אחרי מחיקת Container)
killall cfprefsd

# בדיקת חתימת PKG
pkgutil --check-signature /path/to/file.pkg

# התקנת Rosetta 2 שקטה
softwareupdate --install-rosetta --agree-to-license
```

---

## קישורים ולקריאה נוספת

- [Check app installation and processes on Mac — Apple Support](https://support.apple.com/guide/apple-platform-support/check-app-installation-and-processes-apda5f8a096c/web)
- [Learn about App Store security protections](https://support.apple.com/guide/apple-platform-support/learn-about-app-store-security-protections-apd1a7b8e19c/web)
- [Distribute content with mobile device management](https://support.apple.com/guide/deployment/distribute-content-depe210182ce/web)
- [Explainer: the app sandbox — Eclectic Light](https://eclecticlight.co/2020/09/24/explainer-the-app-sandbox/)

---

## 🎬 סרטון סיכום

<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/z_52E-9epcY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

## תמונות מהחוברת ומהמצגת

!!! tip "עזרים ויזואליים"
    תמונות אלו ממחישות את הממשק הנלמד בשיעור.

![השוואת סוגי התקנה](../assets/images/Lesson_05/L05_LegacySlide_Slide103_image33.jpg)
![דיאגרמת ABM ו-MDM](../assets/images/Lesson_05/L05_LegacySlide_Slide121_image134.jpg)
![ממשק Self Service](../assets/images/Lesson_05/L05_LegacySlide_Slide66_image11.jpg)
![App Store ב-Tahoe](../assets/images/Lesson_05/L05_TahoeUI_26-Tahoe-App-Store-scaled.png)
![Force Quit ב-Tahoe](../assets/images/Lesson_05/L05_TahoeUI_26-Tahoe-Force-Quit-scaled.png)
