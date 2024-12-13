#!/bin/bash
g++ -o drawing_area drawing_area.cpp `pkg-config --cflags --libs gtk+-3.0`
