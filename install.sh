#!/bin/bash

### Install script for CCA DFXML Reader in Bitcurator

# Make /usr/share/ccatools if doesn't already exist
if [ ! -d /usr/share/ccatools ]; then
  sudo mkdir /usr/share/ccatools
fi

# Make /usr/share/ccatools/dfxmlreader if doesn't already exist
if [ ! -d /usr/share/ccatools/dfxmlreader ]; then
  sudo mkdir /usr/share/ccatools/dfxmlreader
fi

# Move files into /usr/share/ccatools/dfxmlreader
sudo mv main.py /usr/share/ccatools/dfxmlreader
sudo mv cca_read_dfxml.py /usr/share/ccatools/dfxmlreader
sudo mv launch /usr/share/ccatools/dfxmlreader
sudo mv design.py /usr/share/ccatools/dfxmlreader
sudo mv design.ui /usr/share/ccatools/dfxmlreader
sudo mv icon.png /usr/share/ccatools/dfxmlreader
sudo mv LICENSE /usr/share/ccatools/dfxmlreader
sudo mv README.md /usr/share/ccatools/dfxmlreader

# Make "CCA Tools" folder on Desktop if doesn't already exist
if [ ! -d "/home/bcadmin/Desktop/CCA Tools" ]; then
  sudo mkdir "/home/bcadmin/Desktop/CCA Tools"
fi

# Create launch.desktop file
sudo touch '/home/bcadmin/Desktop/CCA Tools/DFXML Reader.desktop'
echo '[Desktop Entry]' | sudo tee --append '/home/bcadmin/Desktop/CCA Tools/DFXML Reader.desktop'
echo 'Type=Application' | sudo tee --append '/home/bcadmin/Desktop/CCA Tools/DFXML Reader.desktop'
echo 'Name=DFXML Reader' | sudo tee --append '/home/bcadmin/Desktop/CCA Tools/DFXML Reader.desktop'
echo 'Exec=/usr/share/ccatools/dfxmlreader/launch' | sudo tee --append '/home/bcadmin/Desktop/CCA Tools/DFXML Reader.desktop'
echo 'Icon=/usr/share/ccatools/dfxmlreader/icon.png' | sudo tee --append '/home/bcadmin/Desktop/CCA Tools/DFXML Reader.desktop'

# Change permissions, ownership for CCA Tools
sudo chown -R bcadmin:bcadmin '/home/bcadmin/Desktop/CCA Tools'
sudo chown -R bcadmin:bcadmin '/usr/share/ccatools/dfxmlreader'
sudo find '/home/bcadmin/Desktop/CCA Tools' -type d -exec chmod 755 {} \;
sudo find '/home/bcadmin/Desktop/CCA Tools' -type f -exec chmod 644 {} \;

# Make files executable
sudo chmod u+x '/home/bcadmin/Desktop/CCA Tools/DFXML Reader.desktop'
sudo chmod u+x /usr/share/ccatools/dfxmlreader/launch
