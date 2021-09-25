#-- Imports
import pygame


class ListBox:
	def __init__(self, surface, rect, bg, border=False, border_color=(255, 255, 255), curve = 10):
		self.surface = surface
		self.rect = rect
		self.border = border
		self.border_color = border_color
		self.bg = bg
		self.curve = curve
	
		#-- Scroll
		self.speed = 10
		self.scroll_y = 0
		self.scroll_start = 0
		self.scroll_end = 0

		#-- Graphics stuff
		self.listbox_surface = pygame.Surface((self.rect.w, self.rect.h), pygame.SRCALPHA)

		#-- Buffers
		self.labels = []
		self.selected = None

	def add_label(self, label):
		self.labels.append(label)
	
	def update_rect(self, rect):
		if self.rect != rect and rect.w > 10 and rect.h > 10:
			self.rect = rect
			self.listbox_surface = pygame.Surface((self.rect.w, self.rect.h), pygame.SRCALPHA)

	def event(self, event):
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			if event.type == pygame.MOUSEBUTTONDOWN:
				#-- Scroll events
				if event.button == 4:
					#-- Scrolling upwards
					if self.scroll_y < self.scroll_start:
						self.scroll_y += self.speed
				if event.button == 5:
					#-- Scrolling downwards
					if self.scroll_end > self.rect.h:
						self.scroll_y -= self.speed

	def get_selected(self):
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			return self.selected

	def draw(self):
		
		#-- Rendering
		self.listbox_surface.fill((0, 0, 0, 0))
		
		if self.border:
			pygame.draw.rect(self.listbox_surface, self.bg, [0, 0, self.rect.w-1, self.rect.h-1], border_radius = self.curve)
			pygame.draw.rect(self.listbox_surface, self.border_color, [0, 0, self.rect.w-1, self.rect.h-1], 2, self.curve)
		else:
			pygame.draw.rect(self.listbox_surface, self.bg, [0, 0, self.rect.w-1, self.rect.h-1], border_radius = self.curve)

		#-- Drawing labels
		x = 10
		y = 10
		for i in self.labels:
			i.surface = self.listbox_surface
			i.update_rect(pygame.Rect(x, y + self.scroll_y, self.rect.w - 20, 40))
			y += 50
			self.scroll_end = y + self.scroll_y

		for i in self.labels:
			#-- Displaying which label u r being currently hovered
			rect = pygame.Rect(self.rect.x + i.rect.x, self.rect.y + i.rect.y, i.rect.w, i.rect.h)
			if rect.collidepoint(pygame.mouse.get_pos()):
				i.set_focus()
				self.selected = i
			else:
				i.remove_focus()

			# Rendering only the visible parts
			if i.rect.h > 0 and i.rect.y < self.rect.h:
				i.draw()

		self.surface.blit(self.listbox_surface, (self.rect.x, self.rect.y))

