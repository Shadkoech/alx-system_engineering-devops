alias ls = "rm * - Create a script that creates an alias.
echo "hello $USER" -> prints hello user, where user is the current Linux user
PATH=$PATH:/action -> Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program.
echo $PATH | tr ':' '\n' | wc -l -> counts the number of directories in the PATH.
printevn -> lists environment variables.
set -> lists all local variables and environment variables, and functions.
BEST="School" -> C reates a new local variable 
export BEST="School" -> creates a new global variable.
echo $((128 + $TRUEKNOWLEDGE)) -> prints result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line.
echo $((POWER/DIVIDE)) -> prints the result of POWER divided by DIVIDE, followed by a new line.

