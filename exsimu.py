#!/usr/bin/env python3
import modules.exsimuapi
import time
from exapi import ExAPI
from depth import depth

#    pair = "btc_usd"


class exsimu(ExAPI):

    def __init__(self, data, name='exsimu'):
        self.api = modules.exsimuapi.API(data)
        self.name = name
        self.curdepth = {}

    def get_fees(self, **kwargs):
        kwargs.setdefault('pair', 'btc_eur')
        if kwargs['pair'] == 'btc_eur':
            return 0.002
        else:
            return Exception('cannot get fees')

    def get_balance(self, dummy=None):
        try:
            return self.api.get_balance()
        except Exception as e:
            print(e)
            raise Exception('cannot get balance')

    def add_order(self, order, price, vol, pair='btc_eur'):
        s = self.api.add_order(pair=pair,
                               order=order,
                               price=price,
                               vol=vol)
        return s

    def active_orders(self):
        return self.api.get_active_orders()

    def cancel_order(self, orderid):
        return self.api.cancel_order(orderid)

    def get_trades(self, **kwargs):
        pass

    def print_depth(self, **kwargs):
        print(self.curdepth)

    def get_depth(self, **kwargs):
        kwargs.setdefault('pair', 'btc_eur')
        try:
            s = self.api.get_depth(kwargs)
        except Exception as e:
            print(e)
        d = depth(**s)
        self.curdepth[kwargs['pair']] = [d, time.time()]
        return d
