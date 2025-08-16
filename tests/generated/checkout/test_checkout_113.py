import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-6721", "title": "Checkout scenario 6721", "data": {"sku": "SKU6721", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6721@example.com", "threshold": 210}},
    {"id": "CHECKOUT-6722", "title": "Checkout scenario 6722", "data": {"sku": "SKU6722", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6722@example.com", "threshold": 220}},
    {"id": "CHECKOUT-6723", "title": "Checkout scenario 6723", "data": {"sku": "SKU6723", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6723@example.com", "threshold": 230}},
    {"id": "CHECKOUT-6724", "title": "Checkout scenario 6724", "data": {"sku": "SKU6724", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6724@example.com", "threshold": 240}},
    {"id": "CHECKOUT-6725", "title": "Checkout scenario 6725", "data": {"sku": "SKU6725", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6725@example.com", "threshold": 250}},
    {"id": "CHECKOUT-6726", "title": "Checkout scenario 6726", "data": {"sku": "SKU6726", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6726@example.com", "threshold": 260}},
    {"id": "CHECKOUT-6727", "title": "Checkout scenario 6727", "data": {"sku": "SKU6727", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6727@example.com", "threshold": 270}},
    {"id": "CHECKOUT-6728", "title": "Checkout scenario 6728", "data": {"sku": "SKU6728", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6728@example.com", "threshold": 280}},
    {"id": "CHECKOUT-6729", "title": "Checkout scenario 6729", "data": {"sku": "SKU6729", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6729@example.com", "threshold": 290}},
    {"id": "CHECKOUT-6730", "title": "Checkout scenario 6730", "data": {"sku": "SKU6730", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6730@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
