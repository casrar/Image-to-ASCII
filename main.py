from PIL import Image, UnidentifiedImageError
from pathlib import Path
import shutil


def main():
    def get_file():
        input_path = Path('Input')
        for p in input_path.iterdir():
            return p

    def create_output_file(filename):
        filename = str(filename.stem) + '.txt'
        output_path = Path('Output') / filename
        return output_path

    def get_output_file_path():
        output_path = Path('Output')
        return output_path

    def map_to_ascii(color):
        if color >= 240:
            return "*"
        elif 225 <= color < 240:
            return "^"
        elif 210 <= color < 225:
            return "o"
        elif 180 <= color < 195:
            return "i"
        elif 165 <= color < 180:
            return "}"
        elif 150 <= color < 165:
            return "{"
        elif 135 <= color < 150:
            return "+"
        elif 120 <= color < 135:
            return "="
        elif 105 <= color < 120:
            return "G"
        elif 90 <= color < 105:
            return "E"
        elif 75 <= color < 90:
            return "M"
        elif 60 <= color < 75:
            return "W"
        elif 45 <= color < 60:
            return "$"
        elif 30 <= color < 45:
            return "&"
        elif 15 <= color < 30:
            return "@"
        else:
            return "#"

    def dimensions(img):
        img_width = int(img.size[0])
        img_length = int(img.size[1] * 0.4)  # 0.4 is to scale image

        scale_factor = (max((img_width, img_length)) / 250)

        img_width = int(img_width / scale_factor)
        img_length = int(img_length / scale_factor)

        return img_width, img_length

    def resize_img(img):
        img_dimensions = dimensions(img)

        img_resized = img.resize((img_dimensions[0], img_dimensions[1]))
        img_resized = img_resized.convert("L")

        return img_resized

    try:
        with open(create_output_file(get_file()), 'w') as f:
            with Image.open(get_file()) as img:
                img_dimensions = dimensions(img)
                new_img = resize_img(img)
                px = new_img.load()
                x=0
                y=0

                while y < img_dimensions[1]:
                    while x < img_dimensions[0]:
                        f.write(map_to_ascii(px[x,y]))
                        x = x + 1
                    y = y + 1
                    x = 0
                    f.write("\n")

                shutil.move(str(get_file()), str(get_output_file_path()))
                print("Finished!")
    except AttributeError as e:
        print("There is no image in the Input Directory!")
    except FileNotFoundError as e:
        print("You are missing the Input or Output Directory !")
    except UnidentifiedImageError as e:
        print("This program requires image files!")


if __name__ == '__main__':
    main()





