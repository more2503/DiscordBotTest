#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <time.h>
#include <unistd.h>
#include <string.h>
#define FILE_name "assembler.mps"
#define MAX_LINE_LEN 255

int reg[32];

int *getReg(char *inreg) {
    if (!strcmp(inreg, "t0"))
        return &reg[8];
    else if (!strcmp(inreg, "t1"))
        return &reg[9];
    else if (!strcmp(inreg, "t2"))
        return &reg[10];    
    else if (!strcmp(inreg, "t3"))
        return &reg[11];
    else if (!strcmp(inreg, "t4"))
        return &reg[12];
    else if (!strcmp(inreg, "t5"))
        return &reg[13];
    else if (!strcmp(inreg, "t6"))
        return &reg[14];
    else if (!strcmp(inreg, "t7"))
        return &reg[15];
    else if (!strcmp(inreg, "t8"))
        return &reg[24];
    else if (!strcmp(inreg, "t9"))
        return &reg[25];
    return NULL;
}

int execute(char *line) {
    // Code Parser
    
    char *arg = strtok(line, " ");
    int *reg1;
    int *reg2;
    int imm;

    if (!strcmp(arg, "li")) {
        arg = strtok(NULL, " ");
        int *reg1 = getReg(arg);
        if (reg1 == NULL)
            return 0; // unknown register
        arg = strtok(NULL, " "),
        imm = atoi(arg);
        *reg1 += imm;
        return 1;
    } else if (!strcmp(arg, "add")) {
        arg = strtok(NULL, " ");
    }
    return 0;
}

int main() {
    char *read_line = malloc(MAX_LINE_LEN * sizeof(char));
    FILE *file = fopen(FILE_name, "r");
    // int reg[32] = {0x0};  // initialize register;

    while (fgets(read_line, MAX_LINE_LEN, file) != NULL ) {
        if (!execute(read_line))
            printf("ERROR;");
    }

    return 0;
}