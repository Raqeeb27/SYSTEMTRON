# Script: tic-tac-toe.py
# Description: Tic-Tac-Toe Game
# Author: Mohammed Abdul Raqeeb
# Date: 30/06/2024

try:
    from colorama import Fore, Style
except ImportError:
    print("This script requires the \'colorama\' module.\nPlease install it using \'pip install colorama\' and try again.")
    exit(1)

from random import choice
from time import sleep


# Define colors and styles
blue = Fore.BLUE
cyan = Fore.CYAN
green  = Fore.GREEN
magenta = Fore.MAGENTA
red = Fore.RED
yellow = Fore.YELLOW
bright = Style.BRIGHT
reset = Style.RESET_ALL

positions = ['0','1','2','3','4','5','6','7','8']
remaining_positions = ['0','1','2','3','4','5','6','7','8']
attempts = 0

def print_board():
    def colored_pos(pos):
        if positions[pos] == 'X':
            return f"{red}{bright}{positions[pos]}{reset}"
        elif positions[pos] == 'O':
            return f"{yellow}{bright}{positions[pos]}{reset}"
        else:
            return f"{positions[pos]}{reset}"

    print(f"\n  {colored_pos(0)} {cyan}{bright}|{reset} {colored_pos(1)} {cyan}{bright}|{reset} {colored_pos(2)} \n {cyan}{bright}---|---|---{reset}")
    print(f"  {colored_pos(3)} {cyan}{bright}|{reset} {colored_pos(4)} {cyan}{bright}|{reset} {colored_pos(5)} \n {cyan}{bright}---|---|---{reset}")
    print(f"  {colored_pos(6)} {cyan}{bright}|{reset} {colored_pos(7)} {cyan}{bright}|{reset} {colored_pos(8)} \n")

def check_winner(player):
    win_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in win_positions:
        if all(positions[i] == player for i in win):
            sleep(0.3)
            print(f"\n{magenta}{bright}\'{player}\' WON the match!!!{reset}")
            sleep(0.5)
            return True
    return False

def single_player_mode():
    global attempts
    print(f"\n{green}{bright}You : {red}\'X\'{reset}\n{blue}{bright}Computer : {yellow}\'O\'{reset}")
    sleep(0.5)
    print_board()
    while attempts < 9:
        player = 'X' if attempts % 2 == 0 else 'O'
        try:
            if player == 'X':
                playerPosition = input(f"{green}\'{player}\' chance\nEnter {player} position: {reset}")
            else:
                playerPosition = choice(remaining_positions)
                print(f"{bright}{blue}\'O\' chance\nComputer Position : {yellow}\'{playerPosition}\'{reset}")
                sleep(0.5)

            if positions[int(playerPosition)] in ['O','X']:
                print_board()
                print(f"{red}{bright}Invalid Position for '{player}'\n{reset}")
                sleep(0.5)
                continue
            else:
                positions[int(playerPosition)] = f"{player}"
                print_board()
                sleep(0.5)
                remaining_positions.remove(str(playerPosition))
                if check_winner(player):
                    break
        except:
            print_board()
            print(f"{bright}{red}Invalid Position for \'{player}\'\nSelect position from 0 - 8\n{reset}")
            sleep(0.5)
            continue
        attempts += 1

def two_player_mode():
    global attempts
    print_board()
    while attempts < 9:
        player = 'X' if attempts % 2 == 0 else 'O'
        player_colour = Fore.GREEN if attempts % 2 == 0 else Fore.BLUE
        try:
            playerPosition = int(input(f"{bright}{player_colour}\'{player}\' chance\nEnter {player} position: {reset}"))

            if positions[playerPosition] in ['O','X']:
                print_board()
                print(f"{red}{bright}Invalid Position for \'{player}\'\n{reset}")
                sleep(0.5)
                continue
            else:
                positions[playerPosition] = f"{player}"
                print_board()
                sleep(0.5)
                if check_winner(player):
                    break
        except:
            print(f"{red}{bright}\nInvalid Position \nSelect position from 0 - 8\n{reset}")
            sleep(0.5)
            continue
        attempts += 1

def main():
    global attempts
    global positions
    global remaining_positions

    while True:
        print(f"\n{magenta}{bright}" + " TIC - TAC - TOE ".center(32, "-"))
        print(f" New Game ".center(32, "-") + f"{reset}")
        print(f"{blue}\nChoose the game mode :\n{yellow}1. Single Player Mode\n2. Two Player Mode{reset}")
        choice = input(f"{magenta}{bright}\n---> {reset}")

        if choice == "1":
            single_player_mode()
        elif choice == "2":
            two_player_mode()
        else:
            print(f"\n{red}{bright}Invalid choice!!!{reset}")

        if attempts >= 9:
            print(f"{yellow}{bright}It's a DRAW !!!\n!!! GAME OVER !!!\n{reset}")

        sleep(0.5)
        play_again = input(f"{blue}\nDo you want to play again (Y/n): ").strip().lower()
        if play_again in ["", "y", "yes"]:
            print()
            attempts = 0
            positions = ['0','1','2','3','4','5','6','7','8']
            remaining_positions = ['0','1','2','3','4','5','6','7','8']
            continue
        elif play_again in ["n", "no"]:
            sleep(0.5)
            print(f"\n{magenta}{bright}!!! Game Over !!!\nHOPE YOU ENJOYED 😇{reset}\n")
            break
        else:
            sleep(0.5)
            print(f"\n{red}{bright}Unrecognized Input\n{magenta}!!! Game Over !!!{reset}\n")
            break

if __name__ == "__main__":
    main()
