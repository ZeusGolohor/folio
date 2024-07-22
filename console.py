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

    prompt = "(Guze) "
    sports = {}
    selected_sports = {}
    online = environ.get("ONLINE", "True")
    url = "https://www.livescores.com/"
    file1 = "./livescores/live_football.html"
    file2 = "./livescores/live_football_usa_mls.html"
    instance = WebPageMonitor()
    args = {"file": file1, "file2": file2, "online": online, "url": url}

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
                kvparser = arg.split("=", 1)
                key = kvparser[0]
                value = kvparser[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace("_", " ")
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
        if results == None:
            if self.args["online"] == "True":
                print("An error occurred while trying to visit the internet, ")
                print("please check you internet connection")
            else:
                print(
                    "An unknown error occurred, check arguments passed to the software, or the offline file being parsed"
                )
        else:
            return results

    def do_list_of_sports(self, arg):
        """
        A  method used to list all available sport
        that can be monitored.
        """
        sports = self.set_dict_of_sports()
        if sports:
            print("To select a sport use the command below")
            print("Usage: select_sport <sport_number>")
            headers = ["Number", "Sport"]
            table = []
            for key, value in sports.items():
                new_sport = []
                new_sport.append(key)
                new_sport.append(value["name"])
                table.append(new_sport)
            print(tabulate(table, headers, tablefmt="grid"))

    def do_select_sport(self, arg):
        """
        A method used to select a paraticular sport.
        """
        if arg:
            result = self.instance.select_sport(arg, **self.args)
            if result == None:
                print("***{} is not a valid entry***".format(arg))
                print("Select a sport via it's number:")
                self.do_list_of_sports(arg)
            else:
                headers = ["Number", "Sport"]
                table = [["{}".format(arg), "{}".format(result[int(arg)]["name"])]]
                print("You have selected:")
                print(tabulate(table, headers, tablefmt="grid"))
        else:
            print("Select a sport via it's number:")
            self.do_list_of_sports(arg)

    def do_select_all_available_sports(self, arg):
        """
        A method used to select all available sports
        """
        result = self.instance.select_all_available_sports(**self.args)
        if result == None:
            print("There was an error selecting all sports, try again.")
        else:
            print("You have successfully selected all available sports for monitoring.")
            self.do_all_monitored_sports(arg)

    def do_all_monitored_sports(self, arg):
        """
        A method used to list all monitored sports.
        """
        selected_sports = self.instance.all_monitored_sports()
        if len(selected_sports) <= 0:
            print(
                "No sports selected run 'list_of_sports' to get the list of available sports to monitor"
            )
        else:
            print("List of all monitored sports:")
            headers = ["Number", "Sport"]
            table = []
            for key, value in selected_sports.items():
                new_sport = []
                new_sport.append(key)
                new_sport.append(value["name"])
                table.append(new_sport)
            print(tabulate(table, headers, tablefmt="grid"))

    def do_delete_monitored_sport(self, arg):
        """
        A method used to delete a monitored sport.
        """
        selected_sports = self.instance.get_selected_sports()
        if len(selected_sports.keys()) == 0:
            print("You are currently not monitoring any sport(s)")
            print(
                "Run the command 'list_of_sports' to get the list of sports you can monitor"
            )
        else:
            if arg:
                result = self.instance.delete_monitored_sport(arg)
                if result:
                    print("From monitored sports, you have deleted:")
                    headers = ["Number", "Sport"]
                    table = []
                    new_sport = []
                    new_sport.append(arg)
                    new_sport.append(result)
                    table.append(new_sport)
                    print(tabulate(table, headers, tablefmt="grid"))
                else:
                    print(
                        "***{} is not a valid sport number you are monitoring***".format(
                            arg
                        )
                    )
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
        if result == True:
            print("All monitored sports have been deleted")
        else:
            print("An Error occurred, please try again.")

    def do_all_lt(self, arg):
        """
        A method used to get all live games leagues and tournaments
        """
        monitored_sports = self.instance.all_monitored_sports()
        if monitored_sports:
            result = self.instance.all_lt(**self.args)
            # print(result)
            # exit()
            for key, value in monitored_sports.items():
                headers = ["Number", "Sport"]
                table = []
                new_sport = []
                new_sport.append(key)
                new_sport.append(value['name'])
                table.append(new_sport)
                print(tabulate(table, headers, tablefmt="grid"))
                key2 = result.get(value['name'])
                if key2:
                    for key3, value3 in key2.items():
                        headers2 = ["League or Tournament", "Date"]
                        table2 = []
                        new_lt = []
                        new_lt.append(key3)
                        new_lt.append(value3['date'])
                        table2.append(new_lt)
                        print(tabulate(table2, headers2, tablefmt="grid"))
                        headers3 = ["Time", "Team", "Score", "Score", "Team"]
                        table3 = []
                        for key4, value4 in value3['live_lt'].items():
                            new_match = []
                            new_match.append(value4['time'])
                            new_match.append(value4['home'])
                            new_match.append(value4['home_score'])
                            new_match.append(value4['away_score'])
                            new_match.append(value4['away'])
                            table3.append(new_match)
                        print(tabulate(table3, headers3, tablefmt="grid"))
                        print()
                else:
                    headers = ["Number", "League or Tornament", "Sport", "Date"]
                    table2 = []
                    new_lt = []
                    new_lt.append("NO LIVE")
                    new_lt.append("SPORT")
                    new_lt.append("AT THE MOMENT FOR")
                    new_lt.append(value["name"])
                    table2.append(new_lt)
                    print(tabulate(table2, headers, tablefmt="grid"))
                    print()
        else:
            print("no sports")
            self.do_all_monitored_sports(arg)

    def do_add_lt(self, arg):
        """
        A method used to add live leagues or tournaments.
        """
        monitored_sports = self.instance.all_monitored_sports()
        if monitored_sports:
            args = arg.split(" ")
            try:
                number = int(args[0])
                key = monitored_sports.get(number)
                if key:
                    if len(args) < 2:
                        print("An error occurred")
                        print("You need to pass the league or tournament number")
                        print(
                            "Usage: add_lt <sport number> <league or tournament number(s)"
                        )
                    else:
                        print(key)
                else:
                    print(
                        "***'{}' not part of your list of monitored sports".format(
                            number
                        )
                    )
                    self.do_all_monitored_sports(arg)
            except Exception as e:
                # print(e)
                print("An error occurred")
                print("***'{}' is not a valid entry, try again***".format(args[0]))
        else:
            print(
                "An error occurred. Make sure you already selected sport(s) to monitor"
            )
            self.do_all_monitored_sports(arg)

    def do_football_today(self, arg):
        """
        A method to print football games for the day
        """
        result = self.instance.football_today(self.online)
        if (result):
            for key, value in result.items():
                headers = ["League or Tournament", "Date"]
                table = []
                new_lt = []
                new_lt.append(value["name"])
                new_lt.append(value["date"])
                table.append(new_lt)
                print(tabulate(table, headers, tablefmt="grid"))
                headers2 = ["Time", "Home", "Score", "Score", "Away"]
                table2 = []
                for key1, value1 in value["live_lt"].items():
                    # print(key1, value1)
                    new_lt2 = []
                    new_lt2.append(value1["time"])
                    new_lt2.append(value1["home"])
                    new_lt2.append(value1["home_score"])
                    new_lt2.append(value1["away_score"])
                    new_lt2.append(value1["away"])
                    table2.append(new_lt2)
                print(tabulate(table2, headers2, tablefmt="grid"))
                print()
                print()
        else:
            headers = ["Number", "League or Tornament", "Sport", "Date"]
            table2 = []
            new_lt = []
            new_lt.append("NO")
            new_lt.append("SPORT")
            new_lt.append("TODAY FOR")
            new_lt.append("Football")
            table2.append(new_lt)
            print(tabulate(table2, headers, tablefmt="grid"))
            print()
            print()

    def do_football_live(self, arg):
        """
        A method to get football live games
        """
        result = self.instance.football_live(self.online)
        if (result):
            for key, value in result.items():
                headers = ["League or Tournament", "Date"]
                table = []
                new_lt = []
                new_lt.append(value["name"])
                new_lt.append(value["date"])
                table.append(new_lt)
                print(tabulate(table, headers, tablefmt="grid"))
                headers2 = ["Time", "Home", "Score", "Score", "Away"]
                table2 = []
                for key1, value1 in value["live_lt"].items():
                    # print(key1, value1)
                    new_lt2 = []
                    new_lt2.append(value1["time"])
                    new_lt2.append(value1["home"])
                    new_lt2.append(value1["home_score"])
                    new_lt2.append(value1["away_score"])
                    new_lt2.append(value1["away"])
                    table2.append(new_lt2)
                print(tabulate(table2, headers2, tablefmt="grid"))
                print()
                print()
        else:
            headers = ["Number", "League or Tornament", "Sport", "Date"]
            table2 = []
            new_lt = []
            new_lt.append("NO LIVE")
            new_lt.append("SPORT")
            new_lt.append("AT THE MOMENT FOR")
            new_lt.append("FOOTBALL")
            table2.append(new_lt)
            print(tabulate(table2, headers, tablefmt="grid"))
            print()
            print()

    def do_basketball_live(self, arg):
        """
        A method to get live basketball games
        """
        result = self.instance.basketball_live(self.online)
        if (result):
            for key, value in result.items():
                headers = ["League or Tournament", "Date"]
                table = []
                new_lt = []
                new_lt.append(value["name"])
                new_lt.append(value["date"])
                table.append(new_lt)
                print(tabulate(table, headers, tablefmt="grid"))
                headers2 = ["Time", "Home", "Score", "Score", "Away"]
                table2 = []
                for key1, value1 in value["live_lt"].items():
                    # print(key1, value1)
                    new_lt2 = []
                    new_lt2.append(value1["time"])
                    new_lt2.append(value1["home"])
                    new_lt2.append(value1["home_score"])
                    new_lt2.append(value1["away_score"])
                    new_lt2.append(value1["away"])
                    table2.append(new_lt2)
                print(tabulate(table2, headers2, tablefmt="grid"))
                print()
                print()
        else:
            headers = ["Number", "League or Tornament", "Sport", "Date"]
            table2 = []
            new_lt = []
            new_lt.append("NO LIVE")
            new_lt.append("SPORT")
            new_lt.append("AT THE MOMENT FOR")
            new_lt.append("BASKETBALL")
            table2.append(new_lt)
            print(tabulate(table2, headers, tablefmt="grid"))
            print()
            print()

    def do_basketball_today(self, arg):
        """
        A method to get today games for basketball
        """
        result = self.instance.basketball_today(self.online)
        if (result):
            for key, value in result.items():
                headers = ["League or Tournament", "Date"]
                table = []
                new_lt = []
                new_lt.append(value["name"])
                new_lt.append(value["date"])
                table.append(new_lt)
                print(tabulate(table, headers, tablefmt="grid"))
                headers2 = ["Time", "Home", "Score", "Score", "Away"]
                table2 = []
                for key1, value1 in value["live_lt"].items():
                    # print(key1, value1)
                    new_lt2 = []
                    new_lt2.append(value1["time"])
                    new_lt2.append(value1["home"])
                    new_lt2.append(value1["home_score"])
                    new_lt2.append(value1["away_score"])
                    new_lt2.append(value1["away"])
                    table2.append(new_lt2)
                print(tabulate(table2, headers2, tablefmt="grid"))
                print()
                print()
        else:
            headers = ["Number", "League or Tornament", "Sport", "Date"]
            table2 = []
            new_lt = []
            new_lt.append("NO")
            new_lt.append("SPORT")
            new_lt.append("TODAY FOR")
            new_lt.append("BASKETBALL")
            table2.append(new_lt)
            print(tabulate(table2, headers, tablefmt="grid"))
            print()
            print()

    def do_hockey_today(self, arg):
        """
        A method used to get today hockey games.
        """
        result = self.instance.hockey_today(self.online)
        if (result):
            for key, value in result.items():
                headers = ["League or Tournament", "Date"]
                table = []
                new_lt = []
                new_lt.append(value["name"])
                new_lt.append(value["date"])
                table.append(new_lt)
                print(tabulate(table, headers, tablefmt="grid"))
                headers2 = ["Time", "Home", "Score", "Score", "Away"]
                table2 = []
                for key1, value1 in value["live_lt"].items():
                    # print(key1, value1)
                    new_lt2 = []
                    new_lt2.append(value1["time"])
                    new_lt2.append(value1["home"])
                    new_lt2.append(value1["home_score"])
                    new_lt2.append(value1["away_score"])
                    new_lt2.append(value1["away"])
                    table2.append(new_lt2)
                print(tabulate(table2, headers2, tablefmt="grid"))
                print()
                print()
        else:
            headers = ["Number", "League or Tornament", "Sport", "Date"]
            table2 = []
            new_lt = []
            new_lt.append("NO")
            new_lt.append("SPORT")
            new_lt.append("TODAY FOR")
            new_lt.append("HOCKEY")
            table2.append(new_lt)
            print(tabulate(table2, headers, tablefmt="grid"))
            print()
            print()

    def do_hockey_live(self, arg):
        """
        A method to get live hockey games.
        """
        result = self.instance.hockey_live(self.online)
        if (result):
            for key, value in result.items():
                headers = ["League or Tournament", "Date"]
                table = []
                new_lt = []
                new_lt.append(value["name"])
                new_lt.append(value["date"])
                table.append(new_lt)
                print(tabulate(table, headers, tablefmt="grid"))
                headers2 = ["Time", "Home", "Score", "Score", "Away"]
                table2 = []
                for key1, value1 in value["live_lt"].items():
                    # print(key1, value1)
                    new_lt2 = []
                    new_lt2.append(value1["time"])
                    new_lt2.append(value1["home"])
                    new_lt2.append(value1["home_score"])
                    new_lt2.append(value1["away_score"])
                    new_lt2.append(value1["away"])
                    table2.append(new_lt2)
                print(tabulate(table2, headers2, tablefmt="grid"))
                print()
                print()
        else:
            headers = ["Number", "League or Tornament", "Sport", "Date"]
            table2 = []
            new_lt = []
            new_lt.append("NO")
            new_lt.append("SPORT")
            new_lt.append("AT THE MOMENT FOR")
            new_lt.append("HOCKEY")
            table2.append(new_lt)
            print(tabulate(table2, headers, tablefmt="grid"))
            print()
            print()

    def do_tennis_today(self, arg):
        """
        A method used to get today games for tennis
        """
        result = self.instance.tennis_today(self.online)
        if (result):
            print(result)
        else:
            pass



if __name__ == "__main__":
    GUZECommand().cmdloop()
