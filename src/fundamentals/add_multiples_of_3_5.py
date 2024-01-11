def sum_of_multiples(num):
  a = 0
  x = range(num)
  
  for i in x:
    if i % 3 == 0 or i % 5 == 0:
      a += i
  return a
#list comprehension
  # return sum([i for i in range(num) if i % 3 == 0 or i % 5 == 0])

def test_sum_of_multiples_solution():
    assert sum_of_multiples(10) == 23
    assert sum_of_multiples(20) == 78
    assert sum_of_multiples(0) == 0
    assert sum_of_multiples(1) == 0
    assert sum_of_multiples(200) == 9168
    assert sum_of_multiples(64) == 933
