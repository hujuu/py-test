
first = gets.chop
second = gets.chop

#print first

if first[-1] == second[0] then
  if second[-1] == "n" then
    print "NG"
  else
    print "OK"
  end
else
  print "NG"
end
