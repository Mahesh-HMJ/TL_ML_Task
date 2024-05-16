import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Path to the input text file containing captions
input_text_file = 'extractedCaptions.txt'

# Path to the output text file where preprocessed and padded captions will be saved
output_text_file = 'preprocessed_captions.txt'

# Parameters for preprocessing

max_length = 20  # Maximum length of sequences (for padding and truncating)

# Read the captions data from the text file
captions_data = []
with open(input_text_file, 'r', encoding='utf-8') as file:
    captions_data = file.readlines()

# Create a tokenizer and fit it on the captions data
tokenizer = Tokenizer()
tokenizer.fit_on_texts(captions_data)

# Convert the captions to sequences of token IDs
sequences = tokenizer.texts_to_sequences(captions_data)

# Pad or truncate sequences to the specified length
padded_sequences = pad_sequences(sequences, maxlen=max_length, padding='post')

# Write the preprocessed and padded captions to the output text file
with open(output_text_file, 'w', encoding='utf-8') as file:
    for sequence in padded_sequences:
        # Convert each sequence to a string and write it to the file
        sequence_str = ' '.join(map(str, sequence))
        file.write(sequence_str + '\n')

print(f"Preprocessed and padded captions have been saved to {output_text_file}.")

