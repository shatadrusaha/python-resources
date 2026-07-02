# 03 - Collaboration on GitHub

## Goals
- Collaborate through pull requests (PRs).
- Write review-friendly commits and PR descriptions.
- Use protected branches and clean merge strategies.

## Recommended team flow
1. Sync main.
2. Create short-lived feature branch.
3. Commit in logical chunks.
4. Push and open PR early.
5. Address feedback with focused follow-up commits.
6. Merge after checks pass.

## Opening a strong PR
Include:
- What changed.
- Why it changed.
- How to test.
- Risks and rollback notes.

## Branch naming examples
- feature/user-profile-card
- fix/token-refresh-bug
- chore/update-ci-cache

## Review checklist
- Does this change solve the stated problem?
- Are tests or validation steps included?
- Are commits readable and scoped?
- Is there hidden coupling or side effects?

## Syncing your branch during review
```bash
git fetch origin
git rebase origin/main
# or merge origin/main
git push --force-with-lease
```

## Tags and releases basics
```bash
git tag -a v1.2.0 -m "Release 1.2.0"
git push origin v1.2.0
```

## GitHub habits that scale
- Require status checks before merge.
- Protect main from direct pushes.
- Prefer squash or rebase merge based on team policy.
