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
       # Main Frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=framepadding, pady=framepadding)

        # Configure grid layout for main_frame
        self.main_frame.grid_columnconfigure((0, 1, 2), weight=1)  # 3 columns for tiles
        self.main_frame.grid_rowconfigure(2, weight=1)  # Allow tile row to expand

        # Title Label
        self.projectLabel = ctk.CTkLabel(
            self.main_frame,
            text="Projects",
            font=("Arial", 45)
        )
        self.projectLabel.grid(row=0, column=0, columnspan=3, pady=framepadding, sticky="n")

        # Entry Field
        self.CTkEntry = ctk.CTkEntry(
            self.main_frame,
            placeholder_text="Enter Project Name",
            width=reswidth / 2
        )
        self.CTkEntry.grid(row=1, column=0, columnspan=3, pady=framepadding)

        # Project Tiles (3 side-by-side)
        # Configure 3 columns and 3 rows
        for col in range(3):
            self.main_frame.grid_columnconfigure(col, weight=1)
        for row in range(3, 6):  # Assuming rows 0–2 are used for label/entry
            self.main_frame.grid_rowconfigure(row, weight=1)

        # Create 9 tiles
        for i in range(9):
            row = i // 3 + 2  # Start at row 3
            col = i % 3

            tile = ctk.CTkFrame(
                self.main_frame,
                width=reswidth / 5,
                height=resheight / 2,
                corner_radius=10
            )
            tile.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

            # Optional: Add content
            ctk.CTkLabel(tile, text=f"Project {i+1}", font=("Arial", 14)).pack(pady=5)
            ctk.CTkButton(tile, text="Launch").pack(pady=5)







    
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
        

        