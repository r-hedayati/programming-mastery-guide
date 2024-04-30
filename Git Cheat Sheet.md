## Definitions
`GIT - distributed-is-the-new-centralized `
- The major difference between Git and any other VCS (Subversion and friends included) is the way Git thinks about its data (Git take snapshots not differences). 
- Git has three main states that your files can reside in: modified, staged, and committed: 
  - **Working directory (tree):** it contains the current state of the project, including any changes that we've made. 
  - **Staging area**: it contains the changes that have been marked to be included in the next commit.
  - **Git directory:** it contains the history of all the files and changes (in `.git` directory (local directory)).
  
- The basic Git workflow goes something like this:
  1) You `modify` files in your working tree.
  2) You selectively `stage` just those changes you want to be part of your next commit, which adds only those changes to the staging area.
  3) You do a `commit`, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.
- Remember that each file in your **working directory** can be in one of two states: **tracked** or **untracked**. 
  - **Tracked** files are files that were in the last snapshot, as well as any newly staged files; they can be **unmodified**, **modified**, or **staged**. In short, tracked files are files that Git knows about.
  - **Untracked** files are any files in your working directory that were not in your last snapshot and are not in your staging area. In short, everything else.
- **Commit:** it captures a snapshot of the project's currently staged changes.
- **Clone:**
- **Push:**
- **Pull:**
- **Branch:** a pointer to a particular commit. It represents an independent line of development in a project. The default branch that git creates for you when a new repository is initialized is called **MAIN** (**MASTER**). The main branch is commonly used to represent the known good state of a project. So, it is better to commit the last code in there and use another branch for testing.
- **Forking**: a way of creating a copy of the given repo so that it belongs to our user. Our user will be able to push changes to the forked copy, even when we can't push changes to the other repo.
- **Pull request**: after changing and modifying the selected project, we can pull request to notify the developers of that project to apply our changes

## Step-by-Step Procedure
1.  ` git init `: initializing a new git repository for tracking files
2. ` git add <file/directory name>`: adding files to **staging area**
   -  ` git add .`: adding all changes from **working directory** to **staging area** (add precisely this content to the next commit):
3. ` git commit `: adding files to local git repository: 
    - ` git commit -m 'writing your message' `: writing an inline message for the current commit
    - ` git commit -a `: skip staging area
    -  ` git commit -a -m ''writing your message' `: all in once (for small changes)
4. ` git push `: sending last changes to the remote git repository (GitHub/GitLab): 

**Git** should know who **commit** a file. It can be recognizable by using ` gitconfig ` command with one **name** and an **email**. 
> ` git config --global user.name <name>`  
> ` git config --global user.email <email adress>`
> 
We have multiple ` gitconfig ` files, two of which are more usable: 
- ` --global ` : all the repositories settings
- ` --local ` : the current repository setting

## Other git commands
- `git config --global --edit`: if you want to change any `git config` settings (you can see different level of config by changing `--global` to `--local` or `system`)
- `git config --list`: checking your current git settings
- ` git clone <URL>`: target an existing repository and create a clone, or copy of the target repository. A repository can be cloned in the following two ways:
  - HTTPS: using username and password
  - SSH: using SSH key pair and store public key in our profile
- ` git remote add <name> <URL> `: If you want to create a remote repository yourself.
  - name: the reference for the server, which is typically origin
  - URL: grabbed from the GitHub page.
  - ` git remote -v `: verify if you have already set up a remote upstream
- ` git push --set-upstream origin main `: set up your local branch (main) to an associate branch on an indicated remote server (origin).
  - ` -u ` can be substituted with ` --set-upstream`
- ` git pull` : getting the last changes from git remote repository
- ` git status ` : Showing some information of git repository status
- ` git log `: Showing history information of all commits
  - ` git log --oneline `: one line per commit
  - ` git log --graph `: showing commits in a graph
  - ` git log -p `: showing the details of each commit
  - ` git log --stat `: showing some statistic of each commit
- ` git show <git id> `: showing the specific commit using its ID 
- `git diff`: showing the differences between the working directory and .git directory.
  - `git diff --staged` or `git diff --cached`: showing the differences between the working directory and staging are.
  - `git diff <filename/directory>`: if you want the differences of a specific file/directory.
  - `git difftool`: it opens up the diff tool that you have set up (like vscode)
- ` git reset `: remove from staging area
  - ` git reset -p `: using for specific changes
- ` git mv <filename old> <filename new> `: moving/renaming the files in git
- ` git rm <filename>`: removing a specific file 
- - `.gitignore ` file: Often, you’ll have a class of files that you don’t want Git to automatically add or even show you as being untracked. Here is an example of this file, more examples can be found [here](https://github.com/github/gitignore).
  ```
  # ignore all .a files
  *.a

  # but do track lib.a, even though you're ignoring .a files above
  !lib.a

  # only ignore the TODO file in the current directory, not subdir/TODO
  /TODO

  # ignore all files in any directory named build
  build/

  # ignore doc/notes.txt, but not doc/server/arch.txt
  doc/*.txt

  # ignore all .pdf files in the doc/ directory and any of its subdirectories
  doc/**/*.pdf
  ```


## Branching
please click on this [link](https://learngitbranching.js.org/) for understanding git branching using visualization
- ` git checkout -b <branch name> `: Creating new branch
- ` git branch `: showing all branches
- ` git branch -d <branch name> `: delete a specific branch
- ` git branch -r `: looking at the remote branches that our Git repo is currently tracking
- ` git checkout <branch name>` : moving to the specific branch by its name
- ` git merge <branch name> `: merging the specific branch with main branch 
- `git fetch`: This command copies the commits done in the remote repository to the remote branches 
  - The difference between git fetch and git pull: git fetch only fetches remote updates but git pull fetches + merges
  - The difference between git fetch and git remote update: git fetch downloads but the other one shows
  
## Expert commands
- ` git add -p `: show the difference before adding to the staging area.
- ` git commit --amend `: allow us to modify and add changes to the most recent commit. 
  - Avoid amending commits that have already been made public because it will overwrite the previous commit. 
- ` git revert `: used for undoing changes to a repository's commit history. When a bad commit happen, we can undo it using this command and keep the bad commit in the commits' history
  - ` git revert <commit id> `: using for specific commit
- ` git remote show <origin or other name> `: complete information about remote repository or specific rep
- ` git remote update `: get the contents of a remote branch without auto merging
- ` diff <filename 1> <filename 2> `: show the difference between two codes
  - ` -u `: unified version, showing better 
  - `wdiff`, `meld`, `KDiff3`, and `vimdiff` are other tools
  - `git diff`: helps us to track the difference before committing
    - ` git diff <filename>`: track specific file





