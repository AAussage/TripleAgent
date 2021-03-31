#!/usr/bin/env python3
import time

class Evenement:
	def __init__(player_id):
		self.player_id = player_id


class Timer:
	def __init__(self, text, time=60):
		self.time = time
		self.text_base = text
		self.text_to_push = self.text_base.format(self.time)
		self.PLAYER_DONE = False
		self.countdown(self.time)

	def countdown(self,time_left):
		self.time = time_left
		self.text_to_push = self.text_base.format(self.time)
		self.push_text()
		time.sleep(1)

		new_time = self.time - 1
		if (new_time) > 0 and (self.PLAYER_DONE == False):
			self.countdown(new_time)

	def push_text(self):
		print(self.text_to_push)

if __name__ == "__main__":
	texte_a_afficher = "Alors la du coup c'est le texte statique du timer de 15 secondes, et il reste {:02d} secondes"
	mon_timer = Timer(texte_a_afficher,time=15)
