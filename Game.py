import World

def render():
    print("Current world temp is", world.temperature.getTemperature())
    print("Current time is",
          world.time.current_year,"year",
          world.time.current_day,"day",
          world.time.current_hour,
          "hour from world creating.")

    print("Now is", world.time.times_of_day)

def update():
    world.tick()

def printHelp():
    print("Welcome to world simulate!")
    print("Enter 'd' to skip 24 hours")
    print("Enter 'm' to skip 1 month")
    print("Enter 'y' to skip 1 year")
    print("Enter 'v' to skip 1 century")
    print("Enter 'h' to print this help")
    print("Enter 'q' to quit simulation")

def inputPlayer():
    global skipsteps
    if skipsteps==1:
        key=input()
        if key=="q":
            quit()
        if key=="d":
            skipsteps=23
        if key=="m":
            skipsteps=world.time.getStepsInYear()/12
        if key=="y":
            skipsteps=world.time.getStepsInYear()
        if key=="v":
            skipsteps=world.time.getStepsInCentury()
        if key=="h":
            printHelp()
    else:
        skipsteps=skipsteps-1

world=World.World()
mainloop=1
skipsteps=1

printHelp()

while mainloop:
    inputPlayer()
    update()
    render()
