import os
import sys
import subprocess

def findDirs():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pywin32'])  # install win32api package
    except subprocess.CalledProcessError as e:
        print(e.returncode)
        print(e.output)

    import win32api                   # imports package
    drives = win32api.GetLogicalDriveStrings()   # returns String of drives
    driveList = drives.split('\000')[:-1]    # formats drives into a list of strings
    return driveList


def fileSearch(drive, substring, fileEnding):
    print("-------------" + drive + "-------------")
    for root, dirs, files in os.walk(drive):  # utilizes builtin walk method to iterate through each file and subdirectory
        for file in files:
            if substring.lower() in file.lower() and file.endswith(fileEnding):  # specifies file type to search for
                try:
                    location = os.path.abspath(os.path.join(root, file))  # Catches path for current file within loop
                    size = os.stat(location).st_size  # returns file size in bytes
                    print("Name: " + file)
                    print("Location: " + location)
                    print("Size: " + str(size // 1000) + ' kbs ' + str(size // 1000000) + ' mbs\n')
                except:
                    print("An Error occurred trying to access the file, " + file)


def main():
    keyword = input("Enter keyword for file searching: ")
    confirmEnding = input("Would you like to specify a file type?(Y/N): ")
    if confirmEnding == "Y" or confirmEnding == "y":
        fileEnding = input("Enter file post-fix: ")
    else: 
        fileEnding = ""

    driveList = findDirs()
    for drive in driveList:  # calls fileSearch function for each drive in the list
        fileSearch(drive, keyword, fileEnding)

    input("Press Enter to exit")


main()

