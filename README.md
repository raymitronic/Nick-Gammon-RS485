# Nick-Gammon-RS485 - Created by Sthing

Python implementation of Nick Gammon's RS485 library for the Arduino.

Adaptation of the library for debug purposes and to make it work with actual communications.

Current status = tested actual communication with an Arduino (custom shield using MAX485) sending a RNET message every 10 seconds.

Setup:
- Raspberry pi B+ (current OS is Retropie)
- USB-RS485 usb adapter
- Arduino uno + Raymitronic DMN2 shield (custom shield with BoB, MAX485, sensors,...)
- Raymitronic RNET BreakOutBoard for RS485 (RJ45 connection board)
