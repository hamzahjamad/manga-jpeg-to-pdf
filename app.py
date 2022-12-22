import os
from dotenv import load_dotenv
from helpers import pdf_title_generator, pdf_file_generator, move_to_last_chapters

load_dotenv()

LAST_CHAPTER = os.getenv('LAST_CHAPTER')
MANGA_DIRECTORY = os.getenv('MANGA_DIRECTORY')
MANGA_TITLE = os.getenv('MANGA_TITLE')
IS_USING_HUMANIZED_CHAPTER_TITLE = os.getenv('IS_USING_HUMANIZED_CHAPTER_TITLE') \
                                     .lower() in ('true', '1', 't')

SOURCE_PATH = MANGA_DIRECTORY + MANGA_TITLE + "/"

all_items = list(os.walk(SOURCE_PATH))

if LAST_CHAPTER  != "":
    all_items = move_to_last_chapters(all_items, LAST_CHAPTER)

for directory_details in all_items:
    chapter_path = directory_details[0] + "/"
    chapter_directory_name = chapter_path.split("/")[-2:][0]
    chapter_title = pdf_title_generator(
        MANGA_TITLE, 
        chapter_directory_name,
        IS_USING_HUMANIZED_CHAPTER_TITLE)

    if chapter_title is not None:
       print("Generating " + chapter_title)
       pdf_file_generator(chapter_path, chapter_title)
