#!/usr/bin/env python3
# Created by: Santiago Hewett
# Created on: Oct 19, 2023
# This program will ask the user
# for a integer then check if the integer
# is positive negative or zero


def main():
    # Get the user integer
    print("This program will ask the user for a integer")
    print("then it will display if the integer is positive, negative or zero.")

    user_int = int(input("Please enter your integer: "))

    # Check if the users int is positive, negative or zero

    if user_int > 0:
        # Display if the users number is positive

        print("\n{} is positive".format(user_int))

    elif user_int < 0:
        # Display if the users number is negative

        print("\n{} is negative".format(user_int))

    else:
        # Display if the users number is zero

        print("\nYour number is just zero")


if __name__ == "__main__":
    main()
