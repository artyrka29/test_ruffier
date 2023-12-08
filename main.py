from kivy.app import App#втановлюємо біблотеку ківі
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from instructions import *
from timer import Timer

Window.clearcolor = (.33, .69, .76, 1)
lbl_color = (1, .66, .34, 1)
btn_color = (.29, .53, .94, 1)

name = ""
age = 0
p1 = 0
p2 = 0
p3 = 0


def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False
lbl_color = (1, .25, .20, 1)

class InstrScr(Screen):#стоворюємо клас для текусту
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_instruction, color=(1, .25, .20, 1), bold=True)#добавдяемо текст і колір для нього
        lbl_name = Label(text="Ведіть ім'я фамілію:", halign='right',color=lbl_color, bold=True)#добаляємо текст і вод клавіатури
        self.input_name = TextInput(text="імя", multiline=False)#водим текст який там буде написаний спочатку
        lbl_age = Label(text="Ведіть номер карточки мами:", halign='right',color=lbl_color, bold=True)#добавдяємо текст і вод клавіатури     
        self.input_age = TextInput(text="7", multiline=False)#водим текст який там буде написаний спочатку
        self.btn = Button(text='Почати', size_hint=(.3, .2), pos_hint={'center_x':.5},bold= True, background_color=(.29, .53, .94, 1))#добавляємо кнопку почати
        self.btn.on_press = self.next

        line1 = BoxLayout(size_hint=(.8, None), height="30sp")#сторіємо лінію для тексту
        line2 = BoxLayout(size_hint=(.8, None), height="30sp")#створюємо лінію для тексту

        line1.add_widget(lbl_name)#добавляєм в текст і вод з клавіатури в лінію
        line1.add_widget(self.input_name)#

        line2.add_widget(lbl_age)#добавляєм в текст і вод з клавіатури в лінію
        line2.add_widget(self.input_age)

        main_line = BoxLayout(orientation='vertical', padding=10, spacing=10)#добавляємо в одну лінію щоб відредагувати текст і зробити проміжки
        main_line.add_widget(instr)#добавляємо instr в main_line
        main_line.add_widget(line1)#добавляємо line1 в main_line
        main_line.add_widget(line2)#добавляємо line2 в main_line
        main_line.add_widget(self.btn)#добавляємо btn в msin_line

        self.add_widget(main_line)#відображати main_line

    def next(self):
        self.manager.current = 'second'




class PulseScr(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        instr = Label(text=txt_test1, color=lbl_color, bold=True)#добавдяемо текст і колір для нього

        self.lbl_sec = Label(text="пройшло секунд: 0 ",color=lbl_color,bold=True)
        lbl_result = Label(text="Ведіть результати:", halign='right', color=lbl_color,bold=True)
        self.input_result = TextInput(text="1", multiline=False)#водим текст який там буде написаний спочатку
        self.input_result.set_disabled(True)
        self.btn = Button(text='Почати', size_hint=(.3, .2), pos_hint={'center_x':.5},bold= True, background_color=lbl_color)#добавляємо кнопку почати
        self.btn.on_press = self.next

        main_line = BoxLayout(orientation='vertical', padding=10, spacing=10)#добавляємо в одну лінію щоб відредагувати текст і зробити проміжки
        main_line.add_widget(instr)
        main_line.add_widget(self.lbl_sec)
        line = BoxLayout(size_hint=(.8,None), height="30sp")
        line.add_widget(lbl_result)
        line.add_widget(self.input_result)
        main_line.add_widget(line)
        main_line.add_widget(self.btn)

    def next(self):
        self.manager.current = 'third'



class SitsScr(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        instr = Label(text=txt_sits, color=lbl_color,bold=True)

        self.sits = Label(text="зали присід 10", color=lbl_color,bold=True)
        self.btn = Button(text='Почати', size_hint=(.3, .2), pos_hint={'center_x':.5},bold= True, background_color=lbl_color)#добавляємо кнопку почати
        self.btn.on_press = self.next
        main_line = BoxLayout(orientation='vertical', padding=10, spacing=10)#добавляємо в одну лінію щоб відредагувати текст і зробити проміжки
        main_line.add_widget(instr)
        main_line.add_widget(self.sits)
        main_line.add_widget(self.btn)

        self.add_widget(main_line)

    def next(self):
        self.manager.current = 'fourth'


class PulseScr2(Screen):
    pass
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_test3, color=lbl_color, bold=True)
        lbl_pulse = Label(text="Рахуйте пульс", color=lbl_color, bold=True)
        self.lbl_sec = Label(text="Пройшло секунд: 0", color=lbl_color, bold=True)

        lbl_result = Label(text="Результат:", halign='right', color=lbl_color, bold=True, font_size=40)
        self.input_result = TextInput(text="0", multiline=False)
        lbl_after_res = Label(text="Результат після відпочинку:", halign='right', color=lbl_color, bold=True, font_size=40)
        self.input_after_res = TextInput(text="0", multiline=False)

        self.btn = Button(text='Почати', size_hint=(.3, .4), pos_hint={'center_x': .5}, bold=True,
                          background_color=btn_color)
        self.btn.on_press = self.next

        main_line = BoxLayout(orientation='vertical', padding=10, spacing=15)
        main_line.add_widget(instr)
        main_line.add_widget(lbl_pulse)
        main_line.add_widget(self.lbl_sec)

        line1 = BoxLayout(size_hint=(.8, None), height="30sp")
        line2 = BoxLayout(size_hint=(.8, None), height="30sp")
        line1.add_widget(lbl_result)
        line1.add_widget(self.input_result)
        line2.add_widget(lbl_after_res)
        line2.add_widget(self.input_after_res)

        main_line.add_widget(line1)
        main_line.add_widget(line2)
        main_line.add_widget(self.btn)

        self.add_widget(main_line)

    def next(self):
        self.manager.current = 'fifth'


    def next(self):
        self.manager.current = 'fifth'

class ResultScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.instr = Label(text="Ваш індекс Руфʼє:-14.8")
        self.index = Label(text="Працездатність серця: висока")
        main_line = BoxLayout(orientation="vertical", size_hint=(.5, .1), pos_hint={'center_x': .5, 'center_y': .5})
        main_line.add_widget(self.instr)
        main_line.add_widget(self.index)
        self.add_widget(main_line)


class HeartCheck(App):#
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name='first'))
        sm.add_widget(PulseScr(name='second'))
        sm.add_widget(SitsScr(name='third'))
        sm.add_widget(PulseScr2(name='fourth'))
        sm.add_widget(ResultScr(name='fifth'))
        return sm
    



app = HeartCheck()#щоб коли ми писали app працював клас HeartCheck
app.run()#команда run запуску код
