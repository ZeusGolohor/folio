#!/usr/bin/env python3
"""
A script used to monitor a web page
"""
from models.base_model import BaseModel
from bs4 import BeautifulSoup
from os import environ
import requests
import re



class WebPageMonitor(BaseModel):
    """
    A class used to monitor a web page
    """
    sports = {}
    selected_sports = {}
    url = 'https://www.livescores.com'
    lt = {}


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
                        if (name == 'Football'):
                            main_link = link[:-6] + 'footbal/live/'
                        else:
                            main_link = link[:-6] + 'live/'
                        self.sports[i] = {'name': name, 'link': main_link}
                        i += 1
                return (self.sports)
            elif (kwargs['online'] == 'True'):
                try:
                    response = requests.get(kwargs['url'])
                    file = {'fp': response.content}
                    monitor = self.init_BeautifulSoup(**file)
                    header = monitor.find('header', class_='Nd')
                    i = 1
                    for child in header.contents:
                        if (i > 5):
                            break
                        name = child.text
                        link = child.get('href')
                        if (link == '/'):
                            link = '{}{}football/live'.format(self.url, link)
                        else:
                            link = '{}{}live'.format(self.url, link)
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
            print(e)
            return (None)

    def select_all_available_sports(self, **kwargs):
        """
        A method used to select all available sports
        """
        if (not self.sports):
            self.set_dict_of_sports(**kwargs)
        sport_list = self.list_of_sports()
        if (sport_list == None):
            return (None)
        elif(sport_list):
            for key, value in sport_list.items():
                sport = sport_list.get(int(key))
                if (sport is None):
                    return (None)
                elif (sport):
                    self.selected_sports[int(key)] = sport
                else:
                    return (None)
            return (self.selected_sports)
        else:
            return (None)

    def select_all_available_sports2(self, **args):
        """
        A method used to select all available sports
        """
        print(args)
        if (args['online'] == 'False'):
            with open(args['file2'], 'r')as fp:
                args = {'fp': fp}
                monitor = self.init_BeautifulSoup(**args)
                print(monitor)
        elif (args['online'] == 'True'):
            for key, value in self.sports.items():
                print("{}: {}".format(key, value))
        
    
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
        
    def delete_all_monitored_sports(self, arg):
        """
        A method used to delete all monitored sports.
        """
        self.selected_sports = {}
        if (len(self.selected_sports) == 0):
            return (True)
        return (False)
    
    def get_live_games(self, kwargs):
        """
        Used to get live games of user selected sports
        """
        if (kwargs['online'] == 'False'):
            for key, value in self.selected_sports.items():
                if (int(key) == 1):
                    lt_details = {}
                    with open(kwargs.get('file'), 'r') as fp:
                        args = {'fp': fp}
                        monitor = self.init_BeautifulSoup(**args)
                        header = monitor.find('header', class_='Nd')
                        active = header.find('a', class_='isActive')
                        active = active.find('span', class_='Pd')
                        active = active.text
                        cen_content = monitor.find('div',  class_='ea', id='content-center')
                        live_games = cen_content.find('div', class_="na")
                        lt = live_games.find_all('div', class_='lb')
                        for div in lt:
                            spans = div.find_all('span')
                            name = '{} - {}'.format(spans[1].text, spans[2].text)
                            date = '{}'.format(spans[3].text)
                            lt_details[name] = {}
                            lt_details[name]['date'] = date
                            lt_details[name]['name'] = name
                            lt_details[name]['live_lt'] = {}
                            i = 1
                            for sib in div.next_siblings:
                                if sib.get('class')[0] == 'lb':
                                    # new lt
                                    break
                                else:
                                    # new live match
                                    time = sib.find('span', class_='ch Yg bh').text
                                    home = sib.find('span', class_='di').text
                                    home_score = sib.find('span', class_='gi').text
                                    away = sib.find('span', class_='ci').next.text
                                    away_score = sib.find('span', class_='hi').text
                                    lt_details[name]['live_lt'][i] = {}
                                    lt_details[name]['live_lt'][i]['time'] = time
                                    lt_details[name]['live_lt'][i]['home'] = home
                                    lt_details[name]['live_lt'][i]['home_score'] = home_score
                                    lt_details[name]['live_lt'][i]['away'] = away
                                    lt_details[name]['live_lt'][i]['away_score'] = away_score
                                i += 1
                    self.lt[active] = lt_details
                else:
                    continue
        elif (kwargs['online'] == 'True'):
            for key, value in self.selected_sports.items():
                lt_details = {}
                # url = value['link']
                url = 'https://www.livescores.com/tennis/2024-07-16/?tz=-7'
                response = requests.get(url)
                file = {'fp': response.content}
                monitor = self.init_BeautifulSoup(**file)
                header = monitor.find('header', class_='Nd')
                active = header.find('a', class_='isActive')
                active = active.find('span', class_='Pd')
                active = active.text
                cen_content = monitor.find('div',  class_='ea', id='content-center')
                live_games = cen_content.find('div', class_="na")
                lt = live_games.find_all('div', class_=re.compile('lb'))
                for div in lt:
                    spans = div.find_all('span')
                    try:
                        name = '{} - {}'.format(spans[1].text, spans[2].text)
                    except Exception as e:
                        continue
                    date = '{}'.format(spans[3].text)
                    lt_details[name] = {}
                    lt_details[name]['date'] = date
                    lt_details[name]['name'] = name
                    lt_details[name]['live_lt'] = {}
                    i = 1
                    for sib in div.next_siblings:
                        if sib.get('class')[0] == 'pa':
                            continue
                        if sib.get('class')[0] == 'lb':
                            # new lt
                            break
                        else:
                            # new live match
                            if (active == 'Football'):
                                # try:
                                #     time = sib.find('span', class_='ch Yg bh').text
                                # except Exception as e:
                                #     time = sib.find('span', class_='ch Yg').text
                                #  # time = sib.find('span', class_=('ch Yg')).text
                                try:
                                    time = sib.find('span', class_='ch Yg')
                                    time = time.text
                                except Exception as e:
                                    print(e)
                                    print(sib)
                                home = sib.find('span', class_='di').text
                                home_score = sib.find('span', class_='gi').text
                                away = sib.find('span', class_='ci').next.text
                                away_score = sib.find('span', class_='hi').text
                                lt_details[name]['live_lt'][i] = {}
                                lt_details[name]['live_lt'][i]['time'] = time
                                lt_details[name]['live_lt'][i]['home'] = home
                                lt_details[name]['live_lt'][i]['home_score'] = home_score
                                lt_details[name]['live_lt'][i]['away'] = away
                                lt_details[name]['live_lt'][i]['away_score'] = away_score
                            elif (active == 'Hockey'):
                                time = sib.find('span', class_=re.compile('ch Yg')).text
                                ht = sib.find('div', class_='Qf')
                                home = ht.text
                                away = ht.next_sibling.text
                                home_score = ''
                                away_score = ''
                                hsas = sib.find('div', class_=re.compile('Mf Nf'))
                                try:
                                    home_score += hsas.contents[0].text
                                except Exception as e:
                                    continue
                                away_score += hsas.contents[1].text
                                bt_score = sib.find('div', class_='Kf')
                                for score in bt_score.contents[0]:
                                    home_score += score.text
                                for score in bt_score.contents[1]:
                                    away_score += score.text
                                lt_details[name]['live_lt'][i] = {}
                                lt_details[name]['live_lt'][i]['time'] = time
                                lt_details[name]['live_lt'][i]['home'] = home
                                lt_details[name]['live_lt'][i]['home_score'] = home_score
                                lt_details[name]['live_lt'][i]['away'] = away
                                lt_details[name]['live_lt'][i]['away_score'] = away_score
                            elif (active == 'Basketball'):
                                # try:
                                #     time = sib.find('span', class_='ch Yg bh').text
                                # except Exception as e:
                                #     time = sib.find('span', class_='ch Yg').text
                                time = sib.find('span', class_=re.compile('ch Yg')).text
                                ht = sib.find('div', class_='Qf')
                                home = ht.text
                                away = ht.next_sibling.text
                                home_score = ''
                                away_score = ''
                                # hsas = sib.find('div', class_='Mf Nf Of')
                                hsas = sib.find('div', class_=re.compile('Mf Nf'))
                                home_score = ''
                                away_score = ''
                                try:
                                    home_score += hsas.contents[0].text
                                except Exception as e:
                                    continue
                                away_score += hsas.contents[1].text
                                bt_score = sib.find('div', class_='Kf')
                                for score in bt_score.contents[0]:
                                    home_score += score.text
                                for score in bt_score.contents[1]:
                                    away_score += score.text
                                
                                # home_score = sib.find('span', class_='gi').text
                                # away = sib.find('span', class_='ci').next.text
                                # away_score = sib.find('span', class_='hi').text
                                lt_details[name]['live_lt'][i] = {}
                                lt_details[name]['live_lt'][i]['time'] = time
                                lt_details[name]['live_lt'][i]['home'] = home
                                lt_details[name]['live_lt'][i]['home_score'] = home_score
                                lt_details[name]['live_lt'][i]['away'] = away
                                lt_details[name]['live_lt'][i]['away_score'] = away_score
                            elif (active == 'Tennis'):
                                print("Tennis")
                                try:
                                    time = sib.find('span', class_='ch Yg bh').text
                                except Exception as e:
                                    time = sib.find('span', class_='ch Yg').text
                                # home = sib.find('span', class_='di').text
                                bt = sib.find('div', class_='If Jf')
                                home = bt.contents[0].next
                                home = home.text
                                away = bt.contents[1].next
                                away = away.text
                                home_score = ''
                                away_score = ''
                                hsas = sib.find('div', class_=re.compile('Kf Jf'))
                                
                                print(time)
                                print(home)
                                print(away)
                                exit()
                                home_score = sib.find('span', class_='gi').text
                                away = sib.find('span', class_='ci').next.text
                                away_score = sib.find('span', class_='hi').text
                                lt_details[name]['live_lt'][i] = {}
                                lt_details[name]['live_lt'][i]['time'] = time
                                lt_details[name]['live_lt'][i]['home'] = home
                                lt_details[name]['live_lt'][i]['home_score'] = home_score
                                lt_details[name]['live_lt'][i]['away'] = away
                                lt_details[name]['live_lt'][i]['away_score'] = away_score
                            elif (active == 'Cricket'):
                                # try:
                                #     time = sib.find('span', class_='ch Yg bh').text
                                # except Exception as e:
                                #     time = sib.find('span', class_='ch Yg').text
                                time = sib.find('span', class_='Mh').text
                                bt = sib.find('div', class_='Nh')
                                home = bt.contents[0].text
                                away = bt.contents[1].text
                                h_s = sib.find('div', class_='Qh')
                                home_score = h_s.find('div', class_='Sh').text
                                a_s = sib.find('div', class_='Ph')
                                away_score = a_s.find('div', class_='Sh').text
                                lt_details[name]['live_lt'][i] = {}
                                lt_details[name]['live_lt'][i]['time'] = time
                                lt_details[name]['live_lt'][i]['home'] = home
                                lt_details[name]['live_lt'][i]['home_score'] = home_score
                                lt_details[name]['live_lt'][i]['away'] = away
                                lt_details[name]['live_lt'][i]['away_score'] = away_score
                        i += 1
                self.lt[active] = lt_details

        else:
            return (None)

    
    def all_lt(self, **kwargs):
        """
        A method used to get all live games leagues and tournaments
        """
        if (len(self.selected_sports) == 0):
            return (None)
        else:
            kwargs['selected_sports'] = self.selected_sports
            self.get_live_games(kwargs)
            return (self.lt)
