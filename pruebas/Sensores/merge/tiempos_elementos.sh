#!/usr/bin/env bash

temp=0

#Elementos
for i in {10000..200000..10000}
do
  #Muestras
  for j in {1..30}
  do
    let "cont+=1"
    res=`echo 100/600 | bc -l`
    output="$(python planificador_merge_lineal.py 1 $i)"
    temp=`echo $temp + $output | bc | awk '{printf "%.10f", $0}'`
    perc=`echo $res*$cont | bc | awk '{printf "%.3f",$0}'`
    echo $perc% terminado
  done
  final=`echo $temp / 30 | bc -l | awk '{printf "%.10f", $0}'`
  echo $final >> elementos
  temp=0
done
