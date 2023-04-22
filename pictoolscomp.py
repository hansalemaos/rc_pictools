from nutikacompile import compile_with_nuitka

wholecommand = compile_with_nuitka(
    pyfile=r"C:\ProgramData\anaconda3\envs\nu\pictools.pyw",
    icon=r"C:\Users\hansc\Downloads\cova.jpg",
    disable_console=True,
    file_version="1.0.0.0",
    onefile=True,
    outputdir="c:\\nuitkapictoicon",
    addfiles=[
    ],
    delete_onefile_temp=False,  # creates a permanent cache folder
    needs_admin=True,
    arguments2add="--msvc=14.3 --noinclude-numba-mode=nofollow",
)
