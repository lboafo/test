"""Wishlist object"""


class WishList(object):
    def __init__(self, wishlist_name="new_list"):
        self._item = None
        self._list_name = wishlist_name

    @property
    def list_name(self):
        return self._list_name

    @list_name.setter
    def list_name(self, value):
        self._list_name = value

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, value):
        self._item = value

    @staticmethod
    def create_list(item_name):
        item_list = item_name
        return item_list


def main():
    wishlist = WishList(wishlist_name="valentine_list")
    print(wishlist.create_list(["ring", "chocolate"]))


if __name__ == '__main__':
    main()