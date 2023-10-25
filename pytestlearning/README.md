

 `pytest test_marker_example.py -s -v -k login`
 `pytest test_marker_example.py -s -v -k "not login"` 
 
# Register marker
- add pytest.ini`
- `pytest test_marker_example.py -s -v -m "not functional"`

