import flask
from flask import request
app = flask.Flask(__name__)
html = '''
      <form action = "http://localhost:5000/input" method = "post">
         <p><input type = "text" name = "filecontents" /></p>
         <p><input type = "text" name = "files" /></p>
         <p><input type = "submit" value = "submit" /></p>
      </form>   
'''
@app.route("/input",methods=["POST","GET"])
def inputpage():
        if request.method == 'POST':
            filecontents = request.form['filecontents']
            files = request.form['files']
            with open("files.txt","w") as f:
                f.write(files)
            with open("filecontents.txt","w") as f:
                f.write(filecontents)
        else:
            return html
app.run()