# r3e2 — command
# One word typed by a player. Print the response:
#   'north' or 'n' -> You walk north.
#   'look'         -> You see a door.
#   'quit'         -> Goodbye.
#   anything else  -> I do not understand.
# Use match/case; the two spellings of north share one case with |.
# Example: n -> prints You walk north.
command = input()
# --- your code below this line ---
match command:
    case "north" | "n":
        print("You walk north.")
    case "look":
        print("You see a door.")
    case "quit":
        print("Goodbye.")
    case _:
        print("I do not understand.")
