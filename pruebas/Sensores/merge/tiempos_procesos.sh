#!/usr/bin/env bash

temp=0

#Procesos
for i in {1..15}
do
  #Muestras
  for j in {1..30}
  do
    let "cont+=1"
    res=`echo 100/450 | bc -l`
    output="$(python planificador_merge_lineal.py $i)"
    temp=`echo $temp + $output | bc | awk '{printf "%.10f", $0}'`
    perc=`echo $res*$cont | bc | awk '{printf "%.3f",$0}'`
    echo $perc% terminado
  done
  final=`echo $temp / 30 | bc -l | awk '{printf "%.10f", $0}'`
  echo $final >> procesos
  temp=0
done
