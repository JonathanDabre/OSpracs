#!/bin/bash
dir=$1

file_count=0
dir_count=0
# Iterate over the contents of the directory

for entry in "$dir"/*; do

  if [ -f "$entry" ]; then

    # This is a regular file

    file_count=$((file_count+1))

  elif [ -d "$entry" ]; then

    # This is a directory

    dir_count=$((dir_count+1))

  fi
done

echo "Found $file_count files and $dir_count directories in $dir"

