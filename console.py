#!/usr/bin/python3
"""The `console.py` module
defines the class `HBNBCommand`"""

import cmd
import shlex
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """creates a command line inteface"""

    prompt = "(hbnb) "
    __classes = ["BaseModel", "User", "Place",
                 "State", "City", "Amenity", "Review"]
    __commands = ["show", "count", "destroy", "all", "update"]

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_create(self, arg):
        """creates a new instance of one of the classes, \
            saves it to the JSON and prints the `id`\n"""
        if arg:
            if arg in type(self).__classes:
                obj = eval(arg)()
                obj.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """prints the string representation of an instance based \
             on the class name and id\n"""
        args = shlex.split(arg)
        if self.is_valid_arg(arg):
            obj_id = args[0] + "." + args[1]
            print(storage.all()[obj_id])

    def do_destroy(self, arg):
        """deletes an instance based on the class name and id\n"""

        args = shlex.split(arg)
        if self.is_valid_arg(arg):
            obj_id = args[0] + "." + args[1]
            storage.all().pop(obj_id)
            storage.save()

    def do_all(self, arg):
        """prints all string representation of all instances \
        based or not on the class name\n"""
        my_list = []
        if arg:
            if arg in type(self).__classes:
                for key in storage.all().keys():
                    if key.startswith(arg):
                        my_list.append(storage.all()[key].__str__())
            else:
                print("** class doesn't exist **")
        else:
            for key in storage.all().keys():
                my_list.append(storage.all()[key].__str__())

        print(my_list)

    def do_count(self, arg):
        """returns the number of instance for a given class"""
        if arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            num_of_instance = 0
            for obj in storage.all().values():
                if type(obj) == eval(arg):
                    num_of_instance = num_of_instance + 1

            print(num_of_instance)

    def do_update(self, arg):
        """updates an instance based on the class name and id\n"""

        if arg.endswith("*dict*"):
            # update from dictionary

            # class name and id
            args = shlex.split(arg[: arg.find("{")])
            obj_id = args[0] + "." + args[1]
            obj_dict = storage.all()[obj_id].to_dict()

            # recreate the dictionary using json
            dict_string = arg[arg.find("{"):].replace("*dict*", "")
            dictionary = ast.literal_eval(dict_string)

            obj_dict.update(dictionary)
            new_obj = eval(args[0])(**obj_dict)
            storage.all()[obj_id] = new_obj
            storage.save()
        else:
            args = shlex.split(arg)
            if self.is_valid_arg(arg):
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    obj_id = args[0] + "." + args[1]

                    obj_dict = storage.all()[obj_id].to_dict()
                    obj_dict[args[2]] = args[3]
                    new_obj = eval(args[0])(**obj_dict)
                    storage.all()[obj_id] = new_obj
                    storage.save()

    def emptyline(self):
        """does nothing when an empty line is entered"""
        return False

    def is_valid_arg(self, args):
        """validates the class name and id"""

        is_valid_class = False

        if args:
            # validate class name
            args = args.split(" ")

            if args[0] in type(self).__classes:
                is_valid_class = True
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

        # if class is valid validate id
        if is_valid_class:
            if len(args) >= 2:
                obj_id = args[0] + "." + args[1]
                if obj_id not in storage.all().keys():
                    print("** no instance found **")
                else:
                    return True
            else:
                print("** instance id missing **")

    def precmd(self, line):
        """formats the `line` before it is interpreted"""

        needs_formatting = False
        if "." in line and "(" in line and ")" in line:
            # if command is valid
            command = line[line.find(".") + 1: line.find("(")]
            if command in HBNBCommand.__commands:
                needs_formatting = True

        if needs_formatting:
            cls_name = line[: line.find(".")]
            cmd = line[(line.find(".") + 1): line.find("(")]
            if cmd == "all" or cmd == "count":
                return "{} {}".format(cmd, cls_name)
            elif cmd == "show" or cmd == "destroy":
                id = line[line.find("(") + 1: line.find(")")].replace('"', "")
                return "{} {} {}".format(cmd, cls_name, id)
            elif cmd == "update":
                # get the id (the argument first)
                params = line[line.find("(") + 1: line.find(")")]
                id = params[: params.find(",")].replace('"', "")
                params = params[params.find(",") + 1:].strip()

                # update from dictionary
                if "{" in params and "}" in params and ":" in params:
                    if params[0] == "{" and params[len(params) - 1] == "}":
                        return "{} {} {} {} {}".format(
                            cmd, cls_name, id, params, "*dict*"
                        )
                else:
                    params = params.split(', ')
                    return "{} {} {} {} {}".format(cmd, cls_name, id, params[0], params[1])
        else:
            return line


if __name__ == "__main__":
    HBNBCommand().cmdloop()
