# cross2016-api

[![Build Status](https://travis-ci.org/chibiegg/cross2016-api.svg)](https://travis-ci.org/chibiegg/cross2016-api)

## Requiements

* Python3.4
* pip
* See `package.pip`

## Quick Start

* `git clone https://github.com/chibiegg/cross2016-api.git`
* `cd cross2016-api/src`
* `pip install -r ../package.pip`
* `cp cross2016/settings.py.template cross2016/settings.py`
* `python manage.py syncdb`
* `python manage.py runserver`
* Open `http://localhost:8000/` for testing.
