# 04 - Advanced Techniques

## Goals
- Edit history responsibly.
- Recover lost work.
- Investigate regressions efficiently.

## Interactive rebase
Use to reorder, squash, split, or reword commits before merge.

```bash
git rebase -i HEAD~5
```

Common actions in the editor:
- pick: keep commit as is.
- reword: edit message.
- squash: combine with previous commit.
- fixup: combine and discard commit message.
- drop: remove commit.

## Cherry-pick
Apply a specific commit from another branch.

```bash
git cherry-pick <commit_sha>
```

## Reflog rescue
Find references to where HEAD pointed in recent history.

```bash
git reflog
git switch -c rescue-branch <reflog_sha>
```

## Bisect for regression hunting
```bash
git bisect start
git bisect bad
git bisect good <known_good_sha>
# test each suggested commit and mark good or bad
git bisect reset
```

## Reset and restore strategy
- restore: recover file content safely.
- reset --soft: move HEAD, keep staged content.
- reset --mixed: move HEAD, unstage content.
- reset --hard: destructive, use with care.

## Hook examples
Use hooks to automate checks.
- pre-commit: run lint and formatting.
- pre-push: run tests.

## Advanced safety rules
- Prefer force-with-lease over force.
- Never rewrite shared public history without agreement.
- Create backup branch before risky history edits.
