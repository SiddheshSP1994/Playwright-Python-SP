import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-1361", "title": "Email scenario 1361", "data": {"sku": "SKU1361", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1361@example.com", "threshold": 610}},
    {"id": "EMAIL-1362", "title": "Email scenario 1362", "data": {"sku": "SKU1362", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1362@example.com", "threshold": 620}},
    {"id": "EMAIL-1363", "title": "Email scenario 1363", "data": {"sku": "SKU1363", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1363@example.com", "threshold": 630}},
    {"id": "EMAIL-1364", "title": "Email scenario 1364", "data": {"sku": "SKU1364", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1364@example.com", "threshold": 640}},
    {"id": "EMAIL-1365", "title": "Email scenario 1365", "data": {"sku": "SKU1365", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1365@example.com", "threshold": 650}},
    {"id": "EMAIL-1366", "title": "Email scenario 1366", "data": {"sku": "SKU1366", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1366@example.com", "threshold": 660}},
    {"id": "EMAIL-1367", "title": "Email scenario 1367", "data": {"sku": "SKU1367", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1367@example.com", "threshold": 670}},
    {"id": "EMAIL-1368", "title": "Email scenario 1368", "data": {"sku": "SKU1368", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1368@example.com", "threshold": 680}},
    {"id": "EMAIL-1369", "title": "Email scenario 1369", "data": {"sku": "SKU1369", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1369@example.com", "threshold": 690}},
    {"id": "EMAIL-1370", "title": "Email scenario 1370", "data": {"sku": "SKU1370", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1370@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
