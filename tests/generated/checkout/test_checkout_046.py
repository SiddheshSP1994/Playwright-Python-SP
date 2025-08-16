import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-2701", "title": "Checkout scenario 2701", "data": {"sku": "SKU2701", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2701@example.com", "threshold": 10}},
    {"id": "CHECKOUT-2702", "title": "Checkout scenario 2702", "data": {"sku": "SKU2702", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2702@example.com", "threshold": 20}},
    {"id": "CHECKOUT-2703", "title": "Checkout scenario 2703", "data": {"sku": "SKU2703", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2703@example.com", "threshold": 30}},
    {"id": "CHECKOUT-2704", "title": "Checkout scenario 2704", "data": {"sku": "SKU2704", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2704@example.com", "threshold": 40}},
    {"id": "CHECKOUT-2705", "title": "Checkout scenario 2705", "data": {"sku": "SKU2705", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2705@example.com", "threshold": 50}},
    {"id": "CHECKOUT-2706", "title": "Checkout scenario 2706", "data": {"sku": "SKU2706", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2706@example.com", "threshold": 60}},
    {"id": "CHECKOUT-2707", "title": "Checkout scenario 2707", "data": {"sku": "SKU2707", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2707@example.com", "threshold": 70}},
    {"id": "CHECKOUT-2708", "title": "Checkout scenario 2708", "data": {"sku": "SKU2708", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2708@example.com", "threshold": 80}},
    {"id": "CHECKOUT-2709", "title": "Checkout scenario 2709", "data": {"sku": "SKU2709", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2709@example.com", "threshold": 90}},
    {"id": "CHECKOUT-2710", "title": "Checkout scenario 2710", "data": {"sku": "SKU2710", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2710@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
