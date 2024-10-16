import os
import random

source_file=r"."

if not os.path.exists(source_file):
    os.makedirs(source_file)

file_types={
    'Images': ['.jpg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar']
}

for category,extension in file_types.items():
    for i in range(5):
        file_name=f"random_file_{category}_{i}{random.choice(extension)}"
        file_path=os.path.join(source_file,file_name)

        with open(file_path,'w') as file:
            file.write("")

os.listdir(source_file)