## Basic Authentication
- This is a method for which an HTTP user agent uses to provide a username and password when making a request.
- In this project, I implemented a Basic Authentication on a simple API

The learning objectives here are:
- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

### Resources
- [REST API Authentication Mechanisms](https://www.youtube.com/watch?v=501dpx2IjGY)
- [Base64 in Python](https://docs.python.org/3/library/base64.html)
- [HTTP header Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
- [Flask](https://palletsprojects.com/p/flask/)
- [Base64 - concept](https://en.wikipedia.org/wiki/Base64)



## Simple API

Simple HTTP API for playing with `User` model.


### Files

#### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

#### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


### Setup

```
$ pip3 install -r requirements.txt
```


### Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


### Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)
