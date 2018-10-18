#!/usr/bin/env bash

temp=0
procesos=15
muestras=5
elementos=1000

rm -rf cargaCPUprocesos
mkdir cargaCPUprocesos

#Procesos
for i in $(eval echo {1..$procesos})
do
  
  nombrearchivo=./cargaCPUprocesos/loadcpu$i

  ./loadcpu.sh $nombrearchivo & #corro en paralelo el script
  #Muestras
  for j in $(eval echo {1..$muestras})
  do
    let "cont+=1"
    aux=`echo $procesos*$muestras | bc`
    res=`echo 100/$aux | bc -l`
    output="$(python3 planificador_matrices.py $i $elementos)"
    temp=`echo $temp + $output | bc | awk '{printf "%.10f", $0}'`
    perc=`echo $res*$cont | bc | awk '{printf "%.3f",$0}'`
    echo $perc% terminado
  done
  pkill -f loadcpu.sh #matamos el proceso
  final=`echo $temp/$muestras | bc -l | awk '{printf "%.10f", $0}'`
  echo $final >> procesos
  temp=0
done


