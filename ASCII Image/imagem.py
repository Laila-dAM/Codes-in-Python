from PIL import Image
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width = 100):
    width, heigth = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized image = image.resize((new_width, new_height))
    return resized_imagem

def grayify(image):
    return image.convert("L")

def pixel_to_ascii(pixel_value):
    return ASCII_CHARS[pixel_value // 25]

def image_to_ascii(image_path, new_width = 100):
    try:
        image = image.open(image_path)
    except Exception as e:
        print(e)
        return

image = resize_image(image, new_width)
image = grayify(image)
pixels = list(image.getdata())
ascii str = ".join([pixel_to_ascii(pixel) for pixel in pixels])
ascii_str_len = len(ascii_str)
    ascii_str = '\n'.join([ascii_str[i:i + new_width] for i in range(0, ascii_str_len, new_width)])
return ascii_str

def save_to_file(ascii_str, output_file):
    with open(output_file, "W") as f:
        f.write(ascii_str)

def main(image_path, output_file = "output.txt", new_width = 100):
    ascii_art = image_to_ascii(image_path, new_width)
    if ascii_art:
        print(ascii_art)
        save_to_file(ascii_art, output_file)
        
"