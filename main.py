import random
from time import sleep
import signal, sys, os
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
import numpy as np

# Constants
__CHANNEL_USERNAME__ = "YourTelegramChannelUsername"
__GROUP_USERNAME__ = "YourTelegramGroupUsername"

# Signal handler for graceful exit
def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)

# Function to display ASCII art banner
def banner(console):
    # ASCII art and banner text
    # (omitted for brevity)

# Utility function to validate user input
def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(f"{tag} cannot be empty or just spaces. Please try again.")
        else:
            return value

# Function to generate rainbow-colored string
def rainbow_gradient_string(customer_name):
    # Generates a rainbow gradient effect on customer_name
    # (omitted for brevity)

# Mock functions for free operations (not implemented here)
def increase_money(amount):
    # Simulates increasing money for free
    return True

def increase_coins(amount):
    # Simulates increasing coins for free
    return True

def king_rank():
    # Simulates granting king rank for free
    return True

def change_id(new_id):
    # Simulates changing ID for free
    return True

def change_name(new_name):
    # Simulates changing name for free
    return True

def change_name_rainbow(new_name):
    # Simulates changing name to rainbow for free
    return True

def number_plates():
    # Simulates giving number plates for free
    return True

def account_delete():
    # Simulates deleting account for free
    return True

def account_register(email, password):
    # Simulates registering a new account for free
    return True

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    
    while True:
        banner(console)
        acc_email = prompt_valid_value("[bold]➤ Account Email[/bold]", "Email", password=False)
        acc_password = prompt_valid_value("[bold]➤ Account Password[/bold]", "Password", password=False)
        acc_access_key = prompt_valid_value("[bold]➤ Access Key[/bold]", "Access Key", password=False)
        
        # Login logic and error handling (not fully implemented here)
        
        while True:
            banner(console)
            choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"]
            console.print(" : Increase Money[/bold cyan]")
            console.print(" : Increase Coins[/bold cyan]")
            console.print(" : King Rank[/bold cyan]")
            console.print(" : Change ID[/bold cyan]")
            console.print(" : Change Name[/bold cyan]")
            console.print(" : Change Name (Rainbow)[/bold cyan]")
            console.print(" : Number Plates[/bold cyan]")
            console.print(" : Account Delete[/bold cyan]")
            console.print(" : Account Register[/bold cyan]")
            console.print(" : Delete Friends[/bold cyan]")
            console.print(" : Unlock Paid Cars[/bold cyan]")
            console.print(" : Unlock all Cars[/bold cyan]")
            console.print(" : Unlock all Cars Siren[/bold cyan]")
            console.print(" : Unlock w16 Engine[/bold cyan]")
            console.print(" : Unlock All Horns[/bold cyan]")
            console.print(" : Unlock Disable Damage[/bold cyan]")
            console.print(" : Unlock Unlimited Fuel[/bold cyan]")
            console.print(" : Unlock House 3[/bold cyan]")
            console.print(" : Unlock Smoke[/bold cyan]")
            console.print(" : Change Race Wins[/bold cyan]")
            console.print(" : Change Race Loses[/bold cyan]")
            console.print(" : Clone Account[/bold cyan]")
            console.print("  : Exit[/bold cyan]", end="\n\n")
            
            service = IntPrompt.ask(f"[bold][?] Select a Service [red][1-{choices[-1]} or 0][/red][/bold]", choices=choices, show_choices=False)
            
            if service == 0: # Exit
                console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                break
            elif service == 1: # Increase Money
                console.print("[bold cyan][!] Insert how much money do you want.[/bold cyan]")
                amount = IntPrompt.ask("[bold][?] Amount[/bold]")
                console.print("[bold cyan][%] Saving your data[/bold cyan]: ", end=None)
                if amount > 0 and amount <= 50000000:
                    if increase_money(amount):
                        console.print("[bold green]SUCCESSFUL.[/bold green]")
                    else:
                        console.print("[bold red]FAILED.[/bold red]")
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please use valid values.[/bold yellow]")
                sleep(2)
            elif service == 2: # Increase Coins
                console.print("[bold cyan][!] Insert how much coins do you want.[/bold cyan]")
                amount = IntPrompt.ask("[bold][?] Amount[/bold]")
                console.print("[bold cyan][%] Saving your data[/bold cyan]: ", end=None)
                if amount > 0 and amount <= 90000:
                    if increase_coins(amount):
                        console.print("[bold green]SUCCESSFUL.[/bold green]")
                    else:
                        console.print("[bold red]FAILED.[/bold red]")
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please use valid values.[/bold yellow]")
                sleep(2)
            elif service == 3: # King Rank
                console.print("[bold cyan][%] Giving you a King Rank[/bold cyan]: ", end=None)
                if king_rank():
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                sleep(2)
            elif service == 4: # Change ID
                console.print("[bold cyan][!] Enter your new ID.[/bold cyan]")
                new_id = Prompt.ask("[bold][?] ID[/bold]")
                console.print("[bold cyan][%] Saving your data[/bold cyan]: ", end=None)
                if change_id(new_id):
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                sleep(2)
            elif service == 5: # Change Name
                console.print("[bold cyan][!] Enter your new Name.[/bold cyan]")
                new_name = Prompt.ask("[bold][?] Name[/bold]")
                console.print("[bold cyan][%] Saving your data[/bold cyan]: ", end=None)
                if change_name(new_name):
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                sleep(2)
            elif service == 6: # Change Name Rainbow
                console.print("[bold cyan][!] Enter your new Rainbow Name.[/bold cyan]")
                new_name = Prompt.ask("[bold][?] Name[/bold]")
                console.print("[bold cyan][%] Saving your data[/bold cyan]: ", end=None)
                if change_name_rainbow(new_name):
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                sleep(2)
            elif service == 7: # Number Plates
                console.print("[bold cyan][%] Giving you a Number Plates[/bold cyan]: ", end=None)
                if number_plates():
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                sleep(2)
            elif service == 8: # Account Delete
                console.print("[bold cyan][!] After deleting your account there is no going back !!.[/bold cyan]")
                answ = Prompt.ask("[bold cyan][?] Do You want to Delete this Account ?![/bold cyan]", choices=["y", "n"], default="n")
                if answ == "y":
                    if account_delete():
                        console.print("[bold green]SUCCESSFUL.[/bold green]")
                    else:
                        console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    break
            elif service == 9: # Account Register
                console.print("[bold cyan][!] Registring new Account.[