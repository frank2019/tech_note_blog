#include  <stdio.h>
#include  <stdint.h>
#include  "test.h"
#include   "test_version.h"

int MyTests() {
    printf("Hello World");
    return  0;
}

int GetVerson(uint32_t *version) {
    if (!version) {
        return -1;
    }
    return  TEST_VERSION_MAJOR << 24 | TEST_VERSION_MINOR << 16 | (TEST_VERSION_PATCHLEVEL << 8) | TEST_VERSION_RELEASER;
}