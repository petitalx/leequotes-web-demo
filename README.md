# leequotes-web-demo

Simple website showcasing the [leequotes](https://pypi.org/project/leequotes/) python library.

A live demo available at https://leequotes.petitapetit.io/

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

## Notes to myself

## How to update the website 

1. push the changes
2. log on the server and pull (with my user)
3. `doas rcctl reload leequotesd`


### How to update the website on python anywhere (legacy)

1. got to python anywhere dashboard : https://www.pythonanywhere.com/user/lxnd/
2. open the web tab
3. open a console in the directory of the source code and run `git pull`
4. in the web tab, press "reload"