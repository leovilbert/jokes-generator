import pyjokes
import time

global total
total = []
count = 0

def again():
    question = input('Do you wanna more jokes? ').strip().upper()[0]

    if question == 'N':
        print(f'The average rating of the jokes was {sum(total) / count}!')
        quit()

def rate():
    print('''Rate this joke:
    [1] Bad
    [2] Ok
    [3] Good
    [4] Funny
    [5] Hilarious''')
    rating = int(input('Rating: '))
    total.append(rating)

def joke():
    joke = pyjokes.get_joke()
    print(joke)

while True:
    joke()
    count += 1
    time.sleep(3)
    rate()
    again()