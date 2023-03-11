import uuid
import os
# import exiftool
import xml.etree.ElementTree as ET
import subprocess
import shutil

exiftool = "/opt/homebrew/bin/exiftool"
path = "../Pictures"
outputPath = "../Folders"
files = os.listdir(path)

code = ""
out = ""
err = ""

totalfiles = len(files)

def run(cmd):
    proc = subprocess.Popen(cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
    return proc.returncode, stdout, stderr

for i in range(len(files)):

    caption = ''

    try:
        code, out, err = run(["/opt/homebrew/bin/exiftool", "-xmp:caption", path+"/"+files[i]])
    except:
        print("Cannot get Caption for file: "+files[i])
        exit
    
    #print(out)
    # print("- [" + str(i) +  "/" + str(totalfiles) + "] - Putting into a folder: " + files[i] )

    # # Save UUID to RAW Filename EXIF tag
    # xml = ""
    # try:
    #     code, out, err = run(["/opt/homebrew/bin/exiftool", "-X", path+"/"+files[i]])
    # except:
    #     print("Cannot create XML for file: "+files[i])
    #     exit

    print(out)
    output = "{}".format(out)
    output =  output.strip("b'Caption                         : ")
    output = output.strip("\\")
    print("---"+output+"---")
    try:
        if(output):
            os.mkdir( outputPath+"/"+output , mode = 0o777)
    except:
        print("Folder exists")

    try:
        print("from:"+path+"/"+files[i])
        print("to:"+outputPath+"/"+output+"/"+files[i])
        dest = shutil.move(path+"/"+files[i], outputPath+"/"+output+"/"+files[i])
    except:
        print("Can't move")
    # file = open("./output/"+files[i]+".xml", 'w')
    # file.write(output[2:].replace("\\n", "\n"))
    # file.close()