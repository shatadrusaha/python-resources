# 02 - Daily Workflows

## Goals
- Work with branches confidently.
- Integrate changes with merge or rebase.
- Keep local and remote branches in sync.

## Branch-based development
```bash
git switch -c feature/login-form
# ... edit files ...
git add .
git commit -m "feat(auth): add login form layout"
git push -u origin feature/login-form
```

## Keeping up with main
```bash
git switch main
git pull --ff-only
git switch feature/login-form
git merge main
```

## Merge vs rebase
- Use merge when you want to preserve branch history.
- Use rebase when you want a linear history before merging.

### Rebase example
```bash
git switch feature/login-form
git fetch origin
git rebase origin/main
# resolve conflicts if needed
git rebase --continue
git push --force-with-lease
```

## Safe conflict resolution loop
1. Run merge or rebase.
2. Open conflicted files and resolve markers.
3. Stage resolved files with add.
4. Continue with commit, merge --continue, or rebase --continue.
5. Verify with status and log.

## Stash for context switching
```bash
git stash push -m "wip: login form validation"
# switch tasks
git stash list
git stash pop
```

## Useful daily commands
```bash
git switch <branch>
git branch -vv
git fetch --all --prune
git pull --ff-only
git push
git stash
```
