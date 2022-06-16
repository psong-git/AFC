import subprocess

print('\033[36m' + '# bin, lib DATE CEHCK' + '\033[0m');

subprocess.call("ls -l $ARKCDC | grep \"bin\"", shell=True)
subprocess.call("ls -l $ARKCDC | grep \"lib\"", shell=True)

print("");