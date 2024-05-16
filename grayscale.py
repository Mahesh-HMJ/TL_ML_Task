import cv2
import os

def grayscale_img(current_folder, destination_folder):
    for filename in os.listdir(current_folder):
        file_path = os.path.join(current_folder, filename)
        img =  cv2.imread(file_path) 
        grayscale_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        destination_folder_path = os.path.join(destination_folder,filename)
        cv2.imwrite(destination_folder_path, grayscale_img)
    print("Task finished successfully")

if __name__ == '__main__':

    current_folder = 'D:\ML_Project\image_captions\Resized_Images'
    destination_folder = 'D:\ML_Project\image_captions\Grayscale_Images'

    grayscale_img(current_folder, destination_folder)