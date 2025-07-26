# travel_history.py
import matplotlib.pyplot as plt
import sqlite3

def display_travel_data():
    # Create a dropdown menu to select the chart type
    chart_types = ['Pie Chart', 'Bar Chart', 'Histogram']
    selected_chart = StringVar()
    selected_chart.set(chart_types[0])  # default value

    def plot_chart():
        chart_type = selected_chart.get()
        if chart_type == 'Pie Chart':
            plot_pie_chart()
        elif chart_type == 'Bar Chart':
            plot_bar_chart()
        elif chart_type == 'Histogram':
            plot_histogram()

    def plot_pie_chart():
        # Retrieve transaction data from database
        c.execute("SELECT destination, COUNT(*) as count FROM transactions12 GROUP BY destination")
        transactions = c.fetchall()
        destinations = [transaction[0] for transaction in transactions]
        counts = [transaction[1] for transaction in transactions]
        plt.pie(counts, labels=destinations, autopct='%1.1f%%')
        plt.title('Transaction Distribution')
        plt.show()

    def plot_bar_chart():
        c.execute("SELECT destination, COUNT(*) as count FROM transactions12 GROUP BY destination")
        transactions = c.fetchall()
        destinations = [transaction[0] for transaction in transactions]
        counts = [transaction[1] for transaction in transactions]
        plt.bar(destinations, counts)
        plt.xlabel('Destination')
        plt.ylabel('Count')
        plt.title('Transaction Distribution')
        plt.show()

    def plot_histogram():
        c.execute("SELECT destination, COUNT(*) as count FROM transactions12 GROUP BY destination")
        transactions = c.fetchall()
        destinations = [transaction[0] for transaction in transactions]
        counts = [transaction[1] for transaction in transactions]
        plt.hist(destinations, bins=len(destinations), weights=counts)
        plt.xlabel('Destination')
        plt.ylabel('Count')
        plt.title('Transaction Distribution')
        plt.show()
