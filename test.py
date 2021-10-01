import pygame
pygame.init()

from entry import *
from listbox import *
from label import *
from button import *


width = 800
height = 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
font = pygame.font.SysFont("Consolas.ttf", 25)


#-- Widgets
entry_r = pygame.Rect(100, 100, screen.get_width()/2 - 100, 50)
entry = Entry(screen, entry_r, font, (255, 255, 255), (165, 165, 165), (38, 40, 50), 10)

listbox_r = pygame.Rect(100, 200, screen.get_width() / 2 - 100, screen.get_height() - 250)
listbox = ListBox(screen, listbox_r, (165, 165, 165), border=True)

label = Label(listbox.listbox_surface, pygame.Rect(0, 0, 0, 0), "Helo", font, border=True, bg = (15, 16, 21))
label2 = Label(listbox.listbox_surface, pygame.Rect(0, 0, 0, 0), "Hey", font, border=True, bg = (15, 16, 21))

listbox.add_label(label)
listbox.add_label(label2)

button_r = pygame.Rect(400, 100, 200, 50)
button = Button(screen, button_r, font, "Click me!",  (255, 255, 255), (165, 165, 165), (40, 40, 40))

for i in range(20):
	label = Label(listbox.listbox_surface, pygame.Rect(0, 0, 0, 0), str(i), font, border=True, bg = (15, 16, 21))
	listbox.add_label(label)

clock = pygame.time.Clock()
running = True
while running:
	clock.tick(64)
	screen.fill((0, 0, 0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		#-- List box event
		listbox.event(event)

		#-- Entry event
		entry.event(event)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				print(entry.get_input())

		#-- Button event
		if button.is_clicked(event):
			print("Clicked!")

	#-- Updating rects
	entry_r = pygame.Rect(100, 100, screen.get_width()/2 - 100, 50)
	listbox_r = pygame.Rect(100, 200, screen.get_width() / 2 - 100, screen.get_height() - 250)
	
	#-- Updating widgets pos
	entry.update_rect(entry_r)
	listbox.update_rect(listbox_r)

	#-- Rendering widgets
	entry.draw()
	listbox.draw()
	button.draw()
	
	pygame.display.update()


