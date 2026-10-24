#!/usr/bin/env ruby

args = ARGV.map do |e|
  # التحويل إلى رقم صحيح إذا كان المدخل رقماً، أو إبقاؤه كما هو إذا كان نصاً
  if e =~ /\A[-+]?\d+\z/
    e.to_i
  else
    e
  end
end

# فرز العناصر (مع معالجة الأخطاء إذا اختلطت النصوص والأرقام فيRuby)
args.sort_by! { |e| [e.class.to_s, e] }

args.each do |e|
  puts e
end
