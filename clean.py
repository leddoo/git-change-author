import sys
import os

base_path = sys.path[0]

def remove(name):
    try:
        os.remove(f"{base_path}/{name}")
    except:
        pass

remove("state.txt")
remove("log-old.txt")
remove("log-new.txt")
remove("diff.txt")

