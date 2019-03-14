## Product API

### Install

```script
pipenv install flask
pipenv install flask-restful
pipenv install flask-sqlalchemy
pipenv install flask-marshmallow
pipenv install marshmallow-sqlalchemy
```

### Create database

```python
from app import db
db.create_all()
```
