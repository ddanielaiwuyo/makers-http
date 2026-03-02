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
create table http_challenge_1;
\c http_challenge_1;
```

You can skip this part below by simply pasting the contents of `setup.sh` into
your terminal. It simply clones the repo for you, sets up the dependecies
and environment and shows how to run the app in 2 steps

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

### Run Program
```bash
flask --app main run
```


## For more information on Flask, read their documentation [Flask's Docs](https://flask.palletsprojects.com/en/stable/)
