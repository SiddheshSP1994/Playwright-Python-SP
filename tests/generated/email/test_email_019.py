import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-1121", "title": "Email scenario 1121", "data": {"sku": "SKU1121", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1121@example.com", "threshold": 210}},
    {"id": "EMAIL-1122", "title": "Email scenario 1122", "data": {"sku": "SKU1122", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1122@example.com", "threshold": 220}},
    {"id": "EMAIL-1123", "title": "Email scenario 1123", "data": {"sku": "SKU1123", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1123@example.com", "threshold": 230}},
    {"id": "EMAIL-1124", "title": "Email scenario 1124", "data": {"sku": "SKU1124", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1124@example.com", "threshold": 240}},
    {"id": "EMAIL-1125", "title": "Email scenario 1125", "data": {"sku": "SKU1125", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1125@example.com", "threshold": 250}},
    {"id": "EMAIL-1126", "title": "Email scenario 1126", "data": {"sku": "SKU1126", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1126@example.com", "threshold": 260}},
    {"id": "EMAIL-1127", "title": "Email scenario 1127", "data": {"sku": "SKU1127", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1127@example.com", "threshold": 270}},
    {"id": "EMAIL-1128", "title": "Email scenario 1128", "data": {"sku": "SKU1128", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1128@example.com", "threshold": 280}},
    {"id": "EMAIL-1129", "title": "Email scenario 1129", "data": {"sku": "SKU1129", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1129@example.com", "threshold": 290}},
    {"id": "EMAIL-1130", "title": "Email scenario 1130", "data": {"sku": "SKU1130", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1130@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
