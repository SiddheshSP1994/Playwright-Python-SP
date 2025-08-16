"""Generate test modules from a YAML catalogue.

This script reads a YAML file containing a list of test cases and emits a
pytest module per suite with parametrised cases.  It serves as an example
for generating large numbers of tests programmatically.
"""
import os
import sys
import yaml
import json


def generate_tests(yaml_path: str, out_dir: str, suite: str) -> None:
    with open(yaml_path, 'r') as f:
        cases = yaml.safe_load(f)
    os.makedirs(out_dir, exist_ok=True)
    file_name = f"test_{suite}_{len(os.listdir(out_dir)) + 1:03d}.py"
    file_path = os.path.join(out_dir, file_name)
    with open(file_path, 'w') as f:
        f.write('import pytest\n\n')
        f.write('@pytest.mark.regression\n')
        f.write('@pytest.mark.parametrize("case", [\n')
        for case in cases:
            f.write(f"    {json.dumps(case)},\n")
        f.write('])\n')
        f.write(f'def test_{suite}(case):\n')
        f.write('    # TODO: implement test using case data\n')
        f.write('    assert case is not None\n')
    print(f"Generated {file_path}")


def main():
    if len(sys.argv) != 4:
        print("Usage: generate_tests.py <yaml-file> <output-dir> <suite>")
        sys.exit(1)
    yaml_path, out_dir, suite = sys.argv[1:]
    generate_tests(yaml_path, out_dir, suite)


if __name__ == '__main__':
    main()