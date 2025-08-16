import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-4611", "title": "Analytics scenario 4611", "data": {"sku": "SKU4611", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4611@example.com", "threshold": 110}},
    {"id": "ANALYTICS-4612", "title": "Analytics scenario 4612", "data": {"sku": "SKU4612", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4612@example.com", "threshold": 120}},
    {"id": "ANALYTICS-4613", "title": "Analytics scenario 4613", "data": {"sku": "SKU4613", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4613@example.com", "threshold": 130}},
    {"id": "ANALYTICS-4614", "title": "Analytics scenario 4614", "data": {"sku": "SKU4614", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4614@example.com", "threshold": 140}},
    {"id": "ANALYTICS-4615", "title": "Analytics scenario 4615", "data": {"sku": "SKU4615", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4615@example.com", "threshold": 150}},
    {"id": "ANALYTICS-4616", "title": "Analytics scenario 4616", "data": {"sku": "SKU4616", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4616@example.com", "threshold": 160}},
    {"id": "ANALYTICS-4617", "title": "Analytics scenario 4617", "data": {"sku": "SKU4617", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4617@example.com", "threshold": 170}},
    {"id": "ANALYTICS-4618", "title": "Analytics scenario 4618", "data": {"sku": "SKU4618", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4618@example.com", "threshold": 180}},
    {"id": "ANALYTICS-4619", "title": "Analytics scenario 4619", "data": {"sku": "SKU4619", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4619@example.com", "threshold": 190}},
    {"id": "ANALYTICS-4620", "title": "Analytics scenario 4620", "data": {"sku": "SKU4620", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4620@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
