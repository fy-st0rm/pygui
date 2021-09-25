import pygame


class Entry:
	def __init__(self, surface, rect, font, active_color, inactive_color, bg, curve = 10):
		self.surface = surface
		self.rect = rect
		self.curve = curve
		
		#-- Colors
		self.active_color = active_color
		self.inactive_color = inactive_color
		self.bg = bg

		self.color = self.inactive_color
		self.active = False

		#-- Font 
		self.input_text = ""
		self.font = font
		
		self.text_texture = self.font.render(self.input_text, True, self.color)
		self.text_pos = [5, self.rect.h / 2 - self.text_texture.get_rect().h / 2]

		#-- Cursor
		char = "a"
		self.cursor_w = self.font.render(char, True, (0, 0, 0)).get_rect().w
		self.cursor_x = self.text_texture.get_rect().w + self.cursor_w
		self.cursor_y = self.text_pos[1]

		self.entry_surface = pygame.Surface((self.rect.w, self.rect.h), pygame.SRCALPHA)

	def get_input(self):
		if self.active:
			temp = self.input_text
			self.input_text = ""
			return temp

	def update_rect(self, rect):
		if self.rect != rect and rect.w > 10 and rect.h > 10:
			self.rect = rect
			self.entry_surface = pygame.Surface((self.rect.w, self.rect.h), pygame.SRCALPHA)

	def event(self, event):	
		#-- Event handler of the entry

		if event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[0]:
				if self.rect.collidepoint(event.pos):
					self.active = True
					self.color = self.active_color
				else:
					self.active = False
					self.color = self.inactive_color

		if self.active:	
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_BACKSPACE:
					self.input_text = self.input_text[:-1]

					if self.input_text != "":
						self.cursor_x -= self.cursor_w

					# Shifting text pos stuff idk
					self.text_pos[0] += 32
					if self.text_pos[0] > 5:
						self.text_pos[0] = 5
				else:
					self.input_text += event.unicode
					self.cursor_x += self.cursor_w

	def draw(self):
		self.text_texture = self.font.render(self.input_text, True, self.color)	

		# If text is wider than text box then push it back
		text_rect = self.text_texture.get_rect()
		if (self.text_pos[0] + text_rect.w + 5 >= self.rect.w):
			self.text_pos[0] -= 1

		#-- Rendering
		self.entry_surface.fill((0, 0, 0, 0))

		pygame.draw.rect(self.entry_surface, self.bg, [0, 0, self.rect.w-1, self.rect.h-1], border_radius = self.curve)		
		self.entry_surface.blit(self.text_texture, self.text_pos)
		
		pygame.draw.rect(self.entry_surface, self.color, [0, 0, self.rect.w-1, self.rect.h-1], 2, self.curve)		
	
		#-- Rendering cursor
		pygame.draw.rect(self.entry_surface, self.inactive_color, [self.cursor_x, self.cursor_y, self.cursor_w, self.text_texture.get_rect().h], border_radius = 2)


		self.surface.blit(self.entry_surface, (self.rect.x, self.rect.y))

			
