from flask import Flask, render_template
import datetime
import ViaHBridge

app = Flask(__name__)
@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'U-bot dashboard'
      }
   return render_template('index.html', **templateData)

@app.route("/<direction>")
def move(direction):
   
   if (direction == 'forward'):
     print ("Move forward")
     ViaHBridge.forwardDrive(0.2)

   if (direction == 'reverse'):
     print ("Move backward")
     ViaHBridge.reverseDrive(0.2)

   if (direction == 'left'):
     print ("Turn left")
     ViaHBridge.spinAntiClockwise(0.2)

   if (direction == 'right'):
     print ("Turn right")
     ViaHBridge.spinClockwise(0.2)

   if (direction == 'stop'):
     print ("Stop")
     ViaHBridge.allStop()
    

   templateData = {
      'direction' : direction 
      }
   return render_template('index.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)