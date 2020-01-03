import unittest
import json
from app import total, app

class TestApp(unittest.TestCase):
    def test_total(self):
        expected_result = 50000005000000
        
        with app.app_context():
            response_json = total()
        
        response_data = json.loads(response_json.data)

        assert response_data['total'] == expected_result