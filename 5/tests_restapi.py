import requests
import pytest

class TestApiZippopotam():
    
    def test_check_status_code(self):
        response = requests.get("http://api.zippopotam.us/de/01067")
        assert response.status_code == 200
                
    def test_check_content_type_equals_json(self):
        response = requests.get("http://api.zippopotam.us/de/01067")
        assert response.headers["Content-Type"] == "application/json"
                
    def test_check_country_equals_germany(self):
        response = requests.get("http://api.zippopotam.us/de/01067")
        response_body = response.json()
        assert response_body["country"] == "Germany"
                
    def test_check_city_equals_dresden_friedrichstadt(self):
        response = requests.get("http://api.zippopotam.us/de/01067")
        response_body = response.json()
        assert response_body["places"][1]["place name"] == "Dresden Friedrichstadt"
                
    def test_check_three_places_are_returned(self):
        response = requests.get("http://api.zippopotam.us/de/01067")
        response_body = response.json()
        assert len(response_body["places"]) == 3
            
    def test_check_dresden_innere_altstadt_longitude_and_latitude(self):
        response = requests.get("http://api.zippopotam.us/de/01067")
        response_body = response.json()
        assert response_body["places"][2]["place name"] == "Dresden Innere Altstadt" and float(response_body["places"][2]["longitude"]) == 51.0507 and float(response_body["places"][2]["latitude"]) == 14612
        
class TestTimestampApi():
    def test_check_status_code(self):
        response = requests.get("https://showcase.api.linx.twenty57.net/UnixTime/fromunix?timestamp=1655197917")
        assert response.status_code == 200
        
    def test_check_content_type_equals_json(self):
        response = requests.get("https://showcase.api.linx.twenty57.net/UnixTime/fromunix?timestamp=1655197917")
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"
        
    @pytest.mark.parametrize("timestamp,result", [("1655197917", "2022-06-14 09:11:57"), ("1654877802", "2022-06-10 16:16:42"), ("1427050451", "2015-03-22 18:54:11")])    
    def test_timestamp_return_date(self,timestamp,result):
        response = requests.get("https://showcase.api.linx.twenty57.net/UnixTime/fromunix?timestamp=" + timestamp)
        response_body = response.json()
        assert response_body == result
        
    def test_value_null_returns_error(self):
        response = requests.get("https://showcase.api.linx.twenty57.net/UnixTime/fromunix?timestamp=")
        response_body = response.json()
        assert response_body["Error"] == "UnixTimeService.RESTHost.fromunix.TryCatch.Try.UnixTimeStamp: Value cannot be null. (Parameter 's') (Parameter 's')"
        
    def test_response_status_code_400(self):
        response = requests.get("https://showcase.api.linx.twenty57.net/UnixTime/fromunix?timestamp")
        assert response.status_code == 400