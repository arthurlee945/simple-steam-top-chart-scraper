from scraper import SteamScrapper


if __name__ == "__main__":
    s_scrapper = SteamScrapper()
    to_email = input("where would you like the email to sent to?: ")
    while "@" not in to_email or "." not in to_email:
        to_email = input("Please enter valid email: ")

    s_scrapper.send_data_to_email(to_addr=to_email)