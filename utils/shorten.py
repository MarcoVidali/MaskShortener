def validate_url(url: str) -> None:    # validates URL
    import validators
    from utils import console
    
    if not validators.url(url):
        console.fancy_print("[-] URL not valid.")
        exit()


def shorten(url_to_mask, url_mask, engineering_words) -> str:    # shortens the url
    import gdshortener
    from utils import console

    # removing last backslash from url_mask
    if url_mask[len(url_mask) - 1] == "/":
        url_mask = url_mask[:-1]
    
    # shortening
    try:
        shortened_url: str = gdshortener.ISGDShortener().shorten(
            url = url_to_mask,
            custom_url = engineering_words
        )[0][8:]
    except gdshortener.GDGenericError:
        console.fancy_print("[-] URL already exists (use different engineering words).")
        exit()
    shortened_url = f"{url_mask}@{shortened_url}"

    return shortened_url