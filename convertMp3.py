###################################################################
#                       Convert Mp3 v1.0                          #
#                                                                 #
# Script to normalize a lot of mp3 files in a directory           #
###################################################################

import os
import sys

dir = sys.argv[1]

if dir == "help":
    print('Usage:\n\tconvertMp3.py ./directory/with/mp3')
    sys.exit(1)

if not os.path.exists(dir):
    print('Cannot open ' + dir)
    sys.exit(1)

files = os.listdir(dir)
if len(files) > 1:
    os.mkdir(dir + "/convert")
for file in files:
    parts = file.split(".")
    if parts[len(parts)-1] == "mp3":
        file = file.replace(" ", "\ ").replace("(", "\(").replace(")", "\)").replace("[", "\[").replace("]", "\]").replace(",", "\,")
        os.system("ffmpeg  -b 192k -i " + dir + "/" + file +  " " + dir + "/convert/" + file)
        
print("\n\nRemember that you need introduce files without strange characters in the name, if not skips the file.\n")
sys.exit(0)