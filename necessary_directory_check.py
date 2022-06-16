import os

dir_name = ['bin', 'lib', 'scripts', 'stats', 'conf', 'dump', 'cache', 'logs', 'proc', 'trace', 'checkpoint', 'data']
env = os.getenv("ARKCDC_HOME")

for line in dir_name:
        path = env + '/' + line
        if os.path.isdir(path):
                print('\033[32m' + '[SUCCESS]' + '\033[0m', end='')
                print(" %s"%path);
        else:
                print('\033[31m' + '[FAIL]' + '\033[0m', end='')
                print(" %s"%path);