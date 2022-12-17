from gpiozero import PWMOutputDevice
from time import sleep
from enum import Enum

# Motors A
PWM_FWD_LEFT = 13 # IN1 - Fwd Left
PWM_REV_LEFT = 6 # IN2 - Rev Left
# Motors B
PWM_FWD_RIGHT = 26 # IN3 - Fwd Right
PWM_REV_RIGHT = 19 # IN4 - Rev Right

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
    print ("U-Bot: Ready...")
    currentTravelMode = allStop()
    speed = 0.2
    while True:
      key = input()

      if (key == "f"):
        allStop()
        currentTravelMode = forwardDrive(speed)
      if (key == "l"):
        allStop()
        currentTravelMode = turnLeft(speed)
      if (key == "r"):
        allStop()
        currentTravelMode = turnRight(speed)
      if (key == "b"):
        allStop()
        currentTravelMode = reverseDrive(speed)
      if (key == "c"):
        allStop()
        currentTravelMode = spinClockwise(speed)
      if (key == "a"):
        allStop()
        currentTravelMode = spinAntiClockwise(speed)
      if (key == "x"):
        allStop()
        currentTravelMode = allStop()
      if (key == "slow"):
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
        print ("Speed: Full")
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



