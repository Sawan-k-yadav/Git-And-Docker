# GIT
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

Check this [Branching Blog](https://www.varonis.com/blog/git-branching) for complete understanding of Branching.

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
+ ``` git log --oneline ``` - It gives all the commit message with their hash key which we have added till now.
+ ``` git revert <commit id> ``` - It will revert back the git from specific commit (with commit id) to working directory. It will ask message for reverting, after adding you message type ``` :qa! ``` to exit message console page to proceed reverting process.
9. ``` git show <hash key id of any commit which we can get from git log>``` - It will show details of which file is updated and what are the new details added.
10. ``` && ``` - To run to command together we can use && in between.  
11. ``` git reset < . or file-name > ``` - To reset the changes which we have added by mistake back from staging to working directory. Then ``` git status ``` to verify if reset is done. Always recommended to add file in .gitignore if we don't want add in central repo.
12. ``` git branch `` - To check in which branch we are working on.
13. ``` git branch branch-name ``` - To create new branch.
14. ``` git checkout branch-name ``` - To switch to other branch.
15. ``` git merge branch-name ``` - To merge to branch.

+ Note: If I will create any file or do any changes in the code from branchA (other than main branch) then after commit that will not appear in main branch. 
+ Merge Conflit -- It happens when we create or write in a file name with same name from different branch. At the time of merge it give conflict.
To resolve conflict we need to manually go an check/verify both the file content which is coming in conflit. If we resolve the issue if there is any or verify both the file content, remove conflit sign massage(current and incoming changes) from the respective file then add the file and commit the changes again.

![alt text](Git-Conflit.png?raw=true "Git Conflit")

16. ``` git branch -d branch-name ``` - To delete branch.

17. Stashing (Hidding) - Often, when you’ve been working on part of your project, things are in a messy state and you want to switch branches for a bit to work on something else. The problem is, you don’t want to do a commit of half-done work just so you can get back to this point later. The answer to this issue is the git stash command.

+ Read this blog of [Stashing](https://www.varonis.com/blog/git-branching) for more details
+ ``` git stash ``` - To add current file or code which we dont want to commit to the stash storage.
+ ``` git stash list ``` - To see all the stashed file with one id which we have added in stash.
+ ``` git stash apply ``` - If you want to apply one of the older stashes and bring it back for work or commit, you can specify it by naming it, like this: ``` git stash apply stash@{2} ```. If you don’t specify a stash id, Git assumes the most recent stash and tries to apply it.
+ ``` git stash clear ``` - To clear stash workspace or storage from stashed files as does not clean by itself after apply the files and bringing back to work or commits.


# Docker

Docker is a powerful tool for building, running and deploying applications, and the Docker Engine (written in Linux) is the core component that makes it all possible.

##  Virtualization

Virtualization uses software to create an abstraction layer over computer hardware, enabling the division of a single computer's hardware components—such as processors, memory and storage—into multiple virtual machines (VMs). Each VM runs its own operating system (OS) and behaves like an independent computer, even though it is running on just a portion of the actual underlying computer hardware.

It follows that virtualization enables more efficient use of physical computer hardware and allows a greater return on an organization’s hardware investment.
Virtualization enables cloud providers to serve users with their existing physical computer hardware.

Popular Virtualization offered by the companies are VMware, Oracle vertual box etc. 

It runs on ``` Hypervisor ``` - It is the software layer that coordinates VMs. It serves as an interface between the VM and the underlying physical hardware, ensuring that each has access to the physical resources it needs to execute. It also ensures that the VMs don’t interfere with each other by impinging on each other’s memory space or compute cycles. Check this Blog for understanding [Virtualization](https://www.ibm.com/topics/virtualization).

![alt text](Virtualization.png?raw=true "Virtualization")

### <span style="color: red;">Limitation of Virtualization</span>

1. Once we will allocate some OS, RAM and Memory to any VM while doing Virtualization, we cannot increase it futher if required as it is fixed and not dynamic. 
2. Also we cannot remove to make useful for Host OS from which it is created.

## Containerization

Containerization is OS-based virtualization that creates multiple virtual units in the userspace, known as Containers. Containers share the same host kernel but are isolated from each other through private namespaces and resource control mechanisms at the OS level.
It is dynamic, means whenever we need we can increase it resource size like memory, cpu and RAM. Also when we are not using it then we can stop container, so it will be free from resources unlike VMs in virtualization. Check this Blog for understanding [Containerization](https://www.geeksforgeeks.org/containerization-using-docker/).

![alt text](Containerization.png?raw=true "Containerization vs Virtualization")

+ ### Port mapping in Docker
        If we have any container (let say it have flask app) then we cannot use it with our host machine directly with host ip (or local host). Port mapping in Docker is the process of mapping a port on the host machine to a port in a container. This allows users to access applications running inside containers from outside the Docker host. 
        
        To assign port mapping when running a new container, users can use the -p option in the docker run command. The syntax is -p host_port:container_port. For example, to map port 8080 on the host to port 80 inside the container, users can use -p 8080:80. Users can specify multiple port mappings by repeating the -p flag. 


## Docker commands:

1. ``` docker ``` - Run this on cmd to check DOcker installed or not
2. ``` docker version ``` - command provides information about the Docker Engine version installed on your system.
3. ``` docker build -t image_name . ``` -It creates docker image with imagename from local folder (.) .
4. ``` docker images ``` - To see the created images
+ ``` docker rmi -f image_name ``` - To delete any image from the docker image list. ``` -f ``` for force delete.
+ ``` docker rmi -f image_name:tag ``` - To delete with whatever the latest tag is present. latest is default tag is not changed.
5. ``` docker run -d -p host_port:container_port image_name ``` -  To RUN the docker container  in detached mode, mapping a specific port on the host machine to a port within the container.
+ ``` -d``` - It imeans detach mode, meaning it will run in the background and you can continue to use the terminal.
6. ``` docker ps ``` - To check details of runninf container.
+ ``` docker ps -a ``` - To check details of all the containers even if they are running or not.
7. ``` docker stop <container_id> ``` - To stop the docker container.
+ ``` docker rm <container_id> ``` - To stop any container.
+ ``` docker rm $(docker ps -a -q) ``` - To remove all containers at once.
8. To determine memory usage, use the ``` docker stats ``` command to monitor running containers. If find any containers which are not use then we can delete, if needed.

## Additional commands:

9. ``` where docker ``` - To check file and .exe file location of docker
10. ``` docker info ``` - To get the full details of docker which which we have installed.
11. ``` docker -v ``` - To check the version of docker installed.

#### For using docker hub and hosting my images in docker we need to login docker hub from the terminal

12. ``` docker login ``` - To login docker hub from terminal. It will ask user name and password which you have given while created docker hun account online.
13. ``` docker tag image_name user_name/repo_name or image_name ``` -  This allows you to push the image to a remote repository of docker hub.
14. ``` docker push user_name/repo_name or image_name ``` -  This command is used to upload a Docker image to a remote repository, such as Docker Hub. This allows you to share your images with others or use them in different environments.
15. ``` docker pull image_name``` - To pull any docker image and run in your local environment inside container.
16. ``` docker run -i -t image_name file_path_where_we_want_to_run ``` - To run the pulled image. -i for interactive mode, -t for see the details or operations on terminal, file_path can be anything where we want to run pulled the image like /bin/bash for ubuntu etc.
17. ``` docker build -t newimage -f Dockerfile1 . ``` - To build new_image with different docker file. If we have more than one docker file in the project then need to use -f dockerfile_name at the end and then dot(.) for choosing local folder.

Note :
+ If we will take any image from docker hub and run directly on local environment for container then it will search locally if the image is available or not and if it will not get then it will pull from docker hub and then it will run inside container in the given file path. Then do your task with the image commands.
+ In case pulling any image from docker hub (ex: ubuntu) we are intalling complete ubuntu inside container, instead it will just take some instance or files of ubuntu for running inside container and we can use ubunut commands to check all the host system resources with that image.
17. If we have not pulled any image from docker hub and we will try to run any image which is available in docker hub with port mapping then again it will search locally if the image is available or not and if it will not get then it will pull from docker hub and then it will run inside container in the given file path. Then do your task with the image commands.

+ Ex. ``` docker run -p host_port:container_port image_name``` - image_name will be any image from docker hub.

18. Listing running containers with volumes: Use the ``` docker ps -a --format '{{.ID}}\t{{.Image}}\t{{.Mounts}}' ``` command to list all containers with their IDs, images, and mounted volumes.
+ volumes is A persistent storage unit that can be used to store data within containers. It's separate from the image.

##### For running container we have 3 ways

1. Created image with docker file and run inside container
2. Pull docker image from docker hub and run inside container
2. Create image with docker container and run or push on docker hub

#
1. ``` docker run --name container_name -it ubuntu /bin/bash``` - To create container with our choice and run on interactive mode on the terminal (-i -t is same as -it) for image ubuntu and bash terminal.
2. ``` docker diff container_name ``` - To see what are the changes we have done in the image inside container.
3. ``` docker commit container_name new_image_name ``` - This will help to create new image for the already created container (of ubuntu for which we had created container).