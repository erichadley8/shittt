#!/bin/bash
while true; do
             ./start-tor-browser.desktop
             python3 code1.py
	     sleep 50
             kill $(pgrep firefox.real)
         done
