# import os
# import numpy as np
# from albumentations import (Compose, HorizontalFlip, RandomRotate90, RandomCrop, RandomBrightnessContrast)
# from PIL import Image
# from albumentations.pytorch import ToTensorV2

# # Define input and output folders
# input_folder = 'path_to_input_folder'
# output_folder = 'path_to_output_folder'

# # Ensure the output folder exists
# os.makedirs(output_folder, exist_ok=True)

# # Define the data augmentation pipeline
# augmentation_pipeline = Compose([
#     HorizontalFlip(p=0.5),
#     RandomRotate90(p=0.5),
#     RandomCrop(width=224, height=224),
#     RandomBrightnessContrast(p=0.2),
#     ToTensorV2()
# ])

# # Process images in the input folder
# for image_name in os.listdir(input_folder):
#     # Check if the file is an image
#     if image_name.endswith(('.jpg', '.png', '.jpeg')):
#         # Load the image using PIL
#         image_path = os.path.join(input_folder, image_name)
#         image = Image.open(image_path)

#         # Convert the image to a NumPy array
#         image_array = np.array(image)

#         # Apply the augmentation pipeline to the image
#         augmented_image = augmentation_pipeline(image=image_array)['image']

#         # Convert the augmented image back to a PIL image
#         augmented_image_pil = Image.fromarray(np.uint8(augmented_image * 255))

#         # Define the path for the augmented image in the output folder
#         augmented_image_path = os.path.join(output_folder, 'aug_' + image_name)

#         # Save the augmented image
#         augmented_image_pil.save(augmented_image_path)

#         print(f"Saved augmented image to {augmented_image_path}")

# print("Data augmentation completed.")

import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

# Sample data
texts = [
    "this is a sample text",
    "another example for padding",
    "sequence data preprocessing"
]

# Tokenization
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

# Padding
max_len = max(len(seq) for seq in sequences)
padded_sequences = pad_sequences(sequences, maxlen=max_len, padding='post')

# Example of decoding padded sequences from a numpy array
def decode_padded_sequences(padded_sequences, tokenizer):
    decoded_sequences = []
    for padded_seq in padded_sequences:
        # Remove padding (0s)
        decoded_seq = [token for token in padded_seq if token != 0]
        # Convert token IDs back to words
        decoded_text = tokenizer.sequences_to_texts([decoded_seq])[0]
        decoded_sequences.append(decoded_text)
    return decoded_sequences

# Decode padded sequences
decoded_texts = decode_padded_sequences(padded_sequences, tokenizer)

print("Original texts:")
print(texts)
print("\nDecoded sequences:")
print(decoded_texts)

