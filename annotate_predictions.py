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
    predictions = [str(x) for x in predictions_glob]

    return sorted(predictions, key=lambda x: int("".join([str(s) for s in x if s.isdigit()])))


def add_box_to_image(img, box_width=450, box_height=650):
    top_x = img.shape[1] - box_width - 5
    top_y = 2
    bottom_x = top_x + box_width
    bottom_y = top_y + box_height

    top_corner = (top_x, top_y)
    bottom_corner = (bottom_x, bottom_y)
    img = cv2.rectangle(img, top_corner, bottom_corner, (255, 255, 255), -1)  # white box (remember BGR, not RBG)
    img = cv2.rectangle(img, top_corner, bottom_corner, (0, 0, 255), 2)  # red outline
    return img


def alert_first_responders(img,  suspect, box_width=450, font=cv2.FONT_ITALIC, font_scale=1, thickness=2, pad=20, space=50,
                           indent=5):
    top_x = img.shape[1] - box_width - 5
    top_y = 5
    text_color_red = (0, 0, 255)
    text_color_black = (0, 0, 0)

    img = cv2.putText(img, 'Weapon Detected!', (top_x + pad, top_y + space), font, font_scale, text_color_red, thickness,
                      cv2.LINE_AA)
    img = cv2.putText(img, 'Alerting First Responders', (top_x + pad, top_y + space * 2), font, font_scale, text_color_red, thickness,
                      cv2.LINE_AA)

    img = cv2.putText(img, 'Active Shooter Spotted', (top_x + pad, top_y + space * 3), font, font_scale, text_color_red, thickness,
                      cv2.LINE_AA)
    img = cv2.putText(img, 'Identity: ' + suspect.name, (top_x + pad+indent, top_y + space * 4), font, font_scale,
                      text_color_black,
                      thickness, cv2.LINE_AA)
    img = cv2.putText(img, 'Age: ' + suspect.age, (top_x + pad+indent, top_y + space * 5), font, font_scale,
                      text_color_black,
                      thickness, cv2.LINE_AA)
    img = cv2.putText(img, 'Gender: ' + suspect.gender, (top_x + pad+indent, top_y + space * 6), font, font_scale,
                      text_color_black,
                      thickness, cv2.LINE_AA)
    img = cv2.putText(img, 'Height: ' + suspect.height, (top_x + pad+indent, top_y + space * 7), font, font_scale,
                      text_color_black,
                      thickness, cv2.LINE_AA)
    img = cv2.putText(img, 'Weight: ' + suspect.weight, (top_x + pad+indent, top_y + space * 8), font, font_scale,
                      text_color_black,
                      thickness, cv2.LINE_AA)
    return img


def lock_doors(img, box_width=450, font=cv2.FONT_ITALIC, font_scale=1, thickness=2, pad=20, space=50,
                indent=5):
    top_x = img.shape[1] - box_width - 5
    top_y = 5 + space * 9
    text_color_red = (0, 0, 255)
    text_color_black = (0, 0, 0)

    img = cv2.putText(img, 'Locking Doors...', (top_x + pad, top_y), font, font_scale, text_color_red, thickness,
                      cv2.LINE_AA)
    return img


def sound_alarm(img, box_width=450, font=cv2.FONT_ITALIC, font_scale=1, thickness=2, pad=20, space=50,
                indent=5):
    top_x = img.shape[1] - box_width - 5
    top_y = 5 + space * 10
    text_color_red = (0, 0, 255)
    text_color_black = (0, 0, 0)

    img = cv2.putText(img, 'Activating Audible Alarm', (top_x + pad, top_y), font, font_scale, text_color_red,
                      thickness,
                      cv2.LINE_AA)
    return img


def alert_sms(img, box_width=450, font=cv2.FONT_ITALIC, font_scale=1, thickness=2, pad=20, space=50,
                indent=5):
    top_x = img.shape[1] - box_width - 5
    top_y = 5 + space * 11
    text_color_red = (0, 0, 255)
    text_color_black = (0, 0, 0)

    img = cv2.putText(img, 'Sending SMS Alert...', (top_x + pad, top_y), font, font_scale, text_color_red,
                      thickness,
                      cv2.LINE_AA)
    return img


def alert_email(img, box_width=450, font=cv2.FONT_ITALIC, font_scale=1, thickness=2, pad=20, space=50,
                indent=5):
    top_x = img.shape[1] - box_width - 5
    top_y = 5 + space * 12
    text_color_red = (0, 0, 255)
    text_color_black = (0, 0, 0)

    img = cv2.putText(img, 'Sending E-Mail Alert...', (top_x + pad, top_y), font, font_scale, text_color_red,
                      thickness,
                      cv2.LINE_AA)
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
    frame_count = len(predictions)

    for i, prediction in enumerate(predictions):
        fname = out_path + "/" + prediction.split("/")[-1]

        img = open_image(prediction)
        # annotated_prediction = annotate_prediction(img)

        if i > 30:
            img = add_box_to_image(img)
            suspect = predict_suspect(img)
            img = alert_first_responders(img, suspect)

        if i > 90:
            img = lock_doors(img)

        if i > 120:
            img = sound_alarm(img)

        if i > 150:
            img = alert_sms(img)

        if i > 180:
            img = alert_email(img)


        save_image(img, fname)


if __name__ == "__main__":
    main()
