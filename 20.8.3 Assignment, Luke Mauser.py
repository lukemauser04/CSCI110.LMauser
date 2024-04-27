import os

import sys

def word_frequency(file_name):
    frequency_count = {}
    
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.lower().split() 
            
            for word in words:
                cleaned_word = ''
                
                for char in word:
                    if char.isalpha():
                        cleaned_word += char
                
                if cleaned_word: 
                    frequency_count[cleaned_word] = frequency_count.get(cleaned_word, 0) + 1

    
    sorted_items = sorted(frequency_count.items())

    return sorted_items

def write_frequencies(frequencies, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("Word              Count\n")
        file.write("=======================\n")
        for word, count in frequencies:
            file.write(f"{word:<16}{count:>4}\n")

input_file = input("Please enter the name of the input file: ")
output_file = input("Please enter the name of the output file: ")

frequencies = word_frequency(input_file)
write_frequencies(frequencies, output_file)
