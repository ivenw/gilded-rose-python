from gilded_rose import GildedRose, Item


BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"


def test_quality_increases_by_1_when_sell_in_greater_than_10():
    items = [Item(BACKSTAGE_PASS, 11, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 1


def test_quality_increases_by_2_when_sell_in_between_6_and_10():
    items = [Item(BACKSTAGE_PASS, 10, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 2


def test_quality_increases_by_3_when_sell_in_between_1_and_5():
    items = [Item(BACKSTAGE_PASS, 5, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 3


def test_quality_is_0_when_sell_in_is_0():
    items = [Item(BACKSTAGE_PASS, 0, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0
