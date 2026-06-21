import os
import shutil
import glob

# Paths
source_dir = "/Users/omerninyo/Library/Mobile Documents/com~apple~CloudDocs/Wediggit/הדרכות macOS 26/קורס מתקדם מלא/macOS 26 Class/_TheClass_v3"
portal_dir = "/Users/omerninyo/Library/Mobile Documents/com~apple~CloudDocs/Wediggit/הדרכות macOS 26/קורס מתקדם מלא/macOS 26 Class/Student_Portal"
docs_dir = os.path.join(portal_dir, "docs")
mkdocs_file = os.path.join(portal_dir, "mkdocs.yml")

# Lesson titles mapped logically based on the course structure
lesson_titles = {
    "01": "שיעור 1: התקנה, הכרה ויישור קו",
    "02": "שיעור 2: ניהול משתמשים ואבטחת נתונים",
    "03": "שיעור 3: אבטחת מידע",
    "04": "שיעור 4: הצפנה ומפתחות",
    "05": "שיעור 5: אפליקציות ותהליכים",
    "06": "שיעור 6: מערכת הקבצים (APFS)",
    "07": "שיעור 7: גיבוי ושחזור",
    "08": "שיעור 8: טרמינל ושירותי רקע",
    "09": "שיעור 9: רשתות",
    "10": "שיעור 10: שיתוף וגישה מרחוק",
    "11": "שיעור 11: ציוד היקפי",
    "12": "שיעור 12: עדכונים ושדרוגים",
    "13": "שיעור 13: תהליך האתחול",
    "14": "שיעור 14: סביבת שחזור ומחיקה",
    "15": "שיעור 15: דיאגנוסטיקה",
    "16": "שיעור 16: ניתוח לוגים (חדר בריחה)"
}

nav_yaml = """
nav:
  - עמוד הבית: index.md
"""

# Process Lessons 1-16
for i in range(1, 17):
    lesson_num = f"{i:02d}"
    lesson_folder_name = f"Lesson_{lesson_num}"
    lesson_docs_dir = os.path.join(docs_dir, lesson_folder_name)
    
    # Ensure dir exists
    os.makedirs(lesson_docs_dir, exist_ok=True)
    
    lesson_nav = f"  - '{lesson_titles.get(lesson_num, f'שיעור {i}')}':\n"
    
    # Copy Asset C
    asset_c = glob.glob(os.path.join(source_dir, f"Lesson_{lesson_num}_Asset_C_*.md"))
    if asset_c:
        dest_c = os.path.join(lesson_docs_dir, "Cheat_Sheet.md")
        shutil.copyfile(asset_c[0], dest_c)
        lesson_nav += f"      - סיכום שיעור: {lesson_folder_name}/Cheat_Sheet.md\n"
        
    # Copy Asset D
    asset_d = glob.glob(os.path.join(source_dir, f"Lesson_{lesson_num}_Asset_D_*.md"))
    if asset_d:
        dest_d = os.path.join(lesson_docs_dir, "Hands_On_Lab.md")
        shutil.copyfile(asset_d[0], dest_d)
        lesson_nav += f"      - תרגול מעשי: {lesson_folder_name}/Hands_On_Lab.md\n"
        
    nav_yaml += lesson_nav

# Also copy Glossary
glossary_src = os.path.join(source_dir, "Glossary.md")
glossary_dest = os.path.join(docs_dir, "Glossary.md")
if os.path.exists(glossary_src):
    shutil.copyfile(glossary_src, glossary_dest)
    nav_yaml += "  - מילון מונחים (Glossary): Glossary.md\n"

# Append Nav to mkdocs.yml
with open(mkdocs_file, "r", encoding="utf-8") as f:
    content = f.read()

# Remove existing nav if it exists
import re
content = re.sub(r'\nnav:\n.*$', '', content, flags=re.DOTALL)

with open(mkdocs_file, "w", encoding="utf-8") as f:
    f.write(content + "\n" + nav_yaml)

print("Assets synced and mkdocs.yml updated successfully!")
