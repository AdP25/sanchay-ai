import os
import whisper
from whisper import utils
import warnings

INPUT_FILE_PATH = "videos/video.mp4"
OUTPUT_DIR = "output"
OUTPUT_TYPE = "vtt"


# INPUT_PATH = os.environ.get(INPUT_FILE_PATH)
# OUTPUT_PATH = os.environ.get(OUTPUT_DIR)
# OUTPUT_TYPE = os.environ.get(OUTPUT_TYPE)

INPUT_PATH = INPUT_FILE_PATH
OUTPUT_PATH = OUTPUT_DIR
OUTPUT_TYPE = OUTPUT_TYPE

# Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse 
# audio and is also a multitasking model that can perform multilingual speech recognition, speech translation, and language identification.
def generateSubtitles():
    # The model is loaded with the name 'tiny'
    model = whisper.load_model("tiny")
    # Using the loaded model to transcribe or generate subtitles for a file specified by the INPUT_PATH variable
    result = model.transcribe(INPUT_PATH)
    # write the generated subtitles to an output file 
    writer = utils.get_writer(OUTPUT_TYPE, OUTPUT_PATH)
    writer_args = {
        "highlight_words": False,
        "max_line_count": None,
        "max_line_width": None,
        "max_words_per_line": None,
    }
    writer(result, OUTPUT_PATH, **writer_args)
    print("⚡️ Success! ⚡️ Subtitles have been generated!")

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    print("\n\n⚡️⚡️⚡️ Video Subtitles & Chapters generator | 100xDevs ⚡️⚡️⚡️")
    print("\n\nStep 1: Generating subtitles for your video. This might take some time, take a kit-kat break 🚀")
    generateSubtitles()