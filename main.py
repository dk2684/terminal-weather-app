# main.py (Script)
# Usage: python -u main.py

import weather # Local

def main():

    print("\n------------- Weather App Opened-------------\n")

    while (True):
        user_input = input(
                            "Please enter an option and press enter:\n" +
                            "\t(1) See Weather Data at Location (US)\n" +
                            "\t(2) How to Interpret Weather Data\n" +
                            "\t(3) About Weather API Provider\n" +
                            "\t(4) Exit Weather App\n" +
                            "-------> "
                            )
        if (user_input == "1"):
            while (True):
                location_choice = input(
                                "Please select a location format:\n" +
                                "\t(1) City, State\n" +
                                "\t(2) Postal/ZIP Code\n" +
                                "\t(3) Previous Page\n" +
                                "-------> "
                                )
                if (location_choice == "1"):
                    user_city = input("Enter City (e.g. San Diego): ")
                    user_state = input("Enter State (e.g. California): ")
                    print()
                    weather.get_using_city(user_city, user_state)
                    print()
                    break
                elif (location_choice == "2"):
                    zip_code = input("Enter Zip Code: ")
                    print()
                    weather.get_using_zip(zip_code)
                    print()
                    break
                elif (location_choice == "3"):
                    print()
                    print("Going back...")
                    print()
                    break
                else:
                    print("\nERROR: Invalid option, please try again.\n")
        elif (user_input == "2"):
            weather.data_details()
        elif (user_input == "3"):
            weather.about_openweather()
        elif (user_input == "4"):
            print("\nExiting Weather App...\n")
            print("------------- Weather App Closed-------------\n")
            exit()
        else:
            print("\nERROR: Invalid option, please try again.\n")

main()