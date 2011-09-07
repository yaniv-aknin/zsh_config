#! /bin/sh

# http://stackoverflow.com/questions/59895/can-a-bash-script-tell-what-directory-its-stored-in

cat > ~/.zshrc << EOF
##### Zsh directory ##############################################
ZSH_DIR="$( cd "$( dirname "$0" )" && pwd )"

for zshrc_snipplet in \$ZSH_DIR/S* ; do
    source \$zshrc_snipplet
done

SITE_CUSTOM_FILE=\$HOME/.zsh.site

if [ -e \$SITE_CUSTOM_FILE ]; then
    source \$SITE_CUSTOM_FILE
fi
EOF
