# 🐧 Linux Cheat Sheet Summary

A comprehensive quick reference guide for essential Linux commands and operations.

---

## 📋 Table of Contents
- [🐧 Linux Cheat Sheet Summary](#-linux-cheat-sheet-summary)
  - [📋 Table of Contents](#-table-of-contents)
  - [Command Structure](#command-structure)
  - [Basic System Commands](#basic-system-commands)
  - [Navigation \& Directory Operations](#navigation--directory-operations)
  - [File Operations](#file-operations)
  - [File Viewing \& Editing](#file-viewing--editing)
  - [Text Processing](#text-processing)
  - [Search \& Find](#search--find)
  - [Permissions \& Ownership](#permissions--ownership)
  - [Archive \& Compression](#archive--compression)
  - [Command Customization](#command-customization)
  - [Wildcards](#wildcards)

---

## Command Structure

| **Command** | **Description** |
|-------------|-----------------|
| `command name -options <input>` | Basic command structure |
| `man <command name>` | Command manual |
| `<>` | Mandatory parameter |
| `[]` | Optional parameter |

---

## Basic System Commands

| **Command** | **Description** |
|-------------|-----------------|
| `cal` | View calendar |
| `cal <date>` | View calendar at specific date |
| `date` | Show current date and time |
| `pwd` | Print working directory |
| `which <package name>` | Show which package/binary is being used |
| `echo $PATH` | View all binary file paths (shell path) |
| `history` | View command history |
| `!<number>` | Rerun command number from history |

---

## Navigation & Directory Operations

| **Command** | **Description** |
|-------------|-----------------|
| `cd` | Change to home directory |
| `cd .` | Stay in current directory |
| `cd ..` | Go to parent directory |
| `cd /` | Go to root directory (absolute path) |
| `ls` | List files and directories |
| `ls -F` | List with file type indicators (`/` for directories) |
| `ls -l` | List in long format (detailed) |
| `ls -a` | List all files including hidden ones (starting with `.`) |

---

## File Operations

| **Command** | **Description** |
|-------------|-----------------|
| `file <filename>` | Identify file type |
| `touch <filename>` | Create new empty file |
| `touch {file,image}_{1,2,3}_{.txt,.png}` | Create multiple files with patterns |
| `mkdir <directory>` | Create new directory |
| `echo 'text' > <filename>` | Create text file with content |
| `rm <filename>` | Delete file |
| `rm -r <directory>` | Delete directory recursively |
| `rm -i <filename>` | Delete with confirmation prompt |
| `rmdir <directory>` | Delete empty directory only |
| `cp <source> <destination>` | Copy files/folders |
| `mv <source> <destination>` | Move files/folders |
| `mv <oldname> <newname>` | Rename file |
| `mv -r <source> <destination>` | Move/rename directories |

---

## File Viewing & Editing

| **Command** | **Description** |
|-------------|-----------------|
| `nano <filename>` | Open file in nano text editor |
| `cat <filename>` | Display file contents |
| `cat -n <filename>` | Display file with line numbers |
| `cat <file1> <file2>` | Concatenate and display multiple files |
| `rev <filename>` | Display file contents in reverse |
| `more <filename>` | View file page by page (good for large files) |
| `more -5 <filename>` | Display only first 5 lines |
| `ls -l \| more` | Pipe command output to more |
| `less <filename>` | View file with navigation (better than more) |
| `head <filename>` | Display first 10 lines of file |
| `head -n 5 <filename>` | Display first 5 lines |
| `head -n -5 <filename>` | Display all except last 5 lines |
| `tail <filename>` | Display last 10 lines of file |
| `tail -n 5 <filename>` | Display last 5 lines |
| `head -n 7 <file> \| tail -n 3` | Display lines 5, 6, and 7 |

---

## Text Processing

| **Command** | **Description** |
|-------------|-----------------|
| `sort <filename>` | Sort file contents alphabetically |
| `sort -r <filename>` | Sort in reverse order |
| `sort -n <filename>` | Sort numerically |
| `sort -u <filename>` | Sort and remove duplicates |
| `ls -l \| sort -k 2` | Sort ls output by second column |
| `xargs` | Convert input to command arguments |
| `date \| xargs echo` | Use date output as echo argument |
| `ls \| xargs rm` | Remove files listed by ls |

---

## Search & Find

| **Command** | **Description** |
|-------------|-----------------|
| `find <directory> <options> <term>` | Search for files in directories |
| `grep '<pattern>' <filename>` | Search for pattern in file |
| `grep '<pattern>' <file1> <file2>` | Search in multiple files |
| `grep -r "hello" .` | Recursive search in current directory |
| `grep -i <pattern> <file>` | Case-insensitive search |
| `grep -c <pattern> <file>` | Count matching lines |
| `grep -v <pattern> <file>` | Invert match (non-matching lines) |
| `grep -n <pattern> <file>` | Show line numbers |
| `grep -w <pattern> <file>` | Match whole words only |

---

## Permissions & Ownership

| **Command** | **Description** |
|-------------|-----------------|
| `chmod <permissions> <file>` | Change file permissions |
| `chmod 700 <file>` | Set permissions to rwx------ |
| **Permission Types:** | |
| `-` | Regular file |
| `d` | Directory |
| `l` | Symbolic link |
| **Permission Format:** | `rwxrwxrwx` (user/group/other) |

---

## Archive & Compression

| **Command** | **Description** |
|-------------|-----------------|
| `tar cfv <archive.tar> <files>` | Create tar archive |
| `tar xvf <archive.tar>` | Extract tar archive |
| `zip <archive.zip> <files>` | Create zip archive |
| `unzip <archive.zip>` | Extract zip archive |

---

## Command Customization

| **Command** | **Description** |
|-------------|-----------------|
| `alias <name>="<command>"` | Create temporary command alias |
| `alias ll="ls -l"` | Create temporary `ll` alias |
| Add to `.bashrc` or `.zshrc` | Make alias permanent |

---

## Wildcards

| **Symbol** | **Description** | **Example** |
|------------|-----------------|-------------|
| `*` | Any number of characters | `*.txt` (all .txt files) |
| `?` | Any single character | `file?.txt` (file1.txt, fileA.txt) |
| `[]` | Range of characters | `file[1-3].txt` (file1, file2, file3) |
| `{}` | Match specific items | `file{1,3,5}.txt` |
| `\` | Escape character | `\*` (literal asterisk) |
| `[^]` | Not in range | `file[^2].txt` (any except file2.txt) |

---

> 💡 **Tip**: Use `man <command>` to get detailed information about any command and its options.
