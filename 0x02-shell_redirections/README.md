# 0x02. Shell, I/O Redirections and filters
> Holberton School Foundations Curiculum: System Engineering & DevOps - Bash

### Contents
- [Learning Objectives](https://github.com/michedomingo/holberton-system_engineering-devops/tree/master/0x02-shell_redirections/#redirections)
- [Tasks](https://github.com/michedomingo/holberton-system_engineering-devops/tree/master/0x02-shell_redirections/#tasks)
___
<a name="redirections"></a>

### 🤓 Learning Objectives
#### Shell, I/O Redirection
- [ ] What do the commands head, tail, find, wc, sort, uniq, grep, tr do
- [ ] How to redirect standard output to a file
- [ ] How to get standard input from a file instead of the keyboard
- [ ] How to send the output from one program to the input of another program
- [ ] How to combine commands and filters with redirections
#### Special Characters
- [ ] What are special characters
- [ ] Understand what do the white spaces, single quotes, double quotes, backslash, comment, pipe, command separator, tilde and how and when to use them
#### Other Man Pages
- [ ] How to display a line of text
- [ ] How to concatenate files and print on the standard output
- [ ] How to reverse a string
- [ ] How to remove sections from each line of files
- [ ] What is the /etc/passwd file and what is its format
- [ ] What is the /etc/shadow file and what is its format
___
<a name="tasks"></a>
## Tasks
> All scripts must be executable and exactly two lines long.

### 0. Hello World
- Write a script that prints “Hello, World”, followed by a new line to the standard output.
- File: [0-hello_world](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/0-hello_world)

### 1. Confused smiley
- Write a script that displays a confused smiley "(Ôo)'.
- File: [1-confused_smiley](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/1-confused_smiley)

### 2. Let's display a file
- Display the content of the /etc/passwd file.
- File: [2-hellofile](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/2-hellofile)

### 3. What about 2?
- Display the content of /etc/passwd and /etc/hosts.
- File: [3-twofiles](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/3-twofiles)

### 4. Last lines of a file
- Display the last 10 lines of /etc/passwd.
- File: [4-lastlines](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/4-lastlines)

### 5. I'd prefer the first ones actually
- Display the first 10 lines of /etc/passwd.
- File: [5-firstlines](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/5-firstlines)

### 6. Line #2
- Write a script that displays the third line of the file iacta.
- File: [6-third_line](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/6-third_line)

### 7. It is a good file that cuts iron without making a noise
- Write a shell script that creates a file named exactly \*\\'"Holberton School"\'\\*$\?\*\*\*\*\*:) containing the text Holberton School ending by a new line.
- File: [7-file](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/7-file)

### 8. Save current state of directory
- Write a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.
- File: [8-cwd_state](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/8-cwd_state)

### 9. Duplicate last line
- Write a script that duplicates the last line of the file iacta.
- File: [9-duplicate_last_line](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/9-duplicate_last_line)

### 10. No more javascript
- Write a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.
- File: [10-no_more_js](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/10-no_more_js)

### 11. Don't just count your directories, make your directories count
- Write a script that counts the number of directories and sub-directories in the current directory.
- The current and parent directories should not be taken into account
- Hidden directories should be counted
- File: [11-directories](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/11-directories)

### 12. What’s new
- Create a script that displays the 10 newest files in the current directory.
- One file per line, sorted from the newest to the oldest
- File: [12-newest_files](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/12-newest_files)

### 13. Being unique is better than being perfect
- Create a script that takes a list of words as input and prints only words that appear exactly once.
- Input/Output format: One line, one word, Words should be sorted
- File: [13-unique](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/13-uniques)

### 14. It must be in that file
- Display lines containing the pattern “root” from the file /etc/passwd
- File: [14-findthatword](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/14-findthatword)

### 15. Count that word
- Display the number of lines that contain the pattern “bin” in the file /etc/passwd.
- File: [15-countthatword](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/15-countthatword)

### 16. What's next?
- Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.
- File: [16-whatsnext](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/16-whatsnext)

### 17. I hate bins
- Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.
- File: [17-hidethisword](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/17-hidethisword)

### 18. Letters only please
- Display all lines of the file /etc/ssh/sshd_config starting with a letter, including capital letters
- File: [18-letteronly](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/18-letteronly)

### 19. A to Z
- Replace all characters A and c from input to Z and e respectively.
- File: [19-AZ](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/19-AZ)

### 20. Without C, you would live in hiago
- Create a script that removes all letters c and C from input.
- File: [20-hiago](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/20-hiago)

### 21. esreveR
- Write a script that reverse its input.
- File: [21-reverse](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/21-reverse)

### 22. DJ Cut Killer
- Write a script that displays all users and their home directories, sorted by users.
- File: [22-users_and_homes](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x02-shell_redirections/22-users_and_homes)
___
