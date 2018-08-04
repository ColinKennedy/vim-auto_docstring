if !has('python')
    echoerr "vim-vim_auto_docstring requires Python. Cannot continue loading this plugin"
    finish
endif

if get(g:, 'vim_auto_docstring_loaded', '0') == '1'
    finish
endif

python << EOF
from vim_auto_docstring.auto_docstring.styles import epydoc
from vim_auto_docstring.auto_docstring.styles import google
from vim_auto_docstring.auto_docstring.styles import numpy
from vim_auto_docstring.auto_docstring.styles import sphinx
from vim_auto_docstring.auto_docstring.config import environment

environment.register_code_style(epydoc.EpydocStyle.name, epydoc.EpydocStyle)
environment.register_code_style(google.GoogleStyle.name, google.GoogleStyle)
environment.register_code_style(numpy.NumpyStyle.name, numpy.NumpyStyle)
environment.register_code_style(sphinx.SphinxStyle.name, sphinx.SphinxStyle)
EOF

let g:vim_auto_docstring_loaded = '1'
