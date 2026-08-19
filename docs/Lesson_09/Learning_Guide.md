# שיעור 09: רשתות
**מדריך עזר לתלמיד**

---

## מטרות השיעור

* **ממשקים וסדרי עדיפויות** - ניהול מיקומי רשת (Network Locations) ו-Service Order.
* **כלי אבחון** - Ping, Traceroute והיכרות עם פקודת העל `networksetup`.
* **חומת האש** - ה-Firewall המובנה של macOS וכיצד הוא פועל.
* **תיבול ארגוני** - אבחון פרופילי Wi-Fi מסוג 802.1X ארגוני וחיבורי VPN פרוקסי פרוסים מרחוק.

---

## 🎧 סקירה (פודקאסט)

<!-- פודקאסט NotebookLM מתוך Captivate -->
<div style="width: 100%; height: 200px; margin-bottom: 20px; border-radius: 6px; overflow: hidden;"><iframe style="width: 100%; height: 200px;" frameborder="no" scrolling="no" allow="clipboard-write" seamless src="https://player.captivate.fm/episode/67a8f7c6-ffba-4387-824a-b30a7eeef5ae/"></iframe></div>

---

## מושגים ומונחי יסוד (Terms & Concepts)

| מושג | הסבר |
|---|---|
| **מיקום רשת (Network Location)** | פרופיל המאגד בתוכו את כלל הגדרות הרשת (כתובות IP, שרתי DNS, ופרוקסי). מאפשר לעבור במהירות בין תצורת "בית", "משרד" ועוד, ללא שינוי ההגדרות בפרופיל אחר. |
| **סדר עדיפויות (Service Order)** | הסדר שבו המק מחפש ומתחבר לרשתות פנויות. ניתן לגרור שירות (למשל Ethernet מעל Wi-Fi) להעדפת חיבור קווי. |
| **חומת אש (Firewall - ALF)** | חומת האש ב-macOS פועלת ברמת האפליקציה (Application Layer). שולטת אילו אפליקציות רשאיות לקבל חיבורים נכנסים (Inbound). |
| **מצב "חמקן" (Stealth Mode)** | מונע מהמק להגיב לבקשות סריקה ברשת (כמו ICMP Ping). המק הופך "רואה ואינו נראה" עבור מחשבים אחרים ברשת. |
| **פרופיל 802.1X** | מנגנון אימות מתקדם לארגונים (WPA-Enterprise). מסופק לרוב כ-Configuration Profile (פיילוד מה-MDM) המגדיר אוטומטית תעודות (Certificates). |
| **Proxy ו-VPN** | כלים לניתוב או הצפנת התעבורה. במחשב מנוהל (MDM), הגדרות אלו לרוב נפרסות כ-Payload שאינו ניתן לשינוי על ידי המשתמש. |

> *← תעודות (Certificates) שנדרשות ל-802.1X נלמדו לעומק בשיעור 04 (MDM ואבטחה) — כאן רואים כיצד MDM דוחף אותן אוטומטית למק של העובד.*

!!! important "Stealth Mode בסביבה ארגונית"
    הפעילת Stealth Mode יכולה לשבש כלי ניטור רשת שבודק את ה-Mac באמצעות Ping. אם Ping לא עובד — זה לא אומר שהמק כבוי; וודאו תחילה שהמק מחובר על ידי Bonjour / `dns-sd -B`. בסביבות ארגוניות הפעילו דרך MDM.

!!! note "הערה היסטורית"
    פקודת `ifconfig` נחשבת כיום למיושנת ברוב הפצות לינוקס (שהחליפו אותה ב-`ip`), אך ב-macOS היא נותרה נתמכת ויעילה לחלוטין לאבחון ממשקים ברמת הליבה.

---

## פקודות טרמינל מתקדמות וכלים (Terminal Commands)

!!! warning
    הפקודה `networksetup` היא ה"אולר השוויצרי" לניהול רשת. רוב הפקודות המשנות תצורה דורשות הרשאות מנהל (`sudo`).

    *← ה-Firewall מתנהל על ידי `socketfilterfw` שרץ כ-Daemon תחת launchd — נלמד בשיעור 08 (Terminal). אפשר לעקוב אחריו ב-Console בדיוק כמו אחרי כל Daemon אחר.*

### 1. הצגת מידע (ללא צורך בהרשאות)
```bash
# רשימת כל שירותי הרשת (שירות עם * מושבת)
networksetup -listallnetworkservices

# הצגת הגדרות IP/Subnet לשירות ספציפי
networksetup -getinfo "Wi-Fi"

# אחזור כתובת ה-MAC הפיזית
networksetup -getmacaddress "Ethernet"

# צפייה בשרתי DNS מוגדרים ידנית
networksetup -getdnsservers "Wi-Fi"

# הצגת כל מיקומי הרשת במערכת והמיקום הפעיל
networksetup -listlocations
networksetup -getcurrentlocation
```

### 2. שינוי תצורה (מחייב sudo)
```bash
# הגדרת כרטיס למשיכת IP מ-DHCP
sudo networksetup -setdhcp "Ethernet"

# הגדרת IP סטטי, Subnet, ו-Router
sudo networksetup -setmanual "Ethernet" 192.168.1.100 255.255.255.0 192.168.1.1

# הגדרת שרתי DNS (להחזרה לאוטומטי השתמש ב-empty במקום כתובות)
sudo networksetup -setdnsservers "Wi-Fi" 8.8.8.8 8.8.4.4

# מעבר מהיר למיקום רשת אחר (מחיל הכל מיידית)
sudo networksetup -switchtolocation "Office"
```

### 3. כלי אבחון ובדיקה (Diagnostics)
| כלי / פקודה | ייעוד |
|---|---|
| `ping -c 4 apple.com` | שולח 4 בקשות ICMP לבדיקת זמינות וזמן תגובה (Latency). |
| `traceroute google.com` | מציג את כל הראוטרים/Hops בדרך ליעד לאיתור ניתוקים בניתוב. |
| `nslookup apple.com` | שאילתת DNS פשוטה לתרגום שם לכתובת IP. |
| `dig apple.com` | שאילתת DNS מקצועית ומפורטת לזמני מענה וסוגי רשומות. |
| `netstat -rn` | מציג את טבלת הניתוב (Routing Table) הפנימית של המערכת. |
| `lsof -i :80` | מציג אילו אפליקציות ותהליכים מאזינים לפורט מסוים (למשל 80). |

---

## קבצים ונתיבים שימושיים

| הנתיב | תיאור הקובץ |
|---|---|
| `/Library/Preferences/SystemConfiguration/preferences.plist` | קובץ התצורה הראשי של המיקומים והרשת. אדמינים מוחקים אותו לאיפוס מוחלט של הרשת במקרה תקלה. |
| `/Library/Preferences/com.apple.alf.plist` | קובץ ההעדפות של ה-Application Layer Firewall (ALF). |

---

## קישורים מומלצים ולקריאה נוספת

* [Use network locations on Mac](https://support.apple.com/en-us/105129) - שימוש במיקומי רשת ב-macOS.
* [Change Firewall settings on Mac](https://support.apple.com/guide/mac-help/change-firewall-settings-on-mac-mh34041/mac) - חומת האש המובנית.
* [Connect to an 802.1X network](https://support.apple.com/guide/mac-help/connect-to-an-8021x-network-on-mac-mchlp1094/mac) - התחברות לרשת ארגונית.
* [Deploy Wi-Fi payload settings for Apple devices](https://support.apple.com/guide/deployment/wi-fi-payload-settings-dep40eb424c/web) - פריסת הגדרות MDM לרשתות.

---

## 🎬 סרטון סיכום

<!-- סרטון סיכום מתוך YouTube -->
<div style="margin-bottom: 20px; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <iframe width="100%" height="450" src="https://www.youtube.com/embed/5uY9kabOEXE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

## עזרים ויזואליים

!!! tip "המחשה ויזואלית (עזר לתלמיד)"
    תמונות אלו ממחישות את הממשק או המנגנון הרלוונטי לנושא השיעור.

![Slide131_image161](../assets/images/Lesson_09/L09_LegacySlide_Slide131_image161.png)
![Slide131_image45](../assets/images/Lesson_09/L09_LegacySlide_Slide131_image45.jpg)
![Slide133_image161](../assets/images/Lesson_09/L09_LegacySlide_Slide133_image161.png)
![Slide133_image45](../assets/images/Lesson_09/L09_LegacySlide_Slide133_image45.jpg)
![Slide134_image164](../assets/images/Lesson_09/L09_LegacySlide_Slide134_image164.png)
![Slide23_image41](../assets/images/Lesson_09/L09_LegacySlide_Slide23_image41.jpg)
![Slide74_image14](../assets/images/Lesson_09/L09_LegacySlide_Slide74_image14.jpg)
![Slide74_image15](../assets/images/Lesson_09/L09_LegacySlide_Slide74_image15.jpg)
![Slide99_image103](../assets/images/Lesson_09/L09_LegacySlide_Slide99_image103.png)
![Slide99_image30](../assets/images/Lesson_09/L09_LegacySlide_Slide99_image30.jpg)
![Slide99_image31](../assets/images/Lesson_09/L09_LegacySlide_Slide99_image31.jpg)
![26-Tahoe-Finder-Connect-to-Server-scaled](../assets/images/Lesson_09/L09_TahoeUI_26-Tahoe-Finder-Connect-to-Server-scaled.png)
![26-Tahoe-Finder-Network-scaled](../assets/images/Lesson_09/L09_TahoeUI_26-Tahoe-Finder-Network-scaled.png)
![26-Tahoe-Settings-Network-scaled](../assets/images/Lesson_09/L09_TahoeUI_26-Tahoe-Settings-Network-scaled.png)
![26-Tahoe-Settings-Wi-Fi-scaled](../assets/images/Lesson_09/L09_TahoeUI_26-Tahoe-Settings-Wi-Fi-scaled.png)
