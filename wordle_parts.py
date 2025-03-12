def is_five_letters(word):
    if(len(word)==5):
       return True
    return False

def is_yellow(guess, secret, pos):
    letter = guess[pos] # Guessed letter at `pos`
    guess_pos = []  # List of positions of `letter`` in `guess`
    secret_pos = [] # List of positions of `letter`` in `secret``
    # Build a list of `guess` positions containing `letter`
    for i in range(len(guess)):
        if letter == guess[i]:
            guess_pos.append(i)
    # Build a list of `secret` positions containing `letter`
    for i in range(len(secret)):
        if letter == secret[i]:
            secret_pos.append(i)
    if len(secret_pos)==0 or pos in secret_pos:
        # Not yellow if `letter` not in 'secret' (actually, red)
        # Not yellow if `pos` in `secret` is `letter` (actually, green)
        return False
    else:
        # Might be yellow... `letter` is in `secret` but 
        # not at `pos` in `secret`
        if len(secret_pos) >= len(guess_pos):
            # Yellow if (in addition to the above) more instances of `letter`
            # exist in `secret` than in `guess`
            return True
        elif guess_pos.index(pos) + 1 <= len(secret_pos):
            # Yellow if (in addition to the above) there are more guesses
            # of `letter` than exist in `secret` AND this instance (`pos`) 
            # of `letter` in `guess`` is NOT one of the extra ones (which 
            # would be red not yellow).
            return True
        else:
            # All other cases: not yellow
            return False

def is_green(guess, secret, pos):
    return guess[pos] == secret[pos]

def is_red(guess, secret, pos):
    return not(guess[pos] in secret)