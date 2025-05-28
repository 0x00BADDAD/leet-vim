vim9script noclear




def CreateAndAddBuf(name: string): number
    var bufnr   = bufadd(name)
    var bufname = bufname(bufnr)
    setbufvar(bufname, "&buflisted", 1)
    setbufvar(bufname, "&bufhidden", "hide") ## This helps to change the buffers without saving them to a file
    call bufload(bufnr)
    call setbufline(bufnr, 1, [name .. 'buffer1_name', name .. 'buffer2_name', name .. 'buffer3_name'])
    setbufvar(bufname, "&modifiable", 0)
    setbufvar(bufname, "&modified", v:false)
    setbufvar(bufname, "&buftype", "nofile")
    setbufvar(bufname, "&swapfile", 0)
    return bufnr
enddef

## I have a buffer and i press <CR> it will create a buffer and load it.
## There has to be a history so that when the '-' button is pressed we go back and '+' button
## we move ahead.

def AppendHistory(name: string): void
    ## pass
enddef

def MoveHead()
    var buffer_name = getline('.')
    if !bufexists(buffer_name)
        var bufnr = CreateAndAddBuf(buffer_name)
    endif
    AppendHistory(buffer_name)
    exe 'buf ' .. buffer_name
enddef


def InitUI()
    var bufnr = CreateAndAddBuf('Init buffer')
    exe 'buf ' .. bufname(bufnr)
enddef


nnoremap <unique> <leader>qq :call <SID>InitUI()<CR>
nnoremap <unique> -- :call <SID>MoveHead()<CR>

