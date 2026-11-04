# r11e1 — guess the number (mini-project)
# The first line is the secret number (1 to 100). Then guesses arrive one per line.
# For each guess:
#   not digits                 -> print 'numbers only'
#   outside 1-100              -> print 'between 1 and 100'
#   lower than the secret      -> print 'higher'
#   higher than the secret     -> print 'lower'
#   equal                      -> print 'correct in N' where N counts only the valid guesses, then stop
# Example: secret 42; guesses 50, abc, 25, 42 -> prints lower / numbers only / higher / correct in 3
secret = int(input())
# --- your code below this line ---
tries = 0
while True:
    text = input()
    if not text.isdigit():
        print("numbers only")
        continue
    guess = int(text)
    if guess < 1 or guess > 100:
        print("between 1 and 100")
        continue
    tries += 1
    if guess < secret:
        print("higher")
    elif guess > secret:
        print("lower")
    else:
        print(f"correct in {tries}")
        break
