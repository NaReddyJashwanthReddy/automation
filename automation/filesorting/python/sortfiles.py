import os
import shutil

source_file=r"."

file_types={
    'Images': ['.jpg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar']
}

for folders in file_types:
    file_path=os.path.join(source_file,folders)
    if not os.path.exists(file_path):
        os.makedirs(file_path)

for filename in os.listdir(source_file):
    if os.path.isfile(os.path.join(source_file,filename)):
        move=False
        for file,extention in file_types.items():
            ext=os.path.splitext(filename)[1].lower()
            if ext in extention:
                shutil.move(os.path.join(source_file,filename),
                            os.path.join(source_file,file,filename))
                print(f"moved the {filename} to {file}")
                move=True 
                break 
        if not move:
            python=os.path.join(source_file,"python")
            if not os.path.exists(python):
                os.makedirs(python)
            shutil.move(os.path.join(source_file,filename),
                        os.path.join(python,filename))
            print(f'moved to {python}')

print(f'all the files are sorted')