BOT_NAME = "pep_parse"

SPIDER_MODULES = ["pep_parse.spiders"]
NEWSPIDER_MODULE = "pep_parse.spiders"

ROBOTSTXT_OBEY = True

FEEDS = {
    "results/pep_%(time)s.csv": {
        "format": "csv",
        "encoding": "utf8",
        "fields": ["number", "name", "status"],
        "item_classes": ["pep_parse.items.PepParseItem"],
        "overwrite": True,
    }
}
FEED_EXPORT_FIELDS = ["number", "name", "status"]

ITEM_PIPELINES = {
    "pep_parse.pipelines.PepParsePipeline": 300,
}
