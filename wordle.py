with open("words") as f:
    WORDS=[[c for c in line.strip()] for line in f]

def matches(word, guesses={}):
    for c, state in guesses.items():
        if isinstance(state, bool):
            if state != (c in word):
                return False

        elif word[state] != c:
            return False

    return True

def options(words, guesses={}, tried=[]):
    return [word for word in words if "".join(word) not in tried and matches(word, guesses)]

def output(words):
    print("\n".join(["".join(word) for word in words]))

def score(words):
    letters={}

    for word in words:
        for c in word:
            if c not in letters:
                letters[c] = 0
            letters[c]+=1

    return {
        "".join(word): sum([s for c,s in letters.items() if c in word])
        for word in words
    }

def best(scores):
    ordered = sorted([(score,word) for word,score in scores.items()], reverse=True)
    
    return [word for word,score in scores.items() if score==ordered[0][0]]

guesses={}
tried=[]

while True:
    opts = options(WORDS, guesses, tried)
    scores = score(opts)
    print("Best guesses:", ", ".join(best(scores)))

    line = input("Your guess and result? ")

    (guess,result) = line.split(" ")

    tried += [guess]

    for i,a in enumerate(result):
        c = guess[i]

        if a == "Y":
            guesses[c] = i
        elif a == "y":
            guesses[c] = True
        else:
            guesses[c] = False

    print(guesses)
