import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-1011", "title": "Analytics scenario 1011", "data": {"sku": "SKU1011", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1011@example.com", "threshold": 110}},
    {"id": "ANALYTICS-1012", "title": "Analytics scenario 1012", "data": {"sku": "SKU1012", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1012@example.com", "threshold": 120}},
    {"id": "ANALYTICS-1013", "title": "Analytics scenario 1013", "data": {"sku": "SKU1013", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1013@example.com", "threshold": 130}},
    {"id": "ANALYTICS-1014", "title": "Analytics scenario 1014", "data": {"sku": "SKU1014", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1014@example.com", "threshold": 140}},
    {"id": "ANALYTICS-1015", "title": "Analytics scenario 1015", "data": {"sku": "SKU1015", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1015@example.com", "threshold": 150}},
    {"id": "ANALYTICS-1016", "title": "Analytics scenario 1016", "data": {"sku": "SKU1016", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1016@example.com", "threshold": 160}},
    {"id": "ANALYTICS-1017", "title": "Analytics scenario 1017", "data": {"sku": "SKU1017", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1017@example.com", "threshold": 170}},
    {"id": "ANALYTICS-1018", "title": "Analytics scenario 1018", "data": {"sku": "SKU1018", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1018@example.com", "threshold": 180}},
    {"id": "ANALYTICS-1019", "title": "Analytics scenario 1019", "data": {"sku": "SKU1019", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1019@example.com", "threshold": 190}},
    {"id": "ANALYTICS-1020", "title": "Analytics scenario 1020", "data": {"sku": "SKU1020", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1020@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
