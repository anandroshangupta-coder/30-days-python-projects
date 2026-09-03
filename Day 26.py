# ==========================================
# Day 26 - Web Scraper
# 30 Days Python GitHub Project Challenge
# ==========================================

import requests
from bs4 import BeautifulSoup


print("======================================")
print("             WEB SCRAPER")
print("======================================")


# ==========================================
# Get Website URL
# ==========================================

url = input("\nEnter website URL: ").strip()

if url == "":
    print("❌ URL cannot be empty.")
    exit()


# Add https:// if missing
if not url.startswith(("http://", "https://")):
    url = "https://" + url


# ==========================================
# Send Request
# ==========================================

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:

    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

except requests.exceptions.RequestException as error:

    print("\n❌ Unable to access website.")
    print("Error:", error)
    exit()


# ==========================================
# Check Response
# ==========================================

if response.status_code != 200:

    print(
        f"\n❌ Website returned "
        f"status code: {response.status_code}"
    )

    exit()


print("\n✅ Website loaded successfully!")


# ==========================================
# Parse HTML
# ==========================================

soup = BeautifulSoup(
    response.text,
    "html.parser"
)


# ==========================================
# Get Page Title
# ==========================================

title = soup.title

if title:
    page_title = title.get_text(strip=True)
else:
    page_title = "No title found"


print("\n======================================")
print("          WEBSITE INFORMATION")
print("======================================")

print(f"Page Title : {page_title}")
print(f"URL        : {url}")


# ==========================================
# Extract Headings
# ==========================================

print("\n======================================")
print("              HEADINGS")
print("======================================")


headings = soup.find_all(
    ["h1", "h2", "h3"]
)


if headings:

    for number, heading in enumerate(
        headings,
        start=1
    ):

        text = heading.get_text(
            " ",
            strip=True
        )

        if text:
            print(f"{number}. {text}")

else:

    print("No headings found.")


# ==========================================
# Extract Links
# ==========================================

print("\n======================================")
print("               LINKS")
print("======================================")


links = soup.find_all("a")


valid_links = []

for link in links:

    link_text = link.get_text(
        " ",
        strip=True
    )

    link_url = link.get("href")

    if link_url:

        valid_links.append(
            (link_text, link_url)
        )


if valid_links:

    for number, (text, link_url) in enumerate(
        valid_links[:20],
        start=1
    ):

        if text == "":
            text = "No link text"

        print(
            f"{number}. {text} -> {link_url}"
        )

else:

    print("No links found.")


# ==========================================
# Extract Paragraphs
# ==========================================

print("\n======================================")
print("            PARAGRAPHS")
print("======================================")


paragraphs = soup.find_all("p")


if paragraphs:

    count = 0

    for paragraph in paragraphs:

        text = paragraph.get_text(
            " ",
            strip=True
        )

        if text:

            count += 1

            print(f"\n{count}. {text}")

            # Display only first 10
            if count == 10:
                break

else:

    print("No paragraphs found.")


# ==========================================
# Final Result
# ==========================================

print("\n======================================")
print("        SCRAPING COMPLETED! 🎉")
print("======================================")

print(f"Total headings : {len(headings)}")
print(f"Total links    : {len(valid_links)}")
print(f"Total paragraphs: {len(paragraphs)}")

print("======================================")