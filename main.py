import pip as p
import sys as s

def pack_check(pack:str):
    try:
        __import__(pack)
    except ImportError:
        p.main(['install', pack])

[pack_check(x) for x in ['tkinter','customtkinter','datetime']]

import customtkinter as customtkinter
from datetime import datetime as datetime

class App:
    def __init__(self) -> None:
        self.app = customtkinter.CTk()
        self.app.geometry('400x240')
        self.app.resizable(False, False)
        self.app.attributes('-topmost', True)

        self.time_label = customtkinter.CTkLabel(master=self.app, font=('Arial', 24, 'bold'))
        self.banner_label = customtkinter.CTkLabel(master=self.app, text='Time Left in the Day.', font=('Arial', 14, 'normal'))
        self.percentage_label = customtkinter.CTkLabel(master=self.app, font=('Arial', 14, 'bold'))
        self.progress_bar = customtkinter.CTkProgressBar(master=self.app)
        
        self.time_label.pack(padx=20, pady=(30, 5))
        self.banner_label.pack(padx=20, pady=0)
        self.percentage_label.pack(padx=20, pady=(45, 5))
        self.progress_bar.pack(padx=20, pady=0)

        self.update()
        self.app.mainloop()

    def update(self):
        now = datetime.now()
        difference = 24 - (now.hour + now.minute/60 + now.second / 60**2)
        hours = int(difference)
        minutes = int((difference - hours) * 60)
        self.time_label.configure(text=f'{hours:02}:{minutes:02}')
        self.percentage_label.configure(text=f'{(difference / 24 * 100):.1f}% Remaining.')
        self.progress_bar.set(difference/24)

        self.app.after(55000, self.update)



if __name__ == '__main__':
    customtkinter.set_appearance_mode("System")
    color = 'blue'
    if len(s.argv) > 1:
        color = s.argv[1]
    try:
        color = 'green' if color == 'g' else color
        color = 'blue' if color == 'b' else color
        color = 'dark-blue' if color == 'db' else color
        customtkinter.set_default_color_theme(color)
    except:
        customtkinter.set_default_color_theme('blue')

    app = App()