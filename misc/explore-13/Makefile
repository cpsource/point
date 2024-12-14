# Compiler
CC = g++

# Compiler and linker flags from pkg-config
CFLAGS = `pkg-config --cflags gtk+-3.0`
LDFLAGS = `pkg-config --libs gtk+-3.0`

# Target executable
TARGET = drawing_area

# Source files
SRC = drawing_area.cpp  # Replace with your actual source files

# Object files (derived from source files)
OBJ = $(SRC:.cpp=.o)

# Default target
all: $(TARGET)

# Rule to build the target
$(TARGET): $(OBJ)
	$(CC) $(OBJ) -o $(TARGET) $(LDFLAGS)

# Rule to build object files
%.o: %.cpp
	$(CC) $(CFLAGS) -c $< -o $@

# Clean rule to remove generated files
clean:
	rm -f $(OBJ) $(TARGET)

# Phony targets
.PHONY: all clean

