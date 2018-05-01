# Contributing to LionBot Subscriptions

Thank you for your interest in developing for LionBot, a Facebook Messenger bot made by The Lion's Tech Team. This is the guide to the subscriptions web app that allows the verified clubs to send messages to LionBot subscribers.

## 1)  Set up a Python3 Virtual Environment (taken from [here](https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3)):

First type the following in Terminal: 
`python3 -m venv <filepath to your LionBot repo>`

Next, `cd` into the `bin` folder,
`cd bin`

Next, activate the virtual environment: 
`source activate`
- If this doesn't activate the virtual env:
	- Go back to main directory
	- `source bin/activate`

To deactivate the environment, simply write: 
`deactivate `

## 2) Make sure you set up your Database URL

In app.py, the line (`url = urllib.parse.urlparse(os.environ['DATABASE_URL'])`) connects the database to the front-end.

To set up the database on your computer, contact an organizer at `lionbot@adicu.com` in your terminal enter simliar to code to this:
```
export ACCESS_TOKEN=TOKEN_HERE
export CLIENT_ACCESS_TOKEN=TOKEN_HERE
export DATABASE_URL=POSTGRES_HERE
export DEVELOPER_ACCESS_TOKEN=TOKEN_HERE
export SECRET_KEY=TOKEN_HERE
export TZ=America/New_York
export VERIFY_TOKEN=TOKEN_HERE
export YELP_API_KEY=TOKEN_HERE
export WEATHER_API_KEY=TOKEN_HERE
```
# How to Run the Web App

(Written for Mac)
1. Make a branch from git (https://github.com/ADI-Labs/subscriptions)
2. Enter the subscriptions directory on your terminal
3. Activate your virtual env:
	- Make sure you have virtual env installed, further explanation below
	- $ `source bin/activate`
	- Your terminal should now show something like this:
		(subscriptions) MacBook-Pro-51:subscriptions Momo$ 
4. Run the app: $ `python app.py`
5. Run the url in your browser
	- Should look similar to http://127.0.0.1:5000/


# How to contribute to subscriptions

The steps to adding to the subscriptions page:

1. After you have made your own branch from git
	- (https://github.com/ADI-Labs/subscriptions)

## How can I add new features to subscriptions?

### Branching
LionBot Subscriptions is developed by multiple people. To make this easier, we use individual branches for any new feature being implemented. This way, you can work on your code, make changes, all while leaving master as the defacto, working branch.

To add a new feature to the bot, first make a branch off of the latest version of master. 
Locally, you can run `git pull && git checkout [branch]` to switch to the new branch you will be working on.

### How is the subscriptions directory structured/where to put new code

As of 4/27/18:

```
C: \Subscriptions
|--- app.py
|--- CONTRIBUTING.md
|--- bin
|--- includes
|--- lib
|--- templates
|	|__ base.html
| 	|__ googleoauth.html
|	|__ index.html
|	|__ login.html
| 	|__ message.html 
```

## Now what?
Woo! You've gone through the process of adding a new feature to the ]bot. Continue working on new things to help make LionBot even better.




