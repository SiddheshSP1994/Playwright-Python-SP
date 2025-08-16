import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-1601", "title": "Email scenario 1601", "data": {"sku": "SKU1601", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1601@example.com", "threshold": 10}},
    {"id": "EMAIL-1602", "title": "Email scenario 1602", "data": {"sku": "SKU1602", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1602@example.com", "threshold": 20}},
    {"id": "EMAIL-1603", "title": "Email scenario 1603", "data": {"sku": "SKU1603", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1603@example.com", "threshold": 30}},
    {"id": "EMAIL-1604", "title": "Email scenario 1604", "data": {"sku": "SKU1604", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1604@example.com", "threshold": 40}},
    {"id": "EMAIL-1605", "title": "Email scenario 1605", "data": {"sku": "SKU1605", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1605@example.com", "threshold": 50}},
    {"id": "EMAIL-1606", "title": "Email scenario 1606", "data": {"sku": "SKU1606", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1606@example.com", "threshold": 60}},
    {"id": "EMAIL-1607", "title": "Email scenario 1607", "data": {"sku": "SKU1607", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1607@example.com", "threshold": 70}},
    {"id": "EMAIL-1608", "title": "Email scenario 1608", "data": {"sku": "SKU1608", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1608@example.com", "threshold": 80}},
    {"id": "EMAIL-1609", "title": "Email scenario 1609", "data": {"sku": "SKU1609", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1609@example.com", "threshold": 90}},
    {"id": "EMAIL-1610", "title": "Email scenario 1610", "data": {"sku": "SKU1610", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1610@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
