from pelican.settings import DEFAULT_CONFIG
from pelican.readers import MarkdownReader

config = DEFAULT_CONFIG.copy()
# If you need to override default settings (e.g., DOCUTILS_SETTINGS / DEFAULT_LANG):
# config["DEFAULT_LANG"] = "de"

# .read() returns (content, metadata). Keep content only; we don’t need the metadata.
# Assign content to an ALL-CAPS variable to access from template:
INTRO, _ = MarkdownReader(config).read("content/pages/home.md")

AUTHOR = 'Samuel Colburn'
SITENAME = 'Sardine Sound'
SITESUBTITLE = "Live audio for community theater and small events in southeastern MA"
SITEURL = 'https://sardinesound.com'
PATH = 'content'
THEME = 'themes/sardine'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
STATIC_PATHS = ["images"]
PAGE_ORDER_BY = 'sortorder'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

# Blogroll
LINKS = (
    ('About', './about'),
    ('Services', './services'),
    ('Pricing', './pricing'),
    ('Checklists', './checklists'),
)

# Social widget
SOCIAL = (
    ('@sam.codes', 'https://bsky.app/profile/sam.codes'),
)

DEFAULT_PAGINATION = 15
RELATIVE_URLS = True
# MENUITEMS = [
#     ("About", '/hello-world.html')
# ]
