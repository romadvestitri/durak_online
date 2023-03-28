from durak import Durak


class GameRenderer:
	def render_game(self, durak: Durak, my_index=None):
		...

	def sep(self):
		...

	def help(self):
		...


class ConsoleRenderer(GameRenderer):
	@classmethod
	def card_2_str(cls, card):
		return '[' + ''.join(card) + ']' if card is not None else '[  ]'

	@classmethod
	def cards_2_str(cls, cards, enum=True):
		if enum:
			cards = (f"{i}. {cls.card_2_str(c)}" for i, c in enumerate(cards, start=1))
		else:
			cards = (cls.card_2_str(c) for c in cards)
		return ", ".join(cards)

	def render_game(self, durak: Durak, my_index=None):
		self.sep()

		print(f'Козырь – [{durak.trump}], {len(durak.deck)} карт в колоде осталось.')

		for player in durak.players:
			marker = " <-- ходит" if player.index == durak.attacker_index else ""
			me_marker = " (это я) " if player.index == my_index else ""
			print(f"{player.index + 1}: {self.cards_2_str(player.cards)}{marker}{me_marker}")

		if durak.field:
			print()

			pairs = list(durak.field.items())
			for i, (ac, dc) in enumerate(pairs, start=1):
				print(f'{i}. Ходит: {self.card_2_str(ac)} - отбиться: {self.card_2_str(dc)}')

	def sep(self):
		print('-' * 80)

	def help(self):
		self.sep()
		print('Помощь')
		print('  1. a [номер] -- атаковать картой')
		print('  2. d [номер] -- отбиваться картой')
		print('  3. f -- завершить ход, (если не отбился - берет все карты)')
		print('  3. q -- выход')
		self.sep()