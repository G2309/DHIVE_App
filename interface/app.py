import customtkinter as ctk
from color_theme import get_palette
from tabs import create_tabs
from layout import create_layout

# Interface init
app = ctk.CTk()
app.title("D-HIVE")
app.attributes('-fullscreen', True)

# Color theme init
ctk.set_appearance_mode('dark')
colors = get_palette()

# App configuration
app.configure(
        fg_color=colors["base"]
        )

tabs = create_tabs(app, colors)
tabs.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

create_layout(app, colors)

app.mainloop()
