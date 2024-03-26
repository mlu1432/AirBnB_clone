#!/usr/bin/python3
"""Module for HBNBCommand class."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class for the HBNB command interpreter."""
    prompt = '(hbnb) '
    class_dict = {
         'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()  # Print newline for nice EOF exit
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt."""
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.class_dict:
            print("** class doesn't exist **")
            return
        instance = self.class_dict[arg]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """ the string representation of an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """ it deletes an instance based on the class name and id (save the change into the JSON file)."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        args = arg.split()
        if len(args) > 0 and args[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        obj_list = []
        for obj in storage.all().values():
            if len(args) == 0 or obj.__class__.__name__ == args[0]:
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        instance = storage.all()[key]
        setattr(instance, args[2], args[3].strip('"'))
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
