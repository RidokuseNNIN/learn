import random

# Lista przechowująca historię gier
game_history = []

while True:
    # Wybór trybu gry
    mode = input("Choose game mode (single/multiplayer): ").strip().lower()
    if mode == "multiplayer":
        num_random = int(input("Player 1, choose a number for Player 2 to guess: "))
        print("Player 2, it's your turn to guess!")
        min_num, max_num = 1, 500  # Opcjonalnie, ustalony zakres
        max_attempts = 10
    else:
        # Wybór trybu trudności
        difficulty = input("Choose difficulty (easy/medium/hard): ").strip().lower()
        if difficulty == "easy":
            min_num, max_num = 1, 50
            max_attempts = 15
        elif difficulty == "medium":
            min_num, max_num = 1, 100
            max_attempts = 10
        elif difficulty == "hard":
            min_num, max_num = 1, 500
            max_attempts = 7
        else:
            print("Invalid choice. Defaulting to medium difficulty.")
            min_num, max_num = 1, 100
            max_attempts = 10
        # Losowanie liczby
        num_random = random.randint(min_num, max_num)

    # Informacje o grze
    print(f"Try to guess the number between {min_num} and {max_num}.")
    print(f"You have {max_attempts} attempts to guess the number.")
    test_counter = 0

    # Rozpoczęcie gry
    while True:
        try:
            num_user = int(input("give a num: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        test_counter += 1

        # Sprawdzanie limitu prób
        if test_counter >= max_attempts:
            print(f"Game over! You've used all {max_attempts} attempts. The number was {num_random}.")
            break

        # Podpowiedzi
        difference = abs(num_user - num_random)
        if difference <= 5:
            print("You're very close!")
        elif difference > 50:
            print("You're far away!")
        else:
            print("Getting closer!")

        # Sprawdzanie odpowiedzi
        if num_user > num_random:
            print("too much")
        elif num_user < num_random:
            print("to little")
        else:
            # Komunikat końcowy
            print(f"Bravo you got it in {test_counter} tries. The number was {num_random}.")
            game_history.append(test_counter)
            break

    # Zapytanie o ponowną grę
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "no":
        print("Game history:")
        for i, attempts in enumerate(game_history, 1):
            print(f"Game {i}: {attempts} attempts")
        print("Thanks for playing!")
        break