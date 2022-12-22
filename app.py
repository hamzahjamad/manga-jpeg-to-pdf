import os
from dotenv import load_dotenv
from helpers import pdf_title_generator, pdf_file_generator

load_dotenv()

dir_path = os.getenv('MANGA_DIR')
manga_title = os.getenv('MANGA_TITLE')
is_using_humanized_chapter_title = os.getenv('IS_USING_HUMANIZED_CHAPTER_TITLE')
is_using_humanized_chapter_title = is_using_humanized_chapter_title.lower() in ('true', '1', 't')

source_path = dir_path + manga_title + "/"

for directory_details in os.walk(source_path):
    chapter_path = directory_details[0] + "/"
    chapter_folder_name = chapter_path.split("/")[-2:][0]
    chapter_title = pdf_title_generator(
        manga_title, 
        chapter_folder_name,
        is_using_humanized_chapter_title)

    if chapter_title is not None:
       print("Generating " + chapter_title)
       pdf_file_generator(chapter_path, chapter_title)
