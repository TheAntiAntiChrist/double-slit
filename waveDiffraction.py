import pygame
import math

pygame.init()

winX = 400 #width of window, default: 400
winY = 400 #height of window, default: 400

screen = pygame.display.set_mode([winX, winY])
pygame.display.set_caption("Wave Diffraction")

Done = False
clock = pygame.time.Clock()

srcOne = [100, 75] #default: x = 0, y = 75
srcTwo = [100, 125] #default: x = 0, y = 125
wavelength = 10 #wavelength in pixels, default: 10
waveColour = [0, 0, 0] #empty RGB value
waveColour1 = [0, 0, 0] #empty RGB value
waveColour2 = [0, 0, 0] #empty RGB value

phaseStep = 0
phaseStepAmnt = 60

while not Done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #waits for "x" window button press then quits
            Done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: #waits for escape key press then quits
                Done = True

    for x in range(0, 200):
        for y in range(0, 200):
            distanceOne = math.sqrt((x-srcOne[0])**2 + (y-srcOne[1])**2)
            phaseOne = (distanceOne / wavelength) * 360
            phaseOne += phaseStep
            while phaseOne >= 360: #keeps phases within 0-359 degrees
                phaseOne -= 360
            while phaseOne < 0:
                phaseOne += 360
            if math.sin(math.radians(phaseOne)) > 0:
                waveColour1[0] = abs(255*math.sin(math.radians(phaseOne))) #sets red value
                waveColour1[1] = abs(255*math.cos(math.radians(phaseOne))) #sets green value
                waveColour1[2] = 0 #sets blue value to nil
            elif math.sin(math.radians(phaseOne)) < 0:
                waveColour1[2] = abs(255*math.sin(math.radians(phaseOne))) #sets blue value
                waveColour1[1] = abs(255*math.cos(math.radians(phaseOne))) #sets green value
                waveColour1[0] = 0 #sets red value to nil
            else:
                waveColour1 = [0, 255, 0]
            distanceTwo = math.sqrt((x-srcTwo[0])**2 + (y-srcTwo[1])**2)
            phaseTwo = (distanceTwo / wavelength) * 360
            phaseTwo += phaseStep
            while phaseTwo >= 360: #keeps phases within 0-359 degrees
                phaseTwo -= 360
            while phaseTwo < 0:
                phaseTwo += 360
            if math.sin(math.radians(phaseTwo)) > 0:
                waveColour2[0] = abs(255*math.sin(math.radians(phaseTwo))) #sets red value
                waveColour2[1] = abs(255*math.cos(math.radians(phaseTwo))) #sets green value
                waveColour2[2] = 0 #sets blue value to nil
            elif math.sin(math.radians(phaseTwo)) < 0:
                waveColour2[2] = abs(255*math.sin(math.radians(phaseTwo))) #sets blue value
                waveColour2[1] = abs(255*math.cos(math.radians(phaseTwo))) #sets green value
                waveColour2[0] = 0 #sets red value to nil
            else:
                waveColour2 = [0, 255, 0]
            waveColour[0] = (waveColour1[0] + waveColour2[0]) / 2
            waveColour[1] = (waveColour1[1] + waveColour2[1]) / 2
            waveColour[2] = (waveColour1[2] + waveColour2[2]) / 2
            pygame.draw.rect(screen, waveColour, [2*x, 2*y, 2, 2], 0)

    pygame.display.flip()
    clock.tick(60)

    phaseStep -= phaseStepAmnt

pygame.quit()
quit()
