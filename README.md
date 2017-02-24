# A students check-in and checkout prototype.

### 01. setup .gitignore, requirements.txt and README.md

    echo "*.py[cod]" > .gitignore
    echo "Django==1.10.5" > requirements.txt
    echo "# A students check-in and checkout prototype." > README.md

### 02. setup a cloud environment

    # make a new cloud9 workspace 
    #   name it clocking
    #   cloned from git@github.com:5SA/clocking.git
    #   select Blank template
    sudo pip install virtualenv   # admin auth
    virtualenv $HOME/.env
    source $HOME/.env/bin/activate
    pip install -r requirements.txt

### 03. creating the project 'clocking' and verify it

    django-admin startproject clocking
    cd clocking
    # edit clocking/settings.py and add u'clocking-sdoro.c9users.io' to ALLOWED_HOSTS
    python manage.py runserver $IP:$PORT
    # firefox https://clocking-sdoro.c9users.io

### 04. creating the 'clockio' app

    python manage.py startapp clockio

### 05. write your greets view

    # edit clockio/views.py
    > clockio/urls.py
    # edit clocking/urls.py
    # edit clockio/urls.py
    python manage.py runserver $IP:$PORT
    # firefox https://clocking-sdoro.c9users.io/

### 06. make a template inheritance, static files and views

    mkdir -p clockio/templates
    > clockio/templates/base.html
    > clockio/templates/checkin.html
    > clockio/templates/checkout.html
    mkdir -p clockio/static/clockio/css
    > clockio/static/clockio/css/style.css
    # edit clocking/settings.py

### 07. add checkpoints to url

    # edit clockio/urls.py
    # edit clockio/views.py