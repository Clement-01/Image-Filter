from PIL import Image
from image_converter import ListToImage, ImageToList

def main():
  # Open the image.
  dog_img = Image.open("dog.png")
  pixels = ImageToList(dog_img)

  # Apply the grayscale filter.
  filtered_pixels = grayscale(pixels)

  # Save an image
  filtered_image = ListToImage(filtered_pixels)
  filtered_image.save("dog_grayscale.png")
  return


def grayscale(pixels):
  # The variable new_pixels will contains the grayscale image.
  new_pixels = []
  
  for row in range(len(pixels)):
      new_row = []
      for col in range(len(pixels[row])):
          # The body of this loop merely makes a copy of pixels.
          # You will need to compute the grayscale equivalent.
          r, g, b = pixels[row][col]
          avg = (r + g + b)/ 3
          r = avg
          g = avg
          b = avg
          new_row.append((r, g, b))
      new_pixels.append(new_row)
      
  return new_pixels

main()
