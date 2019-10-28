#include <stdio.h>

int main(void) {
  unsigned long a = 512;
  unsigned long b = 191;
  unsigned int c = 0;

  for(int i = 0; i < 40000000; ++i) {
    a = (a * 16807) % 2147483647;
    b = (b * 48271) % 2147483647;

    if ((a & 65535) == (b & 65535)) {
      c += 1;
    }
  }

  printf("%d\n", c);

  return 0;
}
