#          IMPORTS           #
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse, Line, Rectangle, Canvas
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
import random
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
import json


with open('datas/data.txt') as f:
  final = json.load(f)

with open('datas/types.txt') as f:
  types = json.load(f)

with open('datas/Public_Service.txt') as f:
  ps = json.load(f)

with open('datas/RetailandFood.txt') as f:
  retail = json.load(f)

with open('datas/BandF.txt') as f:
  bandf = json.load(f)

with open('datas/Manufacturing.txt') as f:
  manufac = json.load(f)

with open('datas/Other.txt') as f:
  other = json.load(f)



#Window.size = 800,900


class ScreenOne(Screen):
    def __init__(self, **kwargs):
        super(ScreenOne, self).__init__(**kwargs)
        Clock.schedule_once(self._finish_init)


    def _finish_init(self, dt):
        print(self.ids)
        self.wid, self.hei = Window.size
        with self.canvas.before:

            Color(rgb=(1,1,1))
            self.el1 = Ellipse(size=(200,200), pos=((self.wid/2)-100,(self.hei/2)-100),angle_start = 0,angle_end = 120,source = 'logog.png')
            #Color(rgb=(0.95,0.95,0.95))
            Color(rgb=(0,0,0))
            self.el3 = Ellipse(size=(180, 180), pos=((self.wid / 2) - 90, (self.hei / 2) - 90), angle_start=0,angle_end=360)
            Color(rgb=(1,1,1))

            self.el2 = Ellipse(size=(160,160), pos=((self.wid/2)-80,(self.hei/2)-80),angle_start = 0,angle_end = 360,source='log.png')
        #Clock.schedule_once(self.loading)
        print(self.ids)
        self.count = 0
        self.ev = Clock.schedule_interval(self.spin,0.05)

    def spin(self,dt):
        self.count += 1
        self.el1.angle_start = self.el1.angle_start + 10
        self.el1.angle_end = self.el1.angle_start + 90
        if self.count >= 15:
            self.manager.current = 'screen2'

            self.ev.cancel()

class ScreenTwo(Screen):
    def __init__(self, **kwargs):
        super(ScreenTwo, self).__init__(**kwargs)
        Clock.schedule_once(self._finisher)


    def _finisher(self,dt):
        pass



    def testps(self):
        self.manager.current = 'PublicService'
    def testrnf(self):
        self.manager.current = 'Retailnfood'

    def testmanu(self):
        self.manager.current = 'Manufacturing'

    def testbank(self):
        self.manager.current = 'Banking'
    def testother(self):
        self.manager.current = 'Other'

class PublicService(Screen):
    def __init__(self, **kwargs):
        super(PublicService, self).__init__(**kwargs)

        self.page = 0
        self.totallist = []
        for each in ps:
            self.totallist.append(each)
        Clock.schedule_once(self.finish)


    def finish(self,dt):
        self.ids.boxy.clear_widgets()
        if len(self.totallist) > 20:
            for x in range(self.page *10,(self.page+2)*10):
                self.blay = BoxLayout(size_hint_x=1,orientation='vertical')
                self.title =  Label(text=f"{self.totallist[x]['name']}",color=(0,0,0,1),font_size=round((len(self.totallist[x]['name'])*-1)/12)+25,pos_hint={'center_x':0.5,'y':0},outline_color=(1,0,0))
                self.desc =   Label(text=f"{self.totallist[x]['description']}",   color=(0,0,0,1),font_size=15,pos_hint={'center_x':0.5})
                self.phonen = Label(text=f"{self.totallist[x]['phone']}",         color=(0,0,0,1),font_size=18,pos_hint={'center_x':0.5})
                self.b = Button(size_hint=(0.3,0.3), text=f'More Information',pos_hint={'center_x':0.5})



                self.blay.add_widget(self.title)
                self.blay.add_widget(self.desc)
                self.blay.add_widget(self.phonen)
                self.blay.add_widget(self.b)

                self.ids.boxy.add_widget(self.blay)
            self.ids.boxy.bind(minimum_height=self.ids.boxy.setter('height'))

        else:
            for each in self.totallist:
                self.blay = BoxLayout(size_hint_x=1, orientation='vertical')
                self.title = Label(text=f"{each['name']}", color=(0, 0, 0),
                                   font_size=round((len(each['name']) * -1) / 12) + 25,
                                   pos_hint={'center_x': 0.5, 'y': 0}, outline_color=(1, 0, 0))
                self.desc = Label(text=f"{each['description']}", color=(0, 0, 0), font_size=15,
                                  pos_hint={'center_x': 0.5})
                self.phonen = Label(text=f"{each['phone']}", color=(0, 0, 0), font_size=18,
                                    pos_hint={'center_x': 0.5})
                self.b = Button(size_hint=(0.3, 0.3), text=f'More Information', pos_hint={'center_x': 0.5})

                self.blay.add_widget(self.title)
                self.blay.add_widget(self.desc)
                self.blay.add_widget(self.phonen)
                self.blay.add_widget(self.b)

                self.ids.boxy.add_widget(self.blay)
            self.ids.boxy.bind(minimum_height=self.ids.boxy.setter('height'))

    def next(self):
        if self.page < ((len(self.totallist)/20  )):
            self.ids.boxy.clear_widgets()
            self.page += 1
            Clock.schedule_once(self.finish)
        print(self.page)
    def prev(self):
        if self.page > 0:
            self.ids.boxy.clear_widgets()
            self.page -= 1
            Clock.schedule_once(self.finish)

    def tester2(self):
        text = self.ids.choser.text
        self.page = 0
        self.totallist = []
        for each in ps:
            if each['title'] == text:
                self.totallist.append(each)
        Clock.schedule_once(self.finish)
        print(len(self.totallist))

    def searcher(self):
        if self.ids.searchbar.text != "":
            self.totallist = []
            self.ids.boxy.clear_widgets()
            self.searchtxt = str(self.ids.searchbar.text).lower()
            self.searchcounter = 0
            for each in ps:
                if self.searchtxt in str(each['name']).lower():
                    self.blay = BoxLayout(size_hint_x=1, orientation='vertical')
                    self.title = Label(text=f"{each['name']}", color=(0, 0, 0),
                                       font_size=round((len(each['name']) * -1) / 12) + 25,
                                       pos_hint={'center_x': 0.5, 'y': 0}, outline_color=(1, 0, 0))
                    self.desc = Label(text=f"{each['description']}", color=(0, 0, 0), font_size=15,
                                      pos_hint={'center_x': 0.5})
                    self.phonen = Label(text=f"{each['phone']}", color=(0, 0, 0), font_size=18,
                                        pos_hint={'center_x': 0.5})
                    self.b = Button(size_hint=(0.3, 0.3), text=f'More Information', pos_hint={'center_x': 0.5})

                    self.blay.add_widget(self.title)
                    self.blay.add_widget(self.desc)
                    self.blay.add_widget(self.phonen)
                    self.blay.add_widget(self.b)

                    self.ids.boxy.add_widget(self.blay)
                    self.searchcounter += 1
                self.ids.boxy.bind(minimum_height=self.ids.boxy.setter('height'))


            if self.searchcounter == 0:
                self.blay = FloatLayout(size_hint_x=1)
                labe = Label(text=f"No Results Available!", pos_hint={'center_x': 0.5, 'center_y': .5}, color=(0, 0, 0),
                             font_size=40)
                self.blay.add_widget(labe)
                self.ids.boxy.add_widget(self.blay)

                print('NONE!!!')
                self.ids.boxy.bind(minimum_height=self.ids.boxy.setter('height'))

class Retailnfood(Screen):
    def __init__(self, **kwargs):
        super(Retailnfood, self).__init__(**kwargs)

        self.page = 0
        self.totallist = []
        for each in retail:
            self.totallist.append(each)
        Clock.schedule_once(self.finish)


    def finish(self,dt):
        self.ids.boxy.clear_widgets()
        if len(self.totallist) > 20:
            for x in range(self.page *10,(self.page+2)*10):
                self.blay = BoxLayout(size_hint_x=1,orientation='vertical')
                self.title =  Label(text=f"{self.totallist[x]['name']}",color=(0,0,0),font_size=round((len(self.totallist[x]['name'])*-1)/12)+25,pos_hint={'center_x':0.5,'y':0},outline_color=(1,0,0))
                self.desc =   Label(text=f"{self.totallist[x]['description']}",   color=(0,0,0),font_size=15,pos_hint={'center_x':0.5})
                self.phonen = Label(text=f"{self.totallist[x]['phone']}",         color=(0,0,0),font_size=18,pos_hint={'center_x':0.5})
                self.b = Button(size_hint=(0.3,0.3), text=f'More Information',pos_hint={'center_x':0.5})



                self.blay.add_widget(self.title)
                self.blay.add_widget(self.desc)
                self.blay.add_widget(self.phonen)
                self.blay.add_widget(self.b)

                self.ids.boxy.add_widget(self.blay)
            self.ids.boxy.bind(minimum_height=self.ids.boxy.setter('height'))

        else:
            for each in self.totallist:
                self.blay = BoxLayout(size_hint_x=1, orientation='vertical')
                self.title = Label(text=f"{each['name']}", color=(0, 0, 0),
                                   font_size=round((len(each['name']) * -1) / 12) + 25,
                                   pos_hint={'center_x': 0.5, 'y': 0}, outline_color=(1, 0, 0))
                self.desc = Label(text=f"{each['description']}", color=(0, 0, 0), font_size=15,
                                  pos_hint={'center_x': 0.5})
                self.phonen = Label(text=f"{each['phone']}", color=(0, 0, 0), font_size=18,
                                    pos_hint={'center_x': 0.5})
                self.b = Button(size_hint=(0.3, 0.3), text=f'More Information', pos_hint={'center_x': 0.5})

                self.blay.add_widget(self.title)
                self.blay.add_widget(self.desc)
                self.blay.add_widget(self.phonen)
                self.blay.add_widget(self.b)

                self.ids.boxy.add_widget(self.blay)
            self.ids.boxy.bind(minimum_height=self.ids.boxy.setter('height'))

    def next(self):
        if self.page < ((len(self.totallist)/20  )):
            self.ids.boxy.clear_widgets()
            self.page += 1
            Clock.schedule_once(self.finish)
        print(self.page)
    def prev(self):
        if self.page > 0:
            self.ids.boxy.clear_widgets()
            self.page -= 1
            Clock.schedule_once(self.finish)

    def tester2(self):
        text = self.ids.choser.text
        self.page = 0
        self.totallist = []
        for each in retail:
            if each['title'] == text:
                self.totallist.append(each)
        Clock.schedule_once(self.finish)
        print(len(self.totallist))

    def searcher(self):
        if self.ids.searchbar.text != "":
            self.totallist = []
            self.ids.boxy.clear_widgets()
            self.searchtxt = str(self.ids.searchbar.text).lower()
            self.searchcounter = 0
            for each in retail:
                if self.searchtxt in str(each['name']).lower():
                    self.blay = BoxLayout(size_hint_x=1, orientation='vertical')
                    self.title = Label(text=f"{each['name']}", color=(0, 0, 0),
                                       font_size=round((len(each['name']) * -1) / 12) + 25,
                                       pos_hint={'center_x': 0.5, 'y': 0}, outline_color=(1, 0, 0))
                    self.desc = Label(text=f"{each['description']}", color=(0, 0, 0), font_size=15,
                                      pos_hint={'center_x': 0.5})
                    self.phonen = Label(text=f"{each['phone']}", color=(0, 0, 0), font_size=18,
                                        pos_hint={'center_x': 0.5})
                    self.b = Button(size_hint=(0.3, 0.3), text=f'More Information', pos_hint={'center_x': 0.5})

                    self.blay.add_widget(self.title)
                    self.blay.add_widget(self.desc)
                    self.blay.add_widget(self.phonen)
                    self.blay.add_widget(self.b)

                    self.ids.boxy.add_widget(self.blay)
                    self.searchcounter += 1
                self.ids.boxy.bind(minimum_height=self.ids.boxy.setter('height'))


            if self.searchcounter == 0:
                self.blay = FloatLayout(size_hint_x=1)
                labe = Label(text=f"No Results Available!", pos_hint={'center_x': 0.5, 'center_y': .5}, color=(0, 0, 0),
                             font_size=40)
                self.blay.add_widget(labe)
                self.ids.boxy.add_widget(self.blay)

                print('NONE!!!')
                self.ids.boxy.bind(minimum_height=self.ids.boxy.setter('height'))

class Manufacturing(Screen):
    def __init__(self, **kwargs):
        super(Manufacturing, self).__init__(**kwargs)

        self.page = 0
        self.totallist = []
        for each in manufac:
            self.totallist.append(each)
        Clock.schedule_once(self.finish)


    def finish(self,dt):
        self.ids.boxy.clear_widgets()
        if len(self.totallist) > 20:
            for x in range(self.page *10,(self.page+2)*10):
                self.blay = BoxLayout(size_hint_x=1,orientation='vertical')
                self.title =  Label(text=f"{self.totallist[x]['name']}",color=(0,0,0),font_size=round((len(self.totallist[x]['name'])*-1)/12)+25,pos_hint={'center_x':0.5,'y':0},outline_color=(1,0,0))
                self.desc =   Label(text=f"{self.totallist[x]['description']}",   color=(0,0,0),font_size=15,pos_hint={'center_x':0.5})
                self.phonen = Label(text=f"{self.totallist[x]['phone']}",         color=(0,0,0),font_size=18,pos_hint={'center_x':0.5})
                self.b = Button(size_hint=(0.3,0.3), text=f'More Information',pos_hint={'center_x':0.5})



                self.blay.add_widget(self.title)
                self.blay.add_widget(self.desc)
                self.blay.add_widget(self.phonen)
                self.blay.add_widget(self.b)

                self.ids.boxy.add_widget(self.blay)
            self.ids.boxy.bind(minimum_height=self.ids.boxy.setter('height'))

        else:
            for each in self.totallist:
                self.blay = BoxLayout(size_hint_x=1, orientation='vertical')
                self.title = Label(text=f"{each['name']}", color=(0, 0, 0),
                                   font_size=round((len(each['name']) * -1) / 12) + 25,
                                   pos_hint={'center_x': 0.5, 'y': 0}, outline_color=(1, 0, 0))
                self.desc = Label(text=f"{each['description']}", color=(0, 0, 0), font_size=15,
                                  pos_hint={'center_x': 0.5})
                self.phonen = Label(text=f"{each['phone']}", color=(0, 0, 0), font_size=18,
                                    pos_hint={'center_x': 0.5})
                self.b = Button(size_hint=(0.3, 0.3), text=f'More Information', pos_hint={'center_x': 0.5})

                self.blay.add_widget(self.title)
                self.blay.add_widget(self.desc)
                self.blay.add_widget(self.phonen)
                self.blay.add_widget(self.b)

                self.ids.boxy.add_widget(self.blay)
            self.ids.boxy.bind(minimum_height=self.ids.boxy.setter('height'))

    def next(self):
        if self.page < ((len(self.totallist)/20  )):
            self.ids.boxy.clear_widgets()
            self.page += 1
            Clock.schedule_once(self.finish)
        print(self.page)
    def prev(self):
        if self.page > 0:
            self.ids.boxy.clear_widgets()
            self.page -= 1
            Clock.schedule_once(self.finish)

    def tester2(self):
        text = self.ids.choser.text
        print(text)
        self.page = 0
        self.totallist = []
        for each in manufac:
            if each['title'] == text:
                self.totallist.append(each)
        Clock.schedule_once(self.finish)
        print(len(self.totallist))

    def searcher(self):
        if self.ids.searchbar.text != "":
            self.totallist = []
            self.ids.boxy.clear_widgets()
            self.searchtxt = str(self.ids.searchbar.text).lower()
            self.searchcounter = 0
            for each in manufac:
                if self.searchtxt in str(each['name']).lower():
                    self.blay = BoxLayout(size_hint_x=1, orientation='vertical')
                    self.title = Label(text=f"{each['name']}", color=(0, 0, 0),
                                       font_size=round((len(each['name']) * -1) / 12) + 25,
                                       pos_hint={'center_x': 0.5, 'y': 0}, outline_color=(1, 0, 0))
                    self.desc = Label(text=f"{each['description']}", color=(0, 0, 0), font_size=15,
                                      pos_hint={'center_x': 0.5})
                    self.phonen = Label(text=f"{each['phone']}", color=(0, 0, 0), font_size=18,
                                        pos_hint={'center_x': 0.5})
                    self.b = Button(size_hint=(0.3, 0.3), text=f'More Information', pos_hint={'center_x': 0.5})

                    self.blay.add_widget(self.title)
                    self.blay.add_widget(self.desc)
                    self.blay.add_widget(self.phonen)
                    self.blay.add_widget(self.b)

                    self.ids.boxy.add_widget(self.blay)
                    self.searchcounter += 1
                self.ids.boxy.bind(minimum_height=self.ids.boxy.setter('height'))


            if self.searchcounter == 0:
                self.blay = FloatLayout(size_hint_x=1)
                labe = Label(text=f"No Results Available!", pos_hint={'center_x': 0.5, 'center_y': .5}, color=(0, 0, 0),
                             font_size=40)
                self.blay.add_widget(labe)
                self.ids.boxy.add_widget(self.blay)

                print('NONE!!!')
                self.ids.boxy.bind(minimum_height=self.ids.boxy.setter('height'))

class Banking(Screen):
    def __init__(self, **kwargs):
        super(Banking, self).__init__(**kwargs)

        self.page = 0
        self.totallist = []
        for each in bandf:
            self.totallist.append(each)
        Clock.schedule_once(self.finish)


    def finish(self,dt):
        self.ids.boxy.clear_widgets()
        if len(self.totallist) > 20:
            for x in range(self.page *10,(self.page+2)*10):
                self.blay = BoxLayout(size_hint_x=1,orientation='vertical')
                self.title =  Label(text=f"{self.totallist[x]['name']}",color=(0,0,0),font_size=round((len(self.totallist[x]['name'])*-1)/12)+25,pos_hint={'center_x':0.5,'y':0},outline_color=(1,0,0))
                self.desc =   Label(text=f"{self.totallist[x]['description']}",   color=(0,0,0),font_size=15,pos_hint={'center_x':0.5})
                self.phonen = Label(text=f"{self.totallist[x]['phone']}",         color=(0,0,0),font_size=18,pos_hint={'center_x':0.5})
                self.b = Button(size_hint=(0.3,0.3), text=f'More Information',pos_hint={'center_x':0.5})



                self.blay.add_widget(self.title)
                self.blay.add_widget(self.desc)
                self.blay.add_widget(self.phonen)
                self.blay.add_widget(self.b)

                self.ids.boxy.add_widget(self.blay)
            self.ids.boxy.bind(minimum_height=self.ids.boxy.setter('height'))

        else:
            for each in self.totallist:
                self.blay = BoxLayout(size_hint_x=1, orientation='vertical')
                self.title = Label(text=f"{each['name']}", color=(0, 0, 0),
                                   font_size=round((len(each['name']) * -1) / 12) + 25,
                                   pos_hint={'center_x': 0.5, 'y': 0}, outline_color=(1, 0, 0))
                self.desc = Label(text=f"{each['description']}", color=(0, 0, 0), font_size=15,
                                  pos_hint={'center_x': 0.5})
                self.phonen = Label(text=f"{each['phone']}", color=(0, 0, 0), font_size=18,
                                    pos_hint={'center_x': 0.5})
                self.b = Button(size_hint=(0.3, 0.3), text=f'More Information', pos_hint={'center_x': 0.5})

                self.blay.add_widget(self.title)
                self.blay.add_widget(self.desc)
                self.blay.add_widget(self.phonen)
                self.blay.add_widget(self.b)

                self.ids.boxy.add_widget(self.blay)
            self.ids.boxy.bind(minimum_height=self.ids.boxy.setter('height'))

    def next(self):
        if self.page < ((len(self.totallist)/20  )):
            self.ids.boxy.clear_widgets()
            self.page += 1
            Clock.schedule_once(self.finish)
        print(self.page)
    def prev(self):
        if self.page > 0:
            self.ids.boxy.clear_widgets()
            self.page -= 1
            Clock.schedule_once(self.finish)

    def tester2(self):
        text = self.ids.choser.text
        print(text)
        self.page = 0
        self.totallist = []
        for each in bandf:
            if each['title'] == text:
                self.totallist.append(each)
        Clock.schedule_once(self.finish)
        print(len(self.totallist))

    def searcher(self):
        if self.ids.searchbar.text != "":
            self.totallist = []
            self.ids.boxy.clear_widgets()
            self.searchtxt = str(self.ids.searchbar.text).lower()
            self.searchcounter = 0
            for each in bandf:
                if self.searchtxt in str(each['name']).lower():
                    self.blay = BoxLayout(size_hint_x=1, orientation='vertical')
                    self.title = Label(text=f"{each['name']}", color=(0, 0, 0),
                                       font_size=round((len(each['name']) * -1) / 12) + 25,
                                       pos_hint={'center_x': 0.5, 'y': 0}, outline_color=(1, 0, 0))
                    self.desc = Label(text=f"{each['description']}", color=(0, 0, 0), font_size=15,
                                      pos_hint={'center_x': 0.5})
                    self.phonen = Label(text=f"{each['phone']}", color=(0, 0, 0), font_size=18,
                                        pos_hint={'center_x': 0.5})
                    self.b = Button(size_hint=(0.3, 0.3), text=f'More Information', pos_hint={'center_x': 0.5})

                    self.blay.add_widget(self.title)
                    self.blay.add_widget(self.desc)
                    self.blay.add_widget(self.phonen)
                    self.blay.add_widget(self.b)

                    self.ids.boxy.add_widget(self.blay)
                    self.searchcounter += 1
                self.ids.boxy.bind(minimum_height=self.ids.boxy.setter('height'))


            if self.searchcounter == 0:
                self.blay = FloatLayout(size_hint_x=1)
                labe = Label(text=f"No Results Available!", pos_hint={'center_x': 0.5, 'center_y': .5}, color=(0, 0, 0),
                             font_size=40)
                self.blay.add_widget(labe)
                self.ids.boxy.add_widget(self.blay)

                print('NONE!!!')
                self.ids.boxy.bind(minimum_height=self.ids.boxy.setter('height'))

class Other(Screen):
    def __init__(self, **kwargs):
        super(Other, self).__init__(**kwargs)

        self.page = 0
        self.totallist = []
        for each in other:
            self.totallist.append(each)
        Clock.schedule_once(self.finish)


    def finish(self,dt):
        self.ids.boxy.clear_widgets()
        if len(self.totallist) > 20:
            for x in range(self.page *10,(self.page+2)*10):
                self.blay = BoxLayout(size_hint_x=1,orientation='vertical')
                self.title =  Label(text=f"{self.totallist[x]['name']}",color=(0,0,0),font_size=round((len(self.totallist[x]['name'])*-1)/12)+25,pos_hint={'center_x':0.5,'y':0},outline_color=(1,0,0))
                self.desc =   Label(text=f"{self.totallist[x]['description']}",   color=(0,0,0),font_size=15,pos_hint={'center_x':0.5})
                self.phonen = Label(text=f"{self.totallist[x]['phone']}",         color=(0,0,0),font_size=18,pos_hint={'center_x':0.5})
                self.b = Button(size_hint=(0.3,0.3), text=f'More Information',pos_hint={'center_x':0.5})



                self.blay.add_widget(self.title)
                self.blay.add_widget(self.desc)
                self.blay.add_widget(self.phonen)
                self.blay.add_widget(self.b)

                self.ids.boxy.add_widget(self.blay)
            self.ids.boxy.bind(minimum_height=self.ids.boxy.setter('height'))

        else:
            for each in self.totallist:
                self.blay = BoxLayout(size_hint_x=1, orientation='vertical')
                self.title = Label(text=f"{each['name']}", color=(0, 0, 0),
                                   font_size=round((len(each['name']) * -1) / 12) + 25,
                                   pos_hint={'center_x': 0.5, 'y': 0}, outline_color=(1, 0, 0))
                self.desc = Label(text=f"{each['description']}", color=(0, 0, 0), font_size=15,
                                  pos_hint={'center_x': 0.5})
                self.phonen = Label(text=f"{each['phone']}", color=(0, 0, 0), font_size=18,
                                    pos_hint={'center_x': 0.5})
                self.b = Button(size_hint=(0.3, 0.3), text=f'More Information', pos_hint={'center_x': 0.5})

                self.blay.add_widget(self.title)
                self.blay.add_widget(self.desc)
                self.blay.add_widget(self.phonen)
                self.blay.add_widget(self.b)

                self.ids.boxy.add_widget(self.blay)
            self.ids.boxy.bind(minimum_height=self.ids.boxy.setter('height'))

    def next(self):
        if self.page < ((len(self.totallist)/20  )):
            self.ids.boxy.clear_widgets()
            self.page += 1
            Clock.schedule_once(self.finish)
        print(self.page)
    def prev(self):
        if self.page > 0:
            self.ids.boxy.clear_widgets()
            self.page -= 1
            Clock.schedule_once(self.finish)

    def tester2(self):
        text = self.ids.choser.text
        print(text)
        self.page = 0
        self.totallist = []
        for each in other:
            if each['title'] == text:
                self.totallist.append(each)
        Clock.schedule_once(self.finish)
        print(len(self.totallist))

    def searcher(self):
        if self.ids.searchbar.text != "":
            self.totallist = []
            self.ids.boxy.clear_widgets()
            self.searchtxt = str(self.ids.searchbar.text).lower()
            self.searchcounter = 0
            for each in other:
                if self.searchtxt in str(each['name']).lower():
                    self.blay = BoxLayout(size_hint_x=1, orientation='vertical')
                    self.title = Label(text=f"{each['name']}", color=(0, 0, 0),
                                       font_size=round((len(each['name']) * -1) / 12) + 25,
                                       pos_hint={'center_x': 0.5, 'y': 0}, outline_color=(1, 0, 0))
                    self.desc = Label(text=f"{each['description']}", color=(0, 0, 0), font_size=15,
                                      pos_hint={'center_x': 0.5})
                    self.phonen = Label(text=f"{each['phone']}", color=(0, 0, 0), font_size=18,
                                        pos_hint={'center_x': 0.5})
                    self.b = Button(size_hint=(0.3, 0.3), text=f'More Information', pos_hint={'center_x': 0.5})

                    self.blay.add_widget(self.title)
                    self.blay.add_widget(self.desc)
                    self.blay.add_widget(self.phonen)
                    self.blay.add_widget(self.b)

                    self.ids.boxy.add_widget(self.blay)
                    self.searchcounter += 1
                self.ids.boxy.bind(minimum_height=self.ids.boxy.setter('height'))


            if self.searchcounter == 0:
                self.blay = FloatLayout(size_hint_x=1)
                labe = Label(text=f"No Results Available!", pos_hint={'center_x': 0.5, 'center_y': .5}, color=(0, 0, 0),
                             font_size=40)
                self.blay.add_widget(labe)
                self.ids.boxy.add_widget(self.blay)

                print('NONE!!!')
                self.ids.boxy.bind(minimum_height=self.ids.boxy.setter('height'))



class Manager(ScreenManager):
    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    publicservice = ObjectProperty(None)
    retailnfood = ObjectProperty(None)
    manufacturing = ObjectProperty(None)
    banking = ObjectProperty(None)
    other = ObjectProperty(None)
class localbizapp(App):
    def build(self):
        return Manager()


if __name__ == "__main__":
    localbizapp().run()