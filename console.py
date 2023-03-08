#!/usr/bin/python3
"""  An HBNBcommmand interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """ A command line interpreter """
    prompt = ' (hbnb) '

    def do_quit(self,arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'Exits the program'
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
