import unittest
import io
import sys
from contextlib import redirect_stdout

class TestPrintOutput(unittest.TestCase):
    def test_print_output(self):
        # Перенаправляем stdout в буфер
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            you_name = "Ivan"
            print(you_name)
        
        # Получаем то, что было выведено
        output = buffer.getvalue().strip()
        
        # Проверяем, что вывод соответствует ожидаемому
        self.assertEqual(output, "Ivan")