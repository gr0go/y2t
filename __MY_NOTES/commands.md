#### Run the server and enable the debug mode so I don't have to kill the terminal at every change:

My server file is called `server.py`

```bash
flask --app server run --debug
```

This will generate dependencies modules

```bash
pip freeze > requirements.txt
```