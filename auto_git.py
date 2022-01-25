import os
import argparse
from termcolor import colored

def color_print(content, color='cyan'):
    color_list = ['cyan', 'red', 'blue', 'purple']
    print(colored(content, color=color))

class AutoGit:
    def __init__(self, args):
        self.args = args
        self.mode = self.args.mode
        self.mode_dict = {"push": self.push, 
                            "add":self.add}

    def run(self):
        self.mode_dict[self.mode]()


    def push(self):
        command = "git push"
        color_print("AutoGit command: "+command)
        output = os.popen(command).read()
        print(colored(output, color="cyan") )
    
    def add(self):
        command = "git add ."
        color_print("AutoGit command:"+command)
        output = os.popen(command).read()
        
        print(colored(output, color="cyan") )

arg_parser = argparse.ArgumentParser("Auto Git, by Yanjie Ze")
arg_parser.add_argument("-m", "--mode", choices=['push', 'add'], type=str, default="add")


if __name__=="__main__":
    args = arg_parser.parse_args()
    auto_git = AutoGit(args)
    auto_git.run()
    

        
    