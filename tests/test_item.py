from gilded_rose import Item, GildedRose


FOO = "foo"


def test_sell_in_decreases():
    gilded_rose = GildedRose([Item(FOO, 1, 0)])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].sell_in == 0


def test_quality_decreases_by_one():
    gilded_rose = GildedRose([Item(FOO, 1, 1)])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 0


def test_quality_does_not_decrease_below_zero():
    gilded_rose = GildedRose([Item(FOO, 0, 0)])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 0


def test_quality_decreases_by_two_after_sell_in():
    gilded_rose = GildedRose([Item(FOO, 0, 2)])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 0
