#!/usr/bin/gnuplot

cant = `cat elementos | wc -l`
set title "Gráfico de"
set grid
set xlabel "Cantidad de ..."
set ylabel ""
#set xrange [0:cant]
set yrange [0:0.02]
set y2range [0:10]
set ytics nomirror
set y2tics
FACTOR=0.1
set term png
set output "graf.png"
set style line 1 \
    linecolor rgb '#0060ad' \
    linetype 1 linewidth 2 \
    pointtype 7 pointsize 1.5
set style line 2 \
    linecolor rgb '#dd181f' \
    linetype 1 linewidth 2 \
    pointtype 5 pointsize 1.5
plot "elementos" using 1 with linespoints linestyle 1 title "hola",\
     "promedios_elementos" using FACTOR*1 with linespoints linestyle 2 title "chau"
