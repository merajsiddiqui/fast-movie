# fast-movie
A movie booking api similar to book my show

> This is SOA based architecture to provide a simplistic 
> **REST API**  for a movie booking service. Where user can look for 
> movies playing in their city and different cinemas and 
> respectively book tickets for their favorite movie they want




### Application Structure
This is How Our Application is structured
```
π¦fast-moview
 β£ π.github
 β£ π.idea
 β£ π app
 β    β£ π models
 β    β£ π services
 β      β π ExampleEvents.php
 β    β£ π routers
 β    β£ π helpers
 β      β π ExampleHelper.php
 β    β£ π Listeners
 β      β π ExampleEventListener.php
 β£ π.gitignore
 β£ π requirements.txt
 β π Dockerfile
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



