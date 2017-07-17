# mo-lexa
Alexa Skill Cookiecutter project template by @istrategylabs

# Features
- Flask-Ask
- Base skill setup
- Files for intents and utterances

# Usage
Prep
```
brew install cookiecutter
cookiecutter gh:istrategylabs/mo-lexa
cp env.example .env
pip install -r requirements
```
Running
```
gem install foreman
foreman start -f Procfile.dev
```

# Moving Forward

Check out the [Flask-Ask documentation](https://flask-ask.readthedocs.io/en/latest/) and start building! We find it useful to copy and paste your intents, utterances, and custom slot values into their respective file under the resources folder. Files for custom slot values are not included as we find it is best to name those their slot name.
