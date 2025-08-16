import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-1381", "title": "Checkout scenario 1381", "data": {"sku": "SKU1381", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1381@example.com", "threshold": 810}},
    {"id": "CHECKOUT-1382", "title": "Checkout scenario 1382", "data": {"sku": "SKU1382", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1382@example.com", "threshold": 820}},
    {"id": "CHECKOUT-1383", "title": "Checkout scenario 1383", "data": {"sku": "SKU1383", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1383@example.com", "threshold": 830}},
    {"id": "CHECKOUT-1384", "title": "Checkout scenario 1384", "data": {"sku": "SKU1384", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1384@example.com", "threshold": 840}},
    {"id": "CHECKOUT-1385", "title": "Checkout scenario 1385", "data": {"sku": "SKU1385", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1385@example.com", "threshold": 850}},
    {"id": "CHECKOUT-1386", "title": "Checkout scenario 1386", "data": {"sku": "SKU1386", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1386@example.com", "threshold": 860}},
    {"id": "CHECKOUT-1387", "title": "Checkout scenario 1387", "data": {"sku": "SKU1387", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1387@example.com", "threshold": 870}},
    {"id": "CHECKOUT-1388", "title": "Checkout scenario 1388", "data": {"sku": "SKU1388", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1388@example.com", "threshold": 880}},
    {"id": "CHECKOUT-1389", "title": "Checkout scenario 1389", "data": {"sku": "SKU1389", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1389@example.com", "threshold": 890}},
    {"id": "CHECKOUT-1390", "title": "Checkout scenario 1390", "data": {"sku": "SKU1390", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1390@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
