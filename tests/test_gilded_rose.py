from gilded_rose import Item, GildedRose


def test_quality_update_normal():
    items = [
        Item("foo", 1, 50),
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 49
    gilded_rose.update_quality()
    assert items[0].quality == 47


def test_quality_update_brie():
    items = [
        Item("Aged Brie", 1, 1),
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 2
    gilded_rose.update_quality()
    assert items[0].quality == 4


def test_quality_update_sulfuras():
    items = [
        Item("Sulfuras, Hand of Ragnaros", 1, 1),
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 1
    assert items[0].sell_in == 1
    gilded_rose.update_quality()
    assert items[0].quality == 1
    assert items[0].sell_in == 1


def test_quality_update_backstage_pass_sell_in_11():
    items = [
        Item("Backstage passes to a TAFKAL80ETC concert", 11, 1),
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 2
    assert items[0].sell_in == 10
    gilded_rose.update_quality()
    assert items[0].quality == 4
    assert items[0].sell_in == 9


def test_quality_update_backstage_pass_sell_in_6():
    items = [
        Item("Backstage passes to a TAFKAL80ETC concert", 6, 1),
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 3
    assert items[0].sell_in == 5
    gilded_rose.update_quality()
    assert items[0].quality == 6
    assert items[0].sell_in == 4


def test_quality_update_backstage_pass_sell_in_1():
    items = [
        Item("Backstage passes to a TAFKAL80ETC concert", 1, 1),
    ]

    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 4
    assert items[0].sell_in == 0
    gilded_rose.update_quality()
    assert items[0].quality == 0
