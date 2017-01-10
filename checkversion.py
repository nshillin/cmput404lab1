#!/usr/bin/env python

import requests

print requests.__version__

response = response.get("http://google.com/")
print response.status_code
print response.text
