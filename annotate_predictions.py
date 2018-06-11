from util.video_tools import images_to_video
from pathlib import Path
import cv2


class Suspect:
    def __init__(self, name: str, age: int, gender: str, height: str, weight: int):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight


def glob_yolo_predictions():
    predictions_glob = Path.cwd().joinpath("predictions").glob("*.jpg")
    return [str(x) for x in predictions_glob]


def add_box_to_image(img, box_width=350, box_height=350):
    top_x = img.shape[1] - box_width
    top_y = 0
    bottom_x = top_x + box_width
    bottom_y = top_y + box_height

    top_corner = (top_x, top_y)
    bottom_corner = (bottom_x, bottom_y)
    img = cv2.rectangle(img, top_corner, bottom_corner, (255, 255, 255), -1)  # white box (remember BGR, not RBG)
    img = cv2.rectangle(img, top_corner, bottom_corner, (0, 0, 255), 2)  # red outline
    return img


def add_text_to_img(img, suspect, box_width=350, font=cv2.FONT_ITALIC, font_scale=1, thickness=2, pad=20, space=50):
    top_x = img.shape[1] - box_width - 2
    top_y = 2
    text_color_red = (0, 0, 255)
    text_color_black = (0, 0, 0)
    img = cv2.putText(img, '-Suspect Info-', (top_x + pad, top_y + 50), font, font_scale, text_color_red, thickness,
                      cv2.LINE_AA)
    img = cv2.putText(img, 'Identity: ' + suspect.name, (top_x + pad, top_y + 50 + space), font, font_scale, text_color_black,
                      thickness, cv2.LINE_AA)
    img = cv2.putText(img, 'Age: ' + suspect.age, (top_x + pad, top_y + 50 + space * 2), font, font_scale, text_color_black,
                      thickness, cv2.LINE_AA)
    img = cv2.putText(img, 'Gender: ' + suspect.gender, (top_x + pad, top_y + 50 + space * 3), font, font_scale, text_color_black,
                      thickness, cv2.LINE_AA)
    img = cv2.putText(img, 'Height: ' + suspect.height, (top_x + pad, top_y + 50 + space * 4), font, font_scale, text_color_black,
                      thickness, cv2.LINE_AA)
    img = cv2.putText(img, 'Weight: ' + suspect.weight, (top_x + pad, top_y + 50 + space * 5), font, font_scale, text_color_black,
                      thickness, cv2.LINE_AA)
    return img


def annotate_prediction(img):
    suspect = predict_suspect(img)
    img = add_box_to_image(img)
    img = add_text_to_img(img, suspect)
    return img


def open_image(prediction):
    return cv2.imread(prediction)


def save_image(annotated_prediction, fname):
    cv2.imwrite(fname, annotated_prediction)


def predict_suspect(img):
    """
    life selfie goes here
    :param img:
    :return:
    """
    suspect = Suspect("Unknown", "30", "Female", "5\" to 5\"5\'", "120lbs")
    return suspect


def main():  # pragma: no cover
    out_path = str(Path.cwd().joinpath("annotated_predictions"))
    predictions = glob_yolo_predictions()

    for prediction in predictions:
        fname = out_path + "/" + prediction.split("/")[-1]
        img = open_image(prediction)
        annotated_prediction = annotate_prediction(img)
        save_image(annotated_prediction, fname)


if __name__ == "__main__":
    main()
