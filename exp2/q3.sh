#!/bin/bash



read -p "Enter the number: " number



if ((number<10 && number>0));then

echo "Number in range 0 to 9"

else

echo "Number not in range"

fi


