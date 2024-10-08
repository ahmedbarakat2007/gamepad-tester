import pygame
import sys

pygame.init()
pygame.joystick.init()

print('  _____          __           ____          ______        __         ')
print(' / ___/__  ___  / /________  / / /__ ____  /_  __/__ ___ / /____ ____')
print('/ /__/ _ \/ _ \/ __/ __/ _ \/ / / -_) __/   / / / -_|_-</ __/ -_) __/')
print('\___/\___/_//_/\__/_/  \___/_/_/\__/_/     /_/  \__/___/\__/\__/_/ ')
print("Made by Ahmed Barakat")
print("Github : ahmedbarakat2007")
print()
print()

pygame.display.set_caption("Controller Tester")

joystick_count = pygame.joystick.get_count()
print('Controller Tester')
print("Made by Ahmed Barakat")
print("Github : ahmedbarakat2007")
if joystick_count == 0:
    print("No joystick connected!")
    sys.exit()
else:
    print(f"{joystick_count} joystick(s) connected.")

joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Joystick Name: {joystick.get_name()}")
print(f"Number of axes: {joystick.get_numaxes()}")
print(f"Number of buttons: {joystick.get_numbuttons()}")
print(f"Number of hats: {joystick.get_numhats()}")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.JOYBUTTONDOWN:
            print(f"Button {event.button} pressed.")

        if event.type == pygame.JOYBUTTONUP:
            print(f"Button {event.button} released.")
        if event.type == pygame.JOYAXISMOTION:
            for i in range(joystick.get_numaxes()):
                axis_val = joystick.get_axis(i)
                print(f"Axis {i} value: {axis_val}")
        if event.type == pygame.JOYHATMOTION:
            for i in range(joystick.get_numhats()):
                hat_val = joystick.get_hat(i)
                print(f"Hat {i} value: {hat_val}")
pygame.quit()
