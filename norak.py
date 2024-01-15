from PIL import Image
from image_converter import ListToImage, ImageToList

def main():
  # Open the image.
  dog_img = Image.open("dog.png")
  pixels = ImageToList(dog_img)

  # Apply the norak filter.
  filtered_pixels = norak(pixels)

  # Save an image
  filtered_image = ListToImage(filtered_pixels)
  filtered_image.save("dog_norak.png")
  return


def norak(pixels):
  # Convert to norak.
  new_pixels = []
  for row in range(len(pixels)):
    new_row = []
    for col in range(len(pixels[row])):
      r, g, b = pixels[row][col]
      avg = (r + g + b)/ 3
      if avg > 153:
        r = avg
        g = avg
        b = avg

      new_row.append((r, g, b))
    new_pixels.append(new_row)

  return new_pixels

main()
