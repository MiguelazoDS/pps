#!/bin/bash
# by Paul Colby (http://colby.id.au), no rights reserved ;)

PREV_TOTAL=0
PREV_IDLE=0


while true; do
  # Get the total CPU statistics, discarding the 'cpu ' prefix.
  CPU=(`sed -n 's/^cpu\s//p' /proc/stat`)
  IDLE=${CPU[3]} # Just the idle CPU time.

  # Calculate the total CPU time.
  TOTAL=0
  for VALUE in "${CPU[@]}"; do
    let "TOTAL=$TOTAL+$VALUE"
  done

  # Calculate the CPU usage since we last checked.
  let "DIFF_IDLE=$IDLE-$PREV_IDLE"
  let "DIFF_TOTAL=$TOTAL-$PREV_TOTAL"
  let "DIFF_USAGE=(1000*($DIFF_TOTAL-$DIFF_IDLE)/$DIFF_TOTAL+5)/10"
#  echo -en "\rCPU: $DIFF_USAGE%  \b\b" >>  $1  # $1 primer argumento por comando
  echo "$DIFF_USAGE" >>  $1  # $1 primer argumento por comando

  # Remember the total and idle CPU times for the next check.
  PREV_TOTAL="$TOTAL"
  PREV_IDLE="$IDLE"
  
  # Wait before checking again.
  sleep 1
done
