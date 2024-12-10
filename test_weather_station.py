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

test_data_collection()
test_data_storage()