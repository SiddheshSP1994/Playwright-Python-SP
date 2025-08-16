import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-1621", "title": "Checkout scenario 1621", "data": {"sku": "SKU1621", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1621@example.com", "threshold": 210}},
    {"id": "CHECKOUT-1622", "title": "Checkout scenario 1622", "data": {"sku": "SKU1622", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1622@example.com", "threshold": 220}},
    {"id": "CHECKOUT-1623", "title": "Checkout scenario 1623", "data": {"sku": "SKU1623", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1623@example.com", "threshold": 230}},
    {"id": "CHECKOUT-1624", "title": "Checkout scenario 1624", "data": {"sku": "SKU1624", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1624@example.com", "threshold": 240}},
    {"id": "CHECKOUT-1625", "title": "Checkout scenario 1625", "data": {"sku": "SKU1625", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1625@example.com", "threshold": 250}},
    {"id": "CHECKOUT-1626", "title": "Checkout scenario 1626", "data": {"sku": "SKU1626", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1626@example.com", "threshold": 260}},
    {"id": "CHECKOUT-1627", "title": "Checkout scenario 1627", "data": {"sku": "SKU1627", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1627@example.com", "threshold": 270}},
    {"id": "CHECKOUT-1628", "title": "Checkout scenario 1628", "data": {"sku": "SKU1628", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1628@example.com", "threshold": 280}},
    {"id": "CHECKOUT-1629", "title": "Checkout scenario 1629", "data": {"sku": "SKU1629", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1629@example.com", "threshold": 290}},
    {"id": "CHECKOUT-1630", "title": "Checkout scenario 1630", "data": {"sku": "SKU1630", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1630@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
