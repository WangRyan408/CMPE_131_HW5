import pytest
from weather_station import WeatherStation

def test_data_collection():
    station = WeatherStation('sqlite:///weather.db')
    data = station.collect_data()
    assert 'temperature' in data
    assert 'humidity' in data
    assert 'pressure' in data

def test_data_storage():
    station = WeatherStation('sqlite:///weather.db')
    test_data = {'temperature': 20.5}
    station.store_data(test_data)
    # Verify storage