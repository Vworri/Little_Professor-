# Little_Professor-

Backend: Project setup instructions for Linux debian based systems

### Requirements ###
* Python >= 3.5.2
* Django == 1.11.1
* psycopg2 == 2.7.1

### Development setup ###
In the terminal, run:
```
#install pip:
sudo apt install python-pip
sudo -H pip install --upgrade pip

#install virtualenv:
sudo -H pip install virtualenv virtualenvwrapper
echo "export WORKON_HOME=~/Env" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
source ~/.bashrc

#create the virtual env:
mkvirtualenv --python=python3 little_professor

#install Django in the virtual env:
pip install django==1.11.1

#get and run the project
sudo apt install git
git clone https://github.com/Vworri/Little_Professor-.git
git checkout backend #or the required branch
cd Little_Professor-/Little_Professor
./manage.py runserver

#exit virtualenv
deactivate

#enter virtualenv
workon little_professor

```

### Database setup (postgresql) ###
We are using the latest version of PostgreSQL 9.5.7 (at the time of writing)

```
sudo apt update
sudo apt install postgresql
```
After a few moments apt will finish downloading, installing and processing.


We now have PostgreSQL installed and the PostgreSQL service is running in the background.
Use the sudo command to switch to the new "postgres" account.
```
sudo -i -u postgres
```
Within the "postgres" account, create a user from the command line with the createuser command. 
PostgreSQL will prompt you with several questions. Answer "n" to superuser and "y" to the other questions.
```
createuser lil_prof -P --interactive

# Shall the new role be a superuser? (y/n) n
# Shall the new role be allowed to create databases? (y/n) y
# Shall the new role be allowed to create more new roles? (y/n) y
```

Exit out of the postgres account by pressing the 'Ctrl' + 'd'

Create a new database, name it "little_professor_db"
```
createdb little_professor_db
```

Install Postgresql Adapter for Python in the virtualenv
```
workon little_professor
pip install psycopg2
```

Configure project DATABASES settings in settings.py (see existing project)

Finally, apply migrations, run the following command from the project folder
```
./manage.py makemigrations
./manage.py migrate
```

## DB Schema
```python

DBentry = {"Title" = title,
          "Authors" = [],
          "Realease Date" = datetime,
          "Import Date" = datetime,
          "Text" = {"Original" = title.pdf,
                    "Extracted" = title.txt,
                    "NLP'd" = processed_tile
          }
}
```
