# System for argv so we can compile on compile in the terminal
from sys import argv

# All our code from the compiler
from compiler import *

# Colors
from rich.console import Console

console = Console()

if __name__ == '__main__':
    # Get our tokens
    tokens = tokenizer(grabCode(argv[1]))

    # Print our each list in the list on it's own line for more readability
    for token_list in range(len(tokens)):
        console.print(tokens[token_list], style="red on black")