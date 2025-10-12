# -*- coding: utf-8 -*-
import customtkinter as ctk
from tkinter import messagebox



class App(ctk.CTk):
    def __init__(self) -> None:

        reswidth: int = 1080
        resheight: int = 920
        framepadding: int = 3
        ctk.set_appearance_mode("dark")

        super().__init__()

        #Basic Window Setup
        self.title("Pyhton Toolbox")
        self.geometry(f"{reswidth}x{resheight}")

        #Header Frame
        self.header_frame = ctk.CTkFrame(self, height=50)
        self.header_frame.pack(fill="x", side="top", padx=framepadding, pady=framepadding)

        self.header_label = ctk.CTkLabel(self.header_frame, 
                                         text="Python Hub",
                                         font=("Arial", 24))
        self.header_label.grid(row=0,
                               column=0,
                               padx=20,
                               pady=10)
        
        #Sidebar
        self.sidebar_frame = ctk.CTkFrame(self, width=reswidth / 4.5)
        self.sidebar_frame.pack(fill="y", side="left", padx=framepadding, pady=framepadding)

        ctk.CTkButton(self.sidebar_frame, text="Home",).pack(pady=10, padx=10)
        ctk.CTkButton(self.sidebar_frame, text="Settings",).pack(pady=10, padx=10)
        ctk.CTkButton(self.sidebar_frame, text="About",).pack(pady=10, padx=10)
        ctk.CTkButton(self.sidebar_frame, text="Exit", command=self.quit).pack(pady=10, padx=10)
        self.appearnce_switch = ctk.CTkSwitch(self.sidebar_frame, text="Dark Mode", command=self.toggle_appearance)
        self.appearnce_switch.pack(pady=10, side="bottom")
        self.appearnce_switch.select()


        #Main Section
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=framepadding, pady=framepadding)
        self.projectLabel = ctk.CTkLabel(self.main_frame, text = "Projects", font=("Arial", 45))
        self.projectLabel.pack(pady=framepadding, side = "top")

        self.CTkEntry = ctk.CTkEntry(self.main_frame, placeholder_text="Enter Project Name", width=reswidth / 2)
        self.CTkEntry.pack(pady=framepadding, side=("top"))

        #Project Tile
        tile = ctk.CTkFrame(self.main_frame, corner_radius=10)
        tile.pack(pady=10, padx=10, fill="x")

        


    
    def on_button_click(self):
        print("Button clicked!")
        self.counter += 1
        self.label.configure(text=f"Button clicked {self.counter} times")
        print(self.counter)

    def toggle_appearance(self) -> None:
        if self.appearnce_switch.get() == 1:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")
        

        