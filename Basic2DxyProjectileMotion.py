import math

# Accepts an input for any horizontal acceleration (+/- x direction)
xAccel = float(input('Please input horizontal acceleration [float]: '))
# Accepts an input for any vertical acceleration (+/- y direction)
yAccel = float(
    input('Please input vertical acceleration (-9.80665 for grav accel)[float]: '))

# Accepts an x input for an (x,y) origin coordinate
xInitialPosition = float(
    input('Please input the x coordinate of the starting position [float]: '))
# Accepts a y input for an (x,y) origin coordinate
yInitialPosition = float(
    input('Please input the y coordinate of the starting position [float]: '))
# Accepts an input for any initial velocity magnitude...
magnitude = float(
    input('Please input the initial velocity magnitude [float]: '))
# ...and defines which direction (with 0 deg at +x axis on coordinate plane)
angle = float(input(
    'Please input the angle of the vector relative to 0 deg horizontal [float]: '))


#converts entered magnitude into its horizontal component form
def XcompositeParts(initialVelocity, degAngle):

    radAngle = float((degAngle / (180 / math.pi))) #converts from degrees to radians
    radcos = math.cos(radAngle) #finds the cosine of radian-converted degree input

    xcompositepart = initialVelocity * radcos
    return xcompositepart #returns composite part

#converts entered magnitude into its vertical component form
def YcompositeParts(initialVelocity, degAngle):

    radAngle = float((degAngle / (180 / math.pi))) #converts from degrees to radians
    radsin = math.sin(radAngle) #finds the sine of radian-converted degree input

    ycompositepart = initialVelocity * radsin
    return ycompositepart #returns composite part

#finds total time of flight (before projectile hits y = 0)
def projMotTotalTime(acc, velointit, posintit):
    totalTime = float()
    a = float(acc * (1/2)) 
    b = float(velointit)
    c = float(posintit)

    #Uses quadratic formula to solve the quadratic position equation for Xf = 0

    d = float((b ** 2) - (4 * a * c))

    if d < 0:
        print('The equation has no real solution')
    elif d == 0:
        x = float((-b)/(2*a))
        totalTime = x
        
    else:
        x1 = float(-b + math.sqrt(d))/(2*a)
        x2 = float(-b - math.sqrt(d))/(2*a)
        

    if x1 < x2:

        if x2 > 0:
            totalTime = x2

    elif x1 == x2:

        totalTime = x1

    else:

        if x1 > 0:
            totalTime = x1

    return totalTime

# Finds final horizontal position (x value)
def finalHorizPosition(horizAccel, horizVeloComp, totalTime):
    xfinal = float(((1/2) * horizAccel * (totalTime ** 2)) +
                   (horizVeloComp * totalTime) + (xInitialPosition))
    return xfinal

# Finds final horizontal component velocity just before hitting the ground
def finalHorizVelo(totalTime, horizAccel, horizVeloInital):
    finalHorizVelo = float((horizAccel * totalTime) + horizVeloInital)
    return finalHorizVelo

# Finds final vertical component velocity just before hitting the ground
def finalVertiVelo(totalTime, vertAccel, vertiVeloInitial):
    finalVertiVelo = float((vertAccel * totalTime) + vertiVeloInitial)
    return finalVertiVelo

# Finds final magnitude of velocity just before hitting the ground...
def finalVeloMagnitude(finalHorizVelo, finalVertiVelo):
    finalVeloMagnitude = float(
        math.sqrt((finalHorizVelo ** 2) + (finalVertiVelo ** 2)))
    return finalVeloMagnitude

#...and finds the angle (relative to 0 degrees at +x axis) in degrees
def finalVeloAngleDeg(finalHorizVelo, finalVertiVelo):
    finalVeloAngleRadians = float(math.atan(finalVertiVelo / finalHorizVelo))
    tempVeloAngleDegs = float(finalVeloAngleRadians * (180/math.pi))
    finalVeloAngleDegs = float(360 - (abs(tempVeloAngleDegs)))
    return finalVeloAngleDegs

# Uses derivative of position (velocity)'s critical number to find maximum of position function
def maximumHeightTime(acc, yvelointit):
    
    # (VF)0 = at + vi  <------- original Vf = at + Vi velocity formula
    #(0 - yvelointit) = acc * time  <----- algebraic step in reconfiguration of equation
    maxHeightTime = float( (0 - yvelointit) / acc )
    return maxHeightTime

# Uses previous function's time to figure out what height the projectile is at, at the maximum of its arc
def maximumHeight(yAccel, vertCompVelo, yInitialPosition, maxHeightTime):
    maxHeight = float(((1/2) * yAccel * (maxHeightTime ** 2)) +
                      (vertCompVelo * maxHeightTime) + yInitialPosition)
    return maxHeight

# method calls
horizontalComposite = XcompositeParts(magnitude, angle)
verticalComposite = YcompositeParts(magnitude, angle)

totalTime = projMotTotalTime(yAccel, verticalComposite, yInitialPosition)
finalHorizPos = finalHorizPosition(xAccel, horizontalComposite, totalTime)

finalHorizVelo = finalHorizVelo(totalTime, xAccel, horizontalComposite)
finalVertiVelo = finalVertiVelo(totalTime, yAccel, verticalComposite)
finalVeloMagnitude = finalVeloMagnitude(finalHorizVelo, finalVertiVelo)
finalVeloAngleDeg = finalVeloAngleDeg(finalHorizVelo, finalVertiVelo)

maxHeightTime = maximumHeightTime(yAccel, verticalComposite)
maxHeight = maximumHeight(yAccel, verticalComposite,
                          yInitialPosition, maxHeightTime)

# Display
print('')
print('Analysis:')
print('Total time: ', totalTime, ' seconds')
print('Horizontal Distance of: ', finalHorizPos, ' meters')
print('')
print('Final (Unit Vector) velocity of', finalHorizVelo,
      'i meters/second', finalVertiVelo, 'j meters/second')
print('Final (Mag/Deg) velocity of', finalVeloMagnitude,
      'm/s in direction of', finalVeloAngleDeg, 'degrees')
print('')
print('Maximum Height:', maxHeight, 'meters')
print('Time maximum height was reached:', maxHeightTime, 'seconds')
