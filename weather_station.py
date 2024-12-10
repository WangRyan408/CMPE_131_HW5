import sqlite3
import statistics
from datetime import datetime, timedelta


class WeatherStation:
    def __init__(self, db_url):
        self.db_url = db_url
        
    def collect_data(self):
        return {
            'temperature': self._read_temperature(),
            'humidity': self._read_humidity(),
            'pressure': self._read_pressure()
        }
        
    def store_data(self, data):
 # Connect to SQLite database
        conn = sqlite3.connect(self.db_url)
        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS weather_data (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            temperature REAL,
                            humidity REAL,
                            pressure REAL,
                            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                        )''')

        # Insert data into the table
        cursor.execute('''INSERT INTO weather_data (temperature, humidity, pressure)
                        VALUES (?, ?, ?)''', 
                        (data['temperature'], data['humidity'], data['pressure']))

        # Commit and close connection
        conn.commit()
        conn.close()
        
    def analyze_data(self, timeframe):
        conn = sqlite3.connect(self.db_url)
        cursor = conn.cursor()

        # Calculate the start time based on the timeframe
        end_time = datetime.now()
        start_time = end_time - timedelta(hours=timeframe)

        # Query data within the timeframe
        cursor.execute('''SELECT temperature, humidity, pressure FROM weather_data 
                        WHERE timestamp BETWEEN ? AND ?''', 
                        (start_time, end_time))
        rows = cursor.fetchall()

        # Close the connection
        conn.close()

        if not rows:
            return "No data available for the specified timeframe."

        # Analyze data
        temperatures = [row[0] for row in rows]
        humidities = [row[1] for row in rows]
        pressures = [row[2] for row in rows]

        analysis = {
            'average_temperature': statistics.mean(temperatures),
            'average_humidity': statistics.mean(humidities),
            'average_pressure': statistics.mean(pressures),
            'max_temperature': max(temperatures),
            'min_temperature': min(temperatures)
        }

        return analysis