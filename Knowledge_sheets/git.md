# 🧠 Git Cheat Sheet

## 🔸 1. INITIAL SETUP

### Configure user identity
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Initialize a repository
```bash
git init --bare ~/repos/myproject.git
```
Creates an empty repository ending with `.git`.  
Used for shared or remote repos (e.g. on a server).

### Clone an existing repository
```bash
git clone ~/repos/myproject.git myproject
# or from an online repo:
git clone git@github.com:user/project.git
```

---

## 🔸 2. LOCAL WORKFLOW

### Check repository status
```bash
git status
```
Shows changes, untracked files, and current branch.

### Stage files (add to staging area)
```bash
git add file.py
git rm file.py            # remove file from repo
git rm --cached data.csv  # untrack a file without deleting it
```

### Ignore files
Create a `.gitignore` file:
```bash
touch .gitignore
```

Example `.gitignore` for data scientists:
```
# Data & temp files
data/
*.csv
*.parquet
*.pkl
*.h5
*.log

# Notebooks & caches
.ipynb_checkpoints/
__pycache__/
.env
```

### Commit changes
```bash
git commit -m "meaningful message"
git commit -am "commit tracked changes directly"
```

### View history
```bash
git log
```

---

## 🔸 3. REMOTE OPERATIONS

### Push / Pull
```bash
git push
git pull
```

### Fix “no upstream branch” warning
```bash
# Option 1: push and set upstream once
git push -u origin HEAD

# Option 2: make it default
git config --global push.autoSetupRemote true
```

---

## 🔸 4. SSH CONNECTIONS

### How it works
SSH provides secure authentication with a **public/private key pair**.

### Steps
1. Generate a key pair:
   ```bash
   ssh-keygen -t ed25519 -C "your.email@example.com"
   ```
2. Add your public key to GitHub/GitLab:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```
3. Test connection:
   ```bash
   ssh -T git@github.com
   ```

Once configured, you can use SSH URLs:
```bash
git clone git@github.com:user/project.git
```

🔗 Free Git tutorial:  
[Git Scenarios — Dubreu Data Formations](https://dubreu-data-formations.notion.site/Git-Scenarios-1d97799fdd534182aace0920279e8e56)

---

## 🔸 5. BRANCHING & MERGING

### Create and switch branches
```bash
git branch new_branch
git checkout -b new_branch  # create and switch in one step
```

### List and manage branches
```bash
git branch         # list branches
git checkout main  # switch to branch
git branch -d old_branch
git checkout -     # switch to previous branch
```

### Push a new branch to remote
```bash
git push --set-upstream origin new_branch
```

---

## 🔸 6. WORKFLOW IN A TEAM (PULL REQUESTS)

### Typical company workflow
1. **Start from main/develop**
   ```bash
   git checkout main
   git pull
   ```
2. **Create a new branch**
   ```bash
   git checkout -b feature/my_feature
   ```
3. **Make your code changes**
4. **Add and commit**
   ```bash
   git add .
   git commit -m "Implement new feature"
   ```
5. **Push branch to GitHub**
   ```bash
   git push
   ```
6. **Create a Pull Request (PR)**
   - On GitHub/GitLab, open your branch  
   - Click “Compare & pull request”
   - Choose target branch (`main` or `develop`)
   - Add reviewers or assignees  
7. **Review process**
   - Your colleague reviews and approves  
   - If accepted → **Merge PR**
   - If conflicts → resolve (see below)

---

## 🔸 7. FIXING ISSUES & DANGEROUS COMMANDS

### Reset to previous commit (⚠️ destructive)
```bash
git reset --hard HEAD^
```
Reverts all local changes to the previous commit.

### Force push (use with care)
```bash
git push -f
```
Overwrites history on remote — **never use on shared branches**.

### Amend last commit
```bash
git commit --amend
```
Modify the last commit message or add forgotten changes.

---

## 🔸 8. CONFLICT RESOLUTION

### What is a conflict?
A conflict happens when two branches modify the same part of a file differently.  
It occurs during `git merge` or `git rebase`.

Conflict markers look like:
```text
<<<<<<< HEAD
Your version
=======
Their version
>>>>>>> main
```

### Resolve conflicts
1. Manually edit the file to keep the correct version  
2. Mark as resolved:
   ```bash
   git add <file>
   ```
3. Continue the merge/rebase:
   ```bash
   git rebase --continue
   ```

---

## 🔸 9. REBASE & MERGE

### Rebase onto main
```bash
git fetch origin
git rebase origin/main
```
Applies your commits on top of the updated main branch.

### Merge commit
```bash
git merge main
```
Creates a merge commit preserving commit timestamps.

---

## 🔸 9bis. DIFFERENCE BETWEEN MERGE AND REBASE

Both `merge` and `rebase` are used to integrate changes from one branch into another,  
but they work differently and have distinct effects on the commit history.

### 🔹 `git merge`
**Purpose:** Combine two branches while preserving both histories.  
It creates a **new “merge commit”** that links the two histories.

```bash
git checkout main
git merge feature/login
```

**Pros:**
- Keeps the true history of all commits.  
- Useful in team projects where preserving context matters.  
- Simple and non-destructive.

**Cons:**
- History can become cluttered with many merge commits.  
- Harder to read in complex projects.

**Visual example:**
```
A---B---C  (main)
           D---E  (feature)
               M    ← merge commit
```

### 🔹 `git rebase`
**Purpose:** Reapply commits from one branch on top of another —  
rewriting history to create a **linear timeline**.

```bash
git checkout feature/login
git rebase main
```

**Pros:**
- Produces a **clean, linear history** (no merge commits).  
- Easier to follow project evolution.

**Cons:**
- Rewrites commit hashes (changes history).  
- **Never rebase a shared branch** — it can break others’ work.

**Visual example:**
```
Before rebase:
A---B---C  (main)
           D---E  (feature)

After rebase:
A---B---C---D'---E'  (feature)
```

### 🧭 Summary Table

| Command | Effect | History | Safe for shared branches? | Typical Use |
|:--------|:--------|:---------|:--------------------------|:-------------|
| `git merge` | Combines branches with a merge commit | Preserved (non-linear) | ✅ Yes | Collaborative workflows |
| `git rebase` | Reapplies commits onto another branch | Rewritten (linear) | ⚠️ No | Local cleanup before PR |

💡 **Best Practice:**
> Use `rebase` locally to clean up your branch before pushing.  
> Use `merge` on the main branch (via pull requests) to integrate others’ work safely.

---

## 🔸 10. HISTORY & HASHES

Each commit is identified by a **SHA-1 hash** (unique 40-character string).  
The hash depends on:
- Commit content  
- Author  
- Timestamp  
- Parent commit

View the history:
```bash
git log --oneline --graph --decorate
```

---

## 🔸 11. SUMMARY COMMANDS TABLE

| Action | Command | Description |
|:-------|:---------|:-------------|
| Initialize repo | `git init` | Create a new local repository |
| Clone repo | `git clone <url>` | Copy a remote repository |
| Check status | `git status` | View current changes |
| Stage changes | `git add <file>` | Add to staging area |
| Commit | `git commit -m "msg"` | Save staged changes |
| View history | `git log` | Show commit history |
| Branch creation | `git checkout -b <branch>` | Create and switch |
| Merge branch | `git merge <branch>` | Merge into current |
| Rebase | `git rebase <branch>` | Replay commits on top |
| Push | `git push` | Send changes to remote |
| Pull | `git pull` | Get latest remote updates |
| Reset (⚠️) | `git reset --hard HEAD^` | Undo last commit |
| Amend | `git commit --amend` | Modify last commit |
| Delete branch | `git branch -d <branch>` | Remove local branch |

---

## 💡 PRO TIPS

- Always **pull latest changes** before creating a new branch.  
- Prefer **feature branches** → clean, traceable workflow.  
- Avoid `--force` unless you fully understand its impact.  
- Use **meaningful commit messages**:
  ```
  feat: add login endpoint
  fix: correct CSV parsing bug
  refactor: improve data model naming
  ```

📘 **Free Git Learning Resource:**  
[Git Scenarios — Dubreu Data Formations](https://dubreu-data-formations.notion.site/Git-Scenarios-1d97799fdd534182aace0920279e8e56)

