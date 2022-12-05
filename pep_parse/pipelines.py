import csv
from datetime import datetime as dt
from datetime import timezone
from pathlib import Path

STATUS_COL = "Статус"
SUMMARY_COL = "Количество"
STATUS_SUM_FIELDS = [STATUS_COL, SUMMARY_COL]
BASE_DIR = Path("results")


class PepParsePipeline:
    """Создание сводной таблицы по статусам PEP и сохранение в csv."""

    def open_spider(self, spider):
        self.time = (
            dt.now(timezone.utc)
            .isoformat(timespec="seconds")
            .replace(":", "-")
        )
        with open(
            BASE_DIR / f"status_summary_{self.time}.csv", "w", newline=""
        ) as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=STATUS_SUM_FIELDS)
            writer.writeheader()
        self.summary_data = {}
        self.total = 0

    def process_item(self, item, spider):
        if item["status"] in self.summary_data:
            self.summary_data[item["status"]] += 1
        else:
            self.summary_data[item["status"]] = 1
        self.total += 1
        return item

    def close_spider(self, spider):
        with open(
            BASE_DIR / f"status_summary_{self.time}.csv", "a", newline=""
        ) as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=STATUS_SUM_FIELDS)
            for status, number in self.summary_data.items():
                writer.writerow({STATUS_COL: status, SUMMARY_COL: number})
            writer.writerow({STATUS_COL: "Total", SUMMARY_COL: self.total})
        spider.close()
