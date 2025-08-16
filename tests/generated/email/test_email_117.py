import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-7001", "title": "Email scenario 7001", "data": {"sku": "SKU7001", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7001@example.com", "threshold": 10}},
    {"id": "EMAIL-7002", "title": "Email scenario 7002", "data": {"sku": "SKU7002", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7002@example.com", "threshold": 20}},
    {"id": "EMAIL-7003", "title": "Email scenario 7003", "data": {"sku": "SKU7003", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7003@example.com", "threshold": 30}},
    {"id": "EMAIL-7004", "title": "Email scenario 7004", "data": {"sku": "SKU7004", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7004@example.com", "threshold": 40}},
    {"id": "EMAIL-7005", "title": "Email scenario 7005", "data": {"sku": "SKU7005", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7005@example.com", "threshold": 50}},
    {"id": "EMAIL-7006", "title": "Email scenario 7006", "data": {"sku": "SKU7006", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7006@example.com", "threshold": 60}},
    {"id": "EMAIL-7007", "title": "Email scenario 7007", "data": {"sku": "SKU7007", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7007@example.com", "threshold": 70}},
    {"id": "EMAIL-7008", "title": "Email scenario 7008", "data": {"sku": "SKU7008", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7008@example.com", "threshold": 80}},
    {"id": "EMAIL-7009", "title": "Email scenario 7009", "data": {"sku": "SKU7009", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7009@example.com", "threshold": 90}},
    {"id": "EMAIL-7010", "title": "Email scenario 7010", "data": {"sku": "SKU7010", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7010@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
