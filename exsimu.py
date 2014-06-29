#!/usr/bin/env python3
import modules.exsimuapi
import time
from exapi import ExAPI
from depth import depth

#    pair = "btc_usd"


class exsimu(ExAPI):
    depth = {}
    name = 'exsimu'

    def __init__(self, passwd=None):
        self.api = modules.exsimuapi.API()

    def get_fees(self, **kwargs):
        kwargs.setdefault('pair', 'btc_eur')
        if kwargs['pair'] == 'btc_eur':
            return 0.2
        else:
            return Exception('pair?')

    def get_balance(self, dummy=None):
        balance = {}
        try:
            result = self.api.getInfo()['return']['funds']
            for s in ['btc', 'eur']:
                balance[s] = result[s]
            return balance
        except Exception as e:
            print(e)
        pass

    def add_order(self, order, price, vol):
        pass

    def get_trades(self, **kwargs):
        pass

    def get_depth(self, **kwargs):
        kwargs.setdefault('pair', 'btc_eur')
        try:
            s = self.api.get_param(kwargs['pair'], 'depth')
        except Exception as e:
            print(e)
        d = depth(**s)
        exsimu.depth[kwargs['pair']] = [d, time.time()]
        return d
