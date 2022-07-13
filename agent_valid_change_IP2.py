import fileinput
import re
import sys
import os
import subprocess

env = os.getenv("ARKCDC_HOME")
path = env + "/conf/agent.conf"
to_find = "IP="
to_change = "IP=\"256.12%.123\"\n"
to_origin = "IP=\"\"\n"

with fileinput.FileInput(path, inplace = True, backup = '.bak') as f:
    for line in f:
        if to_find in line:
            line = to_origin
        sys.stdout.write(line)