# fast-movie
A movie booking api similar to book my show

> This is SOA based architecture to provide a simplistic 
> **REST API**  for a movie booking service. Where user can look for 
> movies playing in their city and different cinemas and 
> respectively book tickets for their favorite movie they want




### Application Structure
This is How Our Application is structured
```
📦fast-moview
 ┣ 📂.github
 ┣ 📂.idea
 ┣ 📂 app
 ┃    ┣ 📂 models
 ┃    ┣ 📂 services
 ┃      ┗ 📜 ExampleEvents.php
 ┃    ┣ 📂 routers
 ┃    ┣ 📂 helpers
 ┃      ┗ 📜 ExampleHelper.php
 ┃    ┣ 📂 Listeners
 ┃      ┗ 📜 ExampleEventListener.php
 ┣ 📜.gitignore
 ┣ 📜 requirements.txt
 ┗ 📜 Dockerfile
```


### Running Application Without DOCKER
1.  Installing virtualenv 

```shell
macos   - brew install virtualenv
debian  - apt-get install virtualenv
```
2.  Activate virtual environment and installing dependencies
```shell
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```



