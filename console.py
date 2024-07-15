#!/usr/bin/env python3
"""
A script to intract with the application from the console.
"""

import cmd
import shlex
import config
from models.web_page_monitor import WebPageMonitor
import requests
from os import environ
from tabulate import tabulate


if config.SHOW_MESSAGE:
    print(config.DEFAULT_MESSAGE)
    config.SHOW_MESSAGE = False  # Only show once



class GUZECommand(cmd.Cmd):
    """
    A class use to handle the application console.
    """
    prompt = '(Guze) '
    sports = {}
    selected_sports = {}
    online = environ.get('ONLINE', 'True')
    url = 'https://www.livescores.com/'
    file1 = "./livescores/LiveScore_Football_Premier_League_Live_Football_Scores_Egypt.html"
    instance = WebPageMonitor()
    args = {
            'file': file1,
            'online': online,
            'url': url
        }
    

    def do_EOF(self, arg):
        """
        A method used to exist the console.
        """
        return True

    def emptyline(self):
        """
        A method used to overwriting the emptyline method
        """
        return False
    
    def do_quit(self, arg):
        """
        A method used to exit the program
        """
        return True
    
    def _key_value_parser(self, args):
        """
        A method used to creates a dictionary from a list of strings.
        """
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvparser = arg.split('=', 1)
                key = kvparser[0]
                value = kvparser[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict
    
    def set_dict_of_sports(self):
        """
        A method to get dictionary
        of all availbale sports
        """
        
        results = self.instance.set_dict_of_sports(**self.args)
        if (results == None):
            if (self.args['online'] == 'True'):
                print("An error occured while trying to visit the internet, ")
                print("please check you internet connection")
            else:
                print("An unknown error occured, check arguments passed to the software, or the offline file being parsed")
        else:
            return (results)


    def do_list_of_sports(self, arg):
        """
        A  method used to list all available sport
        that can be monitored.
        """
        sports = self.set_dict_of_sports()
        if (sports):
            print('To select a sport use the command below')
            print("Usage: select_sport <sport_number>")
            headers = ['Number', 'Sport']
            table = []
            for key, value in sports.items():
                new_sport = []
                new_sport.append(key)
                new_sport.append(value['name'])
                table.append(new_sport)
            print(tabulate(table, headers, tablefmt='grid'))

    def do_select_sport(self, arg):
        """
        A method used to select a paraticular sport.
        """
        if (arg):
            result = self.instance.select_sport(arg, **self.args)
            if (result == None):
                print("***{} is not a valid entry***".format(arg))
                print("Select a sport via it's number:")
                self.do_list_of_sports(arg)
            else:
                headers = ['Number', 'Sport']
                table = [['{}'.format(arg), '{}'.format(result[int(arg)]['name'])]]
                print('You have selected:')
                print(tabulate(table, headers, tablefmt='grid'))     
        else:
            print("Select a sport via it's number:")
            self.do_list_of_sports(arg) 


    def do_all_monitored_sports(self, arg):
        """
        A method used to list all monitored sports.
        """
        selected_sports = self.instance.all_monitored_sports()
        if (len(selected_sports) <= 0):
            print("No sports selected run 'list_of_sports' to get the list of available sports to monitor")
        else:
            print("List of all monitored sports:")
            headers = ['Number', 'Sport']
            table = []
            for key, value in selected_sports.items():
                new_sport = []
                new_sport.append(key)
                new_sport.append(value['name'])
                table.append(new_sport)
            print(tabulate(table, headers, tablefmt='grid'))
              

    def do_delete_monitored_sport(self, arg):
        """
        A method used to delete a monitored sport.
        """
        selected_sports = self.instance.get_selected_sports()
        if (len(selected_sports.keys()) == 0):
            print("You are currently not monitoring any sport(s)")
            print("Run the command 'list_of_sports' to get the list of sports you can monitor")
        else:
            if (arg):
                result = self.instance.delete_monitored_sport(arg)
                if (result):
                    print('From monitored sports, you have deleted:')
                    headers = ['Number', 'Sport']
                    table = []
                    new_sport = []
                    new_sport.append(arg)
                    new_sport.append(result)
                    table.append(new_sport)
                    print(tabulate(table, headers, tablefmt='grid'))
                else:
                    print('***{} is not a valid sport number you are monitoring***'.format(arg))
                    print("You need to passed the sport number to be deleted")
                    print("Usage: delete_monitored_sport <sport_number>")
                    self.do_all_monitored_sports(arg)
            else:
                print("You need to passed the sport number to be deleted")
                print("Usage: delete_sport <sport_number>")
                self.do_all_monitored_sports(arg)

    def do_delete_all_monitored_sports(self, arg):
        """
        A method used to delete all monitored sports.
        """
        result = self.instance.delete_all_monitored_sports(arg)
        if (result == True):
            print("All monitored sports have been deleted")
        else:
            print("An Error occured, please try again.")

    def do_all_lt(self, arg):
        """
        A method used to get all live games leagues and tournaments
        """
        result = self.instance.all_lt(arg)
        if (result == None):
            print("An error occured. Make sure you already selected sport(s) to monitor")
            self.do_all_monitored_sports(arg)
        else:
            print(result)


if __name__ == "__main__":
    GUZECommand().cmdloop()
