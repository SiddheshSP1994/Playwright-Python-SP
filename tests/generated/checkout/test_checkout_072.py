import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-4261", "title": "Checkout scenario 4261", "data": {"sku": "SKU4261", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4261@example.com", "threshold": 610}},
    {"id": "CHECKOUT-4262", "title": "Checkout scenario 4262", "data": {"sku": "SKU4262", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4262@example.com", "threshold": 620}},
    {"id": "CHECKOUT-4263", "title": "Checkout scenario 4263", "data": {"sku": "SKU4263", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4263@example.com", "threshold": 630}},
    {"id": "CHECKOUT-4264", "title": "Checkout scenario 4264", "data": {"sku": "SKU4264", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4264@example.com", "threshold": 640}},
    {"id": "CHECKOUT-4265", "title": "Checkout scenario 4265", "data": {"sku": "SKU4265", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4265@example.com", "threshold": 650}},
    {"id": "CHECKOUT-4266", "title": "Checkout scenario 4266", "data": {"sku": "SKU4266", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4266@example.com", "threshold": 660}},
    {"id": "CHECKOUT-4267", "title": "Checkout scenario 4267", "data": {"sku": "SKU4267", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4267@example.com", "threshold": 670}},
    {"id": "CHECKOUT-4268", "title": "Checkout scenario 4268", "data": {"sku": "SKU4268", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4268@example.com", "threshold": 680}},
    {"id": "CHECKOUT-4269", "title": "Checkout scenario 4269", "data": {"sku": "SKU4269", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4269@example.com", "threshold": 690}},
    {"id": "CHECKOUT-4270", "title": "Checkout scenario 4270", "data": {"sku": "SKU4270", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4270@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
