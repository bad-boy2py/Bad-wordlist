import sys
import time
import random
import os

# Color snippets
black = "\033[0;30m"
red = "\033[0;31m"
bred = "\033[1;31m"
green = "\033[0;32m"
bgreen = "\033[1;32m"
yellow = "\033[0;33m"
byellow = "\033[1;33m"
blue = "\033[0;34m"
bblue = "\033[1;34m"
purple = "\033[0;35m"
bpurple = "\033[1;35m"
cyan = "\033[0;36m"
bcyan = "\033[1;36m"
white = "\033[0;37m"
nc = "\033[00m"
version = "1.0"

# Regular Snippets
ask = f"{green}[{white}?{green}] {yellow}"
success = f"{yellow}[{white}√{yellow}] {green}"
error = f"{blue}[{white}!{blue}] {red}"
info = f"{yellow}[{white}+{yellow}] {cyan}"
info2 = f"{green}[{white}•{green}] {purple}"
i = f"{red}[+]"

# Slowing write and style
st = 0.00001

def sp1(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(st)


colours = [red, blue, yellow, cyan, purple]
random_color = random.choice(colours)


banner1 = random_color + """██████╗  █████╗ ██████╗                                        
██╔══██╗██╔══██╗██╔══██╗                                       
██████╔╝███████║██║  ██║                                       
██╔══██╗██╔══██║██║  ██║                                       
██████╔╝██║  ██║██████╔╝                                       
╚═════╝ ╚═╝  ╚═╝╚═════╝                                        
                                                               
██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ██╗███████╗████████╗
██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██║██╔════╝╚══██╔══╝
██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     ██║███████╗   ██║   
██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██║╚════██║   ██║   
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗██║███████║   ██║   
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝╚══════╝   ╚═╝   
                                                               \n"""

banner2 = random_color + """ ███████████                █████                                              
░░███░░░░░███              ░░███                                               
 ░███    ░███  ██████    ███████                                               
 ░██████████  ░░░░░███  ███░░███                                               
 ░███░░░░░███  ███████ ░███ ░███                                               
 ░███    ░███ ███░░███ ░███ ░███                                               
 ███████████ ░░████████░░████████                                              
░░░░░░░░░░░   ░░░░░░░░  ░░░░░░░░                                               
                                                                               
                                                                               
                                                                               
 █████   ███   █████                        █████ ████   ███           █████   
░░███   ░███  ░░███                        ░░███ ░░███  ░░░           ░░███    
 ░███   ░███   ░███   ██████  ████████   ███████  ░███  ████   █████  ███████  
 ░███   ░███   ░███  ███░░███░░███░░███ ███░░███  ░███ ░░███  ███░░  ░░░███░   
 ░░███  █████  ███  ░███ ░███ ░███ ░░░ ░███ ░███  ░███  ░███ ░░█████   ░███    
  ░░░█████░█████░   ░███ ░███ ░███     ░███ ░███  ░███  ░███  ░░░░███  ░███ ███
    ░░███ ░░███     ░░██████  █████    ░░████████ █████ █████ ██████   ░░█████ 
     ░░░   ░░░       ░░░░░░  ░░░░░      ░░░░░░░░ ░░░░░ ░░░░░ ░░░░░░     ░░░░░  
                                                                               
                                                                               
                                                                              \n """

banner3 = random_color + """ ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄                                                                   
▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░▌                                                                  
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌                                                                 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌                                                                 
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌                                                                 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌       ▐░▌                                                                 
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌                                                                 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌                                                                 
▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌                                                                 
▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░▌                                                                  
 ▀▀▀▀▀▀▀▀▀▀   ▀         ▀  ▀▀▀▀▀▀▀▀▀▀                                                                   
                                                                                                        
 ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄   ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌           ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌               ▐░▌     ▐░▌               ▐░▌     
▐░▌   ▄   ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌               ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     
▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌               ▐░▌     ▐░░░░░░░░░░░▌     ▐░▌     
▐░▌ ▐░▌░▌ ▐░▌▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌▐░▌               ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌     ▐░▌     
▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌               ▐░▌               ▐░▌     ▐░▌     
▐░▌░▌   ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄█░█▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌     ▐░▌     
▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     
 ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀      
                                                                                                        \n"""


banner4 = random_color + """ ▄▄▄▄    ▄▄▄      ▓█████▄                                        
▓█████▄ ▒████▄    ▒██▀ ██▌                                       
▒██▒ ▄██▒██  ▀█▄  ░██   █▌                                       
▒██░█▀  ░██▄▄▄▄██ ░▓█▄   ▌                                       
░▓█  ▀█▓ ▓█   ▓██▒░▒████▓                                        
░▒▓███▀▒ ▒▒   ▓▒█░ ▒▒▓  ▒                                        
▒░▒   ░   ▒   ▒▒ ░ ░ ▒  ▒                                        
 ░    ░   ░   ▒    ░ ░  ░                                        
 ░            ░  ░   ░                                           
      ░            ░                                             
 █     █░ ▒█████   ██▀███  ▓█████▄  ██▓     ██▓  ██████ ▄▄▄█████▓
▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌▓██▒    ▓██▒▒██    ▒ ▓  ██▒ ▓▒
▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌▒██░    ▒██▒░ ▓██▄   ▒ ▓██░ ▒░
░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ░▓█▄   ▌▒██░    ░██░  ▒   ██▒░ ▓██▓ ░ 
░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░▒████▓ ░██████▒░██░▒██████▒▒  ▒██▒ ░ 
░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ ░ ▒░▓  ░░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   
  ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒ ░ ░ ▒  ░ ▒ ░░ ░▒  ░ ░    ░    
  ░   ░  ░ ░ ░ ▒    ░░   ░  ░ ░  ░   ░ ░    ▒ ░░  ░  ░    ░      
    ░        ░ ░     ░        ░        ░  ░ ░        ░           
                            ░                                    \n"""


banners = [banner1, banner2, banner3, banner4]
random_banner = random.choice(banners) 

os.system("clear")

sp1(random_banner)

# Input prompts
questions = {
    "target_firstname": "What is your target first name?",
    "target_lastname": "What is your target last name?",
    "target_age": "What is your target age?",
    "target_birthday_year": "What is your target birthday year?",
    "target_birthday_month": "What is your target birthday month?",
    "target_birthday_day": "What is your target birthday day?",
    "target_gf_bf": "What is your target girlfriend's or boyfriend's name?",
    "target_talent": "What is your target talent?",
    "target_city": "What is your target city?",
    "target_besthing": "Something that your target Love it so much?",
    "target_bestF": "Her or his best friend?"
}

# Gathering inputs
print("github ==> https://github.com/bad-boy2py")
print("youtube ==> http://www.youtube.com/@user-en4kg8zy4p")
print("")
print("")
print("")
print("")
print("")


answers = {}
for key, question in questions.items():
    answers[key] = input(f"{info}{question} : ")

# Ask for number of lines in the wordlist
num_lines = int(input(f"{info}How many lines do you want in the wordlist? : "))

# Ask for separators
separators = 'space,-,_'.split(',')

save_path = input(f"{info}Enter Path for save your wordlist: ")
if os.path.exists(save_path):
    pass
else:
    print(f"{error}invalid Path, choosing defualt path")
    time.sleep(3)
    save_path = os.getcwd()

# Normalize "space" to actual space character
separators = [' ' if sep.strip() == "space" else sep.strip() for sep in separators]

# Displaying collected information
sp1(f"{success}Collected information:\n")
for key, answer in answers.items():
    sp1(f"{info2}{questions[key]}: {answer} {green} .Done!\n")

# Creating wordlist by mixing the answers with random separators
wordlist = set()
while len(wordlist) < num_lines:
    num_answers = random.randint(2, len(answers))  # Random number of answers per line
    selected_answers = random.sample(list(answers.values()), num_answers)
    combination = random.choice(separators).join(selected_answers)
    wordlist.add(combination)

# Creating wordlist file
wordlist_filename = f"{save_path}\\bad_wordlist.txt"
with open(wordlist_filename, 'w') as f:
    for item in list(wordlist)[:num_lines]:
        f.write(f"{item}\n")

sp1(f"{success}Wordlist has been created in {wordlist_filename}\n")
