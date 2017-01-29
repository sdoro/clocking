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
