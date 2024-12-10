import sqlite3
import statistics
from datetime import datetime, timedelta


class WeatherStation:
    def __init__(self, db_name):
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS weather_data (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            temperature REAL,
                            humidity REAL,
                            pressure REAL,
                            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                          )''')
        conn.commit()
        conn.close()

    def collect_data(self):
        # Simulate weather station readings
        data = {
            'temperature': 22.5,
            'humidity': 60.0,
            'pressure': 1013.25
        }
        return data  # Remove [2] indexing

    def store_data(self, data):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        data = self.collect_data()
        cursor.execute('''INSERT INTO weather_data (temperature, humidity, pressure)
                        VALUES (?, ?, ?)''', 
                        (data['temperature'], data['humidity'], data['pressure']))  # Remove [2] indexing
        conn.commit()
        conn.close()

    def analyze_data(self, timeframe_hours):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        end_time = datetime.now()
        start_time = end_time - timedelta(hours=timeframe_hours)

        cursor.execute('''SELECT temperature, humidity, pressure FROM weather_data 
                        WHERE timestamp BETWEEN ? AND ?''', 
                        (start_time, end_time))
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            return {
                'average_temperature': 0,
                'average_humidity': 0,
                'average_pressure': 0,
                'max_temperature': 0,
                'min_temperature': 0
            }

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