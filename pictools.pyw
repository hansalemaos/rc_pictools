from PIL import Image
from hackyargparser import add_sysargv
from shellextools import (
    format_folder_drive_path_backslash,
    add_multicommands_files,
    change_file_extension,
)
import sys


@add_sysargv
def main(path: str = "", action: str = ""):
    path = format_folder_drive_path_backslash(path)
    img = Image.open(path)

    if action == "convert2ico":
        iconfi = change_file_extension(path=path, extension="ico")
        img.resize((512, 512)).save(iconfi)
    if action == "convert2gray":
        iconfi = change_file_extension(path=path, prefix="gray_", extension="png")
        img.convert("L").save(iconfi)
    if action == "convert2bw":
        iconfi = change_file_extension(path=path, prefix="bw_", extension="png")
        img.convert("1").save(iconfi)
    return 0


if __name__ == "__main__":
    if len(sys.argv) == 1:
        futurnameofcompiledexe = "pictools.exe"
        multicommands = [
            {
                "mainmenuitem": "PicTools",
                "submenu": "Convert to .ico",
                "folderinprogramdata": "RCTools",
                "filetypes": ["bmp", "png", "jpg", "jpeg"],
                "additional_arguments": "--action convert2ico",
            },
            {
                "mainmenuitem": "PicTools",
                "submenu": "Convert to grayscale",
                "folderinprogramdata": "RCTools",
                "filetypes": ["bmp", "png", "jpg", "jpeg"],
                "additional_arguments": "--action convert2gray",
            },
            {
                "mainmenuitem": "PicTools",
                "submenu": "Convert to bw",
                "folderinprogramdata": "RCTools",
                "filetypes": ["bmp", "png", "jpg", "jpeg"],
                "additional_arguments": "--action convert2bw",
            },
        ]
        add_multicommands_files(multicommands, futurnameofcompiledexe)
    else:
        main()

