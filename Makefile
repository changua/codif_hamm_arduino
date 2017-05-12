# Makefile Arduino without IDE
# Written by: lmcapacho
#     2017-2

# default board: Arduino Uno
# if define BOARD=m2560
ifeq ($(BOARD),m2560)
  BOARD_TAG              = m2560
  MCU                    = atmega2560
  F_CPU                  = 16000000L
  AVRDUDE_ARD_PROGRAMMER = wiring
  VARIANT                = mega
endif

ARDUINO_PORT           = /dev/ttyUSB0
AVRDUDE_ARD_BAUDRATE   = 115200

# Include Arduino-mk
include /usr/share/arduino/Arduino.mk
