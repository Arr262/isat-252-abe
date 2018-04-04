#testing the code
#import mock for faking user input


from mock import patch



#import code for testing



@patch("sys.stdin")
def test_get_username(mock_stdin):
	mock_stdin.read.return_value = "Morgan"
	assert get_username() == "Morgan"