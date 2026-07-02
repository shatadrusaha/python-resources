# 06 - Git Cheat Sheet

## Setup
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

## Start and clone
```bash
git init
git clone <url>
```

## Daily status and history
```bash
git status
git log --oneline --graph --decorate --all
git diff
git diff --staged
```

## Add and commit
```bash
git add <file>
git add .
git commit -m "type(scope): message"
```

## Branching
```bash
git switch -c <new-branch>
git switch <branch>
git branch -vv
git branch -d <branch>
```

## Remote sync
```bash
git fetch --all --prune
git pull --ff-only
git push -u origin <branch>
```

## Merge and rebase
```bash
git merge <branch>
git rebase <branch>
git rebase --continue
git rebase --abort
```

## Undo and recovery
```bash
git restore <file>
git restore --staged <file>
git reset --soft HEAD~1
git reset --mixed HEAD~1
git revert <sha>
git reflog
```

## Advanced
```bash
git rebase -i HEAD~N
git cherry-pick <sha>
git bisect start
git stash push -m "wip"
```

## Rules of thumb
- Pull with ff-only to avoid accidental merge commits.
- Use force-with-lease when rebasing published branch history.
- Revert shared history; rewrite only your own branch history.
