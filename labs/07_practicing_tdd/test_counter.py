"""
Test Cases for Counter Web Service
"""
from unittest import TestCase
import status
from counter import app

class CounterTest(TestCase):
    """Test Cases for Counter Web Service"""

    def setUp(self):
        self.client = app.test_client()

    def test_create_a_counter(self):
        """It should create a counter"""
        result = self.client.post("/counters/Najam")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        data = result.get_json()
        self.assertIn("Najam", data)
        self.assertEqual(data["Najam"], 0)

    def test_duplicate_counter(self):
        """It should return an error for duplicates"""
        result = self.client.post("/counters/Rizwan")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        result = self.client.post("/counters/Rizwan")
        self.assertEqual(result.status_code, status.HTTP_409_CONFLICT)

    def test_update_a_counter(self):
        """It should increment the Counter"""
        result = self.client.post("/counters/Fahad")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        data = result.get_json()
        baseline = data["Fahad"]
        # Update the counter
        result = self.client.put("/counters/Fahad")
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        data = result.get_json()
        self.assertEqual(data["Fahad"], baseline + 1)

    def test_read_a_counter(self):
        """It should read the counter"""
        result = self.client.post("/counters/Hasnain")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        # Read the Counter
        result = self.client.get("/counters/Hasnain")
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        data = result.get_json()
        self.assertEqual(data["Hasnain"], 0)

    def test_delete_a_counter(self):
        """It should delete a counter"""
        result = self.client.post("/counters/Faizan")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        # Delete the Counter
        result = self.client.delete("/counters/Faizan")
        self.assertEqual(result.status.code, status.HTTP_204_NO_CONTENT)