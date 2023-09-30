# 0x05. Processes and signals

Herein are projects and exercices that showcase various ways, practices and concept of managing processes in Linux. Processes and signals play a very crucial role in the control and management of software applications and systems. They are directly involved in the following;

	- Process management(Health checking)
	- Signal handling (custom signals, graceful shutdown)
	- Logging and monitoring (signal based alerts, process logs)

The following Bash scripts performs different actions showing how processes are managed;

## Task 0
File

	- 0-what-is-my-pid
This is a bash script that displays its own process ID


## Task 1
File

	- 1-list_your_processes
- A bash script listing all the current running processes, shows the process hierarchy and displays in user-oriented format
- It applies the the ps command and its flags


## Task 2
File

	- 2-show_your_bash_pid
- A script that lists all the current running process as the above task 2 but the list must contain the word bash
- Applies filtering ps flag


## Task 3
File

	- 3-show_your_bash_pid_made_easy
- Bash script that displays the PID alng process name of processes whose name contain the word bash
- Implements the pgrep command


## Task 4
File

	- 4-to_infinity_and_beyond
- A bash script that displys the word "To infinity and beyond" indefinitely. It also adds sleep 2 between each loop
- Loop implemented in the file


## Task 5
File

	-  5-dont_stop_me_now
- A bash script that stop a running process and in our case the process in task 4 above which displays "To infinity and beyond indefinitely"
- Implements the kill command


## Task 6
File

	- 6-stop_me_if_you_can
- A bash script terminates a process in a more flexible way. For instance, it terminates a process from another window
- Implements the pkill command


## Task 7
File

	- 7-highlander
	- 67-stop_me_if_you_can

- In the file 7-highlander is a bash script that does the following;

	1. To infinity and beyond indefinitely
	2. With a sleep 2 in between each iteration
	3. I am invincible!!! when receiving a SIGTERM signal

- In the file 67-stop_me_if_you_can is a script that ends 7-highlander using the pkill command


## Task 8
File

	- 8-beheaded_process
- This is a bash script that kills the process 7-highlander in a more powerful way
- It implements the pkill command with SIGKILL flag
