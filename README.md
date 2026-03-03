### Installation
Make sure you have at least python version `3.13` and above, psql installed
If you don't have postres installed, you can use brew if you're on mac

- Git: [git insallation](https://git-scm.com)
- Python3.13 and above is fine : [python installation](https://python.org/downloads/release/python-3130)
- Postgresql preferrably version 15, [psql installtion](https://postgresql.org)


```bash
brew insall postgresql@15
brew start services postgresql
brew services list # you should see postgres running
```
Visit [Postgres'](https://postgresql.org) official site as they show how to set it up and 
installation for your own device.


### Database configuration
After installation you can then create the database the application is expecting:

And then when you access  your psql shell, run the following:

```bash
create database http_challenge_1;
\c http_challenge_1;
```

You can skip this part below by simply run the `setup.sh` in your terminal.
It simply clones the repo for you, sets up the dependecies
and environment and shows how to run the app in 2 steps.

```
# after copying the file
chmod u+x setup.sh # gives you permissions to execute unless you're not `sudo`

./setup.sh
```

### Cloning repository
```bash
git clone https://github.com/ddanielaiwuyo/makers-http.git ~/makers_http
cd ~/makers_http
```

### Install dependencies and virtual environment
```bash
python3 -m venv env && source ./env/bin/activate

pip install -r requirements.txt
```

### Run Server
```bash
flask --app main run
```


## Run Client
In another terminal, run this:
```bash
curl http://localhost:5000/artists # sends a get requests for all the artists in the db

# makes a post request to create an artist called Mass Of The Fermenting Dregss using
# using query params
curl -X http://localhost:5000/artists?name="Mass+Of+The+Fermenting+Dregss"&genre="Rock"
```


## Run Tests:
To run the tests, you need to expose your current working directory to python's interpreter PATH
especially for module resolutions
```bash
export PYTHONPATH="$PWD"

# And now you can run pytest
pytest
```


## For more information on Flask, read their documentation [Flask's Docs](https://flask.palletsprojects.com/en/stable/)
