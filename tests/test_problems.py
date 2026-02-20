from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout
from importlib import import_module


class TestProblems(unittest.TestCase):
    def _run_problem(self, module_name: str) -> str:
        module = import_module(f"problems.{module_name}")
        self.assertTrue(hasattr(module, "run"))

        buf = io.StringIO()
        with redirect_stdout(buf):
            module.run()
        return buf.getvalue().strip()

    def test_two_sum(self) -> None:
        output = self._run_problem("two_sum")
        self.assertEqual(output, "[0, 1]")

    def test_reverse_linked_list(self) -> None:
        output = self._run_problem("reverse_linked_list")
        self.assertEqual(output, "5 -> 4 -> 3 -> 2 -> 1")

    def test_max_depth(self) -> None:
        output = self._run_problem("max_depth")
        self.assertEqual(output, "3")


if __name__ == "__main__":
    unittest.main()
