# Connexion intro

This project just allows you to get to know a nice wrapper around
Flask called Connexion. More info about it [here](https://connexion.readthedocs.io/en/latest/index.html).

## Local development using virtualenv
Then create a python virtual env:
```shell
python3.10 -m venv env/
```

Install the requirements:
```shell
pip install --upgrade pip
pip install -r requirements.txt
```

Start the app:
```shell
flask run
```
Review the interactive API documentation at http://0.0.0.0:5000/api/v1.0/ui/
