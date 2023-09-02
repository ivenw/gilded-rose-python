from gilded_rose import Item, GildedRose


SULFURAS = "Sulfuras, Hand of Ragnaros"


def test_sell_in_does_not_change():
    items = [Item(SULFURAS, 0, 80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 0


def test_quality_does_not_change():
    items = [Item(SULFURAS, 0, 80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 80
