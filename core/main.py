def main() -> None:    # starting function
    from utils import console, shorten

    console.clear()
    console.banner()

    # getting info
    url_to_mask: str = console.fancy_input("[?] URL to mask:")
    shorten.validate_url(url_to_mask)

    url_mask: str = console.fancy_input("[?] URL mask:")
    shorten.validate_url(url_mask)

    engineering_words: str = console.fancy_input("[?] Engineering words (complex) (separated by _):")

    # giving shortened URL
    shortened_url: str = shorten.shorten(url_to_mask, url_mask, engineering_words)
    console.fancy_print(f"[*] Shortened and masked url: {shortened_url}")

    print("\n\n", end = "")