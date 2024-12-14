from rich import print

from rich.console import Console
from rich.prompt import Prompt

from os import listdir
from os.path import isfile, join

import sys

console = Console()

colors = []
for i in range(60, 240, 10):
    colors.append(f"rgb({i},{i},{i})")

print("\n[bold magenta]  Welcome to [white on grey23] fireguide [/white on grey23][/bold magenta]")

options = ["View heatmap", "Submit number", "Submit new type"]

def main():
    console.print("\n[bold cyan]Select an option:[/bold cyan]\n")
    
    for idx, option in enumerate(options, start=1):
        console.print(f"[white]{idx}. {option}[/white]")
    
    choice = int(Prompt.ask("\nEnter number of your choice", choices=[str(i) for i in range(1, len(options)+1)]))
    print()
    
    if choice != 3:
        files = [f for f in listdir("data") if isfile(join("data", f))]
    
        for idx, option in enumerate(files, start=1):
            console.print(f"[white]{idx}. {option}[/white]")
    
        file = int(Prompt.ask("\nEnter the filename", choices=[str(i) for i in range(1, len(files)+1)]))
    else:
        filename = input("Enter the name of the file you wish to create: ")
        file = open(f"data/{filename}", "x")
        display_options()
    
    if choice == 1:
        content = open(f"data/{files[file-1]}", "r")
    
        times = []
        for i in content:
            times.append(int(i.replace("\n", "")))
        for i in times:
            minimum = min(times)
            maximum = max(times)
            difference = maximum-minimum+1
    
            position = round(((i-minimum)/difference)*18)
            if position > 0:
                heat = colors[position-1]
            else:
                heat = colors[position]
            print(f"[{heat}]██[/{heat}]", end="")
        print("\n")
        main()
    elif choice == 2:
        append = open(f"data/{files[file-1]}", "a")
        time = 1
        print("Enter values in minutes, or 0 to stop")
        while time != 0:
            time = int(input())
            append.write(f"{time}\n")
        main()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
