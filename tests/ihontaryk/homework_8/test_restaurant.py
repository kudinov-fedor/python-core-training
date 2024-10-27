import pytest

from ihontaryk.homework_8.restaurant import ItalianRestaurant, SpanishRestaurant, \
    AustrianRestaurant, Order

menu1 = ItalianRestaurant()
menu2 = SpanishRestaurant()
menu3 = AustrianRestaurant()


@pytest.mark.parametrize('menu, order, expected_result',
                         [(menu1, (Order('first_course', 2, 21),
                                   Order('second_course', 2, 35),
                                   Order('dessert', 2, 18),
                                   Order('beverage', 2, 4)),
                           'Pasta: 42, Potato with chicken: 70, Tiramisu: 36, Sparkling water: 8, '
                           'Total cost: 156'),
                          (menu2, (Order('first_course', 2, 18),
                            Order('second_course', 2, 33),
                            Order('dessert', 2, 20.5),
                            Order('beverage', 2, 4.5)),
                           'Seafood soup: 36, Paella with seafood: 66, Banana mousse: 41.0, Juice: 9.0, '
                           'Total cost: 152.0'),
                          (menu3, (Order('first_course', 2, 23.5),
                                   Order('second_course', 2, 36),
                                   Order('dessert', 2, 18.5),
                                   Order('beverage', 2, 5.25)),
                           'Chicken soup: 47.0, Fried pike-perch fillet: 72, Milk cream strudel : 37.0, Lemonade: 10.5, '
                           'Total cost: 166.5')
                          ])
def test_calculate_total_cost(menu, order, expected_result):
    """
    verify calculate_total_cost function
    """

    menu.get_client_order(order)
    assert menu.calculate_total_cost() == expected_result
