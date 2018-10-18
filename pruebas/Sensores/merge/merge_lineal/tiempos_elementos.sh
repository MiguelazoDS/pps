#!/usr/bin/env bash

temp=0
procesos=15
muestras=5
elementos=2000
inicio=100
saltos=100

#Elementos
for i in $(eval echo {$inicio..$elementos..$saltos})
do
  #Muestras
  for j in $(eval echo {1..$muestras})
  do
    let "cont+=1"
    aux1=`echo $elementos/$saltos | bc -l`
    aux2=`echo $aux1*$muestras | bc`
    res=`echo 100/$aux2 | bc -l`
    output="$(python planificador_merge_lineal.py $procesos $i)"
    temp=`echo $temp + $output | bc | awk '{printf "%.10f", $0}'`
    perc=`echo $res*$cont | bc | awk '{printf "%.3f",$0}'`
    echo $perc% terminado
  done
  final=`echo $temp/$muestras | bc -l | awk '{printf "%.10f", $0}'`
  echo $final >> elementos
  temp=0
done
