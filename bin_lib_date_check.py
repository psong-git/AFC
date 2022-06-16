import subprocess

print('\033[36m' + '# bin, lib DATE CEHCK' + '\033[0m');

subprocess.call("ls -l $ARKCDC_HOME | grep \"bin\" | awk \'{ print $6,$7,$9 }\'", shell=True)
subprocess.call("ls -l $ARKCDC_HOME | grep \"lib\" | awk \'{ print $6,$7,$9 }\'", shell=True)

print("");