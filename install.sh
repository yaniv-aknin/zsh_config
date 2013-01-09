#! /bin/sh

# http://stackoverflow.com/questions/59895/can-a-bash-script-tell-what-directory-its-stored-in

ZSH_DIR="$( cd "$( dirname "$0" )" && pwd )"
[ -z "$HOME_DIR" ] && HOME_DIR="$1"
[ -z "$HOME_DIR" ] && HOME_DIR="$HOME"

cat > "$HOME_DIR"/.zshrc << EOF
##### Zsh directory ##############################################
ZSH_DIR="$ZSH_DIR"

export PATH="$ZSH_DIR/bin":"$PATH"

for zshrc_snipplet in \$ZSH_DIR/S* ; do
    source \$zshrc_snipplet
done

SITE_CUSTOM_FILE=\$HOME/.zsh.site

if [ -e \$SITE_CUSTOM_FILE ]; then
    source \$SITE_CUSTOM_FILE
fi
EOF

cd "$ZSH_DIR"/src
for c_file in *.c; do
    implicit_makefile="$(echo $c_file | sed -e 's/\.c$//')"
    make "$implicit_makefile"
done
