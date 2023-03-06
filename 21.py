# CIT 590 HW 3
# Made by Ze Sheng 57990537
# I wrote all the codes by myself.

from random import randint


def print_instructions(): # the game rule is from https://www.mastersofgames.com/rules/blackjack-rules.htm
    """
        Aim

    The aim of blackjack is to finish the game with a higher total than that of the dealer, without exceeding 21. Going over 21 is commonly known as ‘busting’ and means an automatic loss.

    The Play - Basic Rules

    Blackjack is usually played at a table of 2-7 players and uses one to eight 52-card decks. All number cards (2-10) score the value indicated on them. The face cards (Jack, Queen, King) score 10 points and Ace can either be treated as 1 or 11.

    At the beginning of each round, all players place their bets in their betting positions - also known as ‘boxes’. After the bets have been placed, all players are dealt two cards face-up in front of their respective betting positions. The dealer receives two cards, one face-up and another face-down.

    Starting to the left of the dealer, each player is given a chance to draw more cards. The players can either ‘hit’ or ‘stand’. If the player calls out ‘HIT’, they are given an extra card. They can then either call out ‘HIT’ again, or ‘STAND’ if they do not wish to draw any more cards. The player can ‘HIT’ as many times as they wish, but have to aim not to ‘bust’ (exceed a total of 21).

    If the player busts, they immediately lose their bet.

    After each player has played and either stood or busted, the dealer takes their turn. They can, again, either ‘HIT’ or ‘STAND’. If the dealer’s hand exceeds 21, all players who didn't bust win immediately - their bet is returned along with a matching amount from the dealer's bank.

    If the dealer reaches a valid hand, the cards are totalled and each player’s hand is compared to the dealer’s. If the player scored higher than the dealer, they win. If the player ties with the dealer, the original bet is returned to the player. Otherwise, the player loses their bet.

    A perfect hand combines an ace with a 10, Jack, Queen or King and is known as a ‘Blackjack’.

        """

    print("""
Let's play Simple21!
You'll play against the computer.
Try to get as close to 21 as possible, without going over.

    """)




def ask_yes_or_no(prompt):
    """
    Displays the given prompt and asks the user for input.  If the user's input starts with 'y', returns True.
    If the user's input starts with 'n', returns False.
    For example, calling ask_yes_or_no("Do you want to play again? (y/n)")
    would display "Do you want to play again? (y/n)", wait for user input that starts with 'y' or 'n',
    and return True or False accordingly.
    """
    while True:
        player_input = input(prompt).strip()[0]
        if player_input == 'y' or player_input == 'Y':
            return True
        elif player_input == 'n' or player_input == 'N':
            return False
        else:
            print("Input error! Please enter again!")



def next_card():
    """
    Returns a random "card", represented by an int between 1 and 10, inclusive.
    The "cards" are the numbers 1 through 10 and they are randomly generated, not drawn from a deck of
    limited size.  The odds of returning a 10 are four times as likely as any other value (because in an
    actual deck of cards, 10, Jack, Queen, and King all count as 10).
    """
    card = randint(1, 13)

    # set J Q K to 10
    if card > 10:
        card = 10

    return card


def take_another_card(computer_total_points, user_visible_card):
    """
    Strategy for computer to take another card or not.  According to the computer’s own given
    total points (sum of visible cards + hidden card) and the user's sum of visible cards, you
    need to design a game strategy for the computer to win the game.
    Returns True if the strategy decides to take another card, False if the computer decides not
    to take another card.
    """
    if user_visible_card > 21: # player bursts
        return False
    elif user_visible_card >= 17 and computer_total_points > 17:  # player may burst
        return False
    elif 17 > user_visible_card > computer_total_points:
        return True
    elif computer_total_points <= 17:
        return True
    else:
        return False


def is_game_over(is_user_passed, is_computer_passed):
    """
    Determines if the game is over or not.
    If the given is_user_passed is set to True, the user has passed.
    If the given is_computer_passed is set to True, the computer has passed.
    This function returns True if both the user and the computer have passed,
    and False if either of them has not yet passed.
    """
    if is_user_passed and is_computer_passed:
        print("""-----Game Over------""")
        return True
    else:
        return False
    


def print_status(is_user, name, hidden_card, visible_card, total_points):
    """
    In each turn, prints out the current status of the game.
    If is_user is set to True, the given player is the user.  In this case, print out
    the user's given name, his/her hidden card points, visible card points, and total points.
    If is_user is set to False, the given player is the computer.  In this case, print out
    the computer's given name, and his/her visible card points.

    For example, calling print_status(True, "Brandon", 4, 15, 19) would print:
    Brandon has 4 hidden point(s).
    Brandon has 15 visible point(s).
    Brandon has 19 total point(s).

    As another example, calling print_status(False, "Computer", 1, 19, 20) would print:
    Computer has 19 visible point(s).
    """
    if is_user: # player's status
        print(name + ' has ' + str(hidden_card) + ' hidden point(s).')
        print(name + ' has ' + str(visible_card) + ' visible point(s).')
        print(name + ' has ' + str(total_points) + ' total point(s).')
    else: # computer's status
        print(name + ' has ' + str(visible_card) + ' visible point(s).')



def print_winner(username, user_total_points, computer_name, computer_total_points):
    """
    Determines who won the game and prints the game results in the following format:
    - User's given name and the given user's total points
    - Computer's given name and the given computer's total points
    - The player who won the game and the total number of points he/she won by, or if it's a tie, nobody won.
    """
    print(username, 'has', user_total_points, 'in total.')
    print(computer_name, 'has', computer_total_points, 'in total.')
    score_diff = abs(int(user_total_points-computer_total_points))

    # decide who is winning
    if user_total_points <= 21 and computer_total_points <= 21:
        if user_total_points > computer_total_points:
                print(username, 'wins by', score_diff, 'point(s).')
        elif user_total_points < computer_total_points:
                print(computer_name, 'wins by', score_diff, 'point(s).')
        else:
                print('Nobody wins. It\'s a tie!')
    elif user_total_points > 21 and computer_total_points <= 21:  # other cases
        print(computer_name, 'wins by', score_diff, 'point(s).')
    elif user_total_points <= 21 and computer_total_points > 21:  # other cases
        print(username, 'wins by', score_diff, 'point(s).')
    else:
        print('Nobody wins.')


def run(username, computer_name):
    """
    This function controls the overall game and logic for the given user and computer.
    """
    # deal for player
    is_user = True
    [player_hidden, player_visible] = [next_card(), next_card()]
    # deal for computer:
    [computer_hidden, computer_visible] = [next_card(), next_card()]

    # status for player
    print_status(is_user, username, player_hidden, player_visible, player_hidden + player_visible)

    # status for computer
    is_user = False
    print_status(is_user, computer_name, computer_hidden, computer_visible, computer_hidden + computer_visible)

    # continue the game:
    is_user_passed = False
    is_computer_passed = False

    # continue dealing for player until a pass
    while not is_game_over(is_user_passed, is_computer_passed):
        if not is_user_passed:
            # deal for player:
            another_card_or_not = ask_yes_or_no('Take another card? (y/n)')
            if another_card_or_not:
                another_card = next_card()
                print(username, ' gets ', another_card)
                player_visible += another_card
                print_status(True, username, player_hidden, player_visible, player_hidden + player_visible)
            else:
                print(username, 'passed!')
                is_user_passed = True

        if not is_computer_passed:
            computer_total = computer_hidden + computer_visible
            another_card_or_not = take_another_card(computer_total, player_visible)
            if another_card_or_not:
                another_card = next_card()
                print(computer_name, ' gets ', another_card)
                computer_visible += another_card
                print_status(False, computer_name, computer_hidden, computer_visible, computer_total)
            else:
                print(computer_name, 'passed!')
                is_computer_passed = True
    # game over: print winner:
    player_total = player_hidden + player_visible
    print_winner(username, player_total, computer_name, computer_total)


def main():
    """
    Main Function.
    """

    # print the game instructions
    print_instructions()

    # get and set user's name
    username = input("What's your name?\r\n")

    # set computer's name
    computer_name = "Computer"

    # insert the rest of the code in the main function here
    while True:
        run(username, computer_name)
        another_game_or_not = ask_yes_or_no('Play again? (y/n)')
        if another_game_or_not:
            new_name_or_not = ask_yes_or_no('Modify username? (y/n)')
            if new_name_or_not:
                username = input("Update your name\r\n")
        else:
            print("Thanks for playing! Goodbye!")
            break




if __name__ == '__main__':
    main()