# Dad-Jokes-Bot
**Overview**
- This project is a Discord Bot implemented in Python which sends a message into a discord channel when a user sends a "Dad Joke" to the user if their message meets a certain criteria.
----
**Features**:
- `!quote` returns a embeded image to a channel and stores data in a PostgreSQL database.
- `!random_quote` returns a random quote from the database.
- `im, i'm, Im`implemented a function to parse the next word in a given string and returns.
- Implemented using discord.py Library and PostgreSQL.
- Implemented algorithm to parse a user message and store user in database
- Validated functionality of discord commands and queries  using Unit Tests
----

## Screen Shots
## Required Downloads for this Bot
1. Discord Account and Bot Token. The link to create a Discord Bot can be found here: 
[https://discord.com/developers/docs/game-sdk/applications](https://discord.com/developers/docs/game-sdk/applications)

2. Enter the token for the discord bot in the `key.json` file and enter the database credentials into `config.json`.
The link to download PostgreSQL can be found here:
[https://www.postgresql.org/download/](https://www.postgresql.org/download/)
3. Python3
## File Details
- *requirements.txt* 
- *discord_bot.py*
- *test_discord_bot.py*
- *database.py*
- *test_database.py*
- *test_config.json*  
- *config.json*
- *key.json* 


## To Run the Bot
1.  Download all the files from the repository.
2.  Compile the *setup.py* file using `python setup.py`.
3.  Ensure the discord bot is added to server.
4.  A message should appear noting the discord bot is online `Logged on...`.
