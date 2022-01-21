#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Jan. 19, 2022
# This program uses separate functions to calculate the area
# of a triangle


def calculate_area(base, height):
    # This function cakcukates the area of the triangle

    # Use the area formula
    area = (base * height) / 2

    # Print the final result
    print("The area is {0} cm²".format(area))


def main():
    # this function gets length and width

    while True:
        # Get user input for height
        height_from_user = input("Enter the height of your triangle (cm): ")
        # Make sure that the input is a number
        try:

            height_from_user_float = float(height_from_user)
            base_from_user = input("Enter the base of your triangle (cm): ")
            # Make sure that the input is a number
            try:
                # Get user input for base
                base_from_user_float = float(base_from_user)
                # Call the function
                calculate_area(base_from_user_float, height_from_user_float)
                break
            # Print error message if input is invalid
            except Exception:
                print("Input must be a number")
        # Print error message if input is invalid
        except Exception:
            print("Input must be a number")

        print("")


if __name__ == "__main__":
    main()
