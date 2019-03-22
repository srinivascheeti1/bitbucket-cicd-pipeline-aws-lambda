import os
import re
import zipfile

def pathContainsDot(p):
    c = re.compile('\.\w+')

    for pc in p.split('/'):
        if c.match(pc) != None:
            return True

    return False

def zipfolder(basepath, file):

    print(basepath)
    path = basepath+'/lambda-cicd'
    print(path)

    dirList = os.walk(path)
    for dirEntry in dirList:
        if not pathContainsDot(dirEntry[0]):
            for fileEntry in dirEntry[2]:
                if not fileEntry.endswith('~'):
                    fn = os.path.join(dirEntry[0], fileEntry)
                    en = os.path.join(
                        os.path.relpath(dirEntry[0], path),
                        fileEntry)
                    file.write(fn, en)

    print(basepath)
    path = basepath+'/libs'
    print(path)

    dirList = os.walk(path)
    for dirEntry in dirList:
        if not pathContainsDot(dirEntry[0]):
            for fileEntry in dirEntry[2]:
                if not fileEntry.endswith('~'):
                    fn = os.path.join(dirEntry[0], fileEntry)
                    en = os.path.join(
                        os.path.relpath(dirEntry[0], path),
                        fileEntry)
                    file.write(fn, en)

with zipfile.ZipFile('lambda-cicd.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
    zipfolder(os.getcwd(), archive)
