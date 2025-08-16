import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-9661", "title": "Checkout scenario 9661", "data": {"sku": "SKU9661", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9661@example.com", "threshold": 610}},
    {"id": "CHECKOUT-9662", "title": "Checkout scenario 9662", "data": {"sku": "SKU9662", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9662@example.com", "threshold": 620}},
    {"id": "CHECKOUT-9663", "title": "Checkout scenario 9663", "data": {"sku": "SKU9663", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9663@example.com", "threshold": 630}},
    {"id": "CHECKOUT-9664", "title": "Checkout scenario 9664", "data": {"sku": "SKU9664", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9664@example.com", "threshold": 640}},
    {"id": "CHECKOUT-9665", "title": "Checkout scenario 9665", "data": {"sku": "SKU9665", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9665@example.com", "threshold": 650}},
    {"id": "CHECKOUT-9666", "title": "Checkout scenario 9666", "data": {"sku": "SKU9666", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9666@example.com", "threshold": 660}},
    {"id": "CHECKOUT-9667", "title": "Checkout scenario 9667", "data": {"sku": "SKU9667", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9667@example.com", "threshold": 670}},
    {"id": "CHECKOUT-9668", "title": "Checkout scenario 9668", "data": {"sku": "SKU9668", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9668@example.com", "threshold": 680}},
    {"id": "CHECKOUT-9669", "title": "Checkout scenario 9669", "data": {"sku": "SKU9669", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9669@example.com", "threshold": 690}},
    {"id": "CHECKOUT-9670", "title": "Checkout scenario 9670", "data": {"sku": "SKU9670", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9670@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
