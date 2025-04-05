import unittest
import subprocess
import sys

class TestCalcCTL(unittest.TestCase):
    def test_cli_add(self):
        result = subprocess.run(
            [sys.executable, '-m', 'app_ctl.calctl', 'add', '5', '3'],
            capture_output=True, text=True
        )
        self.assertEqual(result.stdout.strip(), '8.0')
        
    def test_cli_subtract(self):
        result = subprocess.run(
            [sys.executable, '-m', 'app_ctl.calctl', 'subtract', '10', '4'],
            capture_output=True, text=True
        )
        self.assertEqual(result.stdout.strip(), '6.0')
        
    def test_cli_error(self):
        result = subprocess.run(
            [sys.executable, '-m', 'app_ctl.calctl', 'divide', '5', '0'],
            capture_output=True, text=True
        )
        self.assertIn('Error', result.stderr)

class TestCalcCTLSecurity(unittest.TestCase):
    def test_input_validation(self):
        """Test handling of invalid inputs."""
        result = subprocess.run(
            [sys.executable, '-m', 'app_ctl.calctl', 'add', '5', '; echo INJECTION'],
            capture_output=True, text=True
        )
        self.assertNotEqual(result.returncode, 0)  


if __name__ == '__main__':
    unittest.main()