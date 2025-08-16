import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-4911", "title": "Analytics scenario 4911", "data": {"sku": "SKU4911", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4911@example.com", "threshold": 110}},
    {"id": "ANALYTICS-4912", "title": "Analytics scenario 4912", "data": {"sku": "SKU4912", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4912@example.com", "threshold": 120}},
    {"id": "ANALYTICS-4913", "title": "Analytics scenario 4913", "data": {"sku": "SKU4913", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4913@example.com", "threshold": 130}},
    {"id": "ANALYTICS-4914", "title": "Analytics scenario 4914", "data": {"sku": "SKU4914", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4914@example.com", "threshold": 140}},
    {"id": "ANALYTICS-4915", "title": "Analytics scenario 4915", "data": {"sku": "SKU4915", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4915@example.com", "threshold": 150}},
    {"id": "ANALYTICS-4916", "title": "Analytics scenario 4916", "data": {"sku": "SKU4916", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4916@example.com", "threshold": 160}},
    {"id": "ANALYTICS-4917", "title": "Analytics scenario 4917", "data": {"sku": "SKU4917", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4917@example.com", "threshold": 170}},
    {"id": "ANALYTICS-4918", "title": "Analytics scenario 4918", "data": {"sku": "SKU4918", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4918@example.com", "threshold": 180}},
    {"id": "ANALYTICS-4919", "title": "Analytics scenario 4919", "data": {"sku": "SKU4919", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4919@example.com", "threshold": 190}},
    {"id": "ANALYTICS-4920", "title": "Analytics scenario 4920", "data": {"sku": "SKU4920", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4920@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
