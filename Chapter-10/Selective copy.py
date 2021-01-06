import os, shutil
from pathlib import Path
p=Path.home()

destin=(r'C:/Pdf and jpg')
for folderName, subfolders, filenames in os.walk(p):
     for subfolder in subfolders:
         for filename in filenames:
             if filename.endswith('.jpg') or filename.endswith('.pdf'):
                 shutil.copy(os.path.join(folderName,filename),destin)
                 
