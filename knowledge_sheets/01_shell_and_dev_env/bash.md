# 🐚 Bash Command Cheat Sheet

A concise, organized reference of essential Bash commands.  

---

## 📑 Table of Contents
- [Basics](#basics)
- [Navigation](#navigation)
- [Files & Directories](#files--directories)
- [Copy & Move](#copy--move)
- [Users & Permissions](#users--permissions)
- [Viewing & Editing (Vim)](#viewing--editing-vim)
- [Processes](#processes)
- [Scripting & Operators](#scripting--operators)
- [Environment Variables](#environment-variables)
- [Customization (bashrc, aliases, functions)](#customization-bashrc-aliases-functions)
- [Streams & Redirections](#streams--redirections)
- [Package Management](#package-management)
- [Networking](#networking)
- [Compression](#compression)

---

## Basics
```bash
whoami           # Show current user
pwd              # Print working directory
clear            # Clear terminal
reset            # Reset terminal state
command --help   # Show options/help for a command
man <command>    # Open manual page
tldr <command>   # Concise examples (requires install)
which bash       # Path to the bash binary
```

## Navigation
```bash
ls               # List files
ls -a            # Include hidden files (dotfiles)
ls -l            # Long listing (permissions, owner, size, date)
ls -lh           # Long listing with human-readable sizes
ls -lt           # Sort by most recent first

cd <path>        # Change directory
cd               # Go to $HOME
cd -             # Go to previous directory
cd /             # Go to root
.                # Current directory
..               # Parent directory
```

## Files & Directories
```bash
touch file                 # Create empty file (or update timestamp)
echo "text" > file         # Overwrite file with text
echo "text" >> file        # Append text
cat file                   # Print file content

mkdir folder               # Create directory
mkdir Day{1..365}          # Create multiple directories
mkdir -p a/b               # Create parent(s) as needed
mkdir /folder              # Create at root (requires permission)

rmdir emptydir             # Remove empty directory
rm file                    # Remove file
rm -i file                 # Ask before removing
rm -r folder               # Remove directory recursively
rm -ri folder              # Recursive + interactive

trash-cli                  # Safer removal (like Trash) → ~/.local/share/Trash

```

## ls -l fields (example of a symlink):
```bash
lrwxrwxrwx 1 root root 7 Apr 22 2024 bin -> usr/bin
^type/perms ^links ^owner ^group ^size ^date/time ^name -> symlink target
```

## Copy & Move
```bash
cp file path               # Copy file to path
cp -r dir path             # Copy directory recursively
mv source target           # Move/rename file or directory
```

## Users & Permissions
```bash
sudo useradd <user>        # Add a new user (Linux)
chmod +x file              # Add execute for user/group/other
chmod -x file              # Remove execute for all
chmod u+x file             # Add execute for user only
```

## Viewing & Editing (Vim)
```bash
i / I / a / A              # Insert modes (before/line start/after/line end)
o / O                      # New line below / above
Esc                        # Leave insert mode

:w / :q / :wq / :x / :q!   # Write / Quit / Write+Quit / Write+Quit / Force quit
dd / yy / p                # Delete line / Yank line / Paste after
u / Ctrl+r                 # Undo / Redo
/word  + n                 # Search 'word' then next
x                          # Delete character
:                          # Command-line mode
```

## Processes
```bash
Ctrl+Z          # Suspend current process
fg              # Resume most recent suspended job in foreground
htop            # Interactive process viewer (arrows navigate, 'k' to kill)
```

## Scripting & Operators
```bash
#!/bin/bash                 # Shebang: interpreter for script
echo "Hello World"          # Print text
echo "Who am I? $(whoami)"  # Command substitution

now=$(date)                 # Assign command output to variable
echo "Current time: $now"

chmod +x script.sh          # Make executable
./script.sh                 # Run from current directory

cmd1 && cmd2                # Run cmd2 only if cmd1 succeeds
ls /usr/bin/*               # * matches any string
```

## Environment Variables
```bash
echo $HOME                  # Show HOME
printenv                    # List all environment variables
printenv HOME               # Show specific variable
echo $PATH | tr ":" "\n"    # PATH on multiple lines

export ENV="dev"            # Set var (current session only)
export PATH="new:$PATH"     # Prepend to PATH (not persistent)
```

## Python example using env var:
```bash
echo "from os import environ" > envvar.py
echo "print(environ['HOME'])" >> envvar.py
python3 envvar.py
```

## Conda:
```bash
conda activate <env>
conda deactivate
```

## Customization (bashrc, aliases, functions)
```bash
# Aliases
alias hist='history | grep'
alias gco='git commit'

# Functions
cdl () { cd "$1" && ls -lh; }
mcd () { mkdir "$1" && cd "$1"; }
```

## Streams & Redirections
```bash
stdin   # standard input
stdout  # standard output
stderr  # standard error

python3 script.py 2> errors.log   # Redirect errors (stderr) to file
history | grep ssh                # Pipe stdout of history into grep
```

## Package Management
```bash
apt search paint                  # Search packages (Debian/Ubuntu)
sudo apt-get install <pkg>        # Install package

brew install <pkg>                # macOS (Homebrew)
```

## TLDR installation (simplified manuals):
```bash
sudo npm install -g tldr
```

## Networking
```bash
ping example.com                  # Check connectivity & latency
```

## Compression
```bash
zip archive.zip folder/           # Zip folder into archive.zip
```

## Shutdown (Linux):
```bash
sudo shutdown now                 # Power off immediately
```
