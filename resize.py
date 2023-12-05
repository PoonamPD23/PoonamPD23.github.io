from PIL import Image

def resize_image(input_path, output_path, new_size=(1920, 1080)):
    """
    Resize the image at the specified input path and save it to the output path.
    """
    with Image.open(input_path) as img:
        # Resize the image
        img = img.resize(new_size, Image.ANTIALIAS)
        # Save the resized image
        img.save(output_path)

# Example usage
resize_image('/home/posiden/Documents/PhotoFolio-pro/assets/img/res2.jpg', '/home/posiden/Documents/PhotoFolio-pro/assets/img/res2-changed.jpg')
