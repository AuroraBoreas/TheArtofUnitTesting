from my_module import total_value
from unittest.mock import patch

def test_total_value():
    with patch('my_module.db_read') as mock_db_read:
        mock_db_read.return_value = [100, 200]
        assert 300 == total_value(1234)
        mock_db_read.assert_called_with(1234)

if __name__ == "__main__":
    test_total_value()