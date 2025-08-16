import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-1001", "title": "Email scenario 1001", "data": {"sku": "SKU1001", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1001@example.com", "threshold": 10}},
    {"id": "EMAIL-1002", "title": "Email scenario 1002", "data": {"sku": "SKU1002", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1002@example.com", "threshold": 20}},
    {"id": "EMAIL-1003", "title": "Email scenario 1003", "data": {"sku": "SKU1003", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1003@example.com", "threshold": 30}},
    {"id": "EMAIL-1004", "title": "Email scenario 1004", "data": {"sku": "SKU1004", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1004@example.com", "threshold": 40}},
    {"id": "EMAIL-1005", "title": "Email scenario 1005", "data": {"sku": "SKU1005", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1005@example.com", "threshold": 50}},
    {"id": "EMAIL-1006", "title": "Email scenario 1006", "data": {"sku": "SKU1006", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1006@example.com", "threshold": 60}},
    {"id": "EMAIL-1007", "title": "Email scenario 1007", "data": {"sku": "SKU1007", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1007@example.com", "threshold": 70}},
    {"id": "EMAIL-1008", "title": "Email scenario 1008", "data": {"sku": "SKU1008", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1008@example.com", "threshold": 80}},
    {"id": "EMAIL-1009", "title": "Email scenario 1009", "data": {"sku": "SKU1009", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1009@example.com", "threshold": 90}},
    {"id": "EMAIL-1010", "title": "Email scenario 1010", "data": {"sku": "SKU1010", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1010@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
