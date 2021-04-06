from helper import *

try:
    from flask import Flask
except ImportError as __ex:
    print("Install Flask. Exception:", str(__ex))


app = Flask(__name__)

@app.route("/")
def mainpage():
    return readFiletoMemory("show.html")

#@app.route("/0.png")
#def getimg0():
  #  return captureScreen()

#@app.route("/1.png")
#def getimg1():
  #  return captureScreen()

@app.route("/scr/<filename>")
def getscreen(filename):
    return captureScreen()


# main
def main():
    app.run(debug=True)

if __name__=="__main__":
    main()