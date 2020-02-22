#!/bin/bash
PORT="/dev/ttyUSB0"

SYNC=FF #BYTE1
ADDR=01 #BYTE2
BYTE3=${1:-00}
BYTE4=${2:-00}
BYTE5=${3:-00}
BYTE6=${4:-00}
SUM=0  #BYTE7


# Count SUM
hex=''
for i in $* ; do hex+="0x$i "; done
a="0x$ADDR $hex"
SUM=$(eval printf %x $(( ( ${a// /+} 0x0 ) & 0xff )) )

echo "Pelco 'D': $SYNC $ADDR $BYTE3 $BYTE4 $BYTE5 $BYTE6 $SUM"

# Write to port
printf "\x$SYNC\x$ADDR\x$BYTE3\x$BYTE4\x$BYTE5\x$BYTE6\x$SUM" > "$PORT"
