#1/usr/bin/python3
"""This is entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.city import City
import re

class HBNBCommand(cmd.Cmd):
    """The HBNB command"""
    prompt = '(hbnb) '
    models_list = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """The help command for the quit command"""
        print("Quit command to exiy the program")

    def do_EOF(self, line):
        """EOF command to close the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of the Basemodel and prints it id"""
        if not line:
            print("** class name is missing **")
            return

        line = line.split()
        class_name = line[0]

if __name__ == '__main__':
    HBNBCommand().cmdloop()
