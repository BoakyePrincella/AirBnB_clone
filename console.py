#!/usr/bin/python3
"""This is entry point of the command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """The HBNB command"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """The help command for the quit command"""
        print("Quit command to exiy the program")

    def do_EOF(self, line):
        """EOF command to close the program"""
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
