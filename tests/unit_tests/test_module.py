import io
from unittest.mock import patch
from mylib.divers.module import hello_world

@patch('sys.stdout', new_callable=io.StringIO)
def test_hello_world(mock_stdout):
    hello_world()
    assert mock_stdout.getvalue() == 'Hello World!\n'