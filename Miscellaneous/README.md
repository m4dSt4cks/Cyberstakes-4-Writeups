# Miscellaneous

## Can You Look This Over

I was not a big fan of this challenge, you mostly just needed to perform a diff and grep for anything remotely related to backdoor/password/root to find the file (auth-passwd.c).

After that, it's just straight up brute forcing. I saved the password so you can see it without doubling your electric bill.

## Recovery And IDentification

I was unable to get this to work on my linux machine. Thankfully, I eventually got it on Ubuntu. These were the final steps I wrote down, but they may/may not work on your machine.

In ubuntu:

* `unxz disk1.img.xz`
* `unxz disk2.img.xz` 
* `sudo losetup loop30 disk1.img`
* `sudo losetup loop31 disk2.img` 
* `sudo mdadm --create --verbose /dev/md0 --level=5 --raid-devices=3 /dev/loop30 /dev/loop31 missing`
* `sudo mdadm --stop /dev/md0`
* `sudo mdadm --assemble --run /dev/md0 /dev/loop30 /dev/loop31`
* open the folder thing and look at other locations
* `bzip2 -d` on each file and then use `gunzip` to finish extracting everything
* `strings` each file to find the flag

## I SEe You

Use the -i option to make things readable. There are thousands of IPs in the logs, but only 1 runs /bin/sh. I found this after thinking of ways that a web attacker may be different than a normal user.

ausearch -if audit.log -f /bin/sh -i

## Partition Twice, Recover Once

* `fsck` can help fix the image
* testdisk was the only tool I used that found the other partition, using the "Deeper search" functionality
* `fdisk -u sectors -l image.bin` found the hidden image offset, which I extraced using a hex editor (dd would also be a good idea)
* [How to mount LUKS](https://askubuntu.com/questions/835525/how-to-mount-luks-encrypted-file)