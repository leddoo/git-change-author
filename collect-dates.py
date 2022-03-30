import re
import json
import sys
import subprocess

base_path = sys.path[0]

print(f"state is stored in in {base_path}")

contents = subprocess.check_output("git log --pretty=fuller".split(" "))
contents = str(contents, "utf8")

f = open(f"{base_path}/log-old.txt", "w")
f.write(contents)
f.close()

commits = contents.split("\n\ncommit")
dates = [re.search(r"AuthorDate: (.*)\n", commit).groups()[0] for commit in reversed(commits)]

f = open(f"{base_path}/state.txt", "w")
f.write(json.dumps({"i": 0, "dates": dates}))
f.close()

print(f"collected dates for {len(dates)} commits.")

