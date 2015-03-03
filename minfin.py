"""
This module scans 'black' currency market for acceptable rate and pop-up deal info.
"""

import requests
import tkinter as tk
from lxml import html
from time import sleep

USD_RATE = 30  # acceptable rate
URL = "http://minfin.com.ua/currency/auction/usd/sell/all/?sort=time&order=desc"  # 'black' market url


class Deal:
    def __init__(self):
        self._time = ''
        self._rate = ''
        self._currency = ''
        self._deal_sum = ''
        self._message = ''
        self._priority = ''
        self._phone_number = ''

    def __str__(self):
        return 'Time - {time}\n' \
               'Currency - {currency}\n' \
               'Rate - {rate}\n' \
               'Deal sum - {deal_sum}\n' \
               'Message - {message}\n' \
               'Phone - {phone}\n' \
               'Priority - {priority}'.format(time=self.get_time(), currency=self.get_currency(), rate=self.get_rate(),
                                              deal_sum=self.get_deal_sum(), message=self.get_message(),
                                              phone=self.get_phone_number(), priority=self.get_priority())

    def __eq__(self, other):
        return self.get_time() == other.get_time() and self.get_rate() == other.get_rate() \
               and self.get_currency() == other.get_currency() and self.get_deal_sum() == other.get_deal_sum() \
               and self.get_message() == other.get_message() and self.get_phone_number() == other.get_phone_number()

    def get_time(self):
        return self._time

    def get_rate(self):
        return self._rate

    def get_currency(self):
        return self._currency

    def get_deal_sum(self):
        return self._deal_sum

    def get_message(self):
        return self._message

    def get_priority(self):
        return self._priority

    def get_phone_number(self):
        return self._phone_number

    def set_time(self, time):
        self._time = time

    def set_rate(self, rate):
        self._rate = rate

    def set_currency(self, currency):
        self._currency = currency

    def set_deal_sum(self, deal_sum):
        self._deal_sum = deal_sum

    def set_message(self, message):
        self._message = message

    def set_priority(self, priority):
        self._priority = priority

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def is_correct(self):
        if len(self.get_time()) == 0 or len(self.get_rate()) == 0 or len(self.get_currency()) == 0 or \
           len(self.get_deal_sum()) == 0:
            return False
        else:
            return True


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.label = tk.Button(self)
        self.label["text"] = "Hello World\n(click me)"
        self.label.pack(side="top")
        self._quit = tk.Button(self, text="QUIT", fg="red", command=master.destroy)
        self._quit.pack(side="bottom")

# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()


def scan_black_market(url):
    deal_list = []
    page = requests.get(url)
    tree = html.fromstring(page.text)

    deals = tree.xpath('//div[@class="au-deals-list"]')[0]
    for deal_entry in deals:
        deal = Deal()

        time_entry = deal_entry.xpath('small[@class="au-deal-time"]')
        rate_entry = deal_entry.xpath('span[@class="au-deal-currency"]')
        sum_entry = deal_entry.xpath('span[@class="au-deal-sum"]')
        message_entry = deal_entry.xpath('span[@class="au-deal-msg"]')
        phone_number_entry = deal_entry.xpath('span[@class="au-dealer-phone"]')

        if len(time_entry) != 0:
            deal.set_time(time_entry[0].text)

        if len(rate_entry) != 0:
            deal.set_rate(rate_entry[0].text)

        if len(sum_entry) != 0:
            deal.set_deal_sum(sum_entry[0].text)
            deal.set_currency(sum_entry[0].xpath("label")[0].text)

        if len(message_entry) != 0:
            deal.set_message(' '.join(message_entry[0].text.split()))

        if 'au-deal' not in deal_entry.attrib.values():
            deal.set_priority("High")
        else:
            deal.set_priority("Low")

        if len(phone_number_entry) != 0:
            print(dir(phone_number_entry[0].body))
            #print(phone_number_entry[0].xpath('a')[0].attrib.get('data-numbers'))
            #print(dir(phone_number_entry[0]))
            import sys
            sys.exit(1)
            #deal.set_phone_number(phone_number_entry[0].text)

        deal_list.append(deal)
    return deal_list


def main():
    old_deals = []
    counter = 0

    while True:
        all_deals = scan_black_market(URL)
        for deal in all_deals:
            if deal.is_correct() and deal not in old_deals:
                print('#{counter}'.format(counter=counter))
                print(deal)
                print('*' * 50)
                counter += 1
                old_deals.append(deal)
        sleep(90)
        print("slept for 10 sec")


if __name__ == '__main__':
    main()
