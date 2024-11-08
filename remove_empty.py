import sys
import os
from pathlib import Path
import shutil
source = r"/home/ghost/Downloads/pispl/annotated/dock_13_14data_set DONE/dock_13_14data_set/"
# Destination path
destination = r"/home/ghost/Downloads/pispl/annotated/data_set_dock/"
dir_list = os.listdir(source)
for txt in dir_list:
    if txt.endswith(".txt"):
        y=os.path.splitext(txt)[0]
        s = Path(source+y+".jpg")
        #print(s)
        if s.is_file():
            #print("### image available\n",s)
            print(s)
            print(source+txt)
            shutil.copy(source + txt, destination + txt)
            shutil.copy(s, destination)
            print("Files are copied successfully")
