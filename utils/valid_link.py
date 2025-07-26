def set_valid_link(images, invalid_image_link, i):
    return invalid_image_link.replace("{width}", str(images[i]['width'])).replace("{height}", str(images[i]['height']))
