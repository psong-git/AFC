#!/bin/bash

# install file name check
python3 install_file_name_check.py
# bin, lib directory DATE check
python3 bin_lib_date_check.py
# necessary directory check
python3 necessary_directory_check.py
# unnecessary directory check
python3 unnecessary_file_check.py
# sample file check
python3 sample_file_check.py

echo "TEST END"