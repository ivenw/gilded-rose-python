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


class ItemUpdater(Protocol):
    @staticmethod
    def update_sell_in(item: Item) -> None:
        ...

    @staticmethod
    def update_quality(item: Item) -> None:
        ...

    @classmethod
    def update(cls, item: Item) -> None:
        ...


class DefaultUpdater(ItemUpdater):
    @staticmethod
    def update_sell_in(item: Item) -> None:
        item.sell_in -= 1

    @staticmethod
    def update_quality(item: Item) -> None:
        if item.sell_in >= 0:
            update_quality(item, -1)
        else:
            update_quality(item, -2)

    @classmethod
    def update(cls, item: Item) -> None:
        cls.update_sell_in(item)
        cls.update_quality(item)


class AgedBrieUpdater(DefaultUpdater):
    @staticmethod
    def update_quality(item: Item) -> None:
        if item.sell_in >= 0:
            update_quality(item, 1)
        else:
            update_quality(item, 2)


class BackstagePassUpdater(DefaultUpdater):
    @staticmethod
    def update_quality(item: Item) -> None:
        if item.sell_in >= 10:
            update_quality(item, 1)
        elif item.sell_in >= 5:
            update_quality(item, 2)
        elif item.sell_in >= 0:
            update_quality(item, 3)
        else:
            item.quality = 0


class SulfurasUpdater(DefaultUpdater):
    @staticmethod
    def update_sell_in(_: Item) -> None:
        pass

    @staticmethod
    def update_quality(_: Item) -> None:
        pass


class ConjuredUpdater(DefaultUpdater):
    @staticmethod
    def update_quality(item: Item) -> None:
        if item.sell_in >= 0:
            update_quality(item, -2)
        else:
            update_quality(item, -4)


class GildedRose:
    def __init__(self, items: Iterable[Item]):
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            get_item_updater(item).update(item)


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
