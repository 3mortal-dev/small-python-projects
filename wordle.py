import random

from rich import print

WORD_LIST = ["crane", "slate", "audio", "stare", "earth", "house", "peace", "snake"]


def play_wordle():
    # welcome message
    ATTEMPTS = 5
    print("Welcome to [magenta]3mortal's Wordle[/magenta] [cyan]<*-*>[/cyan]")

    word = random.choice(WORD_LIST)

    while(ATTEMPTS):
        # printing attempts with colors based on remaning ones
        match ATTEMPTS:
            case 5|4:
                print(f"You have [green]{ATTEMPTS}/5 [/green] attempts\n")
            case 3|2:
                print(f"You have [yellow]{ATTEMPTS}/5 [/yellow] attempts\n")
            case 1:
                print(f"You have [red]{ATTEMPTS}/5 [/red] attempt\n")
            case _:
                print("")

        guess = input("Enter a 5-letter word: ").lower()

        while(len(guess) != 5 or not guess.isalpha()):
            print("\n[bold red]Invalid word[/bold red]\n")
            guess = input("Please enter a valid 5-letter word: ").lower()
        
        if guess != word:
            for g_ch, w_ch in zip(guess, word):
                if g_ch == w_ch:
                    print(f"[green]{g_ch}[/green] ", end="")
                elif g_ch in word:
                    print(f"[yellow]{g_ch}[/yellow] ", end="")
                else:
                    print(f"[red]{g_ch}[/red] ", end="")
            print("")
        else:
            print("[green]Congratulations[/green] 🎉👑")
            print(f"The word is [cyan]{word}[/cyan]")
            return
        ATTEMPTS-=1  
    print(f"The word was [bold red]{word}[/bold red]")

play_wordle()
