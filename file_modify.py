import fileinput
import re
import sys
import os

env = os.getenv("ARKCDC_HOME")
path = env + "/conf/agent.conf"
to_find = "IP="
to_change = "IP=\"123.123.123.123\"\n"

with fileinput.FileInput(path, inplace = True, backup = '.bak') as f:
        for line in f:
                if to_find in line:
                        line = to_change
                sys.stdout.write(line)