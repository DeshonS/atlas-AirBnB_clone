#!/usr/bin/python3
"""
Entry point of the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """
    Command processor
    """

    prompt = "(hbnb)"
    l_classes = ['BaseModel', 'User',]

    l_c = ['count']

    def precmd(self, arg):
        """
        parses command input
        """
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cnd = cls[1].split('(')
            args = cnd[1].split(')')
            if cls[0] in HBNBCommand.l_classes and cnd[0] in HBNBCommand.l_c:
                arg = cnd[0] + ' ' + cls[0] + ' ' + args[0]
        return arg

    def help_help(self):
        """
        Prints help command description
        """
        print("Provides description of a given command")

    def emptyline(self):
        """
        do nothing when empty line
        """
        pass

    def do_count(self, cls_name):
        """
        counts number of instances of a class
        """
        count = 0
        all_objs = storage.all()
        for k, v in all_objs.items():
            clss = k.split('.')
            if clss[0] == cls_name:
                count = count + 1
        print(count)

    def do_quit(self, line):
        """
        Quit command to exit the command interpreter
        """
        return True

    def do_EOF(self, line):
        """
        EOF command to exit the command interpreter
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()