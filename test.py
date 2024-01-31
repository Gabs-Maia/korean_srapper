from Sync.Scraper.content_scraper import get_table_contentTXT
import Sync.Scraper.translations
from Sync.Scraper.file_handling import in_text

korean = get_table_contentTXT()
in_text(korean, 'korean.txt')