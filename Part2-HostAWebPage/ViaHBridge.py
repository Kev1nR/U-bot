from gpiozero import PWMOutputDevice
from time import sleep
from enum import Enum

# Motors A 
PWM_FWD_LEFT = 26 # IN1 - Fwd Left
PWM_REV_LEFT = 19 # IN2 - Rev Left
# Motors B
PWM_FWD_RIGHT = 13 # IN3 - Fwd Right
PWM_REV_RIGHT = 6 # IN4 - Rev Right

# Init
forwardLeft = PWMOutputDevice (PWM_FWD_LEFT, True, 0, 1000)
reverseLeft = PWMOutputDevice (PWM_REV_LEFT, True, 0, 1000)
forwardRight = PWMOutputDevice (PWM_FWD_RIGHT, True, 0, 1000)
reverseRight = PWMOutputDevice (PWM_REV_RIGHT, True, 0, 1000)

# Current travel mode
class TravelMode(Enum):
  Stop = 0
  Forward = 1
  Reverse = 2
  TurnLeft = 3
  TurnRight = 4
  Spin = 5

currentTravelMode = TravelMode.Stop

def allStop():
    print ("Stopped")
    forwardLeft.value = 0
    reverseLeft.value = 0
    forwardRight.value = 0
    reverseRight.value = 0
    return TravelMode.Stop

def forwardDrive(speed):
    print ("Run forward...")
    forwardLeft.value = speed
    reverseLeft.value = 0
    forwardRight.value = speed
    reverseRight.value = 0
    return TravelMode.Forward

def reverseDrive(speed):
    print ("Run backward...")
    forwardLeft.value = 0
    reverseLeft.value = speed
    forwardRight.value = 0
    reverseRight.value = speed
    return TravelMode.Reverse

def spinClockwise(speed):
    print ("Spin clockwise...")
    forwardLeft.value = 0
    reverseLeft.value = speed
    forwardRight.value = speed
    reverseRight.value = 0
    return TravelMode.Spin
  
def spinAntiClockwise(speed):
    print ("Spin anti-clockwise...")
    forwardLeft.value = speed
    reverseLeft.value = 0
    forwardRight.value = 0
    reverseRight.value = speed
    return TravelMode.Spin

def turnLeft(speed):
    print ("Turning left...")
    forwardLeft.value = speed * 0.5
    reverseLeft.value = 0
    forwardRight.value = speed
    reverseRight.value = 0
    return TravelMode.TurnLeft

def turnRight(speed):
    print ("Turning right...")
    forwardLeft.value = speed
    reverseLeft.value = 0
    forwardRight.value = speed * 0.5
    reverseRight.value = 0
    return TravelMode.TurnRight

def main():
#    while True:
#        forwardDrive(0.15)
#        sleep(2)
#        reverseDrive(0.15)
#        sleep(2)
    print ("U-Bot: Ready...")
    allStop()
    while True:
      key = input()

      if (key == "f"):
        allStop()
        currentTravelMode = forwardDrive(0.2)
      if (key == "l"):
        allStop()
        currentTravelMode = turnLeft(0.2)
      if (key == "r"):
        allStop()
        currentTravelMode = turnRight(0.2)
      if (key == "b"):
        allStop()
        currentTravelMode = reverseDrive(0.2)
      if (key == "c"):
        allStop()
        currentTravelMode = spinClockwise(0.2)
      if (key == "a"):
        allStop()
        currentTravelMode = spinAntiClockwise(0.2)
      if (key == "x"):
        currentTravelMode = allStop()
      if (key == "1"):
        print ("Speed: Slow")
        speed = 0.2
        if (currentTravelMode == TravelMode.Forward):
          forwardDrive(speed)
        if (currentTravelMode == TravelMode.Reverse):
          reverseDrive(speed)
        if (currentTravelMode == TravelMode.TurnLeft):
          turnLeft(speed)
        if (currentTravelMode == TravelMode.TurnRight):
          turnRight(speed)        
      if (key == "medium"):
        print ("Speed: Medium")
        speed = 0.5
        if (currentTravelMode == TravelMode.Forward):
          forwardDrive(speed)
        if (currentTravelMode == TravelMode.Reverse):
          reverseDrive(speed)
        if (currentTravelMode == TravelMode.TurnLeft):
          turnLeft(speed)
        if (currentTravelMode == TravelMode.TurnRight):
          turnRight(speed)        
      if (key == "fast"):
        print ("Speed: Fast")
        speed = 0.75
        if (currentTravelMode == TravelMode.Forward):
          forwardDrive(speed)
        if (currentTravelMode == TravelMode.Reverse):
          reverseDrive(speed)
        if (currentTravelMode == TravelMode.TurnLeft):
          turnLeft(speed)
        if (currentTravelMode == TravelMode.TurnRight):
          turnRight(speed)        
      if (key == "full"):
        peint ("Speed: Full")
        speed = 1.0
        if (currentTravelMode == TravelMode.Forward):
          forwardDrive(speed)
        if (currentTravelMode == TravelMode.Reverse):
          reverseDrive(speed)
        if (currentTravelMode == TravelMode.TurnLeft):
          turnLeft(speed)
        if (currentTravelMode == TravelMode.TurnRight):
          turnRight(speed)        

if __name__ == "__main__":
    try:
      main()
    except KeyboardInterrupt:
      allStop()
      
      

