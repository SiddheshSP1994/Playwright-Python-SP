import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-6421", "title": "Checkout scenario 6421", "data": {"sku": "SKU6421", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6421@example.com", "threshold": 210}},
    {"id": "CHECKOUT-6422", "title": "Checkout scenario 6422", "data": {"sku": "SKU6422", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6422@example.com", "threshold": 220}},
    {"id": "CHECKOUT-6423", "title": "Checkout scenario 6423", "data": {"sku": "SKU6423", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6423@example.com", "threshold": 230}},
    {"id": "CHECKOUT-6424", "title": "Checkout scenario 6424", "data": {"sku": "SKU6424", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6424@example.com", "threshold": 240}},
    {"id": "CHECKOUT-6425", "title": "Checkout scenario 6425", "data": {"sku": "SKU6425", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6425@example.com", "threshold": 250}},
    {"id": "CHECKOUT-6426", "title": "Checkout scenario 6426", "data": {"sku": "SKU6426", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6426@example.com", "threshold": 260}},
    {"id": "CHECKOUT-6427", "title": "Checkout scenario 6427", "data": {"sku": "SKU6427", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6427@example.com", "threshold": 270}},
    {"id": "CHECKOUT-6428", "title": "Checkout scenario 6428", "data": {"sku": "SKU6428", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6428@example.com", "threshold": 280}},
    {"id": "CHECKOUT-6429", "title": "Checkout scenario 6429", "data": {"sku": "SKU6429", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6429@example.com", "threshold": 290}},
    {"id": "CHECKOUT-6430", "title": "Checkout scenario 6430", "data": {"sku": "SKU6430", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6430@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
