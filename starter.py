# import os module
import os

# import shutil module
import shutil

# define a function to organize images
def organize_images(directory):
    # list all files in the directory
    files = os.listdir(directory)

    # loop through each file
    for file in files:
        # get the filename and extension
        filename, extension = os.path.splitext(file)

        # get the model name from the filename
        model_name = filename.split('-')[0].strip()

        # create a new directory for the model if it doesn't exist
        if not os.path.exists(model_name):
            os.makedirs(model_name)

        # move the file to the new directory
        shutil.move(os.path.join(directory, file), os.path.join(model_name, file))

# define a function to separate similar images
def separate_similar_images(directory):
    # list all files in the directory
    files = os.listdir(directory)

    # loop through each file
    for file in files:
        # get the filename and extension
        filename, extension = os.path.splitext(file)

        # get the model name from the filename
        model_name = filename.split('-')[0].strip()

        # create a new directory for the model if it doesn't exist
        if not os.path.exists(model_name):
            os.makedirs(model_name)

        # move the file to the new directory
        shutil.move(os.path.join(directory, file), os.path.join(model_name, file))

# call the organize_images function with the current directory as an argument
organize_images('./')

# call the separate_similar_images function with the current directory as an argument
separate_similar_images('./')
