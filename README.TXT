gitstart python
This will add run git init, add the READM.md, and the .gitignore for Python. It will push to your Github account

https://sourabhbajaj.com/mac-setup/Python/virtualenv.html
To install virtualenv run:
pip install virtualenv

cd my-project/
virtualenv venv --system-site-packages
source venv/bin/activate

export FLASK_APP=application.py
export FLASK_ENV=development
export SECRET_KEY='GDtfDCFYjD'
flask run