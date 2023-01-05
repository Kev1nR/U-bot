from flask import Flask, render_template, request, Response
import datetime
import ViaHBridge2 as motion
from Camera import Camera

app = Flask(__name__)
@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'U-bot dashboard',
      'slowspeed' : 'speedButton-off',
      'mediumspeed' : 'speedButton-off',
      'fastspeed' : 'speedButton-off',
      'fullspeed' : 'speedButton-off',
      'fbutton' : 'button',
      'revbutton' : 'button',
      'rbutton' : 'button',
      'lbutton' : 'button'}
   return render_template('index.html', **templateData)

@app.route("/motion")
def move():
   ts = motion.TravelStatus(motion.TravelMode.Stop, 0.0)

   direction = request.args.get('direction')
   speed = request.args.get('speed')

   if (speed == ''):
      speed = 'zero'
   if (direction == ''):
      direction = 'stop'

   print ("direction is ", direction, ". Speed is ", speed) 
   if (direction == 'forward'):
     print ("Move forward")
     ts.setTravelMode(motion.TravelMode.Forward)
     #.and motion .forwardDrive(0.2)
     
   if (direction == 'reverse'):
     print ("Move backward")
     ts.setTravelMode(motion.TravelMode.Reverse)

#     motion.reverseDrive(0.2)

   if (direction == 'left'):
     print ("Turn left")
     ts.setTravelMode(motion.TravelMode.TurnLeft)
     #motion.spinAntiClockwise(0.2)

   if (direction == 'right'):
     print ("Turn right")
     ts.setTravelMode(motion.TravelMode.TurnRight)
      #motion.spinClockwise(0.2)

   if (direction == 'stop'):
     print ("Stop")
     ts.setTravelMode(motion.TravelMode.Stop)
   #motion.allStop()  

   if (speed == 'zero'):
    slowSpeed = 'speedButton-off'
    mediumSpeed = 'speedButton-off'
    fastSpeed = 'speedButton-off'
    fullSpeed = 'speedButton-off'
    ts.setSpeed(0.0)

   if (speed == 'slow'):
    slowSpeed = 'speedButton-1'
    mediumSpeed = 'speedButton-off'
    fastSpeed = 'speedButton-off'
    fullSpeed = 'speedButton-off'
    ts.setSpeed(0.2)
    
   if (speed == 'medium'):
    slowSpeed = 'speedButton-1'
    mediumSpeed = 'speedButton-2'
    fastSpeed = 'speedButton-off'
    fullSpeed = 'speedButton-off'
    ts.setSpeed(0.5)
    
   if (speed == 'fast'):
    slowSpeed = 'speedButton-1'
    mediumSpeed = 'speedButton-2'
    fastSpeed = 'speedButton-3'
    fullSpeed = 'speedButton-off'
    ts.setSpeed(0.75)

   if (speed == 'full'):
    slowSpeed = 'speedButton-1'
    mediumSpeed = 'speedButton-2'
    fastSpeed = 'speedButton-3'
    fullSpeed = 'speedButton-4'
    ts.setSpeed(1.0)
    
   fbutton = 'button'
   revbutton = 'button'
   rbutton = 'button'
   lbutton = 'button'
   
   if (direction == 'forward'):
    fbutton = 'button-off'
   if (direction == 'reverse'):
    revbutton = 'button-off'
   if (direction == 'right'):
    rbutton = 'button-off'
   if (direction == 'left'):
    lbutton = 'button-off'
   
   if (speed == ''):
      speed = 'zero'
      
   templateData = {
      'direction' : direction, 
      'speed' : speed,
      'slowspeed' : slowSpeed,
      'mediumspeed' : mediumSpeed,
      'fastspeed' : fastSpeed,
      'fullspeed' : fullSpeed,
      'fbutton' : fbutton,
      'revbutton' : revbutton,
      'rbutton' : rbutton,
      'lbutton' : lbutton   
      }
   return render_template('index.html', **templateData)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
#   return ""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)