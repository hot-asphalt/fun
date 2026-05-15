from seleniumbase import SB
import os

with SB(uc=True, test=True, guest=True) as sb:
    url = os.environ["URL"]
    sb.activate_cdp_mode("https://www.aa.com/booking/search?locale=en_US&fareType=Lowest&pax=3&adult=3&type=OneWay&searchType=Award&cabin=&carriers=ALL&travelType=personal&slices=%5B%7B%22orig%22:%22CLT%22,%22origNearby%22:false,%22dest%22:%22HPN%22,%22destNearby%22:false,%22date%22:%222026-06-26%22%7D%5D")
    print("Sleeping for 30 seconds")
    title = sb.get_title()
    print("Title: ", title)
    sb.sleep(30)
    rows = sb.find_elements("div.flight-row")
    title = sb.get_title()
    print("Title: ", title)
    print(f"Found {len(rows)} rows")

    for row in rows:
        print(row.text)

    sb.sleep(1)
