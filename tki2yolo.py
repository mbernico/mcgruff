import glob
from PIL import Image
import os
from pathlib import Path

#IMAGE_PATH = '/Users/feu1/EnOM/data/camry/30JAN18_keep/train_images/'
IMAGE_PATH = str(Path.cwd().joinpath('data'))


class ImageLoader():
    def __init__(self, image_name):
        self._image_name = image_name
        self._image = Image.open(self._image_name + '.jpg')
        self._width, self._height = self._image.size
        self._image.close()

    @property
    def image_size(self):
        return [self._width, self._height]

    @property
    def box_file(self):
        return self._image_name + '.txt'


class BoxParser():
    def __init__(self, box_text):
        self._text = box_text

    @property
    def box_dict(self):
        text = self._text.split()
        d = {}
        d['object'] = text[1]
        d['x0'] = int(text[2])
        d['y0'] = int(text[3])
        d['x1'] = int(text[4])
        d['y1'] = int(text[5])
        return d

class Converter():
    def __init__(self, bounding_box, image_size):
        self._object = bounding_box['object']
        self._x0 = bounding_box['x0']
        self._y0 = bounding_box['y0']
        self._x1 = bounding_box['x1']
        self._y1 = bounding_box['y1']
        self._x_size = image_size[0]
        self._y_size = image_size[1]

    @property
    def category(self):
        object_map = {'gun': 0}
        return object_map[self._object]

    @property
    def width(self):
        return (self._x1 - self._x0) / self._x_size

    @property
    def height(self):
        return (self._y1 - self._y0) / self._y_size

    @property
    def box_center_x(self):
        return self._x0 / self._x_size + 0.5 * self.width

    @property
    def box_center_y(self):
        return self._y0 / self._y_size + 0.5 * self.height


def main():  # pragma: no cover
    file_names = glob.glob(IMAGE_PATH + '/*.txt')
    print(file_names)
    for file_name in file_names:
        image_name = os.path.splitext(file_name)[0]
        loader = ImageLoader(image_name)
        with open(loader.box_file) as infile:
            with open(image_name + '_yolo.txt', 'w') as outfile:
                for line in infile:
                    parser = BoxParser(line)
                    converter = Converter(parser.box_dict, loader.image_size)
                    outfile.write('{0} {1} {2} {3} {4}\n'.format(
                        converter.category, converter.box_center_x,
                        converter.box_center_y, converter.width,
                        converter.height))


if __name__ == '__main__':  # pragma: no cover
    main()
