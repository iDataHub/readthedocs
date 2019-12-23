#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File      : test.py
@Time      : 2019/12/23
@Docstring : No news is good news.
'''

import faker
import os
import re
import requests
import threading


def main():
    def is_available(link, **kwargs):
        prompt = '[{:<3}]: {}\n'
        try:
            response = requests.head(link, **kwargs)
            if response.status_code >= 400:
                print(prompt.format(response, link))
        except requests.exceptions.ConnectionError:
            print(prompt.format('CE', link))
        except requests.exceptions.ReadTimeout:
            print(prompt.format('RT', link))


    def extract_domain_names(links):
        domain_pattern = re.compile(r'(?<=//)[^/]+(?=/|$)')
        domain_names = sum(map(domain_pattern.findall, links), list())
        for ith in range(len(domain_names)):
            domain_names[ith] = '.'.join(domain_names[ith].split('.')[-2:])
        return set(domain_names)


    links = list()
    link_pattern = re.compile(r'https?://[^\)\s]+')

    for dirpath, dirnames, filenames in os.walk(os.path.curdir):
        for filename in filenames:
            if filename.endswith('.md'):
                with open(os.path.join(dirpath, filename), 'r') as f:
                    links += link_pattern.findall(f.read())

    headers = {'user-agent': faker.Faker().user_agent()}
    for link in links:
        threading.Thread(target=is_available,
            args=(link, ),
            kwargs=dict(headers=headers, timeout=3)
        ).start()

    print('Domain names:', extract_domain_names(links))



if __name__ == '__main__':
    main()
