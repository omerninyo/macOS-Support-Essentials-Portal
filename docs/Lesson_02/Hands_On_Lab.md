# שיעור 02: ניהול משתמשים ואבטחת נתונים
**מעבדה מעשית (תרגול לתלמיד)**

## מעבדה 1: אבטחה חסרת סיסמה (Passkeys) והיכרות עם אפליקציית Passwords

**מטרת המעבדה:**

התנסות מעשית ביצירת Passkey חדש לחלוטין מול שרת מרוחק, הבנת תהליך האימות בעזרת Secure Enclave, וסקירת התוצאה בתוך אפליקציית ניהול הסודות של macOS.

**דרישות קדם:**

* מחשב Mac הפועל על macOS 15 ומעלה.
* קורא טביעות אצבע (Touch ID) מוגדר, או שימוש בסיסמת המחשב החלופית.

**שלבי המעבדה:**

### חלק א': יצירת ה-Passkey

1. פתח את דפדפן Safari במחשבך.
2. נווט אל אתר המעבדה (סביבת בדיקות ציבורית של מפתחי FIDO): [https://webauthn.io/](https://webauthn.io/).
3. בתיבת ה-**Username**, בחר שם משתמש ייחודי (למשל השם שלך בצירוף מספר אקראי: `OmerAppleClass123`).
4. ודא כי סוג ה-Attestation מכוון ל-`None` (לצורך ההדגמה) ולחץ על הכפתור **Register**.
5. מערכת macOS תזהה את בקשת הרישום ותקפיץ חלונית פופ-אפ. החלונית תשאל אם תרצה ליצור מפתח גישה (Passkey) עבור משתמש זה.
6. אמת את זהותך בעזרת מגע ב-**Touch ID** (או הזנת סיסמת המחשב המקומית).
7. לאחר האימות, תראה באתר הודעת התחברות מוצלחת. ברקע, ה-Secure Enclave של ה-Mac שלך ייצר זוג מפתחות קריפטוגרפיים ושמר את המפתח הפרטי ב-iCloud Keychain מבלי לחשוף אותו לרשת.

### חלק ב': התחברות נטולת סיסמה

1. כעת, באותו דף של [webauthn.io](https://webauthn.io/), גלול חזרה למעלה ולחץ על לחצן ה-**Authenticate** (לאחר שווידאת ששם המשתמש שלך עדיין רשום בתיבה).
2. חלון של Safari יקפוץ וישאל "האם להשתמש ב-Passkey שלך?".
3. גע שוב ב-**Touch ID**.
4. נכנסת לאתר מידית, ללא הקלדת סיסמה וללא יכולת לשכוח אותה (Passwordless Sign-In).

### חלק ג': צפייה בסודות באפליקציית Passwords

1. פתח את ה-Spotlight (קיצור דרך Command + Space) והקלד **Passwords**. לחץ Enter לפתיחת האפליקציה.
2. אמת את זהותך ב-Touch ID כדי לפתוח את מנהל הסודות המובנה.
3. בסרגל הצד (Sidebar), בחר בקטגוריית **Passkeys**.
4. ברשימה, מצא את הרשומה עבור `webauthn.io`.
5. לחץ עליה. שים לב שלא מופיעה "סיסמה" גלויה (מכיוון שהיא אינה קיימת כתמליל רגיל וחשוף), אלא מצוין מפורשות שזהו Passkey עם תאריך היצירה שלו.


!!! tip "המחשה ויזואלית (עזר לתלמיד)"
    תמונות אלו ממחישות את הממשק או המנגנון הרלוונטי לנושא השיעור.

![Slide87_image22](../assets/images/Lesson_02/L02_LegacySlide_Slide87_image22.jpg)
![Slide87_image23](../assets/images/Lesson_02/L02_LegacySlide_Slide87_image23.jpg)
![Slide89_image24](../assets/images/Lesson_02/L02_LegacySlide_Slide89_image24.jpg)
![Slide90_image25](../assets/images/Lesson_02/L02_LegacySlide_Slide90_image25.jpg)
![Slide91_image26](../assets/images/Lesson_02/L02_LegacySlide_Slide91_image26.jpg)
![26-Tahoe-Fast-User-Lockscreen-scaled](../assets/images/Lesson_02/L02_TahoeUI_26-Tahoe-Fast-User-Lockscreen-scaled.png)
![26-Tahoe-Settings-Lock-Screen-scaled](../assets/images/Lesson_02/L02_TahoeUI_26-Tahoe-Settings-Lock-Screen-scaled.png)
![26-Tahoe-Settings-Touch-ID-scaled](../assets/images/Lesson_02/L02_TahoeUI_26-Tahoe-Settings-Touch-ID-scaled.png)
