# leequotes-web-demo

A simple website showcasing the leequotes lib

Live demo available at http://lxnd.pythonanywhere.com/

## How to update the website (for maintainers)

1. got to python anywhere dashboard : https://www.pythonanywhere.com/user/lxnd/
2. open the web tab
3. open a console in the directory of the source code and run `git pull`
4. in the web tab, press "reload"

## How to install

Just type

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

then

```
flask --app flask_app run
```