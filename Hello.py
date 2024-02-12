from tr_st import init_global_tornado_hook, CustomRule
from tornado.web import RequestHandler
from json_db import JsonDatabase
import random


class lrcpayment(RequestHandler):
    def initialize(self, database):
        self.database = database
    def get(self, user1,user2,amount):
        database = JsonDatabase("payment.json")
        if f"{user1},{user2},{amount}" in database.db.values():
            for k,v in list(database.db.items()):
                if v == f"{user1},{user2},{amount}":
                    del database.db[k]
            database.update({})
            return {"received":"true"}
        return {"received":"false"}

class APIhandler:
    def __init__(self) -> None:pass
    def addt(self,user1,user2,amount):
        JsonDatabase("payment.json").update({str(random.randint(111111,999999)):f"{user1},{user2},{amount}"})

init_global_tornado_hook([CustomRule(r'/payment/(.*)/(.*)/(.*)/', lrcpayment, {})])
