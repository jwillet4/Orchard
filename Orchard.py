import sys
import random


# Logan Willett
# Runs a game of Orchard
def simulateOrchard():
    # Fruits is ordered initially by name to account for the basket function
    fruits = [{'name': 'apples', 'count': 10}, {'name': 'cherries', 'count': 10},
              {'name': 'pears', 'count': 10}, {'name': 'plums', 'count': 10}]
    crow = 0
    '''
    1: apples
    2: cherries
    3: pears
    4: plums
    5: basket
    6: crow
    '''
    while True:
        rollVal = roll()
        if 1 <= rollVal <= 4:
            # Ensures the fruit count is not already at 0
            if fruits[rollVal - 1].get('count') != 0:
                fruits[rollVal - 1]['count'] = fruits[rollVal - 1].get('count') - 1
        elif rollVal == 5:
            fruits = basket(fruits)
        elif rollVal == 6:
            crow += 1
        # Maps the fruits list to a new list of only the count values
        if sum(map(lambda fruit: fruit.get('count'), fruits)) == 0:
            return 'win'
        elif crow == 9:
            return 'lose'


# Picks two fruits with the highest count
def basket(fruits):
    for i in range(2):
        # Sort so the highest count fruit will be at index 0
        fruits.sort(key=lambda k: k['count'], reverse=True)
        if fruits[0].get('count') != 0:
            fruits[0]['count'] = fruits[0].get('count') - 1
        # Reorder fruits to original order
        fruits.sort(key=lambda k: k['name'])
    return fruits


# Returns 1-6
def roll():
    return random.randint(1, 6)


# Take sample size from bash
sampleSize = int(sys.argv[1])
# List of Orchard outcomes
outcomes = []
for i in range(sampleSize):
    outcomes.append(simulateOrchard())
print('Wins:', outcomes.count('win'))
print('Loses:', outcomes.count('lose'))
print(outcomes.count('win') / sampleSize * 100, '% chance to win')
