#!/usr/bin/python3

from datetime import datetime
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.statee import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
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
        obj_list = []
        try:
            obj_dict = models.storage.all()
            if arg:
                for key, value in obj_dict.items():
                    if value.__class__.__name__ == arg:
                        obj_list.append(str(value))
            else:
                for value in obj_dict.values():
                    obj_list.append(str(value))
            print(obj_list)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
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
