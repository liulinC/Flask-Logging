## Flask-Logging

Filter certain requests from the Flask log. Useful during development when requests fill up with /static/ URLs. Not for use in production, Flask-Logging monkey patches the ```werkzeug``` logging function.

#### Installation

```
pip install flask-logging
```

#### Usage

```
from flask_logging import Filter
filter = Filter('static')
```

Filters any request with the word 'static' from the log.

Filtering more than one word:

```
filter = Filter('static', 'admin')
```

Updating the filter:

```
filter = Filter('static')
filter.filters = 'static', 'admin'
```
