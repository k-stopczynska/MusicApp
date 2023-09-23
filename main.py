from search import use_search_engine
from recording import get_details_from_recording


def main():
    mode = input(
        "Do you want to use a search engine(1) or identify a song "
        "on a short sample using microphone(2)? (1/2) ")
    if mode == '1':
        use_search_engine()
    elif mode == '2':
        get_details_from_recording()
    else:
        main()


if __name__ == "__main__":
    main()
