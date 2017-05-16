# DebtRemoteReference

**What the app was to do**

    > **User Need 1:​** Look Up Customer Debt Information by National ID or Mobile
       Number
      **Resolution:**​ The app will allow search by either national ID or mobile number
      the input should be validated and if a customer is found the details displayed if not
      an explanation that the customer is not found.

    > **User Need 2:**​ Download Debtors
      **Resolution:​** The app will allow the viewing on a dynamic table on the front
      end that is searchable via javascript by any of the fields in the table. The
      same table can also be downloaded as Excel.

    > **User Need 3:​** User Roles
      Resolution:​ The app will have two user roles - roleA and roleB - the first can
      perform User Need 1 only, and the latter User Need 1 & 2.

**What id does so far**

######Allows remote users to:

                  - register, login
                  - view list of deptors.
######Allows admins to:

                  - Create remote users
                  - Create roles and assign them to remote users
                  - Create new debtors
                  - View  and download list of new debtors

>Disclaimer: THe app was supposed to use *roles* created by *admins* to *enable* or *disable* the download
button. What it does now is, when a list of debtors is accessed the button disappears when remote users login and appears when admins login in.


Live app is published on pythonanywhere and can be accessed on this link

Register and login as remote user
Use the following credentials to access admin module:

  **Email:** *grshoe@admin.com*
  **Username:** *grshoeadmin*
  **password:** *grshoeadmin2017*

Deployment Set Up (Ubuntu 161.0)
===============================

#### Prerequisites

  - Ubuntu 16.0 OS
  - Admin privileges

#### Setting Up Python Development Environment

  * Update your OS by issuing `sudo apt-get update` or `sudo apt-get -y upgrade` which comes with python pre-installed.
    > Use python 2.7.12 for this project

  * Install `pip` to help you manage software packages for Python.
  * Install other needed development tools `sudo apt-get install build-essential libssl-dev libffi-dev sudo libapache2-mod-wsgi python-dev`
  * Enable `mod_wsgi` (*an Apache HTTP server mod that enables Apache to serve Flask applications.*) , run the following command: `sudo a2enmod wsgi`
  * Set Up a Virtual Environment - to ensure this project's set of dependencies won't disrupt any of your other projects. Use the following commands for setup:
  ```$ sudo apt-get install virtualenv

     $ sudo apt install virtualenvwrapper

     $ echo "source /usr/share/virtualenvwrapper/virtualenvwrapper.sh" >> ~/.bashrc

     $ export WORKON_HOME=~/.virtualenvs

     $ mkdir $WORKON_HOME

     $ echo "export WORKON_HOME=$WORKON_HOME" >> ~/.bashrc
  ```
  * Create a Virtual environment for your project:
    `mkvirtualenv -p python2.7 remoteapp`
    > You will use `deactivate` or `workon` anywhere on your terminal to deactivate and activate your virtual environment. e.g workon remoteapp

#### Clone Project

Use this command to copy this project to your local directory ` git clone https://github.com/crakama/DebtRemoteReference.git`

With you virtual environment activated,navigate to project's **root** directory, which is **remoterefapp** and issue `pip install -r requirements.txt`
to install project's dependencies.

#### Configure Database

* Ensure you have MySQL installed ` pip install flask-sqlalchemy mysql-python`.
* At the terminal, login as a root user. `mysql -u root` and issue the following commands to create a new user with password and privileges:
  ``` mysql> CREATE USER 'gr_admin'@'localhost' IDENTIFIED BY 'gr2017';

      mysql> CREATE DATABASE remoteapp_db;

      mysql> GRANT ALL PRIVILEGES ON remoteapp_db . * TO 'gr_admin'@'localhost';

  ```
* create an `instance` directory in the **remoterefapp** directory, and then create a `config.py` file. Add the following configuration settings:
  ```# instance/config.py
     SECRET_KEY = 'p9Bv<3Eid9%$i01'
    SQLALCHEMY_DATABASE_URI = 'mysql://gr_admin:gr2016@localhost/remoteapp_db'
  ```
### Test the app  locally

* Set the `FLASK_CONFIG` and `FLASK_APP` environsment variables before running the app like so:
   ```$ export FLASK_CONFIG=development
      $ export FLASK_APP=run.py
      $ flask run
   ```
* If the app pulls an error, try to debug and fix the error before proceeding to the next stage.

#### Configure and Enable a New Virtual Host
* Issue the following command in your terminal: `sudo nano /etc/apache2/sites-available/remoterefapp.conf`
to create the file and add the following content:
```<VirtualHost *:80>
		ServerName <fill in ServerName>
		ServerAdmin <fill in ServerAdmin >
		WSGIScriptAlias / /var/www/remoterefapp/flaskapp.wsgi
		<Directory /var/www/remoterefapp/remoterefapp/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/remoterefapp/remoterefapp/static
		<Directory /var/www/remoterefapp/remoterefapp/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
  </VirtualHost>
```
* Enable the virtual host with the following command `sudo a2ensite remoterefapp`

> Make sure you have your virtual environment activated and all dependencies from
**requirements.txt** installed.

* Migrate your Database. With your virtual environment active, navigate to the project directory
and issue the following commands.
```export FLASK_CONFIG=production
   export FLASK_APP=run.py
   export SQLALCHEMY_DATABASE_URI='mysql://your-username:your-password@your-host-address/your-database-name'
   flask db upgrade
```
>If you happen to encounter *import error* such as *No module found* know that your dependencies
did not install successfully. You will have to use **requirements.txt** file to install missing dependencies one by one.


#### Create the .wsgi File

Move to the **root** directory and create a file named `flaskapp.wsgi` with following commands:
`sudo nano flaskapp.wsgi ` add the following to set environment variables and tell the host to get `app` variable from `run.py` file to serve it as the application.

``` import os
    import sys

    path = '/home/<fill in username>/<project-directory-name>'
    if path not in sys.path:
        sys.path.append(path)

    os.environ['FLASK_CONFIG'] = 'production'
    os.environ['SECRET_KEY'] = 'p9Bv<3Eid9%$i01'
    os.environ['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@host-address/database-name'

    from run import app as application
```
#### Restart Apache server

* Restart Apache with the following command to apply the changes:
`sudo service apache2 restart`

####Run the web app on your virtual Host

* You can register as new user and login
* Admin module will not be available unless you create a new user at the terminal as shown below
```$ flask shell
    >>> from app.models import RemoteUser
    >>> from app import db
    >>> gr_admin = RemoteUser(email="gradmin@admin.com",username="gradmin",password="gradmin2017",is_admin=True)
    >>> db.session.add(admin)
    >>> db.session.commit()
```
* login as an admin user and add roles, and assign them to remote users.
