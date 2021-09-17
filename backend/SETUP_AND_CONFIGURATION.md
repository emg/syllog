# Set up Syllog

How to set up the Syllog back end on Ubuntu

## Prerequisites

1. A web server

2. sudo / wheel / root access to (1.)

3. Ability to create https certificates. For free from the letsencrypt
project, for example.

4. Ability to install packages on the server.

## Install required packages

sudo apt-get install apache2 postgresql python3 virtualenv libapache2-mod-wsgi-py3


## Set up PostgreSQL

1. Set up PostgreSQL

# Set the password for user postgres
$ sudo passwd postgres

# Enable, then start the postgresql service
$ sudo systemctl enable postgresql
$ sudo systemctl start postgresql


2. Create PostgreSQL user 'syllog' owning database 'syllog'.

First, grab a password from https://random.org/ or your favorite
source of passwords. Make a note of it. You'll need it later.

Then:

Shift to the super user
```
$ sudo -s
```

Shift user to the postgres user
```
# su - postgres
```

Create the syllog user

```
$ createuser --interactive --pwprompt
Enter name of role to add: syllog
Enter password for new role: <make up something, or use random.org>
Enter it again: <repeat same password>
Shall the new role be a superuser? (y/n) y
```

Create the the database 'syllog' owned by the user 'syllog'

```
$ createdb -O syllog syllog
```

Log out of the postgres user into the root user

```
$ logout
```

Exit from the root user into your own user

```
# exit
```

## Set up a space for the web server files

```
$ sudo mkdir -p /srv/web/default/http/ /srv/web/default/log/
```

## Git clone this repo

You must git clone this repo somewhere where your web server can read
the files. You should probably, however, clone it ouside of the http
space, so that only selected files are visible to the web server.

```
$ cd /srv/web/default
$ sudo mkdir git
$ sudo chown root:www-data git
$ sudo chmod -R 6755 git/
$ cd git
$ sudo git clone https://github.com/emg/syllog.git
```

## Set up a virtualenv

```
$ cd /srv/web/default
$ sudo virtualenv virtualenv
$ sudo virtualenv --python=python3 virtualenv
$ sudo -s
# source /srv/web/default/virtualenv/bin/activate
# pip install --upgrade pip
# cd /srv/web/default/git/syllog/backend/Django/logsyllogsite
# pip install -r requirements.txt
# exit
```


## Configure the Django backend

First make a copy of the local_settings.py file for local modification.

```
$ cd /srv/web/default/git/syllog/backend/Django/logsyllogsite/logsyllogsite
$ sudo cp local_settings.py.template local_settings.py
```

Now edit the loca_settings.py for your needs. Especially set:

- ALLOWED_HOSTS must contain the ServerName (DNS entry) of your web server.
- Set DEBUG = False
- Set DEV = False
- Set the PostgreSQL connection info, including password

```
$ sudo vi local_settings.py
```

## Set up the Django database

First create the database

```
$ source /srv/web/default/virtualenv/bin/activate
$ cd /srv/web/default/git/syllog/backend/Django/logsyllogsite
$ python3 manage.py migrate
```

Then, while still having the virtualenv activated, create the web site
Django admin superuser:

```
$ python3 manage.py createsuperuser
```

## Collect Django static files

Collect static files for Django. For this, we need to do it as `sudo
-s` root, since we need to write to directories that are owned by
root.

```
$ sudo -s
# cd /srv/web/default/git/syllog/backend/Django/logsyllogsite
# source /srv/web/default/virtualenv/bin/activate
# python manage.py collectstatic
```

## Set up Apache

There are sample Apache .conf files in `syllog/backend/Apache-conf/`.

Other than that, you're on your own here. Please don't follow these
instructions unless you know what they do.

1. Copy these to your Apache `sites-available` directory.

2. Edit them for your local needs. Then enable them with
`a2ensite`. You'll need to also create the letencrypt
certificate. DuckDuckGo is your friend.

## Create the syllog directory in the web server space

```
$ cd /srv/web/default/http
$ sudo mkdir syllog
$ sudo chown -R root:www-data syllog
$ sudo chmod -R 6755 syllog
$ cd syllog
$ sudo ln -s ../../git/syllog/frontend/index.html 
$ sudo ln -s ../../git/syllog/frontend/webapp/ ./applet
$ sudo ln -s ../../git/syllog/frontend/target/ .
$ sudo ln -s ../../git/syllog/backend/Django/logsyllogsite/static .
```

## Restart Apache

1. Check if the syntax works OK

   ```sudo apachectl -t```

   If this reports errors, fix them.

2. Restart apache

   ```sudo apachectl restart```
