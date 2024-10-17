import customtkinter as ctk
from color_theme import get_palette

# Interface init
app = ctk.CTk()
app.title("D-HIVE")
app.attributes('-fullscreen', True)

# Color theme init
ctk.set_appearance_mode('dark')
colors = get_palette()

app.mainloop()
