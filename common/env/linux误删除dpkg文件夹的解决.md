

 			[误删除/var/lib/dpkg解决办法](https://www.cnblogs.com/shamojituan/p/7466379.html) 		



sudo mkdir -p /var/lib/dpkg/{alternatives,info,parts,triggers,updates}
 Recover some backups:
 sudo cp /var/backups/dpkg.status.0 /var/lib/dpkg/status
 Now, lets see if your dpkg is working (start praying):
 apt-get download dpkg
 sudo dpkg -i dpkg*.deb If everything is "ok" then repair your base files too: apt-get download base-files sudo dpkg -i base-files*.deb
 Now try to update your package list, etc.:
 dpkg --audit
 sudo apt-get update
 sudo apt-get check

www.cnblogs.com/shamojituan