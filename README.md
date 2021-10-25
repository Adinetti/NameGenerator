# NameGenerator

A simple full name generator in python.  

[![Tests Action Status](https://github.com/Adinetti/NameGenerator/workflows/tests/badge.svg)](https://github.com/Adinetti/NameGenerator/actions)

# Documentation

## int get_size()

- Return current count of unique full name in the generator.  

## str generate_name()

- Return random unique full name. Return names never repeat. If get_size return 0, generate_name() raise StopIteration exeption.