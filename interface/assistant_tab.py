import customtkinter as ctk

def setup_assistant_tab(tab, colors):
    """
    Sets up layout and funct. for the 'Auxiliares' tab.
    """
    # Create left/right frames
    # Left frame =  user options
    # Right frame = input
    left_frame = ctk.CTkFrame(tab, width=500, fg_color=colors["base"])
    left_frame.grid(row=0, column=0, padx=10, pady=20, sticky="ns")

    right_frame = ctk.CTkFrame(tab, fg_color=colors["mantle"])
    
