import os

# path & file
env = os.getenv("ARKCDC_HOME")
path1 = env + "/conf/agent.conf"
path2 = env + "/conf/conn/conn_sample.conn"
path3 = env + "/conf/global.conf"
path4 = env + "/conf/extract/extract_conf.sample"
path5 = env + "/conf/send/send_conf.sample"
path6 = env + "/conf/post/post_conf.sample"
path7 = env + "/conf/mapper/extract_map.sample"
path8 = env + "/conf/mapper/post_map.sample"

# func
def isfile_check(path):
    if os.path.isfile(path):
        print('\033[32m' + '[SUCCESS]' + '\033[0m', end='')
        print(" %s"%path);
    else:
        print('\033[31m' + '[FAIL]' + '\033[0m', end='')
        print(" %s"%path);

print('\033[36m' + '# SAMPLE FILE CEHCK' + '\033[0m');

for i in range(1, 9):
    isfile_check(globals()['path' + str(i)])

print("");