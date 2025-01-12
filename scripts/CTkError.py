import customtkinter as ctk

class CTkError(ctk.CTkFrame):
    def __init__(self, *args, title="Error",size_x=140, size_y=90,error_message, button_1_text, button_2_text="", **kwargs):
        super().__init__(*args)
        ## Geometry and Theme Settings

        self.top_level = ctk.CTkToplevel(self)
        self.top_level.focus_set()

        print(self.winfo_screenwidth()/2 - self.winfo_width())
        print(self.winfo_screenheight()/2 - self.winfo_height())

        self.top_level.geometry(f"{size_x}x{size_y}+{int(self.winfo_screenwidth()/2 - self.winfo_width())}+{int(self.winfo_screenheight()/2 - self.winfo_height())}")
        self.top_level.title(title)
        self.top_level.resizable(False, False)

        self.columnconfigure((0,2), weight=1)
        self.rowconfigure((0,2), weight=1)

        self.Label_1 = ctk.CTkLabel(self.top_level,width=100,text=error_message,wraplength=size_x-50, justify='center')
        self.Label_1.grid(row=0,column=1, padx=30,pady=10)

        if(button_1_text and not button_2_text):
            self.Button_0 = ctk.CTkButton(self.top_level,corner_radius=20, width=100,text=button_1_text, command=lambda: self.destroy())
            self.Button_0.grid(row=1, column=1,pady=(0,10))

        if(button_2_text):
            self.Button_0 = ctk.CTkButton(self.top_level,corner_radius=20, width=100,text=button_1_text, command=lambda: self.destroy())
            self.Button_0.grid(row=1, column=0,pady=(0,20))

            self.Button_0 = ctk.CTkButton(self.top_level,corner_radius=20,text=button_2_text, command=lambda: self.destroy())
            self.Button_0.grid(row=1, column=2)

        self.top_level.attributes('-topmost', True)