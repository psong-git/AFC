import os

dir_name1 = ['stats', 'logs']
dir_name2 = ['dump', 'cache', 'trace', 'checkpoint']
sub_dir_name = ['extract', 'post', 'recv', 'send']

env = os.getenv("ARKCDC_HOME")

print('\033[36m' + '# UNNECESSARY FILE CHECK' + '\033[0m');

# case1 : directory has 'extract', 'post', 'recv', 'send'
for line in dir_name1:
    path1 = env + '/' + line
    for line in sub_dir_name:
            path2 = path1 + '/' + line
            if os.listdir(path2):
                print('\033[31m' + '[FAIL]' + '\033[0m', end='')
                print(" %s"%path2);
            else:
                print('\033[32m' + '[SUCCESS]' + '\033[0m', end='')
                print(" %s"%path2);

# case2 : directory don't have them
for line in dir_name2:
    path = env + '/' + line
    if os.listdir(path):
        print('\033[31m' + '[FAIL]' + '\033[0m', end='')
        print(" %s"%path);
    else:
        print('\033[32m' + '[SUCCESS]' + '\033[0m', end='')
        print(" %s"%path);

print("");