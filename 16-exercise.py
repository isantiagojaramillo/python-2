import random;

options = ('rock', 'paper', 'scissors');

computer_wins = 0;
user_wins = 0;

rounds = 1;

while True:

    print('*' * 10);
    print('ROUND', rounds);
    print('*' * 10);

    print('computer_wins', computer_wins);
    print('user_wins', user_wins);

    user_option = input('rock, paper or scissors ');
    user_option = user_option.lower();

    rounds += 1;

    if not user_option in options:
      print('INVALID OPTION');
      continue

    computer_option = random.choice(options);

    print('User option: '+ user_option);
    print('Computer option: '+ computer_option);

    if user_option == computer_option:
        print('TIE!');
    elif user_option == 'rock':
        if computer_option == 'SCISSORS':
            print('ROCK WINS TO SCISSORS');
            print('USER WON!');
            user_wins += 1;
        else:
            print('PAPER WINS TO ROCK');
            print('COMPUTER WON!');
            computer_wins += 1;
    elif user_option == 'paper':
        if computer_option == 'rock':
            print('PAPER WINS TO ROCK');
            print('USER WON');
            user_wins += 1;
        else:
            print('SCISSORS WIN TO PAPER');
            print('COMPUTER WON!');
            computer_wins += 1;
    elif user_option == 'scissors':
        if computer_option == 'paper':
            print('SCISSORS WIN TO PAPER');
            print('USER WON!');
            user_wins += 1;
        else:
            print('ROCK WINS TO SCISSORS');
            print('COMPUTER WON!');
            computer_wins += 1;

    if computer_wins == 2:
      print('COMPUTER WINS!');
      break

    if user_wins == 2:
      print('USER WINS!');
      break