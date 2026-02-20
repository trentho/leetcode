from __future__ import annotations

import importlib
import sys


USAGE = "Usage: python main.py <problem_module>  (e.g. lc_0104_max_depth)"


def main() -> None:
    if len(sys.argv) < 2:
        print(USAGE)
        return

    module_name = sys.argv[1]

    if module_name.startswith("problems."):
        target = module_name
    else:
        target = f"problems.{module_name}"

    module = importlib.import_module(target)

    if not hasattr(module, "run"):
        raise AttributeError(f"{target} must define a run() function")

    module.run()


if __name__ == "__main__":
    main()
