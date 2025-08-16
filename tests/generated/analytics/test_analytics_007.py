import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-0411", "title": "Analytics scenario 411", "data": {"sku": "SKU411", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user411@example.com", "threshold": 110}},
    {"id": "ANALYTICS-0412", "title": "Analytics scenario 412", "data": {"sku": "SKU412", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user412@example.com", "threshold": 120}},
    {"id": "ANALYTICS-0413", "title": "Analytics scenario 413", "data": {"sku": "SKU413", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user413@example.com", "threshold": 130}},
    {"id": "ANALYTICS-0414", "title": "Analytics scenario 414", "data": {"sku": "SKU414", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user414@example.com", "threshold": 140}},
    {"id": "ANALYTICS-0415", "title": "Analytics scenario 415", "data": {"sku": "SKU415", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user415@example.com", "threshold": 150}},
    {"id": "ANALYTICS-0416", "title": "Analytics scenario 416", "data": {"sku": "SKU416", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user416@example.com", "threshold": 160}},
    {"id": "ANALYTICS-0417", "title": "Analytics scenario 417", "data": {"sku": "SKU417", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user417@example.com", "threshold": 170}},
    {"id": "ANALYTICS-0418", "title": "Analytics scenario 418", "data": {"sku": "SKU418", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user418@example.com", "threshold": 180}},
    {"id": "ANALYTICS-0419", "title": "Analytics scenario 419", "data": {"sku": "SKU419", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user419@example.com", "threshold": 190}},
    {"id": "ANALYTICS-0420", "title": "Analytics scenario 420", "data": {"sku": "SKU420", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user420@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
