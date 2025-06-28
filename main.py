import datetime


class Note:
	def __init__(self, content, title):
		self.content = content
		self.title = title
		self.timestamp = datetime.datetime.now()

	def __str__(self):
		return f'--- {self.title} ({self.timestamp.strftime('%H:%M %Y.%m.%d')}) ---\n{self.content}\n'


class NoteManager:
	def __init__(self):
		self.notes = []

	def add_note(self, content, title):
		note = Note(content, title)
		self.notes.append(note)

	def view_notes(self):
		if not self.notes:
			return

		for i, note in enumerate(self.notes):
			print(f'\nNote #{i+1}:')
			print(note)

	def delete_note(self, index):
		try:
			if 0 <= index < len(self.notes):
				deleted_note = self.notes.pop(index)
				print(f'Note "{deleted_note.title}" deleted.')
			else:
				print('Invalid index number.')
		except ValueError:
			pass

def main():
	manager = NoteManager()
	while True:
		print('\nNotes App Menu:')
		print('1. Add Note')
		print('2. Delete Note')
		print('3. View Notes')
		print('4. Exit')

		choise = input('Enter you choise: ')

		if choise == '1':
			title = input('Enter note title (optional): ')
			content = input('Enter note content text: ')

			manager.add_note(content, title if title else 'Untitled Note')

		elif choise == '2':
			try:
				index = int(input('Enter note number: ')) - 1
				manager.delete_note(index)
			except ValueError:
				print('Invalid input. Please enter a number.')

		elif choise == '3':
			manager.view_notes()

		elif choise == '4':
			break

if __name__ == '__main__':
	main()
