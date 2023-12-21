from customtkinter import *
from tkinter import PhotoImage, messagebox
from threading import *
from keyboard import *
from datetime import *

def windowSettings(main: Variable):
    set_appearance_mode("Dark")
    x = ((main.winfo_screenwidth() - main.winfo_reqwidth()) / 2) - 210
    y = ((main.winfo_screenheight() - main.winfo_reqheight()) / 2) - 50
    main.geometry("500x270")
    main.wm_geometry("+%d+%d" % (x, y))
    main.title("CPS Test")
    main.resizable(width=False, height=False)
    
def buttonSettings(Button: CTkButton):
    Button.configure(font=('Roboto', 18), text_color="snow", width=100, height=45, fg_color="gray7", hover_color="gray30")

class rootMenu:
    
    def __init__(self) -> None:
        
        self.count = 0
        self.timeout = 3
        
        self.windowRoot = CTk()
        windowSettings(self.windowRoot)
        
        def stop():
            Timer.cancel()
        
        def quitButton():
            if messagebox.askyesno(title="Warning", message="Are you sure?"):
                self.windowRoot.destroy()
        
        def end():
            self.label.configure(text=f"You've clicked {self.count} times in {self.timeout} seconds!")
            self.button_play.configure(text="Begin")
            self.count = 0
            
        
        def beginButton():
            self.count += 1
            if self.count == 1:
                self.button_play.configure(text="CLICK!!!")
                stop_button.place
                Timer(self.timeout, end).start()
        
        self.button_exit = CTkButton(master=self.windowRoot, text="Exit", command=quitButton)
        buttonSettings(self.button_exit)
        self.button_exit.place(rely=0.75, relx=0.5, anchor=CENTER)
        
        self.label = CTkLabel(master=self.windowRoot, text="CPS Test", font=('Roboto', 18))
        self.label.place(rely=0.3, relx=0.5, anchor=CENTER)
        
        stop_button = CTkButton(master=self.windowRoot, text="Stop", command=stop)
        buttonSettings(stop_button)
        
        self.button_play = CTkButton(master=self.windowRoot, text="Begin", command=beginButton)
        buttonSettings(self.button_play)
        self.button_play.place(relx=0.5, rely=0.55, anchor=CENTER)
        
        self.windowRoot.mainloop()
        pass
