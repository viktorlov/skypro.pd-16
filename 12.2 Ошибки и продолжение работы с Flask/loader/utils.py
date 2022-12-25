import json

from config import UPLOAD_FOLDER, POST_PATH
from exceptions import WrongImgType


# def save_uploaded_image(picture):
#    filename = picture.filename

def save_picture(picture):
    types_file = ["jpg", "png", "gif", "jpeg"]
    picture_type = picture.filename.split(".")[-1]
    if picture_type not in types_file:
        raise WrongImgType(f"Неверный формат файла! Допустимы только {', '.join(types_file)}")

    picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"
    picture.save(picture_path)
    return picture_path


def add_post(post_list, post):
    post_list.append(post)
    with open(POST_PATH, "w", encoding="UTF-8") as file:
        json.dump(post_list, file)
