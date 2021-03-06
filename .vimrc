set nocompatible
execute pathogen#infect()
filetype plugin indent on

set t_Co=256
set shell=/bin/bash
set laststatus=2
set timeoutlen=300
set backspace=2
set showcmd

let g:airline#extensions#tabline#enabled = 1
let g:airline_powerline_fonts = 1
let g:airline_theme='gruvbox'

" NERDTree
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
map <C-n> :NERDTreeToggle<CR>
"autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
let g:NERDTreeDirArrowExpandable = '▸'
let g:NERDTreeDirArrowCollapsible = '▾'

" Folds
setlocal foldmethod=indent

set hlsearch
set number
set rnu
set tabstop=4
set softtabstop=4
set shiftwidth=4
set noshowmode
syntax on
set background=dark
set list
set listchars=tab:\|\ ,trail:~,extends:>,precedes:<
set splitright
set splitbelow
set mouse=a

let mapleader = ","
nnoremap <Leader>w :w<CR>
nnoremap <Leader>q :bd<CR>
nnoremap <Leader>z u<CR>
nnoremap <Leader>r :redo<CR>

" Go through buffers
nnoremap <silent> <C-Right> :bn<CR>
nnoremap <silent> <C-Left> :bp<CR>
nnoremap <Tab> :bn<CR>
nnoremap <S-Tab> :bp<CR>

set undofile
set undodir=~/.vim/undodir

command W :execute ':silent w !sudo tee % > /dev/null' | :edit!

"set expandtab for python
au Filetype python setl et ts=4 sw=4

"set spaces instead of tab for jsx
au Filetype javascript.jsx setl et ts=2 sts=2 sw=2

:hi PreProc ctermfg=magenta cterm=bold guifg=#FF00FF

let g:jsx_ext_required = 0

" Format document
nnoremap <F7> mzgg=G`z

" Remove trailing spaces
fun! <SID>StripTrailingWhitespaces()
	let l = line(".")
	let c = col(".")
	%s/\s\+$//e
	call cursor(l, c)
endfun

autocmd FileType c,cpp,python,html,bash,vim,css,jinja,javascript,php,m,h,hpp,makefile autocmd BufWritePre <buffer> :call <SID>StripTrailingWhitespaces()
" NE DIRAJ!!!
color gruvbox

map Od <C-Left>
map Oc <C-Right>
map! Od <C-Left>
map! Oc <C-Right>
map Oa <C-Up>
map Ob <C-Down>
map! Oa <C-Up>
map! Ob <C-Down>

" fixed page scrolling
noremap <C-Down> <C-E>
noremap <C-Up> <C-Y>


" HNEI arrows.
"noremap <buffer> <silent> e gk
"noremap <buffer> <silent> n gj
"noremap <silent> i l
" Last search.
"noremap k n
"noremap K N
" mark
"noremap j m
"noremap J M
" _r_ = inneR text objects.
"onoremap r i
" l/L insert
"noremap l i
"noremap L I
" EOW.
"noremap m e
"noremap M E


