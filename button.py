#-- Imports
import pygame


class Button:
	def __init__(self, surface, rect, font, text, active_color, inactive_color, bg, curve = 10):
		self.surface = surface
		self.rect = rect
		self.font = font
		self.text = text
		self.active_color = active_color
		self.inactive_color = inactive_color
		self.bg = bg
		self.curve = curve

		self.active = False
		self.color = self.inactive_color

	def is_clicked(self, event):
		if self.active:
			if event.type == pygame.MOUSEBUTTONDOWN:
				if pygame.mouse.get_pressed()[0]:
					return True
		return False

	def draw(self):
		mouse_pos = pygame.mouse.get_pos()

		if self.rect.collidepoint(mouse_pos):
			self.color = self.active_color
			self.active = True
		else:
			self.color = self.inactive_color
			self.active = False

		#-- Rendering the button frame
		pygame.draw.rect(self.surface, self.bg, self.rect, border_radius = self.curve)
		pygame.draw.rect(self.surface, self.color, self.rect, 2, self.curve) 

		#-- Loading text texture
		self.text_texture = self.font.render(self.text, True, self.color)
		
		#-- Rendering text
		x = self.rect.x + (self.rect.width / 2 - self.text_texture.get_rect().width / 2)
		y = self.rect.y + (self.rect.height / 2 - self.text_texture.get_rect().height / 2)

		self.surface.blit(self.text_texture, (x, y))

