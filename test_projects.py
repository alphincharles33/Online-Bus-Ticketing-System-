import sys
import os
import unittest
from unittest.mock import patch, MagicMock
import sqlite3

# Add the directory containing projects.py to PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import functions from the main script
from projects import calculate_price, recognic2, book_ticketfun, display_travel_data

class TestTravelBookingSystem(unittest.TestCase):

    # Test calculate_price function
    def test_calculate_price_valid(self):
        # Test valid source and destination
        result = calculate_price("Karwar", "Ankola")
        self.assertEqual(result, 150)

    def test_calculate_price_invalid(self):
        # Test invalid source and destination
        result = calculate_price("Karwar", "Unknown")
        self.assertIsNone(result)

    # Test recognic2 function with mocking
    @patch('projects.sr.Recognizer')
    def test_recognic2_valid(self, mock_recognizer):
        # Mock the recognizer to return a valid response
        mock_recognizer.return_value.recognize_google.return_value = "i want to book"
        result = recognic2()
        self.assertEqual(result, "i want to book")

    @patch('projects.sr.Recognizer')
    def test_recognic2_invalid(self, mock_recognizer):
        # Mock the recognizer to raise an UnknownValueError
        mock_recognizer.return_value.recognize_google.side_effect = sr.UnknownValueError()
        result = recognic2()
        self.assertIsNone(result)

    # Test book_ticketfun function with mocking
    @patch('projects.qrcode.QRCode')
    @patch('projects.sqlite3.connect')
    def test_book_ticketfun(self, mock_db_connect, mock_qrcode):
        # Mock database connection and cursor
        mock_cursor = MagicMock()
        mock_db_connect.return_value.cursor.return_value = mock_cursor

        # Mock QR code generation
        mock_qrcode_instance = MagicMock()
        mock_qrcode.return_value = mock_qrcode_instance

        # Call the function
        book_ticketfun()

        # Assert that the database insert was called
        mock_cursor.execute.assert_called_once()

        # Assert that QR code generation was called
        mock_qrcode_instance.add_data.assert_called_once()
        mock_qrcode_instance.make.assert_called_once()

    # Test display_travel_data function with mocking
    @patch('projects.sqlite3.connect')
    @patch('projects.plt.show')
    def test_display_travel_data_pie_chart(self, mock_show, mock_db_connect):
        # Mock database connection and cursor
        mock_cursor = MagicMock()
        mock_db_connect.return_value.cursor.return_value = mock_cursor

        # Mock database query result
        mock_cursor.fetchall.return_value = [("Ankola", 5), ("Bangalore", 3)]

        # Call the function
        display_travel_data()

        # Assert that the database query was called
        mock_cursor.execute.assert_called_once()

        # Assert that matplotlib's show() was called
        mock_show.assert_called_once()

if __name__ == "__main__":
    unittest.main()