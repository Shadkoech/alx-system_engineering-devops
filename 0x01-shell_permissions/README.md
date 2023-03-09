Shell  permissions
su betty -> switches current user to betty
id -un -> prints the effective username of the current user
groups -> Prints all groups the user is in
chown betty hello -> changes the owner of the file hello to betty
touch hello -> Creates an empty file called hello
chmod u+x hello -> Executes the file hello
chmod u+x,g+x,o+r -> adds execute permission to owner, group and allows other to read
chmod ugo+x hello -> Adds excute permission to owner, group and others
