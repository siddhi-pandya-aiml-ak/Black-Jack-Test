# Python Task 1 : Blackjack-Test

## Project Structure

-   card.py -- Defines the Card class (rank, suit, and value logic).
-   game.py -- Contains game logic, dealer and player turns, and
    bankroll handling.
-   main.py -- Entry point to run the game.

------------------------------------------------------------------------

## How to Run

1.  Open a terminal inside the project folder.

2.  Run:

    python main.py

3.  Follow the prompts:

    -   h → Hit
    -   s → Stand
    -   y → Play next round

------------------------------------------------------------------------

## Game Rules

-   Player starts with \$1000.
-   Fixed bet is \$50 per round.
-   A new 52-card deck is created every round.
-   Number cards = face value.
-   J, Q, K = 10.
-   A = 11 (automatically adjusted to 1 if total exceeds 21).
-   Player bust (\>21) = Lose.
-   Dealer hits until total is 17 or more.
-   Player wins if:
    -   Dealer busts, or
    -   Player total is greater than dealer.


-   Player loses if:
    -   Player busts, or
    -   Dealer total is greater than or equal to player.
-   Game ends when bankroll is less than \$50.

## Demo of Black-Jack Game

<img width="967" height="805" alt="Screenshot from 2026-02-20 19-28-22" src="https://github.com/user-attachments/assets/9d10e26e-05aa-49cc-b5b0-9f5fcc78dd7f" />

<img width="974" height="738" alt="Screenshot from 2026-02-20 19-29-44" src="https://github.com/user-attachments/assets/bc864232-c9b0-4453-9df7-5b4b8d8f96e5" />
