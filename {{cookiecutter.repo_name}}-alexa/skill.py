import logging
from decouple import config
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from raven.contrib.flask import Sentry

app = Flask(__name__)

ask = Ask(app, "/alexa")
logging.getLogger("flask_ask").setLevel(config('LOG_LEVEL'))
if config('ASK_APPLICATION_ID'):
    app.config['ASK_APPLICATION_ID'] = config('ASK_APPLICATION_ID')
if config('SENTRY_DSN'):
    sentry = Sentry(app, dsn=config('SENTRY_DSN'))


@app.route("/")
def hello():
    return "{{cookiecutter.repo_name}}-alexa"


@ask.launch
def start_game():
    return statement('Set up a launch intent')


@ask.intent("AMAZON.HelpIntent")
def help():
    return statement('Set up a help intent')


@ask.intent("AMAZON.CancelIntent")
def cancel():
    return statement('Okay')


@ask.intent("AMAZON.StopIntent")
def stop():
    return statement('Okay')


@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    app.run(debug=True)
