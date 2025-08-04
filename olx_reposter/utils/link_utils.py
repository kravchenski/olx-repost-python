def replace_placeholders_with_dimensions(template_url, width, height):
    return template_url.replace("{width}", str(width)).replace("{height}", str(height))
