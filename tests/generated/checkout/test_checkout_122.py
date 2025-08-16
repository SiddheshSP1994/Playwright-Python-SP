import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-7261", "title": "Checkout scenario 7261", "data": {"sku": "SKU7261", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7261@example.com", "threshold": 610}},
    {"id": "CHECKOUT-7262", "title": "Checkout scenario 7262", "data": {"sku": "SKU7262", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7262@example.com", "threshold": 620}},
    {"id": "CHECKOUT-7263", "title": "Checkout scenario 7263", "data": {"sku": "SKU7263", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7263@example.com", "threshold": 630}},
    {"id": "CHECKOUT-7264", "title": "Checkout scenario 7264", "data": {"sku": "SKU7264", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7264@example.com", "threshold": 640}},
    {"id": "CHECKOUT-7265", "title": "Checkout scenario 7265", "data": {"sku": "SKU7265", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7265@example.com", "threshold": 650}},
    {"id": "CHECKOUT-7266", "title": "Checkout scenario 7266", "data": {"sku": "SKU7266", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7266@example.com", "threshold": 660}},
    {"id": "CHECKOUT-7267", "title": "Checkout scenario 7267", "data": {"sku": "SKU7267", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7267@example.com", "threshold": 670}},
    {"id": "CHECKOUT-7268", "title": "Checkout scenario 7268", "data": {"sku": "SKU7268", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7268@example.com", "threshold": 680}},
    {"id": "CHECKOUT-7269", "title": "Checkout scenario 7269", "data": {"sku": "SKU7269", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7269@example.com", "threshold": 690}},
    {"id": "CHECKOUT-7270", "title": "Checkout scenario 7270", "data": {"sku": "SKU7270", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7270@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
