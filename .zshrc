##
# DELUXE-USR-LOCAL-BIN-INSERT
# (do not remove this comment)
##
echo $PATH | grep -q -s "/usr/local/bin"
if [ $? -eq 1 ] ; then
    PATH=$PATH:/usr/local/bin
    export PATH
fi

##### Zsh directory ##############################################
ZSH_DIR=$HOME/.zsh.d

for zshrc_snipplet in $ZSH_DIR/S* ; do
    source $zshrc_snipplet
done

SITE_CUSTOM_FILE=$HOME/.zsh.site

if [ -e $SITE_CUSTOM_FILE ]; then
    source $SITE_CUSTOM_FILE
fi
