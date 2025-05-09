import sys, os
from pathlib import Path
import logging

## do we really gotta do this?
## pkgs_path = os.path.join(os.getcwd(), 'pkgs')
## sys.path.append(pkgs_path)
##
## We can also just set the PYTHONPATH ENV VAR to where our 'pkgs' (package)
## folder is loacted

import pkgs.utils.payload.payload_gen as payload_gen


import asyncio
import aiohttp
import json

#######################Setting Logger Up!#####################################
## set up the logger to console (for level from DEBUG)
logging.basicConfig(level=logging.DEBUG,
                    format= '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M')


console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)


## adding the console handler to root logger of the module
logging.getLogger('').addHandler(console)

##############################################################################







def make_url():
    question_url= 'https://leetcode.com/graphql/'
    return question_url


async def main():
    async with aiohttp.ClientSession() as session:
        payload = payload_gen.payload_gen('question_data', {"titleSlug": "add-two-numbers"})
        async with session.post(make_url(), json=payload) as resp:
            print(resp.status)
            resp_text = await resp.json()
            resp_text = resp_text['data']['question']

            print(f'Type of resp_test is: {type(resp_text)}\n')
            ##for k in resp_text.keys():
            ##    print(f'key-> {k}\n')

            #with open('question.json', 'w') as resp_file:
            #    json.dump(resp_text, resp_file)

            resp_text = '<html><head></head><body>' + resp_text['content'] + '</body></html>'
            ## TODO: to make the os.getcwd() more independent
            ## right now this will only put the .html file in the scrapped-data/static folder if the main script is run from the python dir...
            ## can we make this so that its independent of where this
            ## file is run from?
            data_dir = os.path.join(os.getcwd(), 'scrapped-data', 'static')
            with open(data_dir + f'/{payload['variables']['titleSlug']}.html', 'w') as q_html:
                q_html.write(resp_text)

if __name__ == '__main__':
    ## DON'T FORGET to add the path to python dir to your PYHTONPATH ENV VARIABLE!
    asyncio.run(main())



