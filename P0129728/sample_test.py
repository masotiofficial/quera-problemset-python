import unittest
import os
from subprocess import PIPE, run
import sys


class TestAll(unittest.TestCase):
    def test_sample_0(self):
        with open('source.py', "r") as f:
            ans = 0
            for line in f.readlines():
                line = line.strip()
                self.assertTrue('exec' not in line and ';' not in line)
                if line == '' or line[0] == '#':
                    continue
                ans += 1
            self.assertEqual(1, ans)

    def test_sample_1(self):
        output = self._get_output('saeid')
        self.assertEqual(output, "s i e a D")

    def test_sample_2(self):
        output = self._get_output('tourist')
        self.assertEqual(output, "u s o i T T R")

    def test_sample_3(self):
        output = self._get_output('alexander')
        self.assertEqual(output, "e e a a X R N L D")

    def _get_output(self, input_str):
        source_path = os.path.join(os.path.dirname(__file__), 'source.py')
        command = [sys.executable, source_path]
        result = run(command, input=input_str, stdout=PIPE, stderr=PIPE,
                     universal_newlines=True, text=True)
        self.assertEqual(result.returncode, 0)
        return result.stdout.strip()


if __name__ == '__main__':
    unittest.main()
