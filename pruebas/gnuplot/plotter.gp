#!/usr/bin/gnuplot

cant = `cat datos | wc -l`
set xrange [0:cant]
set yrange [0:12]
set term png
set output "graf.png"
plot "datos" using 1 with lines
