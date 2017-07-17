# {{ cookiecutter.project_name }}
{{ cookiecutter.description }}

# Requirements
- flask-ask
- foreman
- virtualenv
- ngrok

# Installation
```
cp env.example .env
pip install -r requirements
foreman start -f Procfile.dev
```

To expose the skill to Amazon, run `ngrok http 5000` after the server is running.

# Amazon Developer Portal Setup

- Head to https://developer.amazon.com/edw/home.html#/skills.
- Set up interaction mode and save intents, custom slots, and utterances to resources folder.
- Under "Configuration" select HTTPS for endpoint type, and paste in the ngrok endpoint.
- Under "SSL Certificate" choose "My development endpoint is a sub-domain of a domain that has a wildcard certificate from a certificate authority"
- Test!
