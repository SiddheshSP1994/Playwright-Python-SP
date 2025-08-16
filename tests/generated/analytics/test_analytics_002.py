import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-0111", "title": "Analytics scenario 111", "data": {"sku": "SKU111", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user111@example.com", "threshold": 110}},
    {"id": "ANALYTICS-0112", "title": "Analytics scenario 112", "data": {"sku": "SKU112", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user112@example.com", "threshold": 120}},
    {"id": "ANALYTICS-0113", "title": "Analytics scenario 113", "data": {"sku": "SKU113", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user113@example.com", "threshold": 130}},
    {"id": "ANALYTICS-0114", "title": "Analytics scenario 114", "data": {"sku": "SKU114", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user114@example.com", "threshold": 140}},
    {"id": "ANALYTICS-0115", "title": "Analytics scenario 115", "data": {"sku": "SKU115", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user115@example.com", "threshold": 150}},
    {"id": "ANALYTICS-0116", "title": "Analytics scenario 116", "data": {"sku": "SKU116", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user116@example.com", "threshold": 160}},
    {"id": "ANALYTICS-0117", "title": "Analytics scenario 117", "data": {"sku": "SKU117", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user117@example.com", "threshold": 170}},
    {"id": "ANALYTICS-0118", "title": "Analytics scenario 118", "data": {"sku": "SKU118", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user118@example.com", "threshold": 180}},
    {"id": "ANALYTICS-0119", "title": "Analytics scenario 119", "data": {"sku": "SKU119", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user119@example.com", "threshold": 190}},
    {"id": "ANALYTICS-0120", "title": "Analytics scenario 120", "data": {"sku": "SKU120", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user120@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
