#-- Imports
import pygame


class Label:
	def __init__(self, surface, rect, text, font, bg=(0, 0, 0), fg=(255, 255, 255), border = False, border_color = (255, 255, 255), curve = 10):
		self.surface = surface
		self.rect = rect
		self.text = text
		self.font = font
		self.bg = bg
		self.fg = fg
		self.border = border
		self.border_color = border_color
		self.curve = curve

		self.original_bg = self.bg
		
		#-- Graphics
		self.label_surface = pygame.Surface((self.rect.w, self.rect.h), pygame.SRCALPHA)
	
	def set_key(self, key):
		self.key = key
	
	def remove_focus(self):
		r = self.original_bg[0]
		g = self.original_bg[1]
		b = self.original_bg[2]
	
		r -= 10
		g -= 10
		b -= 10
		
		if r < 0: r = 0
		if g < 0: g = 0
		if b < 0: b = 0

		self.bg = (r, g, b)
	
	def set_focus(self):	
		r = self.original_bg[0]
		g = self.original_bg[1]
		b = self.original_bg[2]
	
		r += 10
		g += 10
		b += 10
		
		if r > 255: r = 255
		if g > 255: g = 255
		if b > 255: b = 255

		self.bg = (r, g, b)

	def update_rect(self, rect):
		if self.rect != rect and rect.w > 10 and rect.h > 10:
			self.rect = rect
			self.label_surface = pygame.Surface((self.rect.w, self.rect.h), pygame.SRCALPHA)

	def draw(self):
		#-- Rendering
		self.label_surface.fill((0, 0, 0, 0))
		
		if self.border:
			pygame.draw.rect(self.label_surface, self.bg, [0, 0, self.rect.w-1, self.rect.h-1], border_radius = self.curve)
			pygame.draw.rect(self.label_surface, self.border_color, [0, 0, self.rect.w-1, self.rect.h-1], 2, self.curve)
		else:
			pygame.draw.rect(self.label_surface, self.bg, [0, 0, self.rect.w-1, self.rect.h-1], border_radius = self.curve)

		#-- Rendering text
		self.text_surface = self.font.render(self.text, True, self.fg)
		rect = self.text_surface.get_rect()
		self.label_surface.blit(self.text_surface, (self.rect.w/2-rect.w/2, self.rect.h/2-rect.h/2))
		
		self.surface.blit(self.label_surface, (self.rect.x, self.rect.y))


