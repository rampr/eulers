def sum_of_squares(begin,end):
  '''
  >>> sum_of_squares(1,10)
  385
  '''
  return sum(map(lambda x:x*x,[a for a in xrange(begin,end+1)]))


def squares_of_sum(begin,end):
  '''
  >>> squares_of_sum(1,10)
  3025
  '''
  return sum([a for a in xrange(begin,end+1)])**2

if __name__ == "__main__":
  import doctest
  doctest.testmod()
  print squares_of_sum(1,100)-sum_of_squares(1,100)
