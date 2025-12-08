CXX = g++

.PHONY: all clean

all: solution.elf

solution.elf : solution.cpp
	$(CXX) $^ -o $@

clean:
	rm -rf *.elf
