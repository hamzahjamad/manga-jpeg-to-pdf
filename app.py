import os
from dotenv import load_dotenv
from helpers import pdf_title_generator, pdf_file_generator, move_to_after_last_processed_chapter

load_dotenv()

MANGA_DIRECTORY = os.getenv('MANGA_DIRECTORY')
MANGA_TITLE = os.getenv('MANGA_TITLE')
IS_USING_HUMANIZED_CHAPTER_TITLE = os.getenv('IS_USING_HUMANIZED_CHAPTER_TITLE') \
                                     .lower() in ('true', '1', 't')
SOURCE_PATH = MANGA_DIRECTORY + MANGA_TITLE + "/"

chapter_directories = list(os.walk(SOURCE_PATH))

LAST_PROCESSED_CHAPTER = os.getenv('LAST_PROCESSED_CHAPTER')
if LAST_PROCESSED_CHAPTER  != "":
    chapter_directories = move_to_after_last_processed_chapter(chapter_directories, LAST_PROCESSED_CHAPTER)

for directory_details in chapter_directories:
    chapter_path = directory_details[0] + "/"
    chapter_directory_name = chapter_path.split("/")[-2:][0]
    chapter_title = pdf_title_generator(
        MANGA_TITLE, 
        chapter_directory_name,
        IS_USING_HUMANIZED_CHAPTER_TITLE)

    if chapter_title is not None:
       print("Generating '" + chapter_title + "'")
       pdf_file_generator(chapter_path, chapter_title)
