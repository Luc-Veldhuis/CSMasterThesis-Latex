int main(int argc, char **argv) {

  FILE *fp;
  char buf[255];
  size_t ret;

  fp = fopen(argv[1], "rb");
  int len = 20;
  ret = fread(buf, sizeof *buf, len, fp);
  fclose(fp);

  uint16_t x = 0;
  int32_t y = 0;
  int32_t z = 0;
  uint32_t a = 0;

  memcpy(&x, buf + 1, 2);  // x 1 - 2
  memcpy(&y, buf + 4, 4);  // y 4 - 7
  memcpy(&z, buf + 10, 4); // 10 - 13
  memcpy(&a, buf + 14, 4); // 14 - 17
  if (x > 12300 && x < 12350 && z < -100000000 && z > -100000005 &&
      z != -100000003 && y >= 987654321 && y <= 987654325 && a == 123456789) {
    printf("hey, you hit it \n");
    abort();
  }
  return 7;
}
