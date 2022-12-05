from pathlib import Path

BOT_NAME = "pep_parse"

SPIDER_MODULES = ["pep_parse.spiders"]
NEWSPIDER_MODULE = "pep_parse.spiders"


ROBOTSTXT_OBEY = True

RESULTS_DIR = Path("results")
FEEDS = {
    RESULTS_DIR
    / "pep_%(time)s.csv": {
        "format": "csv",
        "encoding": "utf8",
        "item_classes": ["pep_parse.items.PepParseItem"],
        "overwrite": True,
    }
}
