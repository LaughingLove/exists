#!/bin/bash

if [ ! -d ~/bin ]; then
    echo "~/bin does not exist, creating one.."
    echo ""
    mkdir ~/bin
else
    echo "~/bin exists.."
    echo ""
fi

if [ -f ~/bin/exists.py ]; then
    echo "exists.py found in ~/bin, no need creating symbolic link..."
    echo ""
else
    echo "exists.py not found in ~/bin, creating symbolic link.."
    echo ""
    ln exists.py ~/bin
fi

if grep 'export PATH="/home/$USER/bin:$PATH"' ~/.bashrc
    then
        echo " ~/.bashrc line found! No need to add it..."
        echo ""
    else
        echo "~/.bashrc line not found! Adding line..."
        echo ""
        echo 'export PATH="/home/$USER/bin:$PATH"' >> ~/.bashrc
fi

echo ""
echo "Installation complete! Restart your terminal and type exists.py for the help options!"