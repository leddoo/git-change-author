import json
import os
import sys
import subprocess

base_path = sys.path[0]


def fail(error):
    print(error, file=sys.stderr)
    f = open(f"{base_path}/FAILED", "w")
    f.write("")
    f.close()
    exit(1)


try:
    f = open(f"{base_path}/state.txt", "r")
except:
    fail("state.txt missing")

contents = json.loads(f.read())
f.close()

i = contents["i"]
dates = contents["dates"]

if i >= len(dates):
    fail("state.txt corrupted")

fail("you forgot to set the author!")
author = "Sunny Day <sunny@day.com>"

command = f"GIT_COMMITTER_DATE=\"{dates[i]}\" git commit --amend --no-edit --author=\"{author}\""

os.system(command)


if i + 1 < len(dates):
    contents["i"] = i + 1

    f = open(f"{base_path}/state.txt", "w")
    f.write(json.dumps(contents))
    f.close()
else:
    os.remove(f"{base_path}/state.txt")

    contents = subprocess.check_output("git log --pretty=fuller".split(" "))
    f = open(f"{base_path}/log-new.txt", "wb")
    f.write(contents)
    f.close()

    contents = subprocess.run([
        f"diff",
        f"{base_path}/log-old.txt",
        f"{base_path}/log-new.txt"], stdout=subprocess.PIPE).stdout
    f = open(f"{base_path}/diff.txt", "wb")
    f.write(contents)
    f.close()

