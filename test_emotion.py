import unittest
from emotion_predictor import emotion_predictor

class TestEmotionDetection(unittest.TestCase):
    def test_valid_text(self):
        result = emotion_predictor("I'm happy!")
        self.assertIn('dominant_emotion', result)
        
    def test_empty_text(self):
        result = emotion_predictor("")
        self.assertEqual(result['status'], 400)

if __name__ == '__main__':
    unittest.main()