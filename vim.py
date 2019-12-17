from pynput import keyboard
from pynput.keyboard import Key


class Vim:
    def __init__(self, filepath):
        self.idx = 0
        self.lines = []
        self.filepath = filepath
        self.is_running = True

    def exec(self):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()
        with open(self.filepath, 'r') as f:
            for line in f:
                line = line.strip('\n')
                self.lines.append(line)
            if len(self.lines) == 0:
                self.lines.append('')

        print(f'{self.idx + 1}. {self.lines[self.idx]}')
        while self.is_running:
            pass
        listener.stop()

    def on_press(self, key):
        if (key == Key.shift_l):
            if self.idx > 0:
                self.idx -= 1
                print(f'{self.idx + 1}. {self.lines[self.idx]}')
        elif (key == Key.shift_r):
            if self.idx < len(self.lines) - 1:
                self.idx += 1
                print(f'{self.idx + 1}. {self.lines[self.idx]}')
        elif (key == Key.alt_l):
            self.lines[self.idx] = input(f'{self.idx + 1}. ')
        elif (key == Key.alt_r):
            self.idx += 1
            self.lines.insert(self.idx, '')
            print(f'{self.idx + 1}. {self.lines[self.idx]}')
        elif (key == Key.ctrl_l):
            if len(self.lines) == 1:
                self.lines[0] = ''
            else:
                self.lines.pop(self.idx)
            if self.idx != 0:
                self.idx -= 1
            print(f'{self.idx + 1}. {self.lines[self.idx]}')
        elif (key == Key.ctrl_r):
            with open(self.filepath, 'w') as f:
                f.write('\n'.join(self.lines))
            self.is_running = False
