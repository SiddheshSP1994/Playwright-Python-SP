import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-6471", "title": "Analytics scenario 6471", "data": {"sku": "SKU6471", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6471@example.com", "threshold": 710}},
    {"id": "ANALYTICS-6472", "title": "Analytics scenario 6472", "data": {"sku": "SKU6472", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6472@example.com", "threshold": 720}},
    {"id": "ANALYTICS-6473", "title": "Analytics scenario 6473", "data": {"sku": "SKU6473", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6473@example.com", "threshold": 730}},
    {"id": "ANALYTICS-6474", "title": "Analytics scenario 6474", "data": {"sku": "SKU6474", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6474@example.com", "threshold": 740}},
    {"id": "ANALYTICS-6475", "title": "Analytics scenario 6475", "data": {"sku": "SKU6475", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6475@example.com", "threshold": 750}},
    {"id": "ANALYTICS-6476", "title": "Analytics scenario 6476", "data": {"sku": "SKU6476", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6476@example.com", "threshold": 760}},
    {"id": "ANALYTICS-6477", "title": "Analytics scenario 6477", "data": {"sku": "SKU6477", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6477@example.com", "threshold": 770}},
    {"id": "ANALYTICS-6478", "title": "Analytics scenario 6478", "data": {"sku": "SKU6478", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6478@example.com", "threshold": 780}},
    {"id": "ANALYTICS-6479", "title": "Analytics scenario 6479", "data": {"sku": "SKU6479", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6479@example.com", "threshold": 790}},
    {"id": "ANALYTICS-6480", "title": "Analytics scenario 6480", "data": {"sku": "SKU6480", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6480@example.com", "threshold": 800}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
