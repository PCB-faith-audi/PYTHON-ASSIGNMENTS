import os
import requests
from urllib.parse import urlparse
import hashlib

def fetch_images(urls):
    """
    Ubuntu Image Fetcher
    - Downloads images from given URLs into Fetched_Images folder
    - Checks headers before downloading
    - Skips duplicates (based on file hash)
    - Handles errors gracefully
    """

    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Create directory
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    # Track hashes to avoid duplicates
    seen_hashes = set()

    for url in urls:
        try:
            # First, send a HEAD request to check headers
            head = requests.head(url, timeout=10, allow_redirects=True)
            head.raise_for_status()

            content_type = head.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print(f"❌ Skipped (Not an image): {url}")
                continue

            # Extract filename from URL or assign default
            parsed = urlparse(url)
            filename = os.path.basename(parsed.path) or "downloaded_image.jpg"
            filepath = os.path.join(folder, filename)

            # Now GET the actual content (stream mode)
            response = requests.get(url, timeout=10, stream=True)
            response.raise_for_status()

            # Save file in chunks, compute hash
            file_hash = hashlib.sha256()
            with open(filepath, "wb") as f:
                for chunk in response.iter_content(1024):
                    if chunk:
                        f.write(chunk)
                        file_hash.update(chunk)

            # Check for duplicates
            digest = file_hash.hexdigest()
            if digest in seen_hashes:
                print(f"⚠ Duplicate found, removing {filename}")
                os.remove(filepath)
                continue

            seen_hashes.add(digest)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}\n")

        except requests.exceptions.MissingSchema:
            print(f"❌ Invalid URL: {url}")
        except requests.exceptions.ConnectionError:
            print(f"❌ Connection error for {url}")
        except requests.exceptions.Timeout:
            print(f"❌ Request timed out for {url}")
        except requests.exceptions.HTTPError as e:
            print(f"❌ HTTP error for {url}: {e}")
        except Exception as e:
            print(f"❌ Unexpected error for {url}: {e}")

    print("Connection strengthened. Community enriched.")

if __name__ == "__main__":
    # Accept multiple URLs at once
    user_input = input("Please enter one or more image URLs (separated by spaces): ").strip().split()
    fetch_images(user_input)
