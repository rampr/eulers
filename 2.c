/*
 * sum=4613732
 */

#include <stdio.h>

int main()
{
  int fourM = 4000000;
  int sum = fibonaciSum(fourM);
  printf ("\n sum=%d",sum);
}

int fibonaciSum(n)
{
  int first=1;
  int second=2;
  int i,temp;
  int sum = 0;

  for (first=1;second<n;)
  {
    temp = first;
    first = second;
    second += temp;
    if(first%2==0)
    {
      sum += first;
    }
  }

  return sum;
}
