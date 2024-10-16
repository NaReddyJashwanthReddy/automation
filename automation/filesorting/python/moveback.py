import os
import shutil

source_file=r"."

for filename in os.listdir(os.path.join(source_file,'python')):
    shutil.move(os.path.join(source_file,'python',filename),
                os.path.join(source_file,filename))
    print(f'moved the {filename} back')