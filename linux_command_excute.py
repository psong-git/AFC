import subprocess

subprocess.call("ls -l $ARKCDC | grep \"bin\"", shell=True)
subprocess.call("ls -l $ARKCDC | grep \"lib\"", shell=True)