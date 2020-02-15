# 0x01. Shell, permissions
> Holberton School Foundations Curiculum: System Engineering & DevOps - Bash

### Contents
- [Learning Objectives](https://github.com/michedomingo/holberton-system_engineering-devops/tree/master/0x01-shell_permissions/#permissions)
- [Tasks](https://github.com/michedomingo/holberton-system_engineering-devops/tree/master/0x01-shell_permissions/#tasks)
___
<a name="permissions"></a>

### 🤓 Learning Objectives
#### Permissions
- [ ] What do the commands chmod, sudo, su, chown, chgrp do
- [ ] Linux file permissions
- [ ] How to represent each of the three sets of permissions (owner, group, and other) as a single digit
- [ ] How to change permissions, owner and group of a file
- [ ] Why can’t a normal user chown a file
- [ ] How to run a command with root privileges
- [ ] How to change user ID or become superuser
#### Other Man Pages
- [ ] How to create a user
- [ ] How to create a group
- [ ] How to print real and effective user and group IDs
- [ ] How to print the groups a user is in
- [ ] How to print the effective userid
___
<a name="tasks"></a>
## Tasks
> All scripts must be executable and exactly two lines long.

### 0. My name is Betty
- Create a script that changes your user ID to betty.
- File: [0-iam_betty](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x01-shell_permissions/1-who_am_i)

### 1. Who am I
- Write a script that prints the effective userid of the current user.
- File: [1-who_am_i](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x01-shell_permissions/0-iam_betty)

### 2. Groups
- Write a script that prints all the groups the current user is part of.
- File: [1-who_am_i](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x01-shell_permissions/2-groups)

### 3. New owner
- Write a script that changes the owner of the file hello to the user betty.
- File: [3-new_owner](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x01-shell_permissions/3-new_owner)

### 4. Empty!
- Write a script that creates an empty file called hello.
- File: [4-empty](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x01-shell_permissions/4-empty)

### 5. Execute
- Write a script that adds execute permission to the owner of the file hello.
- File: [5-execute](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x01-shell_permissions/5-execute)

### 6. Multiple permissions
- Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
- File: [6-multiple_permissions](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x01-shell_permissions/6-multiple_permissions)

### 7. Everybody!
- Write a script that adds execution permission to the owner, the group owner and the other users, to the file hello - without commas.
- File: [7-everybody](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x01-shell_permissions/7-everybody)

### 8. James Bond
- Write a script that sets the permission to the file hello with Owner/Group - no permission at all, Other users - all the permissions.
- File: [8-James_Bond](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x01-shell_permissions/8-James_Bond)

### 9. John Doe
- Write a script that sets the mode of the file hello to this: -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
- File: [9-John_Doe](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x01-shell_permissions/9-John_Doe)

### 10. Look in the mirror
- Write a script that sets the mode of the file hello the same as olleh’s mode.
- File: [10-mirror_permissions](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x01-shell_permissions/10-mirror_permissions)

### 11. Directories
- Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.
- File: [11-directories_permissions](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x01-shell_permissions/11-directories_permissions)

### 12. More directories
- Create a script that creates a directory called dir_holberton with permissions 751 in the working directory.
- File: [12-directory_permissions](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x01-shell_permissions/12-directory_permissions)

### 13. Change group
- Write a script that changes the group owner to holberton for the file hello.
- File: [13-change_group](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x01-shell_permissions/13-change_group)

### 14. Owner and group
- Write a script that changes the owner to betty and the group owner to holberton for all the files and directories in the working directory.
- File: [14-change_owner_and_group](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x01-shell_permissions/14-change_owner_and_group)

### 15. Symbolic links
- Write a script that changes the owner and the group owner of the file _hello to betty and holberton respectively.
- File: [15-symbolic_link_permissions](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x01-shell_permissions/15-symbolic_link_permissions)

### 16. If only
- Write a script that changes the owner of the file hello to betty only if it is owned by the user guillaume.
- File: [16-if_only](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x01-shell_permissions/16-if_only)

### 17. Star Wars
- Write a script that will play the StarWars IV episode in the terminal.
- File: [100-Star_Wars](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x01-shell_permissions/100-Star_Wars)

### 17. 18. RTFM
- Create a man page that looks exactly like [this one](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/207/man_holberton.PNG) and passes all checks.
- File: [101-man_holberton](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x01-shell_permissions/101-man_holberton)
___
