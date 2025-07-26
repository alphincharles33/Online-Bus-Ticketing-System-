# travel booking system
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pyaudio
import speech_recognition as sr
import pyttsx3
import time

from PIL import Image, ImageTk
import qrcode
import os
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
from word2number import w2n

# Create a connection to the database
conn = sqlite3.connect('transactions1.db')
# Create a cursor object
c = conn.cursor()
# Create a table to store the transaction data
c.execute("""CREATE TABLE IF NOT EXISTS transactions12 (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            destination TEXT,
            quantity varchar,
            price REAL,
            timestamp TEXT
            )""")

# Commit the changes
conn.commit()

# Initialize the speech recognition engine
r = sr.Recognizer()
m=sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Create a dictionary to store the prices of traveling from one place to another
prices = {
    "Karwar": {"Karwar": 200, "Ankola": 150, "Mysore": 100},
    "Ankola": {"Bangalore": 200, "Ankola": 180, "Mysore": 120},
    "Bangalore": {"Bangalore": 150, "Karwar": 180, "Mysore": 80},
    "Mysore": {"Mysore": 100, "Ankola": 120, "Karwar": 80}
}

# Create a dictionary to store bus details

bus_details = {
    "Karwar": {"Ankola": [{"bus_number": "KA789BR89", "departure_time": "08:00 AM"}, {"bus_number": "KA123BR45", "departure_time": "10:00 AM"}], "Mysore": [{"bus_number": "KA456BR78", "departure_time": "12:00 PM"}]},
    "Ankola": {"Bangalore": [{"bus_number": "KA901BR23", "departure_time": "09:00 AM"}, {"bus_number": "KA567BR89", "departure_time": "11:00 AM"}], "Mysore": [{"bus_number": "KA890BR12", "departure_time": "01:00 PM"}]},
    "Bangalore": {"Karwar": [{"bus_number": "KA345BR67", "departure_time": "10:00 AM"}], "Mysore": [{"bus_number": "KA678BR90", "departure_time": "02:00 PM"}]},
    "Mysore": {"Ankola": [{"bus_number": "KA234BR56", "departure_time": "11:00 AM"}], "Karwar": [{"bus_number": "KA456BR78", "departure_time": "03:00 PM"}]}
}


# text to speech
def text_to_speech(text):
    engine.say(text)
    engine.setProperty('rate', 0)
    engine.runAndWait()

# calculate price
def calculate_price(source, destination):
    if source in prices and destination in prices[source]:
        return prices[source][destination]
    else:
        return None
    
# speech recognize function
def recognize_speech():
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return None
def recognic2():
    with sr.Microphone() as source:
       audio2=m.listen(source)
    try:
        text = m.recognize_google(audio2)
        return text
    except sr.UnknownValueError:
        return None
    
# calculate price function
def handle_input():
    source = combo_source.get()
    destination = combo_destination.get()
    price = calculate_price(source, destination)
    if price:
        result_text1 = f"The price of traveling from........ {source} to ......{destination} is.......... rupees {price}."
        
        result_text = f"The price of traveling from {source} to {destination} is rupees {price}."
        
        text_to_speech(result_text1)
        
        label_result.config(text=result_text )
        label_result.place(x=640,y=570)
        # ask_to_book_ticket()
        
        if result_text:
            book_ticket()
            ask_to_book_ticket()
            # text_to_speech("if you want to continue voice commands please say go ahead?")
            # response =recognic2()
            # print(response)
            # if(response=="go ahead"):
           
        
    else:
        result_text = "Sorry,we couldn't find the price for that route."
        text_to_speech(result_text)
        label_result.config(text=result_text)



def ask_to_book_ticket():
    text_to_speech("if you want to book the ticket.. please say.....i want to book?")
    root.after(2000, get_response)
    
def get_response():
     
    response =recognic2()
    print(response)
    
    if response is None:
        print("Speech recognition failed. Please try again.")
        # You can also add a retry mechanism here
    if (response=="I want to book") :
         book_ticket1()
    else:
        text_to_speech("khopdi thod sale kaa")
    
    

# Call the ask_to_book_ticket function

# sreach busses function
def showbus():
    source = combo_source.get()
    destination = combo_destination.get()
    # price = calculate_price(source, destination)
    try:
     bus_text1 = f"Available buses from...... {source} to .....{destination}.are....:"
     for bus in bus_details[source][destination]:
      bus_text1 += f"\nBus Number: {bus['bus_number']}, Departure Time: {bus['departure_time']}"
     bus_text = "Available buses:"
     for bus in bus_details[source][destination]:
      bus_text += f"\nBus Number: {bus['bus_number']}, \t Departure Time: {bus['departure_time']}"
     
     label_result2.config(text=bus_text )
     label_result2.place(x=640,y=600)
     text_to_speech(bus_text1)
    #  root.after(2000,text_to_speech(bus_text1))
    except :
            text_to_speech("oops!....there are no busses on this route")
    if bus_text:
      handle_input()
    else:
        text_to_speech("pleae enter valid place names")
# source city
def get_source():
    text_to_speech("please  say the source city.")
    source_text = recognize_speech()
    print(source_text)
    combo_source.set(source_text)
    if combo_source:
     get_destination()
# destination city
def get_destination():
    text_to_speech("Please say the .......destination city.")
    destination_text = recognize_speech()
    print(destination_text)
    combo_destination.set(destination_text)
    if combo_destination:
     showbus()


# Create the main window
root = Tk()
root.title("Online Bus Ticketing System")
root.geometry("1800x900")
root.configure(background='lightblue')

image = Image.open(r"D:\LoginWare-internship\bus_projects\istockphoto-1154164634-612x612.jpg")
image=image.resize((780,440))
photo = ImageTk.PhotoImage(image)
background_label = Label(root, image=photo)
background_label.place(x=630,y=75)

# Set the style
style = ttk.Style()
style.configure('TLabel', background='#ACFFAC', font=('Arial', 18))
style.configure('TButton', background='#FF69B4', font=('Arial', 18))
style.configure('TEntry', background='#C7F464', font=('Arial', 18))
style.configure('TCombobox', background='#C7F464', font=('Arial', 18))

# Create the input fields

label_source = Label(root, text="Enter the source city:", bg='lightblue', fg='red', font=('Arial', 22, 'bold'))
label_source.place(x=240, y=90)
combo_source = ttk.Combobox(root, values=list(prices.keys()),width=30,font=('Arial', 15, 'bold'))
combo_source.place(x=240, y=130)
button_source = Button(root, text="Trigger voice commands",fg="darkgreen",relief="groove",bd=5,highlightbackground="green",highlightthickness=5, width=24,command=get_source, bg='lightgray', font=('Arial', 17,'bold'))
button_source.place(x=240, y=450)
label_destination = Label(root, text="Enter the destination city:", bg='lightblue', fg='red', font=('Arial', 22, 'bold'))
label_destination.place(x=240, y=220)
combo_destination = ttk.Combobox(root, values=list(prices.keys()),width=30,font=('Arial', 15, 'bold'))
combo_destination.place(x=240, y=260)

# Create the button to calculate the price
button_calculate = Button(root, text="Calculate Price",relief="groove",bd=7,highlightbackground="green", command=handle_input, bg='lightgray',fg="darkgreen", font=('Arial', 15, 'bold'))
button_calculate.place(x=240,y=370)
# button to show busses
button_busses = Button(root, text="Search Busses",relief="groove",bd=7,highlightbackground="green", command=showbus, bg='lightgray',fg="darkgreen", font=('Arial', 15, 'bold'))
button_busses.place(x=420,y=370)

# Create the label to display the result
label_result = Label(root, text="",bg='lightblue', fg='green', font=('Arial', 18, 'bold'))
label_result.place_forget()
label_result2 = Label(root, text="",bg='lightblue', fg='green', font=('Arial', 18, 'bold'))
label_result2.place_forget()

# Create the combobox for quantity
combo_quantity = ttk.Combobox(root, values=[1, 2, 3, 4, 5], font=('Arial', 5, 'bold'))
combo_quantity.set("qty")
combo_quantity.place_forget()
# combo_quantity.place(x=450, y=620)
# Create the button to book ticket
def book_ticket1():
    global quantity
    text_to_speech("you need to add the.....quantity...please say the number of persons travelling ")
    qty_text = recognize_speech()
    print(qty_text)
    # if(qty_text=="")
    if qty_text:
     #  Extract the integer value from the spoken sentence
     words = qty_text.split()
     for word in words:
         if word.isdigit():
             quantity = int(word)
             break
         else:
             try:
                 quantity = w2n.word_to_num(word)
                 break
             except ValueError:
                 pass
    else:
        quantity=1

    # quantity =int( combo_quantity.get())
    if quantity:
        text_to_speech("to book tickets.... ..please scan the Qr code on the right side ")
        book_ticketfun()
    else:
        messagebox.showerror("Error", "Please select a quantity")
def book_ticket():
 button_book_ticket = Button(root, text="Click to book ticket", command=book_ticket1, relief="groove", bd=7, highlightbackground="green", bg='lightgray', fg="darkgreen", font=('Arial', 15, 'bold'))
 button_book_ticket.place(x=240, y=590)
#  combo_quantity.place(x=450, y=620)




# QR code function
def book_ticketfun():
    global quantity
    label_result.config(text="" )
    label_result2.config(text="")
    background_label.config(image="")

    source = combo_source.get()
    destination = combo_destination.get()
    price = calculate_price(source, destination)
    if price:
        total_price = price*quantity
        # Generate QR code
        qr_code = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L
        )
        qr_code.add_data(f"Source: {source}\nDestination: {destination}\nQuantity: {quantity}\nPrice: {total_price}")
        qr_code.make(fit=True)
        img = qr_code.make_image(fill='black', back_color='white')
        img.save("ticket.png")
        # Insert the transaction data into the table
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        c.execute("INSERT INTO transactions12 (source, destination, quantity, price, timestamp) VALUES (?, ?, ?, ?, ?)",
                   (source, destination,quantity, total_price, timestamp))
        conn.commit()
        # Get the transaction ID
        transaction_id = c.lastrowid
        # display(source, destination,quantity,total_price,)

        # Display the transaction ID and details
        qr_code_img = ImageTk.PhotoImage(Image.open("ticket.png"))
        qr_code_label = Label(root, image=qr_code_img,background="black", bd=7, highlightbackground="darkgreen")
        qr_code_label.image = qr_code_img
        qr_code_label.place(x=800, y=115)
        qr_code_labeltxt = Label(root, text=f"Your ticket no: {transaction_id}\n From: {source}\t To: {destination}\nQuantity: {quantity}\nTotal amount: {total_price}",
                                    bg="lightblue", fg='green',bd=6,highlightbackground="green",highlightthickness=6, font=('Arial', 15, 'bold'))
        qr_code_labeltxt.place_forget()
        qr_code_labeltxt1=Label(root,text="Scan the QR to make payment",foreground='green', bg='lightblue', font=('Arial', 19, 'bold'))
        qr_code_labeltxt1.place(x=800, y=550)
        root.after(6000, lambda: final_message(qr_code_labeltxt))
        root.after(15000, lambda: reset(qr_code_label,qr_code_labeltxt1,))
        root.after(25000,lambda: ticket(source, destination,quantity, total_price, timestamp,transaction_id))
        root.after(18000,lambda:display_travel_data())

    # reset function
def reset(qr_code_label,qr_code_labeltxt1):
    global quantity
    qr_code_label.config(image="",bg="lightblue")
    qr_code_label.place_forget() 
    qr_code_labeltxt1.place_forget() 
    background_label.config(image=photo)
     #final message  
def final_message(qr_code_labeltxt):
    # qr_code_labeltxt = Label(root, text=f"Transaction ID: {transaction_id}\nSource: {source}\Destination: {destination}\nPrice: {price}",
                                    # foreground='lightblue', bg='lightblue', fg='lightblue', font=('Arial', 19, 'bold'))
    # qr_code_labeltxt.place(x=770, y=560)
    # root.after(6000,qr_code_labeltxt.place_forget())
    text_to_speech("your ..transaction ...is completed.. successfully...your ticket had been confirmed")
    messagebox.showinfo(title="booking",message="your ticket has been confirmed")
    root.after(4000,qr_code_labeltxt.place_forget())
   #ticket function 
def ticket(source, destination,quantity, total_price, timestamp,transaction_id): 
    # background_label.config(image=photo)
    top = Toplevel(root)
    top.title("Ticket")
    # top.geometry(500,300)
    label_ticket  = Label(top, text=f"Your ticket number: {transaction_id}\n From: {source}\n To: {destination}\nQuantity: {quantity}\nAmount paid: {total_price}\nTime:{timestamp}",
                                    bg="white", fg='black',bd=6,highlightbackground="black",highlightthickness=6, font=('Arial', 10, 'bold'))
    label_ticket.pack()

# display travel history
def display_travel_data():
    # Create a dropdown menu to select the chart type
    chart_types = ['Pie Chart', 'Bar Chart', 'Histogram']
    selected_chart = StringVar()
    selected_chart.set(chart_types[0])  # default value

    def plot_chart():
        chart_type = selected_chart.get()
        if chart_type == 'Pie Chart':
            root.after(5000,button_chart.place_forget())
            plot_pie_chart()
            root.after(5000,dropdown.place_forget())
        elif chart_type == 'Bar Chart':
            plot_bar_chart()
            root.after(5000,button_chart.place_forget())
            root.after(5000,dropdown.place_forget())
        elif chart_type == 'Histogram':
            plot_histogram()
            root.after(5000,button_chart.place_forget())
            root.after(5000,dropdown.place_forget())

    def plot_pie_chart():
        # Retrieve transaction data from database
        c.execute("SELECT destination, COUNT(*) as count FROM transactions12 GROUP BY destination")
        transactions = c.fetchall()
        # Extract destination and count
        destinations = [transaction[0] for transaction in transactions]
        counts = [transaction[1] for transaction in transactions]
        # Create pie chart
        plt.pie(counts, labels=destinations, autopct='%1.1f%%')
        plt.title('Transaction Distribution')
        plt.show()

    def plot_bar_chart():
        # Retrieve transaction data from database
        c.execute("SELECT destination, COUNT(*) as count FROM transactions12 GROUP BY destination")
        transactions = c.fetchall()
        # Extract destination and count
        destinations = [transaction[0] for transaction in transactions]
        counts = [transaction[1] for transaction in transactions]
        # Create bar chart
        plt.bar(destinations, counts)
        plt.xlabel('Destination')
        plt.ylabel('Count')
        plt.title('Transaction Distribution')
        plt.show()
        root.after(5000,button_chart.pack_forget())

    def plot_histogram():
        # Retrieve transaction data from database
        c.execute("SELECT destination, COUNT(*) as count FROM transactions12 GROUP BY destination")
        transactions = c.fetchall()
        # Extract destination and count
        destinations = [transaction[0] for transaction in transactions]
        counts = [transaction[1] for transaction in transactions]
        # Create histogram
        plt.hist(destinations, bins=len(destinations), weights=counts)
        plt.xlabel('Destination')
        plt.ylabel('Count')
        plt.title('Transaction Distribution')
        plt.show()

    # Create dropdown menu
    dropdown = ttk.OptionMenu(root, selected_chart, *chart_types, command=plot_chart)
    dropdown.place(x=240, y=680)

    # Create button to display chart
    button_chart = Button(root, text="Travel history", command=plot_chart, bg='lightblue', fg="darkgreen", font=('Arial', 15, 'bold'))
    button_chart.place(x=240, y=720)


# Welcome message
welcome_text = "'Advanced ticket booking system'"
welcome_text1="Welcome to Advanced ticket booking system'...you can either click on trigger button ....to activate voice commands......or.....just say activate voice command"
root.after(4000,lambda:text_to_speech(welcome_text1))
root.after(6000,lambda:start())
def start():
    startres=recognize_speech()
    print(startres)
    try:
      if(startres=="activate voice command"):
       get_source()
    except:
        # startres is None:
        print("none")
    
label_welcome = Label(root, text=welcome_text,bd=5,highlightbackground="green",highlightcolor="green",foreground='darkgreen',bg='lightblue', font=('Arial', 33, 'bold'))
label_welcome.place(x=440,y=0)
# Start the main loop
root.mainloop()