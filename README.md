# HUG
Chat Server and Client writen with python

<h1>Install Python 3 and MariaDB</h1>

  Windows:
  Soon windows 11 will have winget

  Base-Debian:
  sudo apt install python3 mariadb-server -y && sudo systemctl enable mariadb-server --now && mysql_secure_installation
  
  Base-Redhat: 
  sudo dnf install python3 mariadb && sudo systemctl enable mariadb-server --now && mysql_secure_installation
  
  MacOS:
  brew install python3 mariadb && brew services start mariadb && mysql_secure_installation
  
 <h1>Import database</h1>
    
   mysql -u root -p
   
   create user 'user'@'localhost' indetified by 'password';
   
   grant all privileges to * . * on 'user'@'localhost';
   flush privileges;
   
   create database hug;
   
   mysql -u user -p hug << hugdatabase.sql
