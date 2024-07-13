#!/usr/bin/env python3
"""
A script used to monitor a web page
"""
from models.base_model import BaseModel
from bs4 import BeautifulSoup
from os import environ
import requests



class WebPageMonitor(BaseModel):
    """
    A class used to monitor a web page
    """
    sports = {}
    selected_sports = {}


    def __init__(self, *args, **kwargs):
        """
        A method used to initialize this class
        """
        super().__init__(*args, **kwargs)

    def init_BeautifulSoup(self, **kwargs):
        """
        A method to initail a file handle as it has been open
        with BeautifulSoup and also select a html parser
        """
        if kwargs:
            if 'fp' in kwargs.keys():
                self.soup = BeautifulSoup(kwargs['fp'], features="lxml")
                return (self.soup)

    def set_dict_of_sports(self, **kwargs):
        """
        A method to get dictionary
        of all availbale sports
        """
        if (len(self.sports.keys()) > 0):
            return (self.sports)
        else:
            if (kwargs['online'] == 'False'):
                with open(kwargs['file'], 'r') as fp:
                    args = {'fp': fp}
                    monitor = self.init_BeautifulSoup(**args)
                    header = monitor.find('header', class_='Nd')
                    i = 1
                    for child in header.contents:
                        if (i > 5):
                            break
                        name = child.text
                        link = child.get('href')
                        self.sports[i] = {'name': name, 'link': link}
                        i += 1
                return (self.sports)
            elif (kwargs['online'] == 'True'):
                try:
                    response = requests.get(self.url)
                    file = {'fp': response.content}
                    monitor = self.init_BeautifulSoup(**file)
                    header = monitor.find('header', class_='Nd')
                    i = 1
                    for child in header.contents:
                        if (i > 5):
                            break
                        name = child.text
                        link = child.get('href')
                        self.sports[i] = {'name': name, 'link': link}
                        i += 1
                    return self.sports
                except Exception as e:
                    print(e)
                    return (None)
        return (None)
    
    def list_of_sports(self):
        """
        A  method used to list all available sport
        that can be monitored.
        """
        return (self.sports)
    
    def select_sport(self, arg, **kwargs):
        """
        A method used to select a paraticular sport.
        """
        try:
            number = int(arg)
            if (not self.sports):
                self.set_dict_of_sports(**kwargs)
            sport_list = self.list_of_sports()
            if (sport_list.get(number) is None):
                return None
            elif (sport_list.get(number) is not None):
                self.selected_sports[number] = sport_list.get(number)
                return ({number: sport_list.get(number)})
        except Exception as e:
            # print(e)
            return (None)
        

    def get_selected_sports(self):
        """
        A method used to return selected sports
        """
        return (self.selected_sports)
        
    def all_monitored_sports(self):
        """
        A method used to list all monitored sports.
        """
        return (self.selected_sports)
    
    def delete_monitored_sport(self, arg):
        """
        A method used to deleted a specific sport from the list
        of monitored sports.
        """
        monitored_sports = self.selected_sports
        delete_sport = monitored_sports.get(int(arg))
        if (delete_sport):
            sport_name = delete_sport['name']
            del self.selected_sports[int(arg)]
            return (sport_name)
        else:
            return (None)
        
    def delete_all_monitored_sport(self, arg):
        """
        A method used to delete all monitored sports.
        """
        self.selected_sports = {}
        if (len(self.selected_sports) == 0):
            return (True)
        return (False)
    
    def all_lt(self, arg):
        """
        A method used to get all live games leagues and tournaments
        """
        self.selected_sports = {}
        if (len(self.selected_sports) == 0):
            return (None)
        else:
            