import os
import re
from PIL import Image

def chapter_directory_to_human_language_transformer(chapter_directory):
    # get the Ch.XXX pattern

    result = None
    try:
        result = re.search('(Ch.[0-9]+)', chapter_directory).group(1)
        result = result.replace("Ch.", "Chapter ")

        chapter_number_original = re.search('([0-9]+)', chapter_directory).group(1)
        chapter_number = int(chapter_number_original) # remove prefix 0 infront of number
        chapter_number = str(chapter_number)

        result = result.replace(chapter_number_original, chapter_number)
    except AttributeError:
        pass

    return result

def pdf_title_generator(manga_title, chapter_directory, is_using_humanized_chapter_title):
    chapter_title = None
    result = None

    if is_using_humanized_chapter_title:
       chapter_title = chapter_directory_to_human_language_transformer(chapter_directory)
    else:
       chapter_title = chapter_directory

    if chapter_title is None or chapter_title == "":
        result = None
    else: 
        result = manga_title + " " + chapter_title + ".pdf"      

    return result

def pdf_file_generator(source_path, chapter_title):
    result = []

    for path in os.listdir(source_path):
        if os.path.isfile(os.path.join(source_path, path)):
            image = Image.open(source_path + path)
            img = image.convert('RGB')
            result.append(img)

    output_file = "output/" + chapter_title
    result[0].save(output_file, save_all=True, append_images=result)