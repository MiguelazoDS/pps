#!/usr/bin/env bash

temp=0
procesos=15
muestras=5
elementos=1000
directorio="cargaCPUprocesos"

if [ -e $directorio ]
then
  rm -rf $directorio
fi
mkdir $directorio

#Procesos
for i in $(eval echo {1..$procesos})
do
  nombrearchivo=./$directorio/loadcpu$i
  #Corremos el script en segundo plano
  ./loadcpu.sh $nombrearchivo &
  #Muestras
  for j in $(eval echo {1..$muestras})
  do
    let "cont+=1"
    aux=`echo $procesos*$muestras | bc`
    res=`echo 100/$aux | bc -l`
    output="$(python planificador_merge_lineal.py $i $elementos)"
    temp=`echo $temp + $output | bc | awk '{printf "%.10f", $0}'`
    perc=`echo $res*$cont | bc | awk '{printf "%.3f",$0}'`
    echo $perc% terminado
  done
  #Matamos el procesos
  pkill -f loadcpu.sh
  final=`echo $temp/$muestras | bc -l | awk '{printf "%.10f", $0}'`
  echo $final >> procesos
  temp=0
done

for i in $directorio/*
do
  datamash mean 1 < $i >> promedios_procesos
done

rm -rf $directorio
