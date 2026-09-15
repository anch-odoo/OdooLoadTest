# Before everything

Watch this [YT tutorial](https://www.youtube.com/watch?v=HaHzHME2eF8&list=PL1pbTTfOBPOrud6OwOwoQoC5MnXMWI1pE&index=8) first

# Back-end load test Flow

1. Create Odoo users:
```
python3 generate_users.py
```

2. Launch the load test:
```
./lt.sh lt_ebusiness.py 8 2000 60 0 50
```

This will launch Locust Web UI, on port 8089, with 8 local workers, 2000 simulated users, for 60 minutes, and add 50 users/s

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

## Use har2locust to capture browsers flows and auto create locust file

- See how to use har2locust in: https://github.com/SvenskaSpel/har2locust
- It would create one User profile with one task
- If you want to test multiple flows, you could simulate your new flow in your browser, download new .har file, export it with har2locust, and copy that one new task and paste it to `e_commerce.py`

## Polish the locust code:

1.  `access_token`, `csrf_token` and `user_speed`

Add this in the beginning of every task

```python
self.client.client.clientpool.close()
self.client.cookiejar.clear()
csrf_token = False
access_token = False
user_speed = randint(MIN_SLEEP, MAX_SLEEP) / 1000.0
```

this will:
- Clear cookie which would make every task call as a new user
- Declare csrf_token and access_token for later use
- User speed is for simulating actual user with some delay

Search the usage of csrf_token and access_token, then find the previous response and add:
```python
) as resp:
    soup = BeautifulSoup(resp.text, 'lxml')
    csrf_token = soup.select_one("input[name='csrf_token']")["value"]
    access_token = soup.select_one("form[data-access-token]")["data-access-token"]
```

- Be mindful: Script from har2locust would include your `access_token` and `csrf_token`, make sure to replace them

2. Remove all `Content-Length` appearance

3. User speed
- Add package `from time import sleep`
- Set static variable
```python
MIN_SLEEP = 1
MAX_SLEEP = 1
```
- Add `sleep(user_speed)` between every request

## Run the load test
```
./lt.sh front-end/e_commerce.py 8 2000 60 0 50
```

Some remarks
1. Increase the load testing workers, maybe it is your load testing limit but not the server
2. Test different number of users per seconds too, there is chance that it would not crash at 10 users/s but crash at 100 users/s

# Useful Link
- odoolib: https://github.com/odoo/odoo-client-lib/blob/master/odoolib/main.py
- OdooLocust: https://github.com/nseinlet/OdooLocust/tree/master
