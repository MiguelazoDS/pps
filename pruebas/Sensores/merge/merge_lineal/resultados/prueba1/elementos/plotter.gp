#!/usr/bin/gnuplot

cant = `cat elementos | wc -l`
set title "Gráfico de"
set grid
set xlabel "Cantidad de ..."
set ylabel "a"
set y2label "b"
set xrange [0:cant]
set y2range [80:100]
set ytics nomirror
set y2tics
set tics out
set autoscale y
#set autoscale y2
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
plot "elementos" using 1 with linespoints linestyle 1 title "hola" axes x1y1,\
     "promedios_elementos" using 1 with linespoints linestyle 2 title "chau" axes x1y2
