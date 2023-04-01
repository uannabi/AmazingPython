MOVE_CURSOR_UP = "\033[1A"
ERASE = "\x1b[2K"

print("Hello")
print("Djin")

print((MOVE_CURSOR_UP+ERASE)* 2, end="")

print("EVERYTHING IS CLEANED!")

