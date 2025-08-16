import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-1131", "title": "Analytics scenario 1131", "data": {"sku": "SKU1131", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1131@example.com", "threshold": 310}},
    {"id": "ANALYTICS-1132", "title": "Analytics scenario 1132", "data": {"sku": "SKU1132", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1132@example.com", "threshold": 320}},
    {"id": "ANALYTICS-1133", "title": "Analytics scenario 1133", "data": {"sku": "SKU1133", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1133@example.com", "threshold": 330}},
    {"id": "ANALYTICS-1134", "title": "Analytics scenario 1134", "data": {"sku": "SKU1134", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1134@example.com", "threshold": 340}},
    {"id": "ANALYTICS-1135", "title": "Analytics scenario 1135", "data": {"sku": "SKU1135", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1135@example.com", "threshold": 350}},
    {"id": "ANALYTICS-1136", "title": "Analytics scenario 1136", "data": {"sku": "SKU1136", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1136@example.com", "threshold": 360}},
    {"id": "ANALYTICS-1137", "title": "Analytics scenario 1137", "data": {"sku": "SKU1137", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1137@example.com", "threshold": 370}},
    {"id": "ANALYTICS-1138", "title": "Analytics scenario 1138", "data": {"sku": "SKU1138", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1138@example.com", "threshold": 380}},
    {"id": "ANALYTICS-1139", "title": "Analytics scenario 1139", "data": {"sku": "SKU1139", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1139@example.com", "threshold": 390}},
    {"id": "ANALYTICS-1140", "title": "Analytics scenario 1140", "data": {"sku": "SKU1140", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1140@example.com", "threshold": 400}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
