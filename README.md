
# Reddit Query

Reddit Query is made of three parts a web scraper, data analysis and data visualizing tool made by Austin Joseph. The application utilizes [PRAW](https://pypi.org/project/praw/) (Python Reddit API Wrapper) to create a catalog of the top 1000 posts on all.reddit.com for the last 24 hours. A summary is then avaliable on a genearated webpage. 

## Getting Started
The project is built to be run in a Docker container go to https://www.docker.com/get-started for how to setup Docker on your machine.

There are two parts to Reddit Query the database and the python applications. The Dockerfiles and setup scripts for both are included in this repository. 

For all subprojects the first step is to clone the repo using `git clone https://github.com/austinobejo/RedditQuery.git`

### Data Scraper

Create [/runtime/redditquery/auth.json](/runtime/redditquery/auth.json.example) based on the information from [/runtime/redditquery/auth.json.example](/runtime/redditquery/auth.json.example) . This file dictates both the login information used by PRAW to create a secure connection to the Reddit servers. ( [Reddit OAuth2 Documentation](https://github.com/reddit-archive/reddit/wiki/OAuth2)), and the login information for the MySQL database.

If you are on Ubuntu or a similar Linux distribution you can run [runtime/build.sh](/runtime/build.sh)  then [runtime/start.sh](/runtime/start.sh) to get the container up and running. Docker will download and configure the required files and images.

### Database

Ensure that [/database/01_setup_auth.sql](/database/01_setup_auth.sql) contains the correct login information(already configured if you're using the defaults)

If you are on Ubuntu or a similar Linux distribution you can run [database/build.sh](/database/build.sh)  then [database/start.sh](/database/start.sh) to get the container up and running. Docker will download and configure the required files and images.

### Prerequisites

```
Docker Version: 18.09.7, build 2d0083d(If running inside a docker container)
```
OR
```
Python Version: 3.7.4-buster (https://www.python.org/downloads/)
Praw Version: 6.3.1 (pip install praw==6.3.1)
MySQL-Connector-Python Version: 8.0.17(pip install mysql-connector-python==8.0.17)
Pandas Version: 0.24.2 (pip install pandas==0.24.2)
Schedule Version: 0.6.0 (pip install schedule==0.6.0)

If youre running in a native python enviorment
```

### Technical Description

Coming Soon


### Planned Features

Coming Soon

## Authors

* **[Austin Joseph](https://github.com/austinobejo)**

