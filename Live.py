import requests
import sys
import os

class Code:
    def __init__(self):
        self.white = "\x1b[1;97m"
        self.green = "\x1b[1;92m"
        self.reset = "\x1b[0m"
        self.l = 54

    def clear(self):
        if os.name == "nt":
            os.system('cls')
        else:
            os.system("clear")

    def divider(self):
        print(f"{self.white}-" * self.l)

    def display_header(self):
        self.divider()
        print(f"{self.white}THE 2FA CODE GENERATOR")
        print(f"{self.white}MADE BY GARRYX")
        self.divider()

    def get_code(self, key):
        url = f"https://livedeadsegs.pythonanywhere.com/2F?key={key.replace(' ','')}"
        response = requests.get(url).text
        return response

    def run(self):
        self.clear()
        self.display_header()
        while True:
            key = input(f"{self.white}Enter Key: ")
            if key == "none":
                sys.exit()
            else:
                code = self.get_code(key)
                print(f"Code: {self.green}{code}{self.reset}")
                self.divider()

if __name__ == "__main__":
    generator = Code()
    generator.run()￼Enter
