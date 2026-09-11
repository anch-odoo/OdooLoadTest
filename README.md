# Before everything

Watch this [YT tutorial](https://www.youtube.com/watch?v=HaHzHME2eF8&list=PL1pbTTfOBPOrud6OwOwoQoC5MnXMWI1pE&index=8) first

# Back-end load test Flow

1. Create Odoo users:
```
python3 generate_users.py
```

2. Launch the load test:
```
lt.sh lt_ebusiness.py 8 2000 60 0 50
```

This will launch Locust Web UI, on port 8089, with 8 local workers, 2000 simulated users, for 60 minutes, and add new users at the rythm of 50/s

3. Prepare conf.ini

```
[odoo]
url=myserver.company.local
db=my_loadtest_db
user=admin
pass=admin
[weight]
saleman=10
webshop=200
[frontend]
min_sleep=5
max_sleep=20
```

# Front-end load test Flow

1. Use har2locust to capture browsers flows and auto create locust file

- See how to use har2locust in: https://github.com/SvenskaSpel/har2locust
- It would create one User profile with one task
- If you want to test multiple flows, you could simulate your new flow in your browser, download new .har file, export it with har2locust, and copy that one new task and paste it to `e_commerce.py`

Be mindful:
- Do not include your `access_token` and `csrf_token` when pushing har2locust output python file to the public

# Useful Link
- odoolib: https://github.com/odoo/odoo-client-lib/blob/master/odoolib/main.py
- OdooLocust: https://github.com/nseinlet/OdooLocust/tree/master
