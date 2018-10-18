#!/usr/bin/gnuplot

cant = `cat datos1 | wc -l`
set title "Gráfico de"
set xlabel "Cantidad de ..."
set ylabel ""
set xrange [0:cant]
set yrange [0:0.02]
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
plot "datos1" using 1 with linespoints linestyle 1 title "hola",\
     "datos2" using 1 with linespoints linestyle 2 title "chau"
