# 0x03. Shell, init files, variables and expansions
> Holberton School Foundations Curiculum: System Engineering & DevOps - Bash

### Contents
- [Learning Objectives](https://github.com/michedomingo/holberton-system_engineering-devops/tree/master/0x03-shell_variables_expansions/#expansions)
- [Tasks](https://github.com/michedomingo/holberton-system_engineering-devops/tree/master/0x03-shell_variables_expansions/#tasks)
___
<a name="expansions"></a>

### 🤓 Learning Objectives
#### General
- [ ] What happens when you type $ ls -l *.txt
#### Shell Initialization Files
- [ ] What are the /etc/profile file and the /etc/profile.d directory
- [ ] What is the ~/.bashrc file
#### Variables
- [ ] What is the difference between a local and a global variable
- [ ] What is a reserved variable
- [ ] How to create, update and delete shell variables
- [ ] What are the roles of the following reserved variables: HOME, PATH, PS1
- [ ] What are special parameters
- [ ] What is the special parameter $??
#### Expansions
- [ ] What is expansion and how to use them
- [ ] What is the difference between single and double quotes and how to use them properly
- [ ] How to do command substitution with $() and backticks
#### Shell Arithmetic
- [ ] How to perform arithmetic operations with the shell
#### The alias Command
- [ ] How to create an alias
- [ ] How to list aliases
- [ ] How to temporarily disable an alias
#### Other help pages
- [ ] How to execute commands from a file in the current shell
___
<a name="tasks"></a>
## Tasks
> All scripts must be executable and exactly two lines long.

### 0. <o>
- Create a script that creates an alias.
- Name: ls, Value: rm *
- File: [0-alias](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/0-alias)

### 1. Hello you
- Create a script that prints hello user, where user is the current Linux user.
- Name: ls, Value: rm *
- File: [1-hello_you](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/1-hello_you)

### 2. The path to success is to take massive, determined action
- Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program.
- File: [2-path](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/2-path)

### 3. If the path be beautiful, let us not ask where it leads
- Create a script that counts the number of directories in the PATH.
- File: [3-paths](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/3-paths)

### 4. Global variables
- Create a script that lists environment variables.
- File: [4-global_variables](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/4-global_variables)

### 5. Local variables
- Create a script that lists all local variables and environment variables, and functions.
- File: [5-local_variables](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/5-local_variables)

### 6. Local variable
- Create a script that creates a new local variable.
- Name: BETTY, Value: Holberton
- File: [6-create_local_variable](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/6-create_local_variable)

### 7. Global variable
- Create a script that creates a new global variable.
- Name: HOLBERTON, Value: Betty
- File: [7-create_global_variable](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/7-create_global_variable)

### 8. Every addition to true knowledge is an addition to human power
- Write a script that prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line.
- File: [8-true_knowledge](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/8-true_knowledge)

### 9. Divide and rule
- Write a script that prints the result of POWER divided by DIVIDE, followed by a new line.
- POWER and DIVIDE are environment variables
- File: [9-divide_and_rule](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/9-divide_and_rule)

### 10. Love is anterior to life, posterior to death, initial of creation, and the exponent of breath
- Write a script that displays the result of BREATH to the power LOVE
- BREATH and LOVE are environment variables
- File: [10-love_exponent_breath](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/10-love_exponent_breath)

### 11. There are 10 types of people in the world -- Those who understand binary, and those who don't
- Write a script that converts a number from base 2 to base 10.
- The number in base 2 is stored in the environment variable BINARY.
- File: [11-binary_to_decimal](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/11-binary_to_decimal)

### 12. Combination
- Create a script that prints all possible combinations of two letters, except oo.
- Letters are lower cases, from a to z, One combination per line
- File: [12-combinations](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/12-combinations)

### 13. Floats
- Write a script that prints a number with two decimal places.
- The number will be stored in the environment variable NUM.
- File: [13-print_float](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/13-print_float)

### 14. Decimal to Hexadecimal
- Write a script that converts a number from base 10 to base 16.
- The number in base 10 is stored in the environment variable DECIMAL
- File: [14-decimal_to_hexadecimal](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/14-decimal_to_hexadecimal)

### 15. What happens when you type ls *.c
- Write a blog post describing step by step what happens when you type ls *.c and hit Enter in your shell.
- URL: WIP

### 16. What is the difference between a hard link and a symbolic link?
- Write a blog post explaining what are hard and symbolic links on Linux, how to create them, and what is the difference between the two.
- URL: [Medium](https://medium.com/@michedomingo/the-difference-between-a-hard-link-and-a-symbolic-link-9b35ab606f9f)

### 17. Everyone is a proponent of strong encryption
- Write a script that encodes and decodes text using the rot13 encryption. 
- Assume ASCII.
- File: [100-rot13](https://github.com/michedomingo/holberton-system_engineering-devops/blob/master/0x03-shell_variables_expansions/100-rot13)
___
