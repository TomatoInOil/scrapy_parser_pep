import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """Сбор информации о статусах PEP."""

    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        all_peps = response.xpath(
            "//section[@id='numerical-index']//td[a][1]/a[starts-with(@href, '/pep-')]/@href"
        ).getall()
        for pep in all_peps:
            yield response.follow(pep, self.parse_pep)

    def parse_pep(self, response):
        data = {}
        pep_title_pattern = (
            r"PEP (?P<number>\d+) \S (?P<name>.+) \| peps\.python\.org"
        )
        title_match = re.match(
            pep_title_pattern, response.xpath("//title/text()").get()
        )
        data["number"] = title_match.group("number")
        data["name"] = title_match.group("name")
        data["status"] = response.xpath(
            "//article//dl/dt[text()='Status']/following-sibling::dd[1]/abbr/text()"
        ).get()
        yield PepParseItem(data)
