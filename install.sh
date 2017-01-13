#!/bin/bash

### Install script for CCA DFXML Reader in Bitcurator

# Make /usr/share/cca-dfxmlreader if doesn't already exist
if [ ! -d /usr/share/cca-dfxmlreader ]; then
  sudo mkdir /usr/share/cca-dfxmlreader
fi

# Move cca_read_dfxml.py to dfxml python dir
sudo mv dfxmlreader/cca_read_dfxml.py /usr/share/dfxml/python/

# Move files into /usr/share/cca-dfxmlreader
sudo mv main.py /usr/share/cca-diskimageprocessor
sudo mv launch /usr/share/cca-diskimageprocessor
sudo mv design.py /usr/share/cca-diskimageprocessor
sudo mv design.ui /usr/share/cca-diskimageprocessor
sudo mv LICENSE /usr/share/cca-diskimageprocessor
sudo mv README.md /usr/share/cca-diskimageprocessor

# Make "CCA Tools" folder on Desktop if doesn't already exist
if [ ! -d "/home/bcadmin/Desktop/CCA Tools" ]; then
  sudo mkdir "/home/bcadmin/Desktop/CCA Tools"
fi

# Create launch.desktop file
sudo touch '/home/bcadmin/Desktop/CCA Tools/DFXML Reader.desktop'
echo '[Desktop Entry]' | sudo tee --append '/home/bcadmin/Desktop/CCA Tools/DFXML Reader.desktop'
echo 'Type=Application' | sudo tee --append '/home/bcadmin/Desktop/CCA Tools/DFXML Reader.desktop'
echo 'Name=DFXML Reader' | sudo tee --append '/home/bcadmin/Desktop/CCA Tools/DFXML Reader.desktop'
echo 'Exec=/usr/share/cca-dfxmlreader/launch' | sudo tee --append '/home/bcadmin/Desktop/CCA Tools/DFXML Reader.desktop'
echo 'Icon=' | sudo tee --append '/home/bcadmin/Desktop/CCA Tools/DFXML Reader.desktop'

# Change permissions, ownership for CCA Tools
sudo chown -R bcadmin:bcadmin '/home/bcadmin/Desktop/CCA Tools'
sudo chown -R bcadmin:bcadmin '/usr/share/cca-dfxmlreader'
sudo find '/home/bcadmin/Desktop/CCA Tools' -type d -exec chmod 755 {} \;
sudo find '/home/bcadmin/Desktop/CCA Tools' -type f -exec chmod 644 {} \;

# Make files executable
sudo chmod u+x '/home/bcadmin/Desktop/CCA Tools/DFXML Reader.desktop'
sudo chmod u+x /usr/share/cca-dfxmlreader/launch
