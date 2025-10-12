# -*- coding: utf-8 -*-
import customtkinter as ctk
from tkinter import messagebox


class App(ctk.CTk):
    def __init__(self) -> None:

        reswidth: int = 1080
        resheight: int = 920

        super().__init__()

        #Basic Window Setup
        self.title("CustomTkinter Example")
        self.geometry(f"{reswidth}x{resheight}")

        #Header Frame
        self.header_frame = ctk.CTkFrame(self, height=50)
        self.header_frame.pack(fill="x", pady=10)

        self.header_label = ctk.CTkLabel(self.header_frame, 
                                         text="Python Hub",
                                         font=("Arial", 24))
        self.header_label.grid(row=0,
                               column=0,
                               padx=20,
                               pady=10)
        
        #Sidebar
        self.sidebar_frame = ctk.CTkFrame(self, width=reswidth / 4.5)
        
        self.sidebar_frame.pack(fill="y", side="left", padx=10, pady=10)


        #Main Section
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.label = ctk.CTkLabel(self.main_frame,
                                text = "Click the button below:")
        self.label.pack(pady=10)
        self.label = ctk.CTkLabel(self.main_frame,
                                text = "My Name is Connor:")
        self.label.pack(pady=10)

        self.button = ctk.CTkButton(self.main_frame,
                                    text="Click Me",
                                    command=self.on_button_click)
        self.button.pack(pady=10)

        self.counter = 0

        self.label = ctk.CTkLabel(self.main_frame,
                                  text=f"Button clicked {self.counter} times")
        self.label.pack(pady=10)
    
    def on_button_click(self):
        print("Button clicked!")
        self.counter += 1
        self.label.configure(text=f"Button clicked {self.counter} times")
        print(self.counter)

        