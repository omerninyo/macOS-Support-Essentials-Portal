# Chapter 09: Network Configuration - גיליון עזר (סיכום שיעור)

## 1. נושאי השיעור

*   **1.** **ממשקים וסדרי עדיפויות:** ניהול מיקומי רשת (Locations) וסדר עדיפויות של חיבורים.
*   **2.** **כלי אבחון (Wireless Diagnostics):** ניטור תעבורה ואיתור תקלות Wi-Fi בממשק.
*   **3.** **חומת האש המובנית:** מטרת ה-Firewall ב-macOS וכיצד הוא פועל.
*   **4.** **תיבול ארגוני:** אבחון תקלות בפרוטוקולי אבטחה כגון 802.1X, Proxy ו-VPN.

גיליון זה מסכם את המושגים, הפקודות והכלים לאבחון וניהול של רשתות, תצורות ומיקומים במערכת macOS.

## מושגים ומונחי יסוד (Terms & Concepts)

* **מיקום רשת (Network Location):** פרופיל המאגד בתוכו את כלל הגדרות הרשת של המק (שירותי רשת פעילים, כתובות IP, שרתי DNS, ופרוקסי). ניתן ליצור מספר מיקומים כדי לעבור במהירות בין תצורת "בית", "משרד" ועוד.
* **סדר עדיפויות של שירותים (Service Order):** הסדר שבו המק מחפש ומתחבר לרשתות פנויות. ניתן לגרור שירות (למשל Ethernet מעל Wi-Fi) כדי להבטיח שהמק יעדיף חיבור קווי כשהוא זמין.
* **חומת אש (Firewall):** חומת האש המובנית ב-macOS פועלת ברמת האפליקציה (Application Layer Firewall - ALF). היא מאפשרת למשתמש לשלוט אילו אפליקציות או שירותים רשאים לקבל חיבורים נכנסים מהרשת (Incoming Connections).
* **מצב "חמקן" (Stealth Mode):** מצב בתוך הגדרות חומת האש שמונע מהמק להגיב לבקשות סריקה ברשת (כגון ICMP Ping או נסיונות גילוי), מה שהופך אותו ל"רואה ואינו נראה" עבור מחשבים אחרים.
* **פרופיל 802.1X:** מנגנון הזדהות מתקדם ברמת הרשת (Network Authentication). לרוב, בסביבות ארגוניות יסופק Configuration Profile המגדיר אוטומטית את אישורי ההתחברות (Credentials) והתעודות (Certificates) כדי לאפשר למק להתחבר מאובטחות לרשת הארגונית בצורה שקופה.
* **פרוקסי (Proxy) ו-VPN:** כלי תקשורת המשמשים לניתוב או הצפנת התעבורה דרך שרת ארגוני. במק מנוהל (MDM), לרוב הגדרות אלו יהיו נעולות ונפרסות מרחוק (למשל Global HTTP Proxy).

---

## פקודות טרמינל מתקדמות וכלים (Terminal Commands & Tools)

### הפקודה העוצמתית `networksetup`
הפקודה `networksetup` היא ה"אולר השוויצרי" לניהול רשת במק מהטרמינל. יש להריץ את רוב הפקודות המשנות תצורה עם הרשאות מנהל (`sudo`).

**הצגת מידע (אין חובה ב-sudo):**
* `networksetup -listallnetworkservices`
  > מציג רשימה של כל שירותי הרשת (Wi-Fi, Ethernet וכו'). שירות המופיע עם כוכבית (*) בסמוך אליו הוא שירות מושבת.
* `networksetup -getinfo "Wi-Fi"`
  > מציג את הגדרות ה-IP, ה-Subnet וה-Router הנוכחיות עבור השירות שצוין.
* `networksetup -getmacaddress "Ethernet"`
  > מאחזר את כתובת ה-MAC הפיזית (Hardware Address) של כרטיס הרשת המסוים.
* `networksetup -getdnsservers "Wi-Fi"`
  > מציג את רשימת שרתי ה-DNS המוגדרים כעת ידנית עבור שירות ה-Wi-Fi.
* `networksetup -listlocations`
  > מציג את כל מיקומי הרשת (Network Locations) שקיימים כרגע במערכת.
* `networksetup -getcurrentlocation`
  > מציג מהו מיקום הרשת הפעיל כעת.

**שינוי תצורה והגדרות IP/DNS (מחייב הרשאות):**
* `sudo networksetup -setdhcp "Ethernet"`
  > מגדיר את כרטיס ה-Ethernet למשוך כתובת IP באופן אוטומטי משרת ה-DHCP.
* `sudo networksetup -setmanual "Ethernet" 192.168.1.100 255.255.255.0 192.168.1.1`
  > מגדיר כתובת IP סטטית, יחד עם Subnet Mask ו-Router.
* `sudo networksetup -setdnsservers "Wi-Fi" 8.8.8.8 8.8.4.4`
  > מגדיר שרתי DNS באופן ידני (על מנת למחוק את השרתים הידניים ולחזור ל-DHCP, יש להשתמש בערך `empty`).

**ניהול שירותים ומיקומים:**
* `sudo networksetup -setnetworkserviceenabled "Bluetooth PAN" off`
  > מכבה לחלוטין את שירות הרשת שצוין.
* `sudo networksetup -createlocation "Office" populate`
  > יוצר מיקום רשת חדש בשם "Office" ומאכלס אותו אוטומטית בשירותי החומרה הקיימים במק.
* `sudo networksetup -switchtolocation "Office"`
  > מחליף את המערכת למיקום רשת אחר ומחיל את כל הגדרות הרשת הרלוונטיות של אותו המיקום באופן מיידי.

### כלי אבחון ובדיקה כלליים (Diagnostics)

* `ping -c 4 apple.com`
  > שולח 4 בקשות אקו (ICMP Echo Request) לשרת כדי לבדוק האם הוא זמין ומה זמן התגובה (Latency). הפקודה תעצור אוטומטית לאחר 4 נסיונות.
* `traceroute google.com`
  > מציג את כל ה"תחנות" (הראוטרים/Hops) שהמידע עובר דרכן עד הגעתו ליעד. כלי מעולה לאבחון היכן בדיוק מתרחש ניתוק ברשת.
* `nslookup apple.com`
  > מבצע שאילתת DNS פשוטה ומציג לאיזו כתובת IP השרת מתרגם את שם המתחם.
* `dig apple.com`
  > כלי מקצועי ומפורט יותר לבדיקת רשומות DNS, המציג את זמני המענה מהשרת ואת סוגי הרשומות המדויקים.
* `ifconfig`
  > פקודת UNIX וותיקה המציגה מידע ברמת הליבה (Interface Level) על כל כרטיסי הרשת והרשתות הווירטואליות. מיועדת יותר לחקירת המצב הפיזי או סביבות Containers.
* `netstat -rn`
  > מציג את טבלת הניתוב (Routing Table) הפנימית של המק.
* `lsof -i :80`
  > מציג אילו תהליכים ואפליקציות פתוחים כרגע במק ומאזינים או מקושרים לפורט ספציפי (בדוגמה זו - פורט 80).

---

## קבצים ונתיבים שימושיים (Useful Paths)

* `/Library/Preferences/SystemConfiguration/preferences.plist`
  > קובץ התצורה הראשי המכיל את כל הגדרות ממשקי הרשת והמיקומים של המק. אדמיניסטרטורים לעיתים מוחקים קובץ זה כדי לאפס לחלוטין את הרשת במערכת במקרה של תקלות חמורות.
* `/Library/Preferences/com.apple.alf.plist`
  > קובץ התצורה של חומת האש (ALF).

---

## לקריאה נוספת והעמקה (Recommended Reading & Enrichment Links)

להלן קישורים רשמיים מתוך Apple Platform Support להעמקה בהגדרות הרשת ותצורות מורכבות:

* **Use network locations on Mac:**
  [https://support.apple.com/en-us/105129](https://support.apple.com/en-us/105129)
* **Change Firewall settings on Mac:**
  [https://support.apple.com/guide/mac-help/change-firewall-settings-on-mac-mh34041/mac](https://support.apple.com/guide/mac-help/change-firewall-settings-on-mac-mh34041/mac)
* **Connect to an 802.1X network on Mac:**
  [https://support.apple.com/guide/mac-help/connect-to-an-8021x-network-on-mac-mchlp1094/mac](https://support.apple.com/guide/mac-help/connect-to-an-8021x-network-on-mac-mchlp1094/mac)
* **Deploy Wi-Fi payload settings for Apple devices:**
  [https://support.apple.com/guide/deployment/wi-fi-payload-settings-dep40eb424c/web](https://support.apple.com/guide/deployment/wi-fi-payload-settings-dep40eb424c/web)
