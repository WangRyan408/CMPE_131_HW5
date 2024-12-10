import pytest
from weather_station import WeatherStation

def test_data_collection():
    station = WeatherStation('weather.db')
    data = station.collect_data()
    assert 'temperature' in data
    assert 'humidity' in data
    assert 'pressure' in data

def test_data_storage():
    station = WeatherStation('weather.db')
    test_data = {'temperature': 20.5}
    station.store_data(test_data)
    # Verify storage

def test_analyze_data():
    station = WeatherStation('weather.db')
    test_data = {
        'temperature': 20.5,
        'humidity': 60.0,
        'pressure': 1013.25
    }
    station.store_data(test_data)
    analysis = station.analyze_data(timeframe_hours=1)
    
    assert 'average_temperature' in analysis
    assert 'average_humidity' in analysis
    assert 'average_pressure' in analysis

       

test_data_collection()
test_data_storage()
test_analyze_data()