#!/usr/bin/env bash

temp=0
procesos=15
muestras=5
elementos=2000
inicio=100
saltos=100
directorio="cargaCPUelementos"

if [ -e $directorio ]
then
  rm -rf $directorio
fi
mkdir $directorio

#Elementos
for i in $(eval echo {$inicio..$elementos..$saltos})
do
  nombrearchivo=./$directorio/loadcpu$i
  #Corremos el script en segundo plano
  ./loadcpu.sh $nombrearchivo &
  #Muestras
  for j in $(eval echo {1..$muestras})
  do
    let "cont+=1"
    aux1=`echo $elementos/$saltos | bc -l`
    aux2=`echo $aux1*$muestras | bc`
    res=`echo 100/$aux2 | bc -l`
    output="$(python planificador_merge_multiprocessing.py $procesos $i)"
    temp=`echo $temp + $output | bc | awk '{printf "%.10f", $0}'`
    perc=`echo $res*$cont | bc | awk '{printf "%.3f",$0}'`
    echo $perc% terminado
  done
  #Matamos el procesos
  pkill -f loadcpu.sh
  final=`echo $temp/$muestras | bc -l | awk '{printf "%.10f", $0}'`
  echo $final >> elementos
  temp=0
done

for i in $directorio/*
do
  datamash mean 1 < $i >> promedios_elementos
done

rm -rf $directorio
