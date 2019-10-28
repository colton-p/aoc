#include <stdio.h>

int main() {

  int R[6] = {0};
  int cnt = 0;


  L1: R[4] = 123  ;
  L2: R[4] = R[4] & 456;
  L3: R[4] = R[4] == 72;
  L4: if (!R[4]) { goto L1; }

  L6: R[4] = 0  ;
  L7: R[3] = R[4] | 65536;
  L8: R[4] = 4332021  ;
  L9: R[2] = R[3] & 255;
  L10: R[4] = R[4] + R[2];
  L11: R[4] = R[4] & 16777215;
  L12: R[4] = R[4] * 65899;
  L13: R[4] = R[4] & 16777215;
  L14: R[2] = 256 > R[3];
  L15: if (!R[2]) { goto L18; }
  L17: goto L29;
  L18: R[2] = 0  ;
  L19: R[1] = R[2] + 1;
  L20: R[1] = R[1] * 256;
  L21: R[1] = R[1] > R[3];
  L22: if (!R[1]) { goto L25; }

  L24: goto L27;
  L25: R[2] = R[2] + 1;
  L26: goto L19;
  L27: R[3] = R[2]  ;
  L28: goto L9  ;
  L29: R[2] = R[4] == R[0];

  // printf("%d\n", R[4]);
  cnt += 1;
  if (cnt > 10000) { return 0; }


  L30: if (!R[2]) { goto L7; }

  return 1;
}
