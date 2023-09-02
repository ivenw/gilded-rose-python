from gilded_rose import GildedRose, Item


AGED_BRIE = "Aged Brie"


def test_quality_increases_by_one():
    items = [Item(AGED_BRIE, 1, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 1


def test_quality_increases_by_two_after_sell_in():
    items = [Item(AGED_BRIE, 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 2


def test_quality_never_exceeds_50():
    items = [Item(AGED_BRIE, 0, 50)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 50
