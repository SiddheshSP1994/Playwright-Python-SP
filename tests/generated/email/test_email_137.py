import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-8201", "title": "Email scenario 8201", "data": {"sku": "SKU8201", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8201@example.com", "threshold": 10}},
    {"id": "EMAIL-8202", "title": "Email scenario 8202", "data": {"sku": "SKU8202", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8202@example.com", "threshold": 20}},
    {"id": "EMAIL-8203", "title": "Email scenario 8203", "data": {"sku": "SKU8203", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8203@example.com", "threshold": 30}},
    {"id": "EMAIL-8204", "title": "Email scenario 8204", "data": {"sku": "SKU8204", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8204@example.com", "threshold": 40}},
    {"id": "EMAIL-8205", "title": "Email scenario 8205", "data": {"sku": "SKU8205", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8205@example.com", "threshold": 50}},
    {"id": "EMAIL-8206", "title": "Email scenario 8206", "data": {"sku": "SKU8206", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8206@example.com", "threshold": 60}},
    {"id": "EMAIL-8207", "title": "Email scenario 8207", "data": {"sku": "SKU8207", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8207@example.com", "threshold": 70}},
    {"id": "EMAIL-8208", "title": "Email scenario 8208", "data": {"sku": "SKU8208", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8208@example.com", "threshold": 80}},
    {"id": "EMAIL-8209", "title": "Email scenario 8209", "data": {"sku": "SKU8209", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8209@example.com", "threshold": 90}},
    {"id": "EMAIL-8210", "title": "Email scenario 8210", "data": {"sku": "SKU8210", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8210@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
