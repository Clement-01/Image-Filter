from PIL import Image
from image_converter import ListToImage, ImageToList

def main():
  # Open the image.
  dog_img = Image.open("dog.png")
  pixels = ImageToList(dog_img)

  # Apply the border filter.
  filtered_pixels = add_border(pixels)

  # Save an image
  filtered_image = ListToImage(filtered_pixels)
  filtered_image.save("dog_border.png")
  return


def add_border(pixels):
  # Convert to have a black border.
  new_pixels = []
  for row in range(len(pixels)):
    new_row = []
    for col in range(len(pixels[row])):
      r, g, b = pixels[row][col]
      if row <= 10 or row >= (len(pixels) - 10) or col <= 10 or col >= (len(pixels[row]) - 10):
        r, g, b = [0, 0, 0]
      new_row.append((r,g,b))
    new_pixels.append(new_row)
  return new_pixels


main()
