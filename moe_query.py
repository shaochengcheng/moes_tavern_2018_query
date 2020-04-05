import requests
import datetime
import calendar
import logging

URL = 'http://carl.cs.indiana.edu/moe/?cert=e3de49bc-3ee8-44c2-9f48-a479098960d4'
DATE_FORMAT = '%Y-%m-%d'


def last_day_of_month_str(year, month, strformat=DATE_FORMAT):
    weekday, ndays = calendar.monthrange(year, month)
    return datetime.date(year, month, ndays).strftime(strformat)


def filename_per_month(year, month):
    return datetime.date(year, month, 1).strftime('%Y-%b') + '-p0.00008'


def query_parameters_by_month(year, month):
    return {
        "email": "shaoc@indiana.edu",
        "qtype": "random-tweets",
        "chance": "0.00008",
        "start": datetime.date(year, month, 1).strftime(DATE_FORMAT),
        "end": last_day_of_month_str(year, month),
        "output": "tweet-content",
        "label": filename_per_month(year, month)
    }


def main():
    # logging.basicConfig()
    # import pdb
    # pdb.set_trace()
    year = 2018
    for month in range(1, 13):
        filename = filename_per_month(year, month)
        with open(filename, 'w') as f:
            payload = query_parameters_by_month(year, month)
            response = requests.post(URL, json=payload)
            if response.status_code != requests.codes.ok:
                logging.error('HTTP error: %s', response)
            else:
                f.write(response.json())


if __name__ == '__main__':
    main()
