#!/usr/bin/python3
"""This is the console for AirBnB"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """this class is entry point of the command interpreter
    """
    prompt = "(hbnb) "
    all_classes = {"BaseModel", "State", "City", "Amenity",
                   "Place", "Review", "User"}

    def emptyline(self):
        """Ignores empty spaces"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program at end of file"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        new_args = []
        for a in args:
            start_idx = a.find("=")
            a = a[0: start_idx] + a[start_idx:].replace('_', ' ')
            new_args.append(a)

        if new_args[0] in classes:
            new_instance = classes[new_args[0]]()
            new_dict = {}
            for a in new_args:
                if a != new_args[0]:
                    new_list = a.split('=')
                    new_dict[new_list[0]] = new_list[1]

            for k, v in new_dict.items():
                if v[0] == '"':
                    v_list = shlex.split(v)
                    new_dict[k] = v_list[0]
                    setattr(new_instance, k, new_dict[k])
                else:
                    try:
                        if type(eval(v)).__name__ == 'int':
                            v = eval(v)
                    except Exception:
                        continue
                    try:
                        if type(eval(str(v))).__name__ == 'float':
                            v = eval(v)
                    except Exception:
                        continue
                    setattr(new_instance, k, v)
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if my_list[0] not in self.all_classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key in objects:
                tmp = objects[key]
                print(tmp)
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        Exceptions:
            NameError: when there is no object taht has the name
        """
        objects = storage.all()
        my_list = []
        if not line:
            for key in objects:
                my_list.append(str(objects[key]))
            print(my_list)
            return
        try:
            args = line.split(" ")
            if args[0] not in self.all_classes:
                raise NameError()
            for key in objects:
                name = key.split('.')
                if name[0] == args[0]:
                    my_list.append(str(objects[key]))
            print(my_list)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instanceby adding or updating attribute
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
            AttributeError: when there is no attribute given
            ValueError: when there is no value given
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if my_list[0] not in self.all_classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key not in objects:
                raise KeyError()
            if len(my_list) < 3:
                raise AttributeError()
            if len(my_list) < 4:
                raise ValueError()
            v = objects[key]
            try:
                v.__dict__[my_list[2]] = eval(my_list[3])
            except Exception:
                v.__dict__[my_list[2]] = my_list[3]
                v.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if my_list[0] not in self.all_classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key in objects:
                del objects[key]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_count(self, line):
        """
            count the number of instances of a class
        """
        counter = 0
        try:
            my_list = line.split(" ")
            if my_list[0] not in self.all_classes:
                raise NameError()
            objects = storage.all()
            for key in objects:
                name = key.split('.')
                if name[0] == my_list[0]:
                    counter += 1
            print(counter)
        except NameError:
            print("** class doesn't exist **")

    def limpiar(self, className, str):
        """
            extrae lo que hay dentro del parentesis
        """
        ListPart1 = str.split(',')
        New_list = []
        aux_id = ListPart1[0].split('"')
        New_list.append(className)
        New_list.append(aux_id[1])
        if len(ListPart1) > 1:
            for i in range(1, len(ListPart1)):
                try:
                    aux = ListPart1[i].split('"')
                    New_list.append(aux[1])
                except Exception:
                    aux = ListPart1[i].split(' ')
                    aux = aux[1].split(')')
                    New_list.append(aux[0])
        return " ".join(i for i in New_list)

    def default(self, line):
        """retrieve all instances of a class and
        retrieve the number of instances
        """
        my_list = line.split('.')
        print(my_list[1])
        if len(my_list) >= 2:
            if my_list[1] == "all()":
                self.do_all(my_list[0])
            elif my_list[1] == "count()":
                self.do_count(my_list[0])
            elif my_list[1][:4] == "show":
                self.do_show(self.limpiar(my_list[0], my_list[1]))
            elif my_list[1][:7] == "destroy":
                self.do_destroy(self.limpiar(my_list[0], my_list[1]))
            elif my_list[1][:6] == "update":
                self.do_update((self.limpiar(my_list[0], my_list[1])))
        else:
            cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
