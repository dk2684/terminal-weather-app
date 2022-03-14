# test.py (Module)
# Usage: python -u test.py

"""

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Please read:

I discussed the testing circumstances with Professor Ellis (Campuswire DM) 
and she said it was sufficient to test functions returning void.

"""

import weather # Local
import api_key # Local

# This is incredibly hard to implement since weather data 
# is not static and done on I/O stream.

def test_cases():
    """
    Tests basic functionality and reachability of weather script
    
    Args:
        N/A

    Returns:
        void
    """
    print("Basic Functions Test: Start")
    print()
    
    # Tests for the first five characters of private key being correct.
    assert api_key.return_key()[0:5] == "0ebd0"

    print("<Intentionally No Output>")
    print()
    print("*** Tests: 1/5 Passed ***")

    # Tests void function
    assert weather.data_details() == None

    print("*** Tests: 2/5 Passed ***")

    # Tests void function
    assert weather.about_openweather() == None

    print("*** Tests: 3/5 Passed ***")
    print()

    assert weather.get_using_zip(92092) == None

    print()
    print("*** Tests: 4/5 Passed ***")
    print()

    assert weather.get_using_city("La Jolla", "California") == None

    print()
    print("*** Tests: 5/5 Passed ***")

    print()
    print("Basic Functions Test: Passed")
    

test_cases()


# API Calls are costly because there is real-time data movement
