#!/usr/bin/env python

import client

test_client = client.client("127.0.0.1", 8000)

print dir(test_client)

print test_client.all_result()
print test_client.area_code("413")
