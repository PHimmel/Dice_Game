"""
A file to work out how the program will determine the match winner and then the overall game winner.

based on arithmetic comparison

take winner from each round and add to counter variable of wins for comp/human respectively

// global variables
human = 0
comp = 0

void determineWinner(int human, int comp) {

if (human > comp) {
    human++;
    }
elif (comp > human) {
    comp++;
    }

// tie game --> human == comp
else {
    pass
    }
}

"""