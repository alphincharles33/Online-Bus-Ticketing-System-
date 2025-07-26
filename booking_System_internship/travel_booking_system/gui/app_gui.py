# app_gui.py
import sys
import os

# Add the 'travel_booking_system' folder to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tkinter import *
from tkinter import messagebox, ttk
from utils.database import create_transaction_table, insert_transaction
from utils.speech_recognition import recognize_speech
from utils.text_to_speech import text_to_speech
from utils.price_calculator import calculate_price
from utils.qr_generator import generate_qr_code
from utils.travel_history import display_travel_data

# Set up the Tkinter window and widgets
root = Tk()
root.title("Travel Price Calculator")
root.geometry("1800x900")
root.configure(background='lightblue')

# Set up the rest of your GUI logic (widgets, buttons, etc.)

root.mainloop()
