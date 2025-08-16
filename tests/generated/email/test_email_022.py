import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-1301", "title": "Email scenario 1301", "data": {"sku": "SKU1301", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1301@example.com", "threshold": 10}},
    {"id": "EMAIL-1302", "title": "Email scenario 1302", "data": {"sku": "SKU1302", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1302@example.com", "threshold": 20}},
    {"id": "EMAIL-1303", "title": "Email scenario 1303", "data": {"sku": "SKU1303", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1303@example.com", "threshold": 30}},
    {"id": "EMAIL-1304", "title": "Email scenario 1304", "data": {"sku": "SKU1304", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1304@example.com", "threshold": 40}},
    {"id": "EMAIL-1305", "title": "Email scenario 1305", "data": {"sku": "SKU1305", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1305@example.com", "threshold": 50}},
    {"id": "EMAIL-1306", "title": "Email scenario 1306", "data": {"sku": "SKU1306", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1306@example.com", "threshold": 60}},
    {"id": "EMAIL-1307", "title": "Email scenario 1307", "data": {"sku": "SKU1307", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1307@example.com", "threshold": 70}},
    {"id": "EMAIL-1308", "title": "Email scenario 1308", "data": {"sku": "SKU1308", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1308@example.com", "threshold": 80}},
    {"id": "EMAIL-1309", "title": "Email scenario 1309", "data": {"sku": "SKU1309", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1309@example.com", "threshold": 90}},
    {"id": "EMAIL-1310", "title": "Email scenario 1310", "data": {"sku": "SKU1310", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1310@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
