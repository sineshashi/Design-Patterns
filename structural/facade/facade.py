'''
When we have a complex logic and some complex functions the we hide the complexity behind a simple interface.
for e.g., public libraries like django provide a simple interface of complex logic.

One practical example, in an ecommerce application, there may be some very complex logics and complex functions \n
like create_new_cart, add_item_to_cart, place_order and many more. To hide this complexity from client we can \n
use a simple interface or class which provides easy access to them.
'''

class Facade:
    @staticmethod
    def create_cart():
        ...

    @staticmethod
    def add_item_to_cart():
        ...

    @staticmethod
    def place_order():
        ...

    @staticmethod
    def cancel_order():
        ...