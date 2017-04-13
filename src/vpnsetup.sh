#!/bin/bash

gnome-terminal -e "bash -c \" cat ~/garb.garb | sudo openconnect vpn.usyd.edu.au --user hwar3828 --passwd-on-stdin; exec bash\""

