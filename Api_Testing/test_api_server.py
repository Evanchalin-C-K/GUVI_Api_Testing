from Api_Testing.api_class import API_testing
import json


class Test_Api_server:
    url = "https://652645bb917d673fd76bed89.mockapi.io/Automation_testing"
    data = {"Name": "priya", "City": "chennai", "Country": "India"}
    data_update = {"Name": "Riya"}

    # Fetch data from the server
    def test_GET_data(self):
        data = API_testing(self.url).fetch_data()
        print(data)

    # Check status code
    def test_status_code(self):
        data = API_testing(self.url).status_code()
        assert data == 200

    # test case for POST method
    def test_POST(self):
        data = self.data
        assert API_testing(self.url).insert_data(data) == 201

    # test case for UPDATE method
    def test_UPDATE(self):
        data = self.data_update
        response = API_testing(self.url).update_data(_id=11, json_data=data)
        assert response == 200

    # test case for DELETE method
    def test_DELETE(self):
        response = API_testing(self.url).delete_data(_id=12)
        print(response)

    def test_GET_data2(self):
        data = API_testing(self.url).fetch_data()
        print(data)
