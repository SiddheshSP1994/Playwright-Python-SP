import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-8461", "title": "Checkout scenario 8461", "data": {"sku": "SKU8461", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8461@example.com", "threshold": 610}},
    {"id": "CHECKOUT-8462", "title": "Checkout scenario 8462", "data": {"sku": "SKU8462", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8462@example.com", "threshold": 620}},
    {"id": "CHECKOUT-8463", "title": "Checkout scenario 8463", "data": {"sku": "SKU8463", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8463@example.com", "threshold": 630}},
    {"id": "CHECKOUT-8464", "title": "Checkout scenario 8464", "data": {"sku": "SKU8464", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8464@example.com", "threshold": 640}},
    {"id": "CHECKOUT-8465", "title": "Checkout scenario 8465", "data": {"sku": "SKU8465", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8465@example.com", "threshold": 650}},
    {"id": "CHECKOUT-8466", "title": "Checkout scenario 8466", "data": {"sku": "SKU8466", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8466@example.com", "threshold": 660}},
    {"id": "CHECKOUT-8467", "title": "Checkout scenario 8467", "data": {"sku": "SKU8467", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8467@example.com", "threshold": 670}},
    {"id": "CHECKOUT-8468", "title": "Checkout scenario 8468", "data": {"sku": "SKU8468", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8468@example.com", "threshold": 680}},
    {"id": "CHECKOUT-8469", "title": "Checkout scenario 8469", "data": {"sku": "SKU8469", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8469@example.com", "threshold": 690}},
    {"id": "CHECKOUT-8470", "title": "Checkout scenario 8470", "data": {"sku": "SKU8470", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8470@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
