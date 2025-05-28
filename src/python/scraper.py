import sys, os

## do we really gotta do this?
## pkgs_path = os.path.join(os.getcwd(), 'pkgs')
## sys.path.append(pkgs_path)
## Nope i have opted for another option, check out scraper.py in
## some/deep/dir/

import asyncio
import aiohttp
import json

import pkgs.utils.payload.payload_gen as payload_gen

## vim keypress sends a req to python process
## and python process maps it to a async coroutine and then runs it
## Aim to design a way to route my requests from vim to HTTP requests over gql API
## different APIs return different data and that data can be further
## used to feed into the subsequent gql --> may be create pipelines of such HTTP
## requests 
## keypress --> a request goes to a server and then maps to a pipeline of HTTP requests  --> buffer with formatted data


def make_url():
    question_url= 'https://leetcode.com/graphql/'
    return question_url


async def main(query_key, vars_data):
    async with aiohttp.ClientSession() as session:
        payload = payload_gen.payload_gen(query_key, vars_data)
        async with session.post(make_url(), json=payload) as resp:
            print(resp.status)
            resp_text = await resp.json()


            data_dir = os.path.join(os.getcwd(), 'scrapped-data', 'json')

            with open(data_dir + f'/{query_key}.json', 'w') as resp_file:
                json.dump(resp_text, resp_file)

            resp_text = resp_text['data']['question']

            print(f'Type of resp_test is: {type(resp_text)}\n')
            for k in resp_text.keys():
                print(f'key-> {k}\n')


            resp_text = '<html><head></head><body>' + resp_text['content'] + '</body></html>'

            data_dir = os.path.join(os.getcwd(), 'scrapped-data', 'static')
            with open(data_dir + f'/{payload['variables']['titleSlug']}.html', 'w') as q_html:
                q_html.write(resp_text)





if __name__ == '__main__':
    asyncio.run(main())



