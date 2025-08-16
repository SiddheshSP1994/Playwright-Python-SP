import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-9721", "title": "Checkout scenario 9721", "data": {"sku": "SKU9721", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9721@example.com", "threshold": 210}},
    {"id": "CHECKOUT-9722", "title": "Checkout scenario 9722", "data": {"sku": "SKU9722", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9722@example.com", "threshold": 220}},
    {"id": "CHECKOUT-9723", "title": "Checkout scenario 9723", "data": {"sku": "SKU9723", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9723@example.com", "threshold": 230}},
    {"id": "CHECKOUT-9724", "title": "Checkout scenario 9724", "data": {"sku": "SKU9724", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9724@example.com", "threshold": 240}},
    {"id": "CHECKOUT-9725", "title": "Checkout scenario 9725", "data": {"sku": "SKU9725", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9725@example.com", "threshold": 250}},
    {"id": "CHECKOUT-9726", "title": "Checkout scenario 9726", "data": {"sku": "SKU9726", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9726@example.com", "threshold": 260}},
    {"id": "CHECKOUT-9727", "title": "Checkout scenario 9727", "data": {"sku": "SKU9727", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9727@example.com", "threshold": 270}},
    {"id": "CHECKOUT-9728", "title": "Checkout scenario 9728", "data": {"sku": "SKU9728", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9728@example.com", "threshold": 280}},
    {"id": "CHECKOUT-9729", "title": "Checkout scenario 9729", "data": {"sku": "SKU9729", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9729@example.com", "threshold": 290}},
    {"id": "CHECKOUT-9730", "title": "Checkout scenario 9730", "data": {"sku": "SKU9730", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9730@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
