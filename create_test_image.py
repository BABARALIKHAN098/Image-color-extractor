from PIL import Image, ImageDraw

def create_test_image():
    img = Image.new('RGB', (300, 300), color='white')
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 100, 300], fill='red')
    d.rectangle([100, 0, 200, 300], fill='green')
    d.rectangle([200, 0, 300, 300], fill='blue')
    img.save('test_image.png')
    print("Test image created.")

if __name__ == "__main__":
    create_test_image()
