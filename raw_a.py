from seleniumbase import SB
import os

with SB(uc=True, test=True, guest=True) as sb:
    url = os.environ["URL"]
    sb.activate_cdp_mode(url)
    print("Sleeping for 30 seconds")
    sb.sleep(30)
    rows = sb.find_elements("div.flight-row")
    print(f"Found {len(rows)} rows")

    for row in rows:
        print(row.text)

    sb.sleep(1)
