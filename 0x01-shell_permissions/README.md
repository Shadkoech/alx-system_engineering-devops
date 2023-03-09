Shell  permissions
su betty -> switches current user to betty
id -un -> prints the effective username of the current user
groups -> Prints all groups the user is in
chown betty hello -> changes the owner of the file hello to betty
touch hello -> Creates an empty file called hello
chmod u+x hello -> Executes the file hello
chmod u+x,g+x,o+r -> adds execute permission to owner, group and allows other to read
chmod ugo+x hello -> Adds excute permission to owner, group and others
chmod 007 hello -> only gives others exclusive permissions
chmod 753 hello -> gives the following permissions to the file hello -rwxr-x-w x
chmod --reference=olleh hello -> Sets the mode of file hello same as olleh
chmod -R ugo+X -> adds execute permission to all directories for owner, group and others
mkdir -m 751 my_dir -> creates a directory my_dir with 751 permission
chgrp school hello -> changes the group owner to school from hello
chown -hR vincent:staff . -> Chnages owner to vincent and group owner to staff
chown -h vincent:staff -hello -> Chnage the owner and group owner of hello to vincent and staff
chown --from=guillaume betty hello - >  changes the owner of the file hello to betty only if it is owned by the user guillaume
