## List of Contents
- [List of Contents](#list-of-contents)
- [Definitions](#definitions)
- [Step-by-Step Procedure](#step-by-step-procedure)
- [Other Git Commands](#other-git-commands)
  - [Log and History](#log-and-history)
  - [Status and Changes](#status-and-changes)
  - [Undoing Changes and Deleting Files](#undoing-changes-and-deleting-files)
  - [gitignore](#gitignore)
  - [Remote Repositories](#remote-repositories)
  - [Tagging and Aliases](#tagging-and-aliases)
- [Branching](#branching)
  - [Merging branches](#merging-branches)

> Best materials to start:
- [Pro Git](https://git-scm.com/book/en/v2)
- [Git Pocket Guide](https://www.amazon.com/Git-Pocket-Guide-Richard-Silverman/dp/1449325866)
- Website to play with git: [Git School](https://git-school.github.io/visualizing-git/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

## Definitions

> GIT - distributed-is-the-new-centralized

- The major difference between Git and any other VCS (Subversion and friends included) is the way Git thinks about its data (Git take snapshots not differences).
- Git has three main states that your files can reside in: modified, staged, and committed:
  - **Working directory (tree):** it contains the current state of the project, including any changes that we've made.
  - **Staging area**: it contains the changes that have been marked to be included in the next commit.
    - The schematic of relation between working directory, staging area, and local repository is as follows:

      ```
      Working directory -> Staging area -> Local repository
      ```

      - Between working directory and staging area, we have `git add` command, and between staging area and local repository, we have `git commit` command.

> The basic Git workflow goes something like this:
  1) You `modify` files in your working tree.
  2) You selectively `stage` just those changes you want to be part of your next commit, which adds only those changes to the staging area.
  3) You do a `commit`, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.
- Remember that each file in your **working directory** can be in one of two states: **tracked** or **untracked**.
  - **Tracked** files are files that were in the last snapshot, as well as any newly staged files; they can be **unmodified**, **modified**, or **staged**. In short, tracked files are files that Git knows about.
  - **Untracked** files are any files in your working directory that were not in your last snapshot and are not in your staging area. In short, everything else.
- **Git directory:** it contains the history of all the files and changes (in `.git` directory (local directory)).
- **Commit:** it captures a snapshot of the project's currently staged changes. Committed snapshots can be thought of as **“safe”** versions of a project.
- **HEAD**: it is a reference (pointer) to the last commit in the currently checked-out branch.
- **Clone:** it creates a copy of an existing Git repository.
- **Push:** it sends the committed changes to a remote repository.
- **Pull:** it fetches and merges changes on the remote server to your working directory.
- **Branch:** a pointer to a particular commit.
  - It represents an independent line of development in a project. The default branch that git creates for you when a new repository is initialized is called **MAIN** (**MASTER**). The main branch is commonly used to represent the known good state of a project. So, it is better to commit the last code in there and use another branch for testing.
- **Forking**: a way of creating a copy of the given repo so that it belongs to our user. Our user will be able to push changes to the forked copy, even when we can't push changes to the other repo.
- **Pull request**: after changing and modifying the selected project, we can pull request to notify the developers of that project to apply our changes

## Step-by-Step Procedure

1. ` git init `: initializing a new git repository for tracking files (in local directory)
2. `git add <file/directory name>`: adding files to **staging area**
   - `git add .`: adding all changes from **working directory** to **staging area** (add precisely this content to the next commit):
3. ` git commit `: adding files to local git repository:
    - ` git commit -m 'writing your message' `: writing an inline message for the current commit
    - ` git commit -a `: skip staging area
    - ` git commit -a -m ''writing your message' `: all in once (for small changes)
4. ` git push `: sending last changes to the remote git repository (GitHub/GitLab):

**Git** should know who **commit** a file. It can be recognizable by using ` gitconfig ` command with one **name** and an **email**.
> `git config --global user.name <name>`  
> `git config --global user.email <email adress>`

We have multiple ` gitconfig ` files, two of which are more usable:

- ` --global ` : all the repositories settings
- ` --local ` : the current repository setting

**Notes:**
- `git config --global --edit`: if you want to change any `git config` settings (you can see different level of config by changing `--global` to `--local` or `system`)
- `git config --list`: checking your current git settings

## Other Git Commands

### Log and History
In Git, the history of commits is stored in a directed acyclic graph (DAG) structure. Each commit points to its parent commit(s), and this allows you to traverse the history of the repository.

- ` git log `: showing history information of **all** commits
  - ` git log -p `: showing the **details** of each commit
    - `git log -p -n <number>`: showing the last `<number>` commits
  - ` git log --stat `: showing some statistic of each commit. This shows information between `git log` and `git log -p`
  - ` git log --oneline `: one line per commit
  - ` git log --graph `: showing commits in a graph. This is useful when you have multiple branches.
    - `git log --pretty=format:"%h - %an, %ar : %s"`: showing the commits in a specific format. You can find more formats [here](https://git-scm.com/docs/git-log#_pretty_formats).
    - `git log --pretty=format:"%h %s" --graph`: showing the commits in a graph with a specific format
  - `git log --since="2 weeks ago"`: showing the commits in the last two weeks
  - `git log -S "<string>"`: showing the commits that contain the specific string. For example `git log -S "hello"` shows the commits that contain the word "hello".

### Status and Changes

- ` git status ` : Showing some information of git repository status 
  - `git status -s`: showing the status in a short format
  - `git status --ignored`: showing the ignored files
- ` git show <git id> `: showing the specific commit using its ID
- ` git add -p `: show the difference before adding to the staging area.

- ` diff <filename 1> <filename 2> `: show the difference between two codes
  - ` -u `: unified version, showing better
  - `wdiff`, `meld`, `KDiff3`, and `vimdiff` are other tools
- `git diff`: showing the differences between the working directory and staging area. 
  - `git diff --staged` or `git diff --cached`: showing the differences between the working directory and the last commit.
  - `git diff <filename/directory>`: if you want the differences of a specific file/directory.
  - `git difftool`: it opens up the diff tool that you have set up (like VSCode) 
    - To setup `difftool` in VSCode, you can use the following command:
     ```
      git config --global diff.tool vscode
      git config --global difftool.vscode.cmd "code --wait --diff $LOCAL $REMOTE"
      ```

### Undoing Changes and Deleting Files

- ` git reset `: remove from staging area
  - ` git reset -p `: using for specific changes
- ` git mv <filename old> <filename new> `: moving/renaming the files in git
- `git rm <filename>`: removing a specific file and also removing it from the staging area
  - Difference between `git rm` and `rm`: `git rm` removes the file from the staging area and the working directory, but `rm` only removes the file from the working directory.
  - `git rm --cached <filename>`: removing the file from the staging area but keeping it in the working directory
  - `git rm -f <filename>`: removing the file from the staging area and the working directory forcefully (from hard disk).
- `git mv <filename old> <filename new>`: moving/renaming the files in git
  - The difference between `git mv` and `mv`: `git mv` moves the file in the staging area and the working directory, but `mv` only moves the file in the working directory.
- `git commit --amend`: allow us to modify and add changes to the most recent commit.
  - Avoid amending commits that have already been made public because it will overwrite the previous commit.
  - `git commit --amend --no-edit`: adding changes to the last commit without changing the commit message. (the previous message will be used)
- `git reset <filename>`: removing the file from the staging area. (staged to untracked)
- `git checkout -- <filename>`: removing the changes from the working directory. This command is used when you want to remove the changes that you have made in the working directory. (modified to unmodified(last snapshot))

- ` git revert `: used for undoing changes to a repository's commit history. When a bad commit happen, we can undo it using this command and keep the bad commit in the commits' history
  - ` git revert <commit id> `: using for specific commit


### gitignore
`.gitignore` is a file that tells Git which files (or directories) to ignore in a project. It is useful when you have files that you don't want to track in your repository, such as temporary files, log files, or build artifacts. Here is an example of this file, more examples can be found [here](https://github.com/github/gitignore).

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

### Remote Repositories

Remote repositories are versions of your project that are hosted on the internet or another network. You can have multiple remote repositories, and you can push and pull changes to and from them.

- `git clone <URL>`: target an existing repository and create a clone, or copy of the target repository. A repository can be cloned in the following two ways:
  - HTTPS: using username and password
  - SSH: using SSH key pair and store public key in our profile

You can connect your local repository to a remote repository. The remote repository can be on GitHub, GitLab, Bitbucket, or any other Git server.
You can create a new repo on these Git servers and connect your local repo to the remote repo using the following commands:

- First, **checking** the remote repositories that your local repository is connected to:
  - `git remote -v`
  - if you need more details about the remote repository:
    - `git remote show <remote name>`
  - To delete a remote repository:
    - `git remote remove <remote name>`
  - To rename a remote repository:
    - `git remote rename <old name> <new name>`
- **Adding** the remote repository (by default, the remote repository is called `origin`):
  - `git remote add origin <URL>`
  - you can add multiple remote repositories to your local repository (this is useful when you want to push your changes to multiple remote repositories)
    - `git remote add <name> <URL>`
  - if you want to remove a remote repository:
    - `git remote remove <name>`
- **Fetching** the changes from the remote repository:
  - `git fetch <remote name>`
    - This command pulls the data to your local repository but does not merge it with your local repository. It only updates the remote tracking branches.
  - `git fetch` is used to update the remote tracking branches.
    - ` git remote update `: get the contents of a remote branch without auto merging
- **Pushing** the changes to the remote repository:
  - `git push <remote name> <branch name in remote repo>`
  - Before that you should set up the upstream branch:
    - `git push --set-upstream origin main`
  - `git push` is used to update the remote repository with the changes that you have made in your local repository.
  - For example, you can delete a remote branch using the following command:
    - `git push <remote name> --delete <branch name>`
  - If you want to push all branches to the remote repository:
    - `git push --all <remote name>`
  - If you want to push all tags to the remote repository:
    - `git push --tags <remote name>`

Or you can **fork** a repo from GitHub and **connect your local repo** to the forked repo using the following commands:

- **Forking** a repo from GitHub:
  - Go to the GitHub page of the repo that you want to fork.
  - Click on the `Fork` button.
  - This will create a copy of the repo in your GitHub account.
  - Copy the URL of the forked repo.
  - Clone the forked repo to your local machine:
    - `git clone <URL>`
    - `cd <repo name>`
\- Connect your local repo to the forked repo:
  - `git remote add upstream <URL>`
  - This command adds the forked repo as a remote repository to your local repo.
  - You can now push your changes to the forked repo using the `git push` command.

 
- `git pull` : getting the last changes from git remote repository


### Tagging and Aliases

- `git tag` : showing the tags. Tags are used to mark specific points in the history of a repository.
  - `git tag -a <tag name> -m <message>`: adding a tag to the last commit
  - `git tag -a <tag name> <commit id> -m <message>`: adding a tag to a specific commit
  - `git tag -d <tag name>`: deleting a tag
  - `git push origin <tag name>`: pushing a tag to the remote repository
  - `git push origin --tags`: pushing all tags to the remote repository
  - `git push origin :refs/tags/<tag name>`: deleting a tag from the remote repository
  - In Github, you can create a release from a tag. This is useful when you want to create a release of your project.
- `git alias`: creating a shortcut for a command. This is useful when you want to create a shortcut for a long command.
  - `git config --global alias.<alias name> <command>`
  - For example, if you want to create an alias for the `git status` command:
    - `git config --global alias.last 'log -1`
  - Sometimes you may want to create an alias for a command that takes arguments. In this case, you can use the following syntax:
    - `git config --global alias.<alias name> '!f() { <command> $1; }; f'`
    - For example, if you want to create an alias for the `git show` command:
      - `git config --global alias.show '!f() { git show $1; }; f'`

## Branching

Branching is a feature available in most modern version control systems. Git branches are effectively a pointer to a snapshot of your changes. When you want to add a new feature or fix a bug—no matter how big or how small—you spawn a new branch to encapsulate your changes. This makes sure that unstable code is never committed to the main codebase, and it also allows you to clean up your feature’s history before merging it into the main branch.

- Each commit has a parent commit, except the first commit, which has no parent. Also, merging two branches creates a new commit with two parents.
- `HEAD` is a reference to the current branch (or commit). When you switch branches with `git checkout`, the `HEAD` is updated to point to the new branch.

> Please click on this [link](https://learngitbranching.js.org/) for understanding git branching using visualization

- ` git branch `: showing all branches
  - **NOTE:** if you create a branch in your **local** repository, the name will be `master` by default. But if you create a branch in a **remote** repository, the name will be `main` by default.
- ` git branch <branch name> `: Creating new branch
  - ` git branch -d <branch name> `: delete a specific branch
  - ` git branch -r `: looking at the remote branches that our Git repo is currently tracking
  - ` git branch -v`: showing the last commit on each branch
  - ` git branch --merged `: showing the branches that are already merged with the current branch
  - ` git branch --no-merged `: showing the branches that are not merged with the current branch
  - ` git branch -a`: showing all branches (local and remote)
- `git checkout <branch name>` : switching to a specific branch
  - **NOTE:** Don't forget that `git checkout <filename>` is used for removing the changes from the working directory.
  - `git checkout -b <branch name>`: creating a new branch and switching to it
  - `git checkout --track <remote branch name>`: creating a new branch that tracks the remote branch 
  - or we can use `git push -u <remote name> <branch name>` to create a new branch in the remote repository and set the upstream branch
- `git fetch`: This command copies the commits done in the remote repository to the remote branches. git fetch does not merge the changes into your local branches. It only updates the remote tracking branches.
  - The difference between git fetch and git pull: git fetch only fetches remote updates but git pull fetches + merges
  - The difference between git fetch and git remote update: git fetch downloads but the other one shows
  
### Merging branches 
Merging is the process of taking the changes from one branch and integrating them into another. This is typically done when a feature is complete and ready to be added to the main codebase.
 - **Fast-forward merging**: This is the simplest type of merging. When you merge a branch into another branch, Git will simply move the pointer of the branch you are merging into to the last commit of the branch you are merging. This is called a fast-forward merge because Git can move the pointer forward in a straight line. Here is the schematic of a fast-forward merge:
 ```
   A---B---C (main)
          \
           D (feature)
   ```
   - After merging the feature branch into the main branch, the schematic will look like this:
   ```
   A---B---C---D (main)
   ```

- ` git merge <branch name> `: merging the specific branch with main branch 
- ` git merge -d <branch name> `: deleting the branch after merging (this will be done only if the branch is merged successfully)
  - ` git merge -D <branch name> `: force deleting the branch after merging

  **Diverge merging**: This is a more complex type of merging. When you merge a branch into another branch, Git will create a new commit that combines the changes from both branches. This is called a diverged merge because Git has to diverge from the main branch to create the new commit. Here is the schematic of a diverged merge:
  ```
    A---B---C (main)
            \ 
            D---E (feature)
    ```
    - After merging the feature branch into the main branch, the schematic will look like this:
    ```
    A---B---C---F (main)
            \   /
            D---E (feature)
    ```
    - In this case, `F` is the new commit that combines the changes from both branches.
  

> Note: We have some long-running branches like `develop` and `release` branches. The `develop` branch is used for developing new features, and the `release` branch is used for releasing new features. The `master` branch is used for the production-ready code. These branches are mostly used in the GitFlow workflow without being deleted. 
> However, the other branches like `feature`, `issue`, and `bugfix` branches are short-lived branches that are created from the `develop` branch and merged back into the `develop` branch after the feature, issue, or bugfix is complete. These branches are deleted after being merged back into the `develop` branch.

### Rebasing
Rebasing is an alternative to merging. It is the process of moving or combining a sequence of commits to a new base commit. Rebasing is typically used to keep a feature branch up to date with the main branch. For example, if you are working on a feature branch and the main branch has been updated with new commits, you can rebase your feature branch onto the main branch to incorporate the new commits.


- `git rebase <branch name>`: rebasing the current branch onto the specified branch
- `git rebase -i <commit id>`: interactive rebase. This command allows you to edit, delete, or squash commits.
- `git rebase --abort`: aborting the rebase process and returning to the state
- `git rebase --continue`: continuing the rebase process after resolving conflicts
- `git rebase --skip`: skipping the current commit and continuing the rebase process
- `git pull --rebase`: pulling the changes from the remote repository and rebasing the current branch onto the remote branch
- `git rebase -i HEAD~n`: rebasing the last n commits interactively
- `git rebase --onto <new base> <old base> <branch name>`: rebasing the specified branch onto the new base, starting from the old base


> Please note that when you push a commit, do not rebase it if it has already been pushed to the remote repository. Rebasing rewrites the commit history, and this can cause problems for other developers who have already pulled the original commits. If you need to rebase a branch that has already been pushed, you should use `git push --force` to overwrite the remote branch with your local branch. However, this should be done with caution and only if you are sure that no one else is working on the same branch.

#### Rebase vs Merge
- **Rebase**: It rewrites the commit history by moving the commits to a new base commit. This creates a linear commit history and makes it easier to understand the changes made in the branch. However, it can cause problems if the branch has already been pushed to the remote repository, as it rewrites the commit history.
- **Merge**: It combines the changes from two branches by creating a new commit that has two parent commits. This preserves the commit history and shows the relationship between the branches. However, it can create a more complex commit history with multiple branches and merge commits.

> In general, it is recommended to use rebase for short-lived branches and merge for long-lived branches. Rebase is useful for keeping a feature branch up to date with the main branch, while merge is useful for combining changes from multiple branches. 
> Also, it is recommended to use rebase when you want to keep a clean commit history and merge when you want to preserve the commit history and show the relationship between the branches.

### Git conflict:
 A conflict occurs when two branches have changed the same part of the same file. Git will not be able to automatically merge the changes, and you will have to resolve the conflict manually.
  - You can use `git status` to see which files have conflicts.
  - You can use `git diff` to see the differences between the conflicting changes.
  - You can use `git mergetool` to open a visual merge tool to help you resolve the conflict.
  - After resolving the conflict, you can use `git add` to mark the conflict as resolved.
  - You can then use `git commit` to create a new commit that resolves the conflict.
  - Or you can use `git merge --abort` to abort the merge and go back to the state before the merge.

## Distributed Git
Git is a distributed version control system, which means that every developer has a complete copy of the repository on their local machine. This allows developers to work offline and commit changes without needing to be connected to a central server. When they are ready, they can push their changes to the remote repository.

The distributed nature of Git allows for greater flexibility and collaboration among developers. Each developer can work on their own branch, make changes, and push those changes to the remote repository without affecting other developers' work. This makes it easier to collaborate on large projects and manage multiple features or bug fixes simultaneously.

- The project maintainer pushes to their public repository, and other developers can pull from it.
- A contributor clones that public repository, makes changes, and pushes them to their own forked repository (public copy).
- The contributor then creates a pull request to the original repository, which the maintainer can review and merge if they approve the changes.

### Commit Guidelines
- Write clear, concise commit messages that describe the changes made.
- Use the imperative mood in commit messages (e.g., "Fix bug" instead of "Fixed bug").
- Group related changes into a single commit to keep the commit history clean.
- Test your changes before committing to ensure they work as expected.
- Avoid committing large binary files or generated files that can be recreated.
- Use branches for new features or bug fixes to keep the main branch stable.
- Regularly pull changes from the remote repository to stay up to date with the latest code.
- Review your changes before committing to catch any mistakes or unnecessary changes.
- Follow the project's coding style and guidelines to maintain consistency in the codebase. (Hooks can be used to enforce this)
- Avoid committing sensitive information, such as passwords or API keys, to the repository.
- Use tags to mark important releases or milestones in the project.
- Communicate with your team about significant changes or updates to the codebase.
- Keep the commit history clean and organized by using tools like interactive rebase to squash or edit commits before pushing to the remote repository.
- For pull requests, create a new branch for each feature or bug fix, and provide a clear description of the changes made in the pull request.

### Create SSH key for GitHub/GitLab
To create an SSH key for GitHub or GitLab, you can follow these steps:
1. Open a terminal or command prompt.
2. Run the following command to generate a new SSH key:
3. ```bash
    ssh-keygen -t rsa -b 4096 -C "<your_email@example.com>"
    ```
4. When prompted, enter a file name for the key (or press Enter to use the default location).
5. If you want to add a passphrase for extra security, enter it when prompted (or leave it empty for no passphrase).
6. After the key is generated, you can find the public key in the specified file (default is `~/.ssh/id_rsa.pub`).
7. Copy the contents of the public key file to your clipboard:
   ```bash
   cat ~/.ssh/id_rsa.pub
   ```
8. Go to your GitHub or GitLab account settings.
9. Navigate to the SSH keys section.
10. Click on "Add SSH key" or "New SSH key."
11. Paste the copied public key into the provided field.
12. Give the key a title (e.g., "My Laptop SSH Key") and click "Add SSH key" or "Save."
13. Now you can use this SSH key to authenticate with GitHub or GitLab when pushing or pulling changes from your repositories.
