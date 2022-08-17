import tkinter as tk
import datetime
import time

class Countdown(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.create_widgets()
        self.show_widgets()
        self.seconds_left=0
        self.sec=0
        self.paused = False
        self._timer_on=False

    def show_widgets(self):
        self.label.pack()
        self.entry.pack()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()
        self.pause.pack()
        self.resume.pack()

    def create_widgets(self):
        self.label=tk.Label(self,text="Enter the Time in Seconds.")
        self.entry=tk.Entry(self,justify="center")
        self.entry.focus_set()
        self.reset=tk.Button(self,text="Reset",command=self.Reset)
        self.stop=tk.Button(self,text="Stop",command=self.Stop)
        self.start=tk.Button(self,text="Start",command=self.Start)
        self.pause=tk.Button(self,text="Pause",command=self.Pause)
        self.resume=tk.Button(self,text="Resume",command=self.Resume)

    def countdown(self):
        self.label["text"]=self.convert_seconds_left_to_time()

        if self.seconds_left:
            self.seconds_left-=1
            self._timer_on=self.after(1000,self.countdown)
        else:
            self._timer_on=False

    def Reset(self):
        self.seconds_left=0
        self.stop_timer() 
        self._timer_on=False
        self.label["text"]="Enter the Time in Seconds."
        self.start.forget()
        self.stop.forget()
        self.reset.forget()
        self.pause.forget()
        self.resume.forget()
        
        self.start.pack()
        self.stop.pack()
        self.reset.pack()
        self.pause.pack()
        self.resume.pack()
        

    def Stop(self):
        self.seconds_left=int(self.entry.get())
        self.stop_timer()

    def Start(self):
        self.seconds_left=int(self.entry.get())
        self.stop_timer()
        self.countdown()
        self.start.forget()
        self.stop.forget()
        self.reset.forget()
        self.pause.forget()
        self.resume.forget()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()
        self.pause.pack()
        self.resume.pack()

        
    def Resume(self):
        self.stop_timer()
        self.countdown()
        self.start.forget()
        self.stop.forget()
        self.reset.forget()
        self.pause.forget()
        self.resume.forget()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()
        self.pause.pack()
        self.resume.pack()
        
        while self.seconds_left>0:
            if self.seconds_left>0:
                self._timer_on.countdown()
                
            else:
                self.paused=False
        time.sleep(1)

    def Pause(self):
        self.stop_timer()
        
        
    def stop_timer(self):
        if(self._timer_on):
            self.after_cancel(self._timer_on)
            self._timer_on=False
            

    def convert_seconds_left_to_time(self):
        return datetime.timedelta(seconds=self.seconds_left)

if (__name__=="__main__"):
    root=tk.Tk()
    root.resizable(False,False)
    countdown=Countdown(root)
    countdown.pack()
    root.mainloop()
        
        
