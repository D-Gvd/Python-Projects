# Connecting a new device: 

1. Create a new empty folder(i.e.Folder A).
2. Change directory to Folder A.
3. git clone https://github.com/username/repo-name.git (change "username" & "repo-name")

    To check:
    1. cd repo-name
    2. git remote -v

# For multiple accounts:

## Configure User
1. cd to Folder A
2. git config user.name "New Name"
3. git config user.email "new-email@example.com"

    To check:
    1. git config user.name
    2. git config user.email

4. Generate SSH keys for account/s:

    1. Open CMD on admin mode.
    2. "ssh-keygen -t ed25519 -C "email_of_account_A" C:/Users/username/.ssh/id_github_A"

5. Add public key/s to GitHUb account:

    1. Locate the file created in step 4, open with notepad then copy contents.
    2. GithHub -> Settings -> SSH Keys -> New Key, past contents here. 

6. Create SSH config file (i.e. "config", no file extension) in the same directory above. 
7. Paste the following:

    Host Account-A (Alias, can be changed)
        HostName github.com
        User git
        IdentifyFile  "C:/Users/username/.ssh/id_github_A"

    Host Account-B (Alias, can be changed)
        HostName github.com
        User git
        IdentifyFile  "C:/Users/username/.ssh/id_github_B"

8. Set which account the local folder will use:

    git remote set-url origin git@Account-A:GH-username/repo-name.git

    To check:
        ssh -T git@github-A

# Making commits:

1. git status
2. git add . (adds all files) / git add file-name.txt (for single files)
3. git commit -m "Commit message"
    *If changes were only made to files that Git is already tracking (have been committed before):
    git commit -am "Commit message"

4. git push -u origin main
    *for subsequent pushes:
    git push
