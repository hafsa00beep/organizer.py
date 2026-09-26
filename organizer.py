import os
import shutil

# تحديد المجلد المراد تنظيمه
target_dir = input("أدخل مسار المجلد المراد تنظيمه: ")

# امتدادات الملفات والمجلدات الخاصة بها
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Audio': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.7z']
}

for filename in os.listdir(target_dir):
    filepath = os.path.join(target_dir, filename)
    
    if os.path.isfile(filepath):
        file_ext = os.path.splitext(filename)[1].lower()
        moved = False
        
        for folder_name, extensions in file_types.items():
            if file_ext in extensions:
                folder_path = os.path.join(target_dir, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(filepath, os.path.join(folder_path, filename))
                print(f"تم نقل {filename} إلى {folder_name}")
                moved = True
                break
                
        if not moved:
            other_path = os.path.join(target_dir, 'Others')
            os.makedirs(other_path, exist_ok=True)
            shutil.move(filepath, os.path.join(other_path, filename))

print("✨ تم تنظيم المجلد بنجاح!")index.html
