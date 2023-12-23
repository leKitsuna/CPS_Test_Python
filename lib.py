from customtkinter import * # type: ignore
from tkinter import messagebox
from threading import Timer

def windowSettings(main: CTk):
    set_appearance_mode("System")
    x = ((main.winfo_screenwidth() - main.winfo_reqwidth()) / 2) - 210
    y = ((main.winfo_screenheight() - main.winfo_reqheight()) / 2) - 50
    main.geometry("500x250")
    main.wm_geometry("+%d+%d" % (x, y))
    main.title("CPS Test by leKitsuna")
    main.resizable(width=False, height=False)
    
def buttonSettings(Button: CTkButton):
    Button.configure(font=('Roboto', 18), text_color="snow", width=100, height=45, fg_color="gray7", hover_color="gray30")


class rootMenu:
    
    def __init__(self) -> None:
        
        self.count = 0
        self.timeout = 3
        
        self.windowRoot = CTk()
        windowSettings(self.windowRoot)
        
        def func_forget():
            self.label_2.configure(text=f"")
            self.button_play.place_forget()
            self.button_exit.place_forget()
            self.label.place_forget()
            
        def func_place():
            self.button_play.place(relx=0.2, rely=0.55, anchor=CENTER)
            self.button_exit.place(rely=0.75, relx=0.2, anchor=CENTER)
            self.label.place(rely=0.3, relx=0.2, anchor=CENTER)

        def quitButton():
            if messagebox.askyesno(title="Warning", message="Are you sure?"):
                self.windowRoot.destroy()
        
        def backMenu():
            self.label_2.configure(text=f"")
            self.return_button.place_forget()
            self.click_button.place_forget()
            func_place()

        def start_click_btn():
            func_forget()
            self.return_button.place(rely=0.9, relx=0.1, anchor=CENTER)
            self.click_button.place(relx=0.5, rely=0.8, anchor=CENTER)
        
        def end():
            self.label_2.configure(text=f"Time: {self.timeout} seconds\nTotal Clicks: {self.count}\nAverage CPS: {int(self.count/self.timeout)}")
            func_place()
            self.click_button.place_forget()
            self.count = 0
        
        def beginButton():
            self.count += 1
            if self.count == 1:
                self.return_button.place_forget()
                Timer(self.timeout, end).start()

        self.button_exit = CTkButton(master=self.windowRoot, text="Exit", command=quitButton)
        buttonSettings(self.button_exit)
        self.button_exit.place(rely=0.75, relx=0.2, anchor=CENTER)
        
        self.label = CTkLabel(master=self.windowRoot, text="CPS Test", font=('Roboto', 25), text_color="snow")
        self.label.place(rely=0.3, relx=0.2, anchor=CENTER)
        
        self.label_2 = CTkLabel(master=self.windowRoot, text="", font=('Roboto', 18), text_color="snow")
        self.label_2.place(relx=0.7, rely=0.5, anchor=CENTER)
        
        self.return_button = CTkButton(master=self.windowRoot, text="Return", command=backMenu)
        buttonSettings(self.return_button)
        self.return_button.configure(width=50, height=20, font=('Roboto', 18))

        self.click_button = CTkButton(master=self.windowRoot, text="CLICK!!", command=beginButton)
        buttonSettings(self.click_button)
        self.click_button.configure(width=130, height=60)
        
        self.label_cps = CTkLabel(master=self.windowRoot, font=('Roboto', 18), text="", text_color="snow")
        self.label_cps.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.button_play = CTkButton(master=self.windowRoot, text="Begin", command=start_click_btn)
        buttonSettings(self.button_play)
        self.button_play.place(relx=0.2, rely=0.55, anchor=CENTER)

        self.windowRoot.mainloop()
        pass
