#!/usr/bin/env bash

temp=0

#Procesos
for i in {1..15}
do
  #Muestras
  for j in {1..30}
  do
    output="$(python planificador_merge_lineal.py $i)"
    temp=`echo $temp + $output | bc | awk '{printf "%.10f", $0}'`
    echo Terminado $i de 15
  done
  final=`echo $temp / 30 | bc -l | awk '{printf "%.10f", $0}'`
  echo $final >> procesos
  temp=0
done

#Elementos
for i in {10000..200000..10000}
do
  #Muestras
  for j in {1..30}
  do
    output="$(python planificador_merge_lineal.py 1 $i)"
    temp=`echo $temp + $output | bc | awk '{printf "%.10f", $0}'`
    echo Terminado $i de 200000
  done
  final=`echo $temp / 30 | bc -l | awk '{printf "%.10f", $0}'`
  echo $final >> elementos
  temp=0
done
