import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-4001", "title": "Email scenario 4001", "data": {"sku": "SKU4001", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4001@example.com", "threshold": 10}},
    {"id": "EMAIL-4002", "title": "Email scenario 4002", "data": {"sku": "SKU4002", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4002@example.com", "threshold": 20}},
    {"id": "EMAIL-4003", "title": "Email scenario 4003", "data": {"sku": "SKU4003", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4003@example.com", "threshold": 30}},
    {"id": "EMAIL-4004", "title": "Email scenario 4004", "data": {"sku": "SKU4004", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4004@example.com", "threshold": 40}},
    {"id": "EMAIL-4005", "title": "Email scenario 4005", "data": {"sku": "SKU4005", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4005@example.com", "threshold": 50}},
    {"id": "EMAIL-4006", "title": "Email scenario 4006", "data": {"sku": "SKU4006", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4006@example.com", "threshold": 60}},
    {"id": "EMAIL-4007", "title": "Email scenario 4007", "data": {"sku": "SKU4007", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4007@example.com", "threshold": 70}},
    {"id": "EMAIL-4008", "title": "Email scenario 4008", "data": {"sku": "SKU4008", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4008@example.com", "threshold": 80}},
    {"id": "EMAIL-4009", "title": "Email scenario 4009", "data": {"sku": "SKU4009", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4009@example.com", "threshold": 90}},
    {"id": "EMAIL-4010", "title": "Email scenario 4010", "data": {"sku": "SKU4010", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4010@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
