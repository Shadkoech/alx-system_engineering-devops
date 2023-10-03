#!/usr/bin/env ruby
#Regex that match hbtn with 2 - 5 t's
puts ARGV[0].scan(/hb[t]{2,5}n/).join
