# Text Summarization App

Playing around with TF-IDF summarization technique

To run locally, create a virtual environment of your choice (I have used virtualenv).

```
npm i -g live-server

pip install virtualenv

python -m virtualenv venv

activate ./venv/bin/activate or venv/Script/activate

pip install -r requirements_dev

flask --app server.py --debug run

# On a new terminal within the repository folder
live-server # to serve the static files
```
