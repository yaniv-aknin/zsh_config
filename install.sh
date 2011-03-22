#! /bin/sh

rsync -avP .zshrc ~/.zshrc
rsync -avP --delete .zsh.d/ ~/.zsh.d/

