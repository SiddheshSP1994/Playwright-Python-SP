import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-5521", "title": "Checkout scenario 5521", "data": {"sku": "SKU5521", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5521@example.com", "threshold": 210}},
    {"id": "CHECKOUT-5522", "title": "Checkout scenario 5522", "data": {"sku": "SKU5522", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5522@example.com", "threshold": 220}},
    {"id": "CHECKOUT-5523", "title": "Checkout scenario 5523", "data": {"sku": "SKU5523", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5523@example.com", "threshold": 230}},
    {"id": "CHECKOUT-5524", "title": "Checkout scenario 5524", "data": {"sku": "SKU5524", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5524@example.com", "threshold": 240}},
    {"id": "CHECKOUT-5525", "title": "Checkout scenario 5525", "data": {"sku": "SKU5525", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5525@example.com", "threshold": 250}},
    {"id": "CHECKOUT-5526", "title": "Checkout scenario 5526", "data": {"sku": "SKU5526", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5526@example.com", "threshold": 260}},
    {"id": "CHECKOUT-5527", "title": "Checkout scenario 5527", "data": {"sku": "SKU5527", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5527@example.com", "threshold": 270}},
    {"id": "CHECKOUT-5528", "title": "Checkout scenario 5528", "data": {"sku": "SKU5528", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5528@example.com", "threshold": 280}},
    {"id": "CHECKOUT-5529", "title": "Checkout scenario 5529", "data": {"sku": "SKU5529", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5529@example.com", "threshold": 290}},
    {"id": "CHECKOUT-5530", "title": "Checkout scenario 5530", "data": {"sku": "SKU5530", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5530@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
