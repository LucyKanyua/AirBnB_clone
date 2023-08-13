#!/usr/bin/python3
"""
This module implements the HBNBCommand class,
which provides a command-line interface
for interacting with models
in the HBNB application.
"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage

Available_Classes_Dict = {"BaseModel": BaseModel,
                          "User": User,
                          "State": State,
                          "City": City,
                          "Amenity": Amenity,
                          "Place": Place,
                          "Review": Review}


class HBNBCommand(cmd.Cmd):
    """
    This class provides a command-line interface for
    managing the HBNB application's models.
    """
    prompt = "(hbnb) "
    classes = Available_Classes_Dict

    def do_quit(self, line):
        """
        Exit the command-line interface.

        Args:
            line (str): The command line input.

        Returns:
            bool: True to exit the program.
        """
        return True

    def do_EOF(self, line):
        """
        Handle the end-of-file signal (Ctrl-D).

        Args:
            line (str): The command line input.

        Returns:
            bool: True to exit the program.
        """
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of a specified model class
        and save it to the storage.

        Args:
            arg (str): The name of the model class
            to create an instance of.

        Notes:
            If the specified class does not exist,
            an error message is displayed.

        Example:
            create User
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print("{}".format(new_instance.id))
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Display the string representation of an instance
        based on its class name and ID.

        Args:
            arg (str): The class name and instance ID
            in the format "class_name instance_id".

        Notes:
            If the specified class does not exist or if
            the instance ID is missing,
            appropriate error messages are displayed.

        Example:
            show User 1234-5678-9012
        """
        argument = arg.split()
        if not argument:
            print("** class name missing **")
            return
        try:
            obj_dict = models.storage.all()
            key = "{}.{}".format(argument[0], argument[1])
            print(obj_dict[key])
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on its class name and ID.

        Args:
            arg (str): The class name and instance
            ID in the format "class_name instance_id".

        Notes:
            If the specified class does not exist,
            if the instance ID is missing,
            or if the instance does not exist,
            appropriate error messages are displayed.

        Example:
            destroy User 1234-5678-9012
        """
        argument = arg.split()
        if not argument:
            print("** class name missing **")
            return
        try:
            obj_dict = models.storage.all()
            key = "{}.{}".format(argument[0], argument[1])
            del obj_dict[key]
            models.storage.save()
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Display a string representation of all instances of a
        specified class or all instances if no class is specified.

        Args:
            arg (str): The class name.

        Notes:
            If the specified class does not exist, a message is displayed.

        Example:
            all User
        """
        obj_list = []
        if arg:
            if arg not in Available_Classes_Dict:
                print("** class doesn't exist **")
                return
            for key, value in models.storage.all().items():
                if key.split(".")[0] == arg:
                    obj_list.append(str(value))
        else:
            for key, value in models.storage.all().items():
                obj_list.append(str(value))
        print(obj_list)

    def do_update(self, arg):
        """
        Update attributes of an instance based
        on its class name and ID.

        Args:
            arg (str): The class name, instance ID,
            attribute name, and new attribute value.

        Notes:
            If the specified class does not exist,
            if the instance ID is missing, or if the instance does not exist,
            appropriate error messages are displayed.

        Example:
            update User 1234-5678-9012 first_name "John"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            obj_dict = models.storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in obj_dict:
                if len(args) > 2:
                    if len(args) > 3:
                        setattr(obj_dict[key], args[2], args[3].strip('"'))
                    else:
                        print("** value missing **")
                else:
                    print("** attribute name missing **")
                models.storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
