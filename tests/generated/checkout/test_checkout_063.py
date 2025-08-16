import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-3721", "title": "Checkout scenario 3721", "data": {"sku": "SKU3721", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3721@example.com", "threshold": 210}},
    {"id": "CHECKOUT-3722", "title": "Checkout scenario 3722", "data": {"sku": "SKU3722", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3722@example.com", "threshold": 220}},
    {"id": "CHECKOUT-3723", "title": "Checkout scenario 3723", "data": {"sku": "SKU3723", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3723@example.com", "threshold": 230}},
    {"id": "CHECKOUT-3724", "title": "Checkout scenario 3724", "data": {"sku": "SKU3724", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3724@example.com", "threshold": 240}},
    {"id": "CHECKOUT-3725", "title": "Checkout scenario 3725", "data": {"sku": "SKU3725", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3725@example.com", "threshold": 250}},
    {"id": "CHECKOUT-3726", "title": "Checkout scenario 3726", "data": {"sku": "SKU3726", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3726@example.com", "threshold": 260}},
    {"id": "CHECKOUT-3727", "title": "Checkout scenario 3727", "data": {"sku": "SKU3727", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3727@example.com", "threshold": 270}},
    {"id": "CHECKOUT-3728", "title": "Checkout scenario 3728", "data": {"sku": "SKU3728", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3728@example.com", "threshold": 280}},
    {"id": "CHECKOUT-3729", "title": "Checkout scenario 3729", "data": {"sku": "SKU3729", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3729@example.com", "threshold": 290}},
    {"id": "CHECKOUT-3730", "title": "Checkout scenario 3730", "data": {"sku": "SKU3730", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3730@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
