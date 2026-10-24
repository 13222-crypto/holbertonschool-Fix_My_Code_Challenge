#!/usr/bin/env ruby

result = ARGV.map { |e| e.to_i }
result.sort!.each do |e|
  puts e
end
