#--Imports
from entry import *
from listbox import *
from label import *

bg_primary = (40,42,54)
bg_secondary = (68,79,90)
chatbox_color = (189, 147, 249)
red = (228,144,144)
yellow = (228,227,144)
blue = (144,156,228)
purple = (189,144,228)
text = (255,255,255)


#TODO: fix the cursor in entry


class App:
	def __init__(self, screen):
		self.screen = screen
		self.running = True
	
		self.font = pygame.font.SysFont("Consolas.ttf", 25)

		self.__declare_widgets()
		self.__add_servers()
		
	def __declare_widgets(self):
		#-- Server list 
		self.sv_list_rect = pygame.Rect(20, 70, self.screen.get_width()/6, self.screen.get_height() - 25)
		self.sv_list_widget = ListBox(self.screen, self.sv_list_rect, bg_primary) 

		#-- Entry
		self.entry_rect = pygame.Rect(self.sv_list_rect.x + self.sv_list_rect.w + 20, self.screen.get_height() - 70, self.screen.get_width() / 1.5, self.screen.get_height() - (self.screen.get_height() - 45))
		self.entry_widget = Entry(self.screen, self.entry_rect, self.font, text, bg_secondary, chatbox_color) 

		#-- Chats
		self.chat_rect = pygame.Rect(self.sv_list_rect.x + self.sv_list_rect.w + 20, 40, self.screen.get_width() / 1.5, self.screen.get_height() - 120)
		self.chat_widget = ListBox(self.screen, self.chat_rect, bg_secondary)

		#-- Label
		self.label_rect = pygame.Rect(20, 30, self.screen.get_width() / 6, self.screen.get_height() - (self.sv_list_rect.h - 10))
		self.label = Label(self.screen, self.label_rect, "Servers", self.font, bg_primary) 

	def __add_servers(self):
		for i in range(20):
			label = Label(self.screen, pygame.Rect(0, 0, 0, 0), str(i), self.font, bg_secondary)
			self.sv_list_widget.add_label(label)

	def __update_widgets(self):
		self.sv_list_rect = pygame.Rect(20, 70, self.screen.get_width()/6, self.screen.get_height() - 95)
		self.sv_list_widget.update_rect(self.sv_list_rect)

		self.entry_rect = pygame.Rect(self.sv_list_rect.x + self.sv_list_rect.w + 20, self.screen.get_height() - 70, self.screen.get_width() / 1.5, self.screen.get_height() - (self.screen.get_height() - 45))
		self.entry_widget.update_rect(self.entry_rect)

		self.chat_rect = pygame.Rect(self.sv_list_rect.x + self.sv_list_rect.w + 20, 40, self.screen.get_width() / 1.5, self.screen.get_height() - 120)
		self.chat_widget.update_rect(self.chat_rect)

		self.label_rect = pygame.Rect(20, 30, self.screen.get_width() / 6, 50)
		self.label.update_rect(self.label_rect)

	def __pack_widgets(self):
		self.sv_list_widget.draw()
		self.entry_widget.draw()
		self.chat_widget.draw()
		self.label.draw()

	def __event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

			#-- Widgets event
			self.entry_widget.event(event)
			self.sv_list_widget.event(event)

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					print(self.entry_widget.get_input())

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					selected = self.sv_list_widget.get_selected()
					if selected:
						print(selected.text)

	def run(self):
		while self.running:
			clock.tick(30)
			self.screen.fill(bg_primary)

			self.__event()
			self.__update_widgets()
			self.__pack_widgets()

			pygame.display.update()


if __name__ == "__main__":
	pygame.init()
	
	screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
	clock = pygame.time.Clock()

	app = App(screen)
	app.run()


