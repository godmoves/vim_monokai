# Vim monokai

A monokai color scheme for vim, inspired by [Erich Gubler](https://github.com/ErichDonGubler/vim-sublime-monokai) and [nfnty](https://github.com/vim-python/python-syntax). If you have any questions, feel free to open an issue :)

## How to use

1. Install [vim plug](https://github.com/junegunn/vim-plug):
```
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

2. Add this to plugins list in your `.vimrc`:
```
 " Plugins will be downloaded under the specified directory.
 call plug#begin('~/.vim/plugged')

 " Declare the list of plugins.
 Plug 'godmoves/vim_monokai'

 " List ends here. Plugins become visible to Vim after this call.
 call plug#end()
```

3. Set the color scheme to monokai:
```
colorscheme vimmonokai
```

4. Some enhancements:
```
" Make your terminal more colorful
set termguicolors

" Enable Italic font
let g:vimmonokai_term_italic = 1
```

