import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-4301", "title": "Email scenario 4301", "data": {"sku": "SKU4301", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4301@example.com", "threshold": 10}},
    {"id": "EMAIL-4302", "title": "Email scenario 4302", "data": {"sku": "SKU4302", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4302@example.com", "threshold": 20}},
    {"id": "EMAIL-4303", "title": "Email scenario 4303", "data": {"sku": "SKU4303", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4303@example.com", "threshold": 30}},
    {"id": "EMAIL-4304", "title": "Email scenario 4304", "data": {"sku": "SKU4304", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4304@example.com", "threshold": 40}},
    {"id": "EMAIL-4305", "title": "Email scenario 4305", "data": {"sku": "SKU4305", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4305@example.com", "threshold": 50}},
    {"id": "EMAIL-4306", "title": "Email scenario 4306", "data": {"sku": "SKU4306", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4306@example.com", "threshold": 60}},
    {"id": "EMAIL-4307", "title": "Email scenario 4307", "data": {"sku": "SKU4307", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4307@example.com", "threshold": 70}},
    {"id": "EMAIL-4308", "title": "Email scenario 4308", "data": {"sku": "SKU4308", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4308@example.com", "threshold": 80}},
    {"id": "EMAIL-4309", "title": "Email scenario 4309", "data": {"sku": "SKU4309", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4309@example.com", "threshold": 90}},
    {"id": "EMAIL-4310", "title": "Email scenario 4310", "data": {"sku": "SKU4310", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4310@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
