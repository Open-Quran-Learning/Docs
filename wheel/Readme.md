# Ayat data base models

## Installation


```bash
pip install -r requirements
pip install ayat.models-0.1-py3-none-any
```
requirements file on main repositry.
## Usage: 
You should first do two things in your code:
- Replace this line with yours like the example
```python
model.app.config["SQLALCHEMY_DATABASE_URI"] = "<your local database link>"

```
Example:
```python
model.app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:root@localhost:5432/postgres"

```

- this import in creating/deleting data base. 

```python
from data_factory import *

```
### create data base
```python
model.setup_db()

```

### delete data base
```python
model.teardown_db()

```
