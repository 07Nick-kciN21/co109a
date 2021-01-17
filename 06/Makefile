CC := gcc -std=c99
CPPC := g++ -std=c++11
TARGET = asm vm dasm asm1

all: $(TARGET)

asm1: asm1.cpp
	$(CPPC) $^ -o $@

asm: asm.cpp
	$(CPPC) $^ -o $@

vm: vm.c
	$(CC) $^ -o $@

dasm: dasm.c
	$(CC) $^ -o $@

clean:
	rm -f *.o *.exe $(TARGET)
