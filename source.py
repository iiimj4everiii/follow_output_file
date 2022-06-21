import os
import time
import threading


def write1000(filepath):
    with open(filepath, 'w', buffering=1) as file_obj:
        for count in range(100):
            file_obj.write(str(count) + '\n')

        file_obj.close()


def follow(filepath):
    with open(filepath, 'r') as file_obj:
        file_obj.seek(0, os.SEEK_END)
        while True:
            line = file_obj.readline()

            if not line:
                time.sleep(0.0001)
                continue

            yield line


filepath = 'test.txt'
file_obj = open(filepath, 'w')
file_obj.close()

write_th = threading.Thread(target=write1000, args=[filepath])
write_th.daemon = True
write_th.start()

loglines = follow(filepath)
for line in loglines:
    print(line)
