""Author William Jeffery Knight
@ W-J-Knight.git
"""
"""Run this script after labeling the color image for yolov5 using text files. 
Will make gray copy of the image generated label for yolov5 by making a copy of 
the label text file that will match the gray image. Doubling the image data for 
training.
"""
# import some magic
import cv2  # need opencv to handle the image data
import shutil  # need shutil make a copy of the text file
import glob  # need glob make list of files in the directory



# make a list of all image files in the directory
jpg_list = list(glob.glob("*.jpg"))


def gray(image, current_file_name, added_file_name="_gray"):
    """Make a gray image and label text file
    Args:"
        image(str):
            Current image in the list. Which a gray will be made.
        current_file_name(str):
            The current name of the image without extention
        added_file_name(str):
            Use to make name for the gary image and it's label text file.
    """
    # Take the color image turn it gray and set to variable
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Make a name for the gary image
    gray_jpg = f"{current_file_name}{added_file_name}.jpg"
    
    # Save the gray copy of image
    cv2.imwrite(gray_jpg, gray_image)
    
    # Make a name for the gray copy for label text file
    gray_txt= f"{current_file_name}{added_file_name}.txt"
    
    # The name of the label text file for color image
    file_txt = f"{current_file_name}.txt"
    
    # Making label text file for the gray image. 
    # By copying the data for color image text to gray image file.
    shutil.copyfile(file_txt, gray_txt)
    print(f"Gray copy being for {current_file_name}.jpg with label")


def main():
    # loop through all images
    for im in jpg_list:
        #read one image to memory at a time
        image = cv2.imread(im)
        # get file name without file extension
        file_name, file_ext = im.split(".")
        gray(image, file_name)


if __name__ == "__main__":
    main()


# Window shown waits for any key pressing event
cv2.destroyAllWindows()
