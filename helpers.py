import os
import re
from PIL import Image

def chapter_folder_to_human_language_transformer(chapter_folder):
    # get the Ch.XXX pattern

    result = None
    try:
        result = re.search('(Ch.[0-9]+)', chapter_folder).group(1)
        result = result.replace("Ch.", "Chapter ")

        chapter_number_original = re.search('([0-9]+)', chapter_folder).group(1)
        chapter_number = int(chapter_number_original) # remove prefix 0 infront of number
        chapter_number = str(chapter_number)

        result = result.replace(chapter_number_original, chapter_number)
    except AttributeError:
        pass

    return result

def pdf_title_generator(manga_title, chapter_folder):
    chapter_title = chapter_folder_to_human_language_transformer(chapter_folder)
    if chapter_title is None:
        return None

    return manga_title + " " + chapter_title + ".pdf"

def pdf_file_generator(source_path, chapter_title):
    res = []

    # Iterate directory
    for path in os.listdir(source_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(source_path, path)):
            image = Image.open(source_path + path)
            img = image.convert('RGB')
            res.append(img)
    # print("All files: ")        
    # print(res)

    output_file = "output/" + chapter_title
    res[0].save(output_file, save_all=True, append_images=res)