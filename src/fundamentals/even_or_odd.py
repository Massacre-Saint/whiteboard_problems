def even_or_odd(number):
  return 'Odd' if number % 2 != 0 else 'Even'

def test_even_or_odd_solution():
    assert even_or_odd(2) == 'Even'
    assert even_or_odd(3) == 'Odd'
    assert even_or_odd(234) == 'Even'
    assert even_or_odd(23333) == 'Odd'
    assert even_or_odd(567) == "Odd"
    assert even_or_odd(2345499) == "Odd"
