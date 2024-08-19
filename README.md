## GIT
It is Source Code Management (SCM) system which is used for version control.

1. While working on any project we need to initialize the git ``` git init ```
2. Then we add all our working files and folder (directory) to staging area with ``` git add . ```
3. After that we can take the snapshot of current current version or whatever code we have creadted
with commit command ``` git commit -m "your message" ```. It also create one hash key (alphanewmeric value)
4. These all process create local repo of our code.
5. Then we push the code to central repo ``` git push -u origin main ```

## Git and Github workflow diagram
![alt text](github.jpg?raw=true "Git and Github workflow")"{width=400px, height=400px}"

## CVCS -  Central version control system
Here people adds all their code to the central repo which can give issue for any small issue in code 

## DVCS  - Distributed version control system
Here people can create local repo before pushing to central repo which can help to manage together with team
and then push to central repo.
So we can use ``` git pull repo-link``` command to see the any changes done by any other developer in the central repo.

## Git Branching
Git branching allows developers to diverge/change from the production version of code to fix a bug or add a feature. Developers create branches to work with a copy of the code without modifying the existing version. You create branches to isolate your code changes, which you test before merging to the main branch.

This branching function is what makes Git really powerful. Multiple people create separate branches to work on their code and merge their changes into the main branch. Branches are meant to be temporary and should be deleted when work is completed.

Check out [Branching Blog](https://www.varonis.com/blog/git-branching) for complete understanding of Branching.

## Git commands
1. git status - checks status od commit, tracked and unstracked file, and related next commands as well
