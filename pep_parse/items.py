import scrapy


class PepParseItem(scrapy.Item):
    """Item модель информации о PEP."""

    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
