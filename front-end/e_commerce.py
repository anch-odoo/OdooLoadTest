from bs4 import BeautifulSoup
from time import sleep
from random import randint

from locust import FastHttpUser, run_single_user, task


MIN_SLEEP = 1
MAX_SLEEP = 1


class localhost(FastHttpUser):
    host = "http://localhost:8069"
    default_headers = {
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7",
        "Connection": "keep-alive",
        "Host": "localhost:8069",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Chromium";v="152", "Not?A_Brand";v="24", "Google Chrome";v="152"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
    }

    @task(5)
    def check_products(self):
        self.client.client.clientpool.close()
        self.client.cookiejar.clear()
        user_speed = randint(MIN_SLEEP, MAX_SLEEP) / 1000.0

        with self.client.request(
            "GET",
            "/shop",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Referer": "http://localhost:8069/",
                "Sec-Fetch-Dest": "iframe",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "GET",
            "/website/translations?hash=40099c13aa79a172460fbaeb7a3ff1c32cf8c15e&lang=en_US",
            headers={
                "Accept": "*/*",
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
                "Referer": "http://localhost:8069/shop",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.client.request(
            "GET",
            "/shop/customizable-desk-9",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Referer": "http://localhost:8069/shop",
                "Sec-Fetch-Dest": "iframe",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "POST",
            "/web/dataset/call_kw/ir.model/get_available_models",
            headers={
                "Accept": "*/*",
                "Origin": "http://localhost:8069",
                "Referer": "http://localhost:8069/shop/customizable-desk-9",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
            json={
                "id": 8,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "model": "ir.model",
                    "method": "get_available_models",
                    "args": [],
                    "kwargs": {
                        "context": {
                            "lang": "en_US",
                            "tz": "Asia/Shanghai",
                            "uid": 2,
                            "allowed_company_ids": [1],
                        }
                    },
                },
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "GET",
            "/website/translations?hash=40099c13aa79a172460fbaeb7a3ff1c32cf8c15e&lang=en_US",
            headers={
                "Accept": "*/*",
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
                "Referer": "http://localhost:8069/shop/customizable-desk-9",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "POST",
            "/website_sale/get_combination_info",
            headers={
                "Accept": "*/*",
                "Origin": "http://localhost:8069",
                "Referer": "http://localhost:8069/shop/customizable-desk-9?attribute_values=50%2C88",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
            json={
                "id": 0,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "product_template_id": 9,
                    "product_id": 13,
                    "combination": [4, 1],
                    "add_qty": 1,
                    "uom_id": None,
                },
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "POST",
            "/shop/products/recently_viewed_update",
            headers={
                "Accept": "*/*",
                "Origin": "http://localhost:8069",
                "Referer": "http://localhost:8069/shop/customizable-desk-9?attribute_values=50%2C88",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
            json={
                "id": 1,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {"product_id": 13},
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.client.request(
            "GET",
            "/shop/category/desks-1",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Referer": "http://localhost:8069/shop/customizable-desk-9?attribute_values=50%2C88",
                "Sec-Fetch-Dest": "iframe",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/website/translations?hash=40099c13aa79a172460fbaeb7a3ff1c32cf8c15e&lang=en_US",
            headers={
                "Accept": "*/*",
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
                "Referer": "http://localhost:8069/shop/category/desks-1",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/shop/desks-1/furn-1118-corner-desk-left-sit-18",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Referer": "http://localhost:8069/shop/category/desks-1",
                "Sec-Fetch-Dest": "iframe",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "GET",
            "/website/translations?hash=40099c13aa79a172460fbaeb7a3ff1c32cf8c15e&lang=en_US",
            headers={
                "Accept": "*/*",
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
                "Referer": "http://localhost:8069/shop/desks-1/furn-1118-corner-desk-left-sit-18",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
        ) as resp:
            pass
        with self.rest(
            "POST",
            "/website_sale/get_combination_info",
            headers={
                "Accept": "*/*",
                "Origin": "http://localhost:8069",
                "Referer": "http://localhost:8069/shop/desks-1/furn-1118-corner-desk-left-sit-18",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
            json={
                "id": 0,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "product_template_id": 18,
                    "product_id": 32,
                    "combination": [],
                    "add_qty": 1,
                    "uom_id": None,
                },
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.client.request(
            "GET",
            "/shop/category/desks-1",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Referer": "http://localhost:8069/shop/desks-1/furn-1118-corner-desk-left-sit-18",
                "Sec-Fetch-Dest": "iframe",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "POST",
            "/shop/products/recently_viewed_update",
            headers={
                "Accept": "*/*",
                "Origin": "http://localhost:8069",
                "Referer": "http://localhost:8069/shop/desks-1/furn-1118-corner-desk-left-sit-18",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
            json={
                "id": 1,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {"product_id": 32},
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "GET",
            "/website/translations?hash=40099c13aa79a172460fbaeb7a3ff1c32cf8c15e&lang=en_US",
            headers={
                "Accept": "*/*",
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
                "Referer": "http://localhost:8069/shop/category/desks-1",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/shop/desks-1/furn-7888-desk-stand-with-screen-21",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Referer": "http://localhost:8069/shop/category/desks-1",
                "Sec-Fetch-Dest": "iframe",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/website/translations?hash=40099c13aa79a172460fbaeb7a3ff1c32cf8c15e&lang=en_US",
            headers={
                "Accept": "*/*",
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
                "Referer": "http://localhost:8069/shop/desks-1/furn-7888-desk-stand-with-screen-21",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "POST",
            "/website_sale/get_combination_info",
            headers={
                "Accept": "*/*",
                "Origin": "http://localhost:8069",
                "Referer": "http://localhost:8069/shop/desks-1/furn-7888-desk-stand-with-screen-21",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
            json={
                "id": 0,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "product_template_id": 21,
                    "product_id": 35,
                    "combination": [],
                    "add_qty": 1,
                    "uom_id": None,
                },
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "POST",
            "/shop/products/recently_viewed_update",
            headers={
                "Accept": "*/*",
                "Origin": "http://localhost:8069",
                "Referer": "http://localhost:8069/shop/desks-1/furn-7888-desk-stand-with-screen-21",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
            json={
                "id": 1,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {"product_id": 35},
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.client.request(
            "GET",
            "/shop/category/desks-1",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Referer": "http://localhost:8069/shop/desks-1/furn-7888-desk-stand-with-screen-21",
                "Sec-Fetch-Dest": "iframe",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/website/translations?hash=40099c13aa79a172460fbaeb7a3ff1c32cf8c15e&lang=en_US",
            headers={
                "Accept": "*/*",
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
                "Referer": "http://localhost:8069/shop/category/desks-1",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
        ) as resp:
            pass

    @task(1)
    def buy_a_product(self):
        self.client.cookiejar.clear()
        csrf_token = False
        access_token = False
        user_speed = randint(MIN_SLEEP, MAX_SLEEP) / 1000.0

        with self.client.request(
            "GET",
            "/shop",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Referer": "http://localhost:8069/",
                "Sec-Fetch-Dest": "iframe",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "GET",
            "/website/translations?hash=40099c13aa79a172460fbaeb7a3ff1c32cf8c15e&lang=en_US",
            headers={
                "Accept": "*/*",
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
                "Referer": "http://localhost:8069/shop",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.client.request(
            "GET",
            "/shop/customizable-desk-9",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Referer": "http://localhost:8069/shop",
                "Sec-Fetch-Dest": "iframe",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "POST",
            "/web/dataset/call_kw/ir.model/get_available_models",
            headers={
                "Accept": "*/*",
                "Origin": "http://localhost:8069",
                "Referer": "http://localhost:8069/shop/customizable-desk-9",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
            json={
                "id": 8,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "model": "ir.model",
                    "method": "get_available_models",
                    "args": [],
                    "kwargs": {
                        "context": {
                            "lang": "en_US",
                            "tz": "Asia/Shanghai",
                            "uid": 2,
                            "allowed_company_ids": [1],
                        }
                    },
                },
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "GET",
            "/website/translations?hash=40099c13aa79a172460fbaeb7a3ff1c32cf8c15e&lang=en_US",
            headers={
                "Accept": "*/*",
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
                "Referer": "http://localhost:8069/shop/customizable-desk-9",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "POST",
            "/website_sale/get_combination_info",
            headers={
                "Accept": "*/*",
                "Origin": "http://localhost:8069",
                "Referer": "http://localhost:8069/shop/customizable-desk-9?attribute_values=50%2C88",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
            json={
                "id": 0,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "product_template_id": 9,
                    "product_id": 13,
                    "combination": [4, 1],
                    "add_qty": 1,
                    "uom_id": None,
                },
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "POST",
            "/website_sale/get_combination_info",
            headers={
                "Accept": "*/*",
                "Origin": "http://localhost:8069",
                "Referer": "http://localhost:8069/shop/customizable-desk-9?attribute_values=50%2C89",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
            json={
                "id": 1,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "product_template_id": 9,
                    "product_id": 13,
                    "combination": [4, 2],
                    "add_qty": 1,
                    "uom_id": None,
                },
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "POST",
            "/website_sale/get_combination_info",
            headers={
                "Accept": "*/*",
                "Origin": "http://localhost:8069",
                "Referer": "http://localhost:8069/shop/customizable-desk-9?attribute_values=50%2C89",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
            json={
                "id": 2,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "product_template_id": 9,
                    "product_id": 14,
                    "combination": [4, 2],
                    "add_qty": 1,
                    "uom_id": None,
                },
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "POST",
            "/website_sale/should_show_product_configurator",
            headers={
                "Accept": "*/*",
                "Origin": "http://localhost:8069",
                "Referer": "http://localhost:8069/shop/customizable-desk-9?attribute_values=50%2C89",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
            json={
                "id": 3,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "product_template_id": 9,
                    "ptav_ids": [4, 2],
                    "is_product_configured": True,
                },
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "POST",
            "/website_sale/product_configurator/get_values",
            headers={
                "Accept": "*/*",
                "Origin": "http://localhost:8069",
                "Referer": "http://localhost:8069/shop/customizable-desk-9?attribute_values=50%2C89",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
            json={
                "id": 4,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "product_template_id": 9,
                    "quantity": 1,
                    "so_date": "2026-09-11 08:55:58",
                    "ptav_ids": [4, 2],
                    "only_main_product": False,
                    "show_packaging": True,
                },
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "POST",
            "/shop/cart/add",
            headers={
                "Accept": "*/*",
                "Origin": "http://localhost:8069",
                "Referer": "http://localhost:8069/shop/customizable-desk-9?attribute_values=50%2C89",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
            json={
                "id": 5,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "product_template_id": 9,
                    "product_id": 14,
                    "quantity": 1,
                    "uom_id": 1,
                    "product_custom_attribute_values": [],
                    "no_variant_attribute_value_ids": [],
                    "linked_products": [],
                },
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.client.request(
            "GET",
            "/shop/cart",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Referer": "http://localhost:8069/shop/customizable-desk-9?attribute_values=50%2C89",
                "Sec-Fetch-Dest": "iframe",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "GET",
            "/website/translations?hash=40099c13aa79a172460fbaeb7a3ff1c32cf8c15e&lang=en_US",
            headers={
                "Accept": "*/*",
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
                "Referer": "http://localhost:8069/shop/cart",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "POST",
            "/shop/express/shipping_address_change",
            headers={
                "Accept": "*/*",
                "Origin": "http://localhost:8069",
                "Referer": "http://localhost:8069/shop/cart",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
            json={
                "id": 0,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "partial_delivery_address": {
                        "name": "Mitchell Admin",
                        "email": "admin@example.com",
                        "street": "215 Vine St",
                        "street2": "",
                        "zip": "18503",
                        "city": "Scranton",
                        "country": "US",
                    }
                },
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "POST",
            "/shop/set_delivery_method",
            headers={
                "Accept": "*/*",
                "Origin": "http://localhost:8069",
                "Referer": "http://localhost:8069/shop/cart",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
            json={"id": 1, "jsonrpc": "2.0", "method": "call", "params": {"dm_id": 1}},
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "POST",
            "/shop/express_checkout",
            headers={
                "Accept": "*/*",
                "Origin": "http://localhost:8069",
                "Referer": "http://localhost:8069/shop/cart",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
            json={
                "id": 2,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "shipping_address": {
                        "name": "Mitchell Admin",
                        "email": "admin@example.com",
                        "street": "215 Vine St",
                        "street2": "",
                        "zip": "18503",
                        "city": "Scranton",
                        "country": "US",
                    },
                    "billing_address": {
                        "name": "Demo User",
                        "email": "demo@test.com",
                        "street": "Rue des Bourlottes 9",
                        "street2": "23",
                        "country": "BE",
                        "city": "Ramillies",
                        "zip": "1367",
                    },
                },
            },
        ) as resp:
            soup = BeautifulSoup(resp.text, 'lxml')
            csrf_token = soup.select_one("input[name='csrf_token']")["value"]
            access_token = soup.select_one("form[data-access-token]")["data-access-token"]
        sleep(user_speed)
        with self.rest(
            "POST",
            "/shop/payment/transaction/37",
            headers={
                "Accept": "*/*",
                "Origin": "http://localhost:8069",
                "Referer": "http://localhost:8069/shop/cart",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
            json={
                "id": 3,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "provider_id": 6,
                    "payment_method_id": 159,
                    "token_id": None,
                    "flow": "direct",
                    "tokenization_requested": False,
                    "landing_route": "/shop/payment/validate",
                    "access_token": access_token,
                    "csrf_token": csrf_token,
                },
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "POST",
            "/payment/demo/simulate_payment",
            headers={
                "Accept": "*/*",
                "Origin": "http://localhost:8069",
                "Referer": "http://localhost:8069/shop/cart",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
            json={
                "id": 4,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "reference": "S00037",
                    "payment_details": "",
                    "simulated_state": "done",
                },
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.client.request(
            "GET",
            "/payment/status",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Referer": "http://localhost:8069/shop/cart",
                "Sec-Fetch-Dest": "iframe",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "GET",
            "/website/translations?hash=40099c13aa79a172460fbaeb7a3ff1c32cf8c15e&lang=en_US",
            headers={
                "Accept": "*/*",
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
                "Referer": "http://localhost:8069/payment/status",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "POST",
            "/payment/status/poll",
            headers={
                "Accept": "*/*",
                "Origin": "http://localhost:8069",
                "Referer": "http://localhost:8069/payment/status",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
            json={
                "id": 0,
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "csrf_token": csrf_token
                },
            },
        ) as resp:
            pass
        sleep(user_speed)
        with self.client.request(
            "GET",
            "/shop/payment/validate",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Referer": "http://localhost:8069/payment/status",
                "Sec-Fetch-Dest": "iframe",
                "Sec-Fetch-Mode": "navigate",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        sleep(user_speed)
        with self.client.request(
            "GET",
            "/shop/confirmation",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Referer": "http://localhost:8069/payment/status",
                "Sec-Fetch-Dest": "iframe",
                "Sec-Fetch-Mode": "navigate",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        sleep(user_speed)
        with self.rest(
            "GET",
            "/website/translations?hash=40099c13aa79a172460fbaeb7a3ff1c32cf8c15e&lang=en_US",
            headers={
                "Accept": "*/*",
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
                "Referer": "http://localhost:8069/shop/confirmation",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
            },
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(localhost)
