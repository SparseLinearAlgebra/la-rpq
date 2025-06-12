#!/usr/bin/env python3
import os
import sys
import re
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage: python txt_to_mat.py <dataset>")
        return
    
    dataset = sys.argv[1]
    dir_path = Path(dataset)
    
    try:
        files = os.listdir(dir_path)
    except Exception as e:
        print(f"Error occurred while reading directory: {e}")
        return
    
    for file in files:
        old_name = file
        name_without_ext, ext = os.path.splitext(old_name)
        
        try:
            num = int(name_without_ext)
        except ValueError:
            print(f"Incorrect filename: {old_name}")
            continue
        
        # 1 -> 0001
        new_num_str = f"{num:04d}"
        new_name = f"{new_num_str}.mat"  # "0001.mat"
        
        old_path = dir_path / old_name
        new_path = dir_path / new_name
        
        try:
            os.rename(old_path, new_path)
        except Exception as e:
            print(f"Error occurred while renaming file: {e}")

if __name__ == "__main__":
    main()