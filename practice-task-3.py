import random

number = random.randint(1, 10)

while True:
  guess = int(input('Please enter your guess: '))
  if(number == guess):
    print('Congratulations, you guessed right!')
    break
  if(number > guess):
    print('Your guess is lower than a correct answer')
  else:
    print('Your guess is higher than a correct answer')