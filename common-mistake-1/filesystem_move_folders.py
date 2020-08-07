import shutil
import os 

# Correct way of moving files between folders

subdir = [x[0] for x in os.walk(files_folder)]
subdir = subdir[1]

for sub_files in os.listdir(files_folder):
    if sub_files.endswith('.csv'):
        shutil.move(files_folder + '/' + sub_files, subdir)
        
# Common mistakes are:
# 1). Copy sub_files instead of path to sub_files, which may cause FileNotFoundError by shutil 
# 2). Fail to access the correct subfolder 
