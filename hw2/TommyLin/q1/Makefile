CC = g++
CFLAGS = -Wall -Wextra
TARGET = line
OUTPUT = result.txt

.PHONY: run check clean
default: $(TARGET)

$(TARGET): $(TARGET).cpp
	$(CC) $(CFLAGS) $? -o $@

run: $(TARGET)
	./$(TARGET)

check: $(TARGET)
	./$(TARGET) > $(OUTPUT)

clean:
	rm -f $(TARGET) $(OUTPUT)
