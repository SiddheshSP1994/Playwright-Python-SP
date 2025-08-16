import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-8521", "title": "Checkout scenario 8521", "data": {"sku": "SKU8521", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8521@example.com", "threshold": 210}},
    {"id": "CHECKOUT-8522", "title": "Checkout scenario 8522", "data": {"sku": "SKU8522", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8522@example.com", "threshold": 220}},
    {"id": "CHECKOUT-8523", "title": "Checkout scenario 8523", "data": {"sku": "SKU8523", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8523@example.com", "threshold": 230}},
    {"id": "CHECKOUT-8524", "title": "Checkout scenario 8524", "data": {"sku": "SKU8524", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8524@example.com", "threshold": 240}},
    {"id": "CHECKOUT-8525", "title": "Checkout scenario 8525", "data": {"sku": "SKU8525", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8525@example.com", "threshold": 250}},
    {"id": "CHECKOUT-8526", "title": "Checkout scenario 8526", "data": {"sku": "SKU8526", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8526@example.com", "threshold": 260}},
    {"id": "CHECKOUT-8527", "title": "Checkout scenario 8527", "data": {"sku": "SKU8527", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8527@example.com", "threshold": 270}},
    {"id": "CHECKOUT-8528", "title": "Checkout scenario 8528", "data": {"sku": "SKU8528", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8528@example.com", "threshold": 280}},
    {"id": "CHECKOUT-8529", "title": "Checkout scenario 8529", "data": {"sku": "SKU8529", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8529@example.com", "threshold": 290}},
    {"id": "CHECKOUT-8530", "title": "Checkout scenario 8530", "data": {"sku": "SKU8530", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8530@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
