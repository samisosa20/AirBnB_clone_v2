#!/usr/bin/python3
"""
Storage Class
"""
import models
import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        if not cls:
            return self.__objects
        list_obj = {}
        for obj, key in self.__objects.items():
            if isinstance(key, cls):
                list_obj[obj] = key
        return list_obj

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serialize objectsto the JSON file"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as file:
            json.dump(my_dict, file)

    def reload(self):
        """serialize the file path to JSON file path
        Exceptions:
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as file:
                load_json = json.load(file)
                for key, value in load_json.items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            return

    def delete(self, obj=None):
        """Delete element in the object
        """
        if obj:
            key = str(obj.__class__.__name__) + '.' + str(obj.id)
            self.__objects.pop(key, None)
            self.save()
        else:
            return
