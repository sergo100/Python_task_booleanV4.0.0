import io, sys
from tasks.task1 import solve

def run_io(input_data):
    old_in, old_out = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = io.StringIO(input_data), io.StringIO()
    try:
        solve()
        return sys.stdout.getvalue().strip()
    finally:
        sys.stdin, sys.stdout = old_in, old_out

def test_case1():
    assert run_io("5 5 5\n") == "True"

def test_case2():
    assert run_io("4 5 6\n") == "False"
