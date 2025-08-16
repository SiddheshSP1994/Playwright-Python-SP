import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-2811", "title": "Analytics scenario 2811", "data": {"sku": "SKU2811", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2811@example.com", "threshold": 110}},
    {"id": "ANALYTICS-2812", "title": "Analytics scenario 2812", "data": {"sku": "SKU2812", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2812@example.com", "threshold": 120}},
    {"id": "ANALYTICS-2813", "title": "Analytics scenario 2813", "data": {"sku": "SKU2813", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2813@example.com", "threshold": 130}},
    {"id": "ANALYTICS-2814", "title": "Analytics scenario 2814", "data": {"sku": "SKU2814", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2814@example.com", "threshold": 140}},
    {"id": "ANALYTICS-2815", "title": "Analytics scenario 2815", "data": {"sku": "SKU2815", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2815@example.com", "threshold": 150}},
    {"id": "ANALYTICS-2816", "title": "Analytics scenario 2816", "data": {"sku": "SKU2816", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2816@example.com", "threshold": 160}},
    {"id": "ANALYTICS-2817", "title": "Analytics scenario 2817", "data": {"sku": "SKU2817", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2817@example.com", "threshold": 170}},
    {"id": "ANALYTICS-2818", "title": "Analytics scenario 2818", "data": {"sku": "SKU2818", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2818@example.com", "threshold": 180}},
    {"id": "ANALYTICS-2819", "title": "Analytics scenario 2819", "data": {"sku": "SKU2819", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2819@example.com", "threshold": 190}},
    {"id": "ANALYTICS-2820", "title": "Analytics scenario 2820", "data": {"sku": "SKU2820", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2820@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
