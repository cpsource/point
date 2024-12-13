# Compiler
CC = gcc

# Compiler and linker flags from pkg-config
PKG_CONFIG = pkg-config
CFLAGS = $(shell $(PKG_CONFIG) --cflags gtk+-3.0)
LDFLAGS = $(shell $(PKG_CONFIG) --libs gtk+-3.0)

# Target executable
TARGET = my_program

# Source files
SRC = main.c  # Replace with your actual source files

# Object files (derived from source files)
OBJ = $(SRC:.c=.o)

# Default target
all: $(TARGET)

# Rule to build the target
$(TARGET): $(OBJ)
	$(CC) $(OBJ) -o $(TARGET) $(LDFLAGS)

# Rule to build object files
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Clean rule to remove generated files
clean:
	rm -f $(OBJ) $(TARGET)

# Phony targets
.PHONY: all clean

