import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-1021", "title": "Checkout scenario 1021", "data": {"sku": "SKU1021", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1021@example.com", "threshold": 210}},
    {"id": "CHECKOUT-1022", "title": "Checkout scenario 1022", "data": {"sku": "SKU1022", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1022@example.com", "threshold": 220}},
    {"id": "CHECKOUT-1023", "title": "Checkout scenario 1023", "data": {"sku": "SKU1023", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1023@example.com", "threshold": 230}},
    {"id": "CHECKOUT-1024", "title": "Checkout scenario 1024", "data": {"sku": "SKU1024", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1024@example.com", "threshold": 240}},
    {"id": "CHECKOUT-1025", "title": "Checkout scenario 1025", "data": {"sku": "SKU1025", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1025@example.com", "threshold": 250}},
    {"id": "CHECKOUT-1026", "title": "Checkout scenario 1026", "data": {"sku": "SKU1026", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1026@example.com", "threshold": 260}},
    {"id": "CHECKOUT-1027", "title": "Checkout scenario 1027", "data": {"sku": "SKU1027", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1027@example.com", "threshold": 270}},
    {"id": "CHECKOUT-1028", "title": "Checkout scenario 1028", "data": {"sku": "SKU1028", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1028@example.com", "threshold": 280}},
    {"id": "CHECKOUT-1029", "title": "Checkout scenario 1029", "data": {"sku": "SKU1029", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1029@example.com", "threshold": 290}},
    {"id": "CHECKOUT-1030", "title": "Checkout scenario 1030", "data": {"sku": "SKU1030", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1030@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
