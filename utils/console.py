def clear() -> None:    # clears the console
    import os

    command: str = "clear"
    if os.name in ["nt", "dos"]:
        command = "cls"
    os.system(command)


def banner() -> None:    # prints the banner
    import termcolor
    import pyfiglet


    termcolor.cprint(
        pyfiglet.figlet_format(
            "MaskShortener"
        ),
        "yellow", "on_grey",
        attrs = ["bold"]
    )


def fancy_input(text: str) -> str:    # colored input
    import termcolor

    # printing input
    termcolor.cprint(
        text,
        "yellow", "on_grey",
        end = ""
    )
    print(" ", end = "")

    # getting input
    answer: str = input()

    return answer


def fancy_print(text: str) -> None:    # colored print
    import termcolor

    # printing input
    termcolor.cprint(
        text,
        "yellow", "on_grey",
        end = ""
    )