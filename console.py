#!/usr/bin/python3
"""Module for HBNBCommand class."""
import cmd

class HBNBCommand(cmd.Cmd):
    """Class for the HBNB command interpreter."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()  # Print newline for nice EOF exit
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

