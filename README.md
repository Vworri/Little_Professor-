# Little_Professor-

Backend: Project setup instructions for Linux debian based systems

### Requirements ###
* Python >= 3.5.2
* Django == 1.11.1
* mongoengine >= 0.13.0

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

#install the following in the virtual env:
pip install django==1.11.1
pip install mongoengine

#get and run the project
sudo apt install git
git clone https://github.com/Vworri/Little_Professor-.git
git checkout backend
cd Little_Professor-/Little_Professor
./manage.py runserver

#exit virtualenv
deactivate

#enter virtualenv
workon little_professor

```

### Database ###
We are using the latest version of MongoDB, v3.4.4 (at the time of writing)

