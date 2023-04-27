#!/bin/bash

read -p "Enter number: " number
# -p is used to prompt the message "Enter number:" to the user


echo "reversed number = $(echo $number | rev)"


#Here are some common options that are used with the read command:

# -p: specifies the prompt that should be displayed to the user.
# -r: disables the interpretation of backslash escape characters.
# -a array: reads input into an array variable.
# -n count: specifies the number of characters to read.
# -s: suppresses the input from being echoed to the terminal.