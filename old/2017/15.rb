N = 40_000_000

a = 512
b = 191
c = 0

def gA(x)
  (x * 16807) % 2147483647
end

def gB(x)
  (x * 48271) % 2147483647
end

N.times do |i|
  #a = (a * 16807) % 2147483647
  #b = (b * 48271) % 2147483647
  a = gA(a)
  b = gB(b)

  if (a & 65535) == (b & 65535)
    c += 1
  end
end

puts c
