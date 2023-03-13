SHELL I/O REDIRECTIONS

echo "Hello, World" -> Prints “Hello, World”, followed by a new line to the standard output.
echo "\"(Ôo)'" -> displays a confused smiley
cat /etc/passwd -> Display the content of the /etc/passwd file
cat /etc/passwd /etc/hosts -> Display the content of /etc/passwd and /etc/hosts
tail /etc/passwd -> Display the last 10 lines of /etc/passwd
head /etc/passwd -> Display the first 10 lines of /etc/passwd
head -3 iacta|tail -1  -> prints the 3rd line of the file iacta
echo " Best School" > '\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)' ->  It is a good file that cuts iron without making a noise
ls -la > ls_cwd_content - Write a script that writes into the file ls_cwd_content the result of the command ls -la
tail -1 iacta >> iacta -> Duplicate last line
find -name "js" -type f -delete -> script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.
find . -type d! -path . print | wc -1 -> counts the number of directories and sub-directories in the current directory.
ls -t | head -> Create a script that displays the 10 newest files in the current directory.
sort | uniq -u -> takes a list of words as input and prints only words that appear exactly once.
grep "root" /etc/passwd -> Display lines containing the pattern “root” from the file /etc/passwd
grep -c bin /etc/passwd -> Display the number of lines that contain the pattern “bin” in the file /etc/passwd
grep root /etc/passwd --after-context=3 -> Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd
grep -v "bin" /etc/passwd - Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.
grep ^ [[:alpha:]] /etc/ssh/sshd_config -> Display all lines of the file /etc/ssh/sshd_config starting with a letter.
tr A Z | tr c e -Replace all characters A and c from input to Z and e respectively.
tr -d 'C' | tr -d 'c' -> Create a script that removes all letters c and C from input.
rev - Write a script that reverse its input.
cut -d : -f 1,6 /etc/passwd | sort - Write a script that displays all users and their home directories, sorted by users.
find . -empty -printf "%f\n" - Write a command that finds all empty files and directories in the current directory and all sub-directories.
find . -name "*.gif" -type f -printf "%f\n" | rev | cut -d. -f2- | rev | LC_ALL=C sort -f*" - Write a script that lists all the files with a .gif extension in the current directory and all its sub-directories.
echo $(cut -c1 | tr -d " \n") -> script that decodes acrostics that use the first letter of each line.
