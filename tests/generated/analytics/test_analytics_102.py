import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-6111", "title": "Analytics scenario 6111", "data": {"sku": "SKU6111", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6111@example.com", "threshold": 110}},
    {"id": "ANALYTICS-6112", "title": "Analytics scenario 6112", "data": {"sku": "SKU6112", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6112@example.com", "threshold": 120}},
    {"id": "ANALYTICS-6113", "title": "Analytics scenario 6113", "data": {"sku": "SKU6113", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6113@example.com", "threshold": 130}},
    {"id": "ANALYTICS-6114", "title": "Analytics scenario 6114", "data": {"sku": "SKU6114", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6114@example.com", "threshold": 140}},
    {"id": "ANALYTICS-6115", "title": "Analytics scenario 6115", "data": {"sku": "SKU6115", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6115@example.com", "threshold": 150}},
    {"id": "ANALYTICS-6116", "title": "Analytics scenario 6116", "data": {"sku": "SKU6116", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6116@example.com", "threshold": 160}},
    {"id": "ANALYTICS-6117", "title": "Analytics scenario 6117", "data": {"sku": "SKU6117", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6117@example.com", "threshold": 170}},
    {"id": "ANALYTICS-6118", "title": "Analytics scenario 6118", "data": {"sku": "SKU6118", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6118@example.com", "threshold": 180}},
    {"id": "ANALYTICS-6119", "title": "Analytics scenario 6119", "data": {"sku": "SKU6119", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6119@example.com", "threshold": 190}},
    {"id": "ANALYTICS-6120", "title": "Analytics scenario 6120", "data": {"sku": "SKU6120", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6120@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
