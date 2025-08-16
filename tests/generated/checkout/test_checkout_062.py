import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-3661", "title": "Checkout scenario 3661", "data": {"sku": "SKU3661", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3661@example.com", "threshold": 610}},
    {"id": "CHECKOUT-3662", "title": "Checkout scenario 3662", "data": {"sku": "SKU3662", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3662@example.com", "threshold": 620}},
    {"id": "CHECKOUT-3663", "title": "Checkout scenario 3663", "data": {"sku": "SKU3663", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3663@example.com", "threshold": 630}},
    {"id": "CHECKOUT-3664", "title": "Checkout scenario 3664", "data": {"sku": "SKU3664", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3664@example.com", "threshold": 640}},
    {"id": "CHECKOUT-3665", "title": "Checkout scenario 3665", "data": {"sku": "SKU3665", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3665@example.com", "threshold": 650}},
    {"id": "CHECKOUT-3666", "title": "Checkout scenario 3666", "data": {"sku": "SKU3666", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3666@example.com", "threshold": 660}},
    {"id": "CHECKOUT-3667", "title": "Checkout scenario 3667", "data": {"sku": "SKU3667", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3667@example.com", "threshold": 670}},
    {"id": "CHECKOUT-3668", "title": "Checkout scenario 3668", "data": {"sku": "SKU3668", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3668@example.com", "threshold": 680}},
    {"id": "CHECKOUT-3669", "title": "Checkout scenario 3669", "data": {"sku": "SKU3669", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3669@example.com", "threshold": 690}},
    {"id": "CHECKOUT-3670", "title": "Checkout scenario 3670", "data": {"sku": "SKU3670", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3670@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
