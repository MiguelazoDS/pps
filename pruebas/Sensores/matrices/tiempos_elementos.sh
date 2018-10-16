#!/usr/bin/env bash

temp=0

#Elementos
for i in {100..2000..100}
do
  #Muestras
  for j in {1..5}
  do
    let "cont+=1"
    res=`echo 100/100 | bc -l`
    output="$(python planificador_matrices.py 15 $i)"
    temp=`echo $temp + $output | bc | awk '{printf "%.10f", $0}'`
    perc=`echo $res*$cont | bc | awk '{printf "%.3f",$0}'`
    echo $perc% terminado
  done
  final=`echo $temp / 5 | bc -l | awk '{printf "%.10f", $0}'`
  echo $final >> elementos
  temp=0
done
