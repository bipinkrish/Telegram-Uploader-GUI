import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
from tkinter import Button, Label, ttk
from tkinter import filedialog
import os
import threading
import linecache
from pyrogram import *
from pyrogram import Client
#import requests
#import time
#import telebot
#import psutil

#clientstarting
try:
    t = linecache.getline(r"info.txt", 1)
    t = t.split('\n')[0]
    ci = linecache.getline(r"info.txt", 2)
    ci = ci.split('\n')[0]
    ai = linecache.getline(r"info.txt", 3)
    ai = ai.split('\n')[0]
    ah = linecache.getline(r"info.txt", 4)
    ah = ah.split('\n')[0]

    app = Client("my_bot",api_id=ai, api_hash=ah,bot_token=t)

except:
    print("client not started")


#class
class tele:

    def run(self):
        #app = Client("my_bot")
        try:
            with app:
              app.send_message(623741973,"Started")
        except:
            pass      
        #self.tvalue = 0
        self.root.mainloop()

    def __init__(self) -> None:

        #window
        self.root = tk.Tk()
        self.frm = ttk.Frame(self.root).grid()
        self.root.title('Telegram')
        self.root.resizable(False, False)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (800/2))
        y_cordinate = int((screen_height/2) - (800/2))
        self.root.geometry("{}x{}+{}+{}".format(800, 800, x_cordinate, y_cordinate))

        #variables
        self.bottoken = tk.StringVar()
        self.apiid = tk.StringVar()
        self.apihash = tk.StringVar()
        self.chatid = tk.StringVar()

        #settingvcontent
        try:
            self.bottoken.set(t)
            self.apiid.set(ai)
            self.apihash.set(ah)
            self.chatid.set(ci)

        except:
            pass

        #entries
        self.bottokenlabel = tk.Label(self.root, text='Bot Token : ', font=('calibre', 10, 'bold'))
        self.bottokenentry = tk.Entry(self.root, textvariable=self.bottoken, font=('calibre', 10, 'normal'),width=50)
        self.apiidlabel = tk.Label(self.root, text='  API ID :', font=('calibre', 10, 'bold'))
        self.apiidentry = tk.Entry(self.root, textvariable=self.apiid, font=('calibre', 10, 'normal'),width=50)
        self.apihashlabel = tk.Label(self.root, text='API Hash :', font=('calibre', 10, 'bold'))
        self.apihashentry = tk.Entry(self.root, textvariable=self.apihash, font=('calibre', 10, 'normal'),width=50)
        self.getitatlabel = tk.Label(self.root, text='(get it at https://my.telegram.org/apps)', font=('calibre', 10))
        self.chatidlabel = tk.Label(self.root, text='Chat ID : ', font=('calibre', 10, 'bold'))
        self.chatidenentry = tk.Entry(self.root, textvariable=self.chatid, font=('calibre', 10, 'normal'),width=50)

        self.bottokenlabel.place(x=150, y=80)
        self.bottokenentry.place(x=250, y=80)
        self.apiidlabel.place(x=150, y=130)
        self.apiidentry.place(x=250, y=130)
        self.apihashlabel.place(x=150, y=180)
        self.apihashentry.place(x=250, y=180)
        self.getitatlabel.place(x=300, y=220)

        #setup
        self.set_btn = tk.Button(self.root, text='Set up',command=self.temp)
        self.set_btn.place(x=370, y=290)
        self.onlylabel = tk.Label(self.root, text='(Set Values then click Setup and Restart, \nno need to setup again untill you change values)', font=('calibre', 10))
        self.onlylabel.place(x=260, y=330)

        #chat
        self.chatidlabel.place(x=150, y=400)
        self.chatidenentry.place(x=250, y=400)

        #browsefile
        self.browfile = tk.Button(self.root, text='Select Files', command=self.browseFiles, width=8, height=1)
        self.browfile.place(x=120, y=460)

        #browsethumb
        self.browfol = tk.Button(self.root, text='Select Thumbnail', command=self.browseThumb, width=15, height=1)
        self.browfol.place(x=90, y=520)

        #optinal
        self.optinallabel = tk.Label(self.root, text='(Optional)', font=('calibre', 10))
        self.optinallabel.place(x=120, y=560)

        #bar
        self.progress = Progressbar(self.root, orient = HORIZONTAL,length = 700, mode = 'determinate')
        self.progress.place(x=50,y=640)

        #submit
        self.sub_btn = tk.Button(self.root, text='Upload',command=self.clicked)
        self.sub_btn.place(x=370, y=700)

    #updatingprogressbar
    def bar(self):
        '''time.sleep(1)
        self.root.update_idletasks()

        for ele in self.files:
            old_value = 0
            new_value = 0 
            self.progresing = True
            self.filesize = os.path.getsize(ele)
            self.pv = 0

            while self.progresing:
                new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

                if old_value:
                    self.value = new_value - old_value
                    self.tvalue = self.tvalue + self.value
                    self.pv = (self.tvalue/self.filesize) * 100
                    self.progress['value'] = int(self.pv) 
                    self.root.update_idletasks()
                    time.sleep(1)

                old_value = new_value
                if self.pv >= 99 and self.pv <=100:
                    self.progresing = False
                    self.progress['value'] = 0'''

        self.progress['value'] = int(self.statuss)
        self.root.update_idletasks()

    #calculatingprogress
    async def progresstg(self,current, total):     
        '''try:
            await app.edit_message_text(chat_id=self.mess.chat.id,message_id=self.mess.id,text=f"{current * 100 / total:.1f}%")                
        except:
            pass'''
        self.statuss = current * 100 / total
        s=threading.Thread(target=self.bar(),daemon=True)
        s.start()

    #browsefiles
    def browseFiles(self):
        try:
            self.flabel.config(text=" ")
        except:
            pass    
        self.files = filedialog.askopenfilenames(initialdir="./", title="Select a File", filetypes=(("all files", "*.*"),("zip files", "*.zip*")))
        self.flabel = tk.Label(self.root, text=self.files, font=('calibre', 10, 'bold')).place(x=250,y=463)

    #browsethumb
    def browseThumb(self):
        try:
            self.tlabel.config(text=" ")
        except:
            pass  
        self.thumb = filedialog.askopenfilename(initialdir="./", title="Select a Picture", filetypes=(("jpg file", "*.jpg*"),("png file", "*.png*")))
        self.tlabel = tk.Label(self.root, text=self.thumb, font=('calibre', 10, 'bold')).place(x=250,y=523)

    #gettingfilepaths
    def get_filepaths(self,directory):
        file_paths = []
        for root, directories, files in os.walk(directory):
            for filename in sorted(files):
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)

        return file_paths
    
    #actualmain
    def clicked(self):
        self.sub_btn.config(state= "disabled")
        self.cid = self.chatidenentry.get()

        with app:
              self.mess = app.send_message(self.cid,"Uploading") 

        #upload
        #url = f'http://localhost:8081/bot{self.token}/sendDocument?chat_id={self.cid}'
        for ele in self.files:
            filepath = ele
            print("sending file")
            try:
                #r = requests.post(url, files={"document": open(filepath, 'rb'),"thumb": open(f"{self.thumb}","rb")})
                with app:
                   app.send_document(chat_id=self.cid, document=filepath, thumb=self.thumb, progress=self.progresstg)
            except:
                #r = requests.post(url, files={"document": open(filepath, 'rb')})   
                with app:
                    app.edit_message_text(chat_id=self.mess.chat.id,message_id=self.mess.id,text="Thumbnail not Found or Selected one is Bigger\n(should be <200kb), Uploding without it")
                    #self.mess = app.send_message(self.cid,"Progress") 
                    app.send_document(chat_id=self.cid, document=filepath, progress=self.progresstg)

            #print(r.text)
            #self.tvalue = 0
            self.progress['value'] = 0
            self.sub_btn.config(state= "normal")
            self.root.update_idletasks()

    #settingnewvalues
    def temp(self):
        #getval
        self.token = self.bottokenentry.get()
        self.cid = self.chatidenentry.get()
        self.apid = self.apiidentry.get()
        self.apihas = self.apihashentry.get()

        #writetofile
        with open("info.txt","w") as file:
            info = f"{self.token}\n{self.cid}\n{self.apid}\n{self.apihas}"
            file.write(info)

        #disabling
        self.bottokenentry.config(state= "disabled")
        self.apiidentry.config(state= "disabled")
        self.apihashentry.config(state= "disabled")
        self.set_btn.config(state= "disabled")
        self.set_btn.config(text= "Restart")   
        self.sub_btn.config(state= "disabled")

    '''def setuptemp(self):

        #startthred
        if(self.flag == 0):
            self.flag = 1
            m=threading.Thread(target=self.ss,daemon=True)
            m.start()
            time.sleep(5)
            self.bottokenentry.config(state= "disabled")
            self.apiidentry.config(state= "disabled")
            self.apihashentry.config(state= "disabled")
            self.set_btn.config(state= "disabled")'''

    '''def ss(self):

        #getvalues
        self.token = self.bottokenentry.get()
        self.apid = self.apiidentry.get()
        self.apihas = self.apihashentry.get()

        #background
        bot = telebot.TeleBot(self.token)
        try:
            bot.log_out()
        except:
            pass 
        
        os.system("freeport 8081")
        cmd = "docker run -p 8081:8081 -e TELEGRAM_API_ID=11223922 -e TELEGRAM_API_HASH=ac6664c07855e0455095d970a98a082d -t riftbit/telegram-bot-api"
        print("Server Starting")
        os.system(cmd)'''


#running
t = tele()
t.run()
