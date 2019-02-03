if !has('pythonx')
    echoerr "vim-vim_auto_docstring requires Python. Cannot continue loading this plugin"
    finish
endif

if get(g:, 'vim_auto_docstring_loaded', '0') == '1'
    finish
endif

let g:vim_auto_docstring_loaded = '1'
