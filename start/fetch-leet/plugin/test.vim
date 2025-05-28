vim9script noclear
# Vim package plugin to fecth stuff from leetcode graph-ql API
# Last Change: 2025 May
# Maintainer: Atharv Bhagya <atharv008@gmail.com>
# License: same as Vim itself. see :h license


if exists("g:loaded_typecorrect")
   finish
endif
g:loaded_typecorrect = 1


if !hasmapto('<Plug>TestAdd;')
    map <unique> <Leader>aa  <Plug>TestAdd;
endif


var count = 0

def Add(msg_str: string)
    count += 1
    echo msg_str .. ' count is: ' .. count
enddef

nnoremap <unique> <script> <Plug>TestAdd; <SID>Add
nnoremap <SID>Add :call <SID>Add("Messi!!!!")<CR>




def Fetcher(args: string)
    echo 'talking to asyncio ' .. args
    var channel = ch_open('localhost:6666', {'mode': 'raw'})
    call ch_sendraw(channel, "Hello, asyncio!\n")  # \n triggers asyncio's reader
    echo 'sent request!'
    var response = ch_readraw(channel)
    echo 'response received from asyncio ' .. response
enddef


command -nargs=+ MakeReq :call Fetcher(<q-args>)


## Here is the mapping that is also exposed to the users to be re-mapped
if !hasmapto('<Plug>TestFetcher;')
    nnoremap <unique> <leader>ff <Plug>TestFetcher;
endif

nnoremap <unique> <script> <Plug>TestFetcher; <SID>Fetcher
nnoremap <SID>Fetcher :MakeReq some args passed<CR>



