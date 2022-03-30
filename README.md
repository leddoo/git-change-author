# git-change-author

stupid simple python scripts to change the author of a git repo.
- changes the author of all commits. you could adapt it to change only specific authors.
- preserves AuthorDate & CommitDate.
- pretty slow.
- use at own risk. definitely read the code first and create a backup of your repo.
- should be run under linux or WSL, because windows ~~sucks~~ uses utf16.

usage:
- change `author` in commit.py
- `cd` into the repo where you want to change the author.
- `python3 path-to-this-repo/collect-dates.py`
- `git rebase --root --exec "python3 path-to-this-repo/commit.py"`
- check `path-to-this-repo/diff.txt`
- `git push -f`
- profit.

