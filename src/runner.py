thonimport sys
import os
import json
import logging
from extractors.tiktok_shop_parser import TikTokShopParser
from outputs.exporters import export_to_csv, export_to_json

logging.basicConfig(level=logging.INFO)

def main():
    if len(sys.argv) < 2:
        logging.error("Please provide the TikTok Shop URL as a command line argument.")
        sys.exit(1)

    url = sys.argv[1]

    try:
        parser = TikTokShopParser(url)
        data = parser.extract_product_data()

        output_format = 'json'  # Default output format
        if len(sys.argv) >= 3:
            output_format = sys.argv[2]

        if output_format == 'csv':
            export_to_csv(data)
        elif output_format == 'json':
            export_to_json(data)
        else:
            logging.error(f"Unsupported output format: {output_format}")
            sys.exit(1)

    except Exception as e:
        logging.error(f"An error occurred while scraping the data: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()