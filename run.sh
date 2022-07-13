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
# agent IP valid check
python3 agent_valid_change_IP.py
adctl start > tmp;
python3 agent_valid_check_msg.py
adctl stop > tmp;
python3 agent_valid_change_IP2.py
echo "TEST END"