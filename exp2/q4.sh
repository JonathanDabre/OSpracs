#!/bin/bash

read -p "Enter n: " n

sum=0


for (( i=1; i<=$n; i++ )); do

  sum=$((sum+i))

done



echo "The sum of the first $n numbers is: $sum"

# don't forget the ";" and $before n: $n