#!/usr/bin/env ruby
#A Ruby script that output: [SENDER],[RECEIVER],[FLAGS]
puts ARGV[0].scan(/(?<=from:|to:|flags:)(.+?)(?=\])/).join(",")
