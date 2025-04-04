import unittest
import subprocess
import sys

class TestCalcCTL(unittest.TestCase):
    def test_cli_add(self):
        result = subprocess.run(
            [sys.executable, '-m', 'src.cli', 'add', '5', '3'],
            capture_output=True, text=True
        )
        self.assertEqual(result.stdout.strip(), '8.0')
        
    def test_cli_subtract(self):
        result = subprocess.run(
            [sys.executable, '-m', 'src.cli', 'subtract', '10', '4'],
            capture_output=True, text=True
        )
        self.assertEqual(result.stdout.strip(), '6.0')
        
    def test_cli_error(self):
        result = subprocess.run(
            [sys.executable, '-m', 'src.cli', 'divide', '5', '0'],
            capture_output=True, text=True
        )
        self.assertIn('Error', result.stderr)
        
if __name__ == '__main__':
    unittest.main()