"""The Gilded Rose Inn"""

from typing import Protocol


MAX_QUALITY = 50


class Item:
    def __init__(self, name: str, sell_in: int, quality: int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemUpdateStrategy(Protocol):
    def update(self, item: Item) -> None:
        ...


class GenericItemUpdateStrategy(ItemUpdateStrategy):
    def update(self, item: Item) -> None:
        item.sell_in -= 1
        if item.quality > 0:
            item.quality -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1


class AgedBrieUpdateStrategy(ItemUpdateStrategy):
    def update(self, item: Item) -> None:
        item.sell_in -= 1
        if item.quality < MAX_QUALITY:
            item.quality += 1
        if item.sell_in < 0 and item.quality < MAX_QUALITY:
            item.quality += 1


class SulfurasUpdateStrategy(ItemUpdateStrategy):
    def update(self, item: Item) -> None:
        del item


class BackstagePassUpdateStrategy(ItemUpdateStrategy):
    def update(self, item: Item) -> None:
        item.sell_in -= 1
        if item.quality < MAX_QUALITY:
            item.quality += 1
            if item.sell_in < 10 and item.quality < MAX_QUALITY:
                item.quality += 1
            if item.sell_in < 5 and item.quality < MAX_QUALITY:
                item.quality += 1
        if item.sell_in < 0:
            item.quality = 0


class ConjuredItemUpdateStrategy(ItemUpdateStrategy):
    def update(self, item: Item) -> None:
        item.sell_in -= 1
        if item.quality > 0:
            item.quality -= 2
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 2


class GildedRose:
    def __init__(self, items: list[Item]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            get_item_update_strategy(item).update(item)


def get_item_update_strategy(item: Item) -> ItemUpdateStrategy:
    MAP = {
        "Aged Brie": AgedBrieUpdateStrategy(),
        "Sulfuras, Hand of Ragnaros": SulfurasUpdateStrategy(),
        "Backstage passes to a TAFKAL80ETC concert": BackstagePassUpdateStrategy(),
        "Conjured Mana Cake": ConjuredItemUpdateStrategy(),
    }
    return MAP.get(item.name, GenericItemUpdateStrategy())
