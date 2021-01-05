#Importing packages
import PIL.Image
import gdown 

#Setting list of possible ascii characters
ASCII_CHARS = ["@", "#", "5", "%", "?", "*", "+", ";", ":", ",", "."]

#Resizing image
#Changing width changes number of ascii characters per row
def size(image, new_width = 1000):
  width, height = image.size
  ratio = height / width
  new_height = int(new_width * ratio)
  resized_image = image.resize((new_width, new_height))
  return resized_image

#Converts each pixel from RGB to greyscale in order to measure the intensity
def gray(image):
  grayscale_image = image.convert("L")
  return grayscale_image

#Converts each pixel to ascii depending on the intensity
def convert_to_acsii(image):
  pixels = image.getdata()
  #finds character that is of a similar intensity to the pixel
  characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
  return characters

def main(new_width = 1000):
  # Save an image in google drive, get the sharable link, then convert it to a direct download link through this website: https://sites.google.com/site/gdocs2direct/home
  gdown.download('https://drive.google.com/uc?export=download&id=1hZpXdelNN_iUMnSiv_SgF_qPmTBmP8jg','wave.jpg',True);

  image = PIL.Image.open('wave.jpg')

  new_image_data = convert_to_acsii(gray(size(image)))

  pixel_count = len(new_image_data)
  ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

  print(ascii_image)
main()
