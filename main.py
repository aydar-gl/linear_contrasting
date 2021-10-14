from PIL import Image


def do_linear_contrast(img, y_min=0, y_max=255):
    width, height = img.size
    pix = img.load()
    x_min, x_max = 255, 0
    for j in range(height):
        for i in range(width):
            pix_bright = sum(pix[i, j]) / 3
            if pix_bright < x_min:
                x_min = pix_bright
            if pix_bright > x_max:
                x_max = pix_bright
    for j in range(height):
        for i in range(width):
            pix_bright = sum(pix[i, j]) / 3
            y_new = (pix_bright - x_min) / (x_max - x_min) * (y_max - y_min) + y_min
            diff = (pix_bright - y_new) / 3
            img.putpixel(
                (i, j),
                (int(pix[i, j][0] - diff + 0.5), int(pix[i, j][1] - diff + 0.5), int(pix[i, j][2] - diff + 0.5))
            )
    return img

if __name__ == '__main__':
    img = Image.open('test.jpg')
    new_img = do_linear_contrast(img)
    new_img.save('new_img.png', 'png')
