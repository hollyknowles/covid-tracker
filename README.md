# CovidTracker

This is a discord bot which informs users of the latest Covid data around the world

- Covid data is from the worldometer API from rapidapi.com https://rapidapi.com/Shouvik/api/worldometer-covid-19
- Discord developer portal for all things discord https://discord.com/developers/applications

TODO: refactor so the data is only called from API 5x per day, and save that data in a json, then when user goes !new, its read from the json and not calling the api everytime 

## How to setup discord:
Go on discord developer portal and create an application  - https://discord.com/developers/applications

Add a bot

Under the OAuth2 menu, generate a URL to invite the bot to your server

On the bot menu and make note of your token to put into a secrets.py file

```python
# In secrets.py file
def get_token():
  return "YOUR_TOKEN"
```

## API Setup

The API used is from rapidAPI.com (link given above), you will need to make an account. Then note the key and the host, and then define them in a secrets.py file.

```python
def get_api_key():
    return "YOUR_KEY"


def get_api_host():
    return "YOUR_HOST"
```

## How to Run
In the terminal or selected IDE: `python3 main.py`

On discord send a message saying: !new COUNTRY DD/MM/YY

