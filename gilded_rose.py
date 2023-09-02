"""The Guilder Rose"""


from typing import Iterable, Protocol


AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONJURED = "Conjured Mana Cake"


class Item:
    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self) -> str:
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose:
    def __init__(self, items: Iterable[Item]):
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            get_item_updater(item).update(item)


class ItemUpdater(Protocol):
    @staticmethod
    def update(item: Item) -> None:
        ...


class DefaultUpdater:
    @staticmethod
    def update(item: Item) -> None:
        update_sell_in(item)
        if item.sell_in >= 0:
            update_quality(item, -1)
        else:
            update_quality(item, -2)


class AgedBrieUpdater:
    @staticmethod
    def update(item: Item) -> None:
        update_sell_in(item)
        if item.sell_in >= 0:
            update_quality(item, 1)
        else:
            update_quality(item, 2)


class BackstagePassUpdater:
    @staticmethod
    def update(item: Item) -> None:
        update_sell_in(item)
        if item.sell_in >= 10:
            update_quality(item, 1)
        elif item.sell_in >= 5:
            update_quality(item, 2)
        elif item.sell_in >= 0:
            update_quality(item, 3)
        else:
            item.quality = 0


class SulfurasUpdater:
    @staticmethod
    def update(_: Item) -> None:
        pass


class ConjuredUpdater:
    @staticmethod
    def update(item: Item) -> None:
        update_sell_in(item)
        if item.sell_in >= 0:
            update_quality(item, -2)
        else:
            update_quality(item, -4)


def update_sell_in(item: Item) -> None:
    item.sell_in -= 1


def update_quality(item: Item, amount: int) -> None:
    item.quality = max(0, min(50, item.quality + amount))


def get_item_updater(item: Item) -> ItemUpdater:
    MAP = {
        AGED_BRIE: AgedBrieUpdater,
        BACKSTAGE_PASSES: BackstagePassUpdater,
        SULFURAS: SulfurasUpdater,
        CONJURED: ConjuredUpdater,
    }
    return MAP.get(item.name, DefaultUpdater)
