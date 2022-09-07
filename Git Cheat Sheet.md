## Definitions
- **Git directory:** it contains the history of all the files and changes.
- **Working directory (tree):** it contains the current state of the project, including any changes that we've made. 
- Staging area: it contains the changes that have been marked to be included in the next commit.
- **Commit:**
- **Clone:**
- **Push:**
- **Pull:**
- **Branch:** a pointer to a particular commit. It represents an independent line of development in a project. The default branch that git creates for you when a new repository is initialized is called **MAIN** (**MASTER**). The main branch is commonly used to represent the known good state of a project. So, it is better to commit the last code in there and use another branch for testing.
- **Forking**: a way of creating a copy of the given repo so that it belongs to our user. Our user will be able to push changes to the forked copy, even when we can't push changes to the other repo.
- **Pull request**: after changing and modifying the selected project, we can pull request to notify the developers of that project to apply our changes

## step-by-step procedure
1. Initializing a new git repository for tracking files: ` git init `
2. Adding files to **staging area**: ` git add <file/directory name>`
   - Adding all changes from working directory to staging area: ` git add *`
3. Adding files to local git repository: ` git commit `
    - ` git commit -m 'writing your message' `
    - Skip staging area: ` git commit -a `
    - All in once (for small changes): ` git commit -a -m ''writing your message' `
4. Sending last changes to the remote git repository (GitHub/GitLab): ` git push `

**git** should know who **commit** a file. It can be recognizable by using ` gitconfig ` command with one **name** and an **email**. 
> ` git config --global user.name <name>`  
> ` git config --global user.email <email adress>`
> 
We have multiple ` gitconfig ` files, two of which are more usable: 
- ` --global ` : all of the repositories settings
- ` --local ` : the current repository setting

## Other git commands
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
- ` git reset `: remove from staging area
  - ` git reset -p `: using for specific changes
- ` git mv <filename old> <filename new> `: moving/renaming the files in git
- ` git rm <filename>`: removing a specific file 


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





