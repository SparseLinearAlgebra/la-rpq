#!/bin/sh
file="$1"
temp_file=$(mktemp)
awk '{ print $2, $1 }' "$file" > "$temp_file" && mv "$temp_file" "$file"