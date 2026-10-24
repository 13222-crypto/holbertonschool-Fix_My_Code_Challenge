#!/usr/bin/env ruby

result = ARGV.select { |e| e =~ /\A[-+]?\d+\z/ }.map(&:to_i)
result.sort.each do |e|
  puts e
end
