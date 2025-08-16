import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-2521", "title": "Checkout scenario 2521", "data": {"sku": "SKU2521", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2521@example.com", "threshold": 210}},
    {"id": "CHECKOUT-2522", "title": "Checkout scenario 2522", "data": {"sku": "SKU2522", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2522@example.com", "threshold": 220}},
    {"id": "CHECKOUT-2523", "title": "Checkout scenario 2523", "data": {"sku": "SKU2523", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2523@example.com", "threshold": 230}},
    {"id": "CHECKOUT-2524", "title": "Checkout scenario 2524", "data": {"sku": "SKU2524", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2524@example.com", "threshold": 240}},
    {"id": "CHECKOUT-2525", "title": "Checkout scenario 2525", "data": {"sku": "SKU2525", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2525@example.com", "threshold": 250}},
    {"id": "CHECKOUT-2526", "title": "Checkout scenario 2526", "data": {"sku": "SKU2526", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2526@example.com", "threshold": 260}},
    {"id": "CHECKOUT-2527", "title": "Checkout scenario 2527", "data": {"sku": "SKU2527", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2527@example.com", "threshold": 270}},
    {"id": "CHECKOUT-2528", "title": "Checkout scenario 2528", "data": {"sku": "SKU2528", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2528@example.com", "threshold": 280}},
    {"id": "CHECKOUT-2529", "title": "Checkout scenario 2529", "data": {"sku": "SKU2529", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2529@example.com", "threshold": 290}},
    {"id": "CHECKOUT-2530", "title": "Checkout scenario 2530", "data": {"sku": "SKU2530", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2530@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
