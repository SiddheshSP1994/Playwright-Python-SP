import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-7621", "title": "Checkout scenario 7621", "data": {"sku": "SKU7621", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7621@example.com", "threshold": 210}},
    {"id": "CHECKOUT-7622", "title": "Checkout scenario 7622", "data": {"sku": "SKU7622", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7622@example.com", "threshold": 220}},
    {"id": "CHECKOUT-7623", "title": "Checkout scenario 7623", "data": {"sku": "SKU7623", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7623@example.com", "threshold": 230}},
    {"id": "CHECKOUT-7624", "title": "Checkout scenario 7624", "data": {"sku": "SKU7624", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7624@example.com", "threshold": 240}},
    {"id": "CHECKOUT-7625", "title": "Checkout scenario 7625", "data": {"sku": "SKU7625", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7625@example.com", "threshold": 250}},
    {"id": "CHECKOUT-7626", "title": "Checkout scenario 7626", "data": {"sku": "SKU7626", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7626@example.com", "threshold": 260}},
    {"id": "CHECKOUT-7627", "title": "Checkout scenario 7627", "data": {"sku": "SKU7627", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7627@example.com", "threshold": 270}},
    {"id": "CHECKOUT-7628", "title": "Checkout scenario 7628", "data": {"sku": "SKU7628", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7628@example.com", "threshold": 280}},
    {"id": "CHECKOUT-7629", "title": "Checkout scenario 7629", "data": {"sku": "SKU7629", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7629@example.com", "threshold": 290}},
    {"id": "CHECKOUT-7630", "title": "Checkout scenario 7630", "data": {"sku": "SKU7630", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7630@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
