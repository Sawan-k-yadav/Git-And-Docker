## GIT
It is Source Code Management (SCM) system which is used for version control.

1. While working on any project we need to initialize the git ``` git init ```
2. Then we add all our working files and folder (directory) to staging area with ``` git add . ```
3. After that we can take the snapshot of current version or whatever code we have created
with commit command ``` git commit -m "your message" ```. It also create one hash key (alphanewmeric value) for every commit to track the changes later.
4. These all process create local repo of our code.
5. Then we push the code to central repo ``` git push -u origin main ```

## Git and Github workflow diagram
![alt text](github.jpg?raw=true "Git and Github workflow")

## CVCS -  Central version control system
Here people adds all their code to the central repo which can give issue for any small issue in code and it will difficult to work on the issue. 

## DVCS  - Distributed version control system
Here people can create local repo before pushing to central repo which can help to manage together with team
and then push to central repo.
So we can use ``` git pull repo-link``` command to see the any changes done by any other developer in the central repo.

## Git Branching
Git branching allows developers to diverge/change from the production version of code to fix a bug or add a feature. Developers create branches to work with a copy of the code without modifying the existing version. You create branches to isolate your code changes, which you test before merging to the main branch.

This branching function is what makes Git really powerful. Multiple people create separate branches to work on their code and merge their changes into the main branch. Branches are meant to be temporary and should be deleted when work is completed.

![alt text](what-is-a-merge.gif?raw=true "Branch merging")

Check out [Branching Blog](https://www.varonis.com/blog/git-branching) for complete understanding of Branching.

## Git commands
1.  ```git status ``` - checks status of commit, tracked and unstracked file, and related next commands as well
2. To connect your local repo to central ``` git config --global user.email "github-emailId" ``` and ``` git config --global user.name "username-of-github" ```
3. ``` git config --list ``` - to check add user name and email
4. ``` which git ``` -  to check where my git is available
5. ``` history ``` - to check all the previous commands which we have ran
6. ``` git rm -rf file-name ``` - to delete any file 
7. ``` clear ``` - to clear the git command screen.
8. ``` git log ``` - It will show the details of all commits which we have done. Like hash key value of the 
commit, pointer to main branch (or whichever branch we are working on), email and user name of github, and the
message which have added to that commit.
9. ``` git show <hash key id of any commit which we can get from git log>``` - It will show details of which file is updated and what are the new details added.
10. ``` && ``` - To run to command together we can use && in between.  
11. ``` git reset < . or file-name > ``` - To reset the change which we have added my mistake. Then ``` git status ``` to verify if reset is done. Always recommended to add file in .gitignore if we don't want add in central repo.
12. ``` git branch `` - To check in which branch we are working on.
13. ``` git branch branch-name ``` - To create new branch.
14. ``` git checkout branch-name ``` - To switch to other branch.
15. ``` git merge branch-name ``` - To merge to branch.


