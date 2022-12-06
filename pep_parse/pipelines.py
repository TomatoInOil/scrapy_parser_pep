import csv
from datetime import datetime, timezone
from pathlib import Path

STATUS_COL = "Статус"
SUMMARY_COL = "Количество"
STATUS_SUM_FIELDS = [STATUS_COL, SUMMARY_COL]
BASE_DIR = Path("results")


class PepParsePipeline:
    """Создание сводной таблицы по статусам PEP и сохранение в csv."""

    def open_spider(self, spider):
        self.time = (
            datetime.now(timezone.utc)
            .isoformat(timespec="seconds")[:-6]
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
        self.summary_data[item["status"]] = (
            self.summary_data.get(item["status"], 0) + 1
        )
        self.total += 1
        return item

    def close_spider(self, spider):
        with open(
            BASE_DIR / f"status_summary_{self.time}.csv", "a", newline=""
        ) as csvfile:
            writer = csv.writer(csvfile)
            rows = sorted(self.summary_data.items())
            rows.append(("Total", self.total))
            writer.writerows(rows)
        spider.close()
