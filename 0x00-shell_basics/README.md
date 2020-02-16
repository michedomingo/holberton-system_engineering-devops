# 0x01. Shell, basics
> Holberton School Foundations Curiculum: System Engineering & DevOps - Bash

### Contents
- [Learning Objectives](https://github.com/michedomingo/holberton-system_engineering-devops/tree/master/0x00-shell_basics/#basics)
- [Tasks](https://github.com/michedomingo/holberton-system_engineering-devops/tree/master/0x00-shell_basics/#tasks)
___
<a name="basics"></a>

### 🤓 Learning Objectives
#### What is the Shell
- [ ] What is the shell
- [ ] What is the difference between a terminal and a shell
- [ ] What is the shell prompt
- [ ] How to use the history (the basics)
#### Navigation
- [ ] What do the commands or built-ins cd, pwd, ls do
- [ ] How to navigate the filesystem
- [ ] What are the . and .. directories
- [ ] What is the working directory, how to print it and how to change it
- [ ] What is the root directory
- [ ] What is the home directory, and how to go there
- [ ] What is the difference between the root directory and the home directory of the user root
- [ ] What are the characteristics of hidden files and how to list them
- [ ] What does the command cd - do
#### Looking Around
- [ ] What do the commands ls, less, file do
- [ ] How do you use options and arguments with commands
- [ ] Understand the ls long format and how to display it
- [ ] A Guided Tour
- [ ] What does the ln command do
- [ ] What do you find in the most common/important directories
- [ ] What is a symbolic link
- [ ] What is a hard link
- [ ] What is the difference between a hard link and a symbolic link
#### Manipulating Files
- [ ] What do the commands cp, mv, rm, mkdir do
- [ ] What are wildcards and how do they work
- [ ] How to use wildcards
#### Working with Commands
- [ ] What do type, which, help, man commands do
- [ ] What are the different kinds of commands
- [ ] What is an alias
- [ ] When do you use the command help instead of man
#### Reading Man Pages
- [ ] How to read a man page
- [ ] What are man page sections
- [ ] What are the section numbers for User commands, System calls and Library functions
#### General
- [ ] What does RTFM mean?
- [ ] What is a Shebang
- [ ] Common shortcuts for Bash
- [ ] What does LTS mean?
___
<a name="tasks"></a>
### Tasks
> All scripts must be executable and exactly two lines long.

#### File: [0-current_working_directory](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x00-shell_basics/0-current_working_directory)
- Prints the absolute path name of the current working directory.

#### File: [1-listit](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x00-shell_basics/1-listit)
- Display the contents list of your current directory.

#### File: [2-bring_me_home](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x00-shell_basics/2-bring_me_home)
- Change the working directory to the user’s home directory.

#### File: [3-listfiles](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x00-shell_basics/3-listfiles)
- Display current directory contents in a long format.

#### File: [4-listmorefiles](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x00-shell_basics/4-listmorefiles)
- Display current directory contents, including hidden files.

#### File: [5-listfilesdigitonly](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x00-shell_basics/5-listfilesdigitonly)
- Display current directory contents.

#### File: [6-firstdirectory](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x00-shell_basics/6-firstdirectory)
- Create a directory named holberton in the /tmp/ directory.

#### File: [7-movethatfile](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x00-shell_basics/7-movethatfile)
- Move the file betty from /tmp/ to /tmp/holberton.

#### File: [8-firstdelete](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x00-shell_basics/8-firstdelete)
- Delete the file betty.

#### File: [9-firstdirdeletion](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x00-shell_basics/9-firstdirdeletion)
- Delete the directory holberton that is in the /tmp directory.

#### File: [10-back](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x00-shell_basics/10-back)
- Change the working directory to the previous one.

#### File: [11-lists](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x00-shell_basics/11-lists)
- List all files in current, parent and /boot directories.

#### File: [11-lists](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x00-shell_basics/11-lists)
- List all files in current, parent and /boot directories.

#### File: [13-symbolic_link](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x00-shell_basics/13-symbolic_link)
- Create a symbolic link to /bin/ls, named __ls__.

#### File: [14-copy_html](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x00-shell_basics/14-copy_html)
- Copy all HTML files that did not exist in parent of working directory.

#### File: [15-lets_move](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x00-shell_basics/15-lets_move)
- Move all files beginning with an uppercase letter to the directory /tmp/u.

#### File: [16-clean_emacs](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x00-shell_basics/16-clean_emacs)
- Delete all files in the current working directory that end with the character ~.

#### File: [17-tree](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x00-shell_basics/17-tree)
- Create the directories welcome/, welcome/to/ and welcome/to/holberton in the current directory.

#### File: [18-commas](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x00-shell_basics/18-commas)
- List all the files and directories of the current directory, separated by commas (,).

#### File: [holberton.mgc](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x00-shell_basics/holberton.mgc)
- Create a magic file holberton.mgc that can be used with the command file to detect Holberton data files. 
___
