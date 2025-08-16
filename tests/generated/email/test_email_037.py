import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-2201", "title": "Email scenario 2201", "data": {"sku": "SKU2201", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2201@example.com", "threshold": 10}},
    {"id": "EMAIL-2202", "title": "Email scenario 2202", "data": {"sku": "SKU2202", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2202@example.com", "threshold": 20}},
    {"id": "EMAIL-2203", "title": "Email scenario 2203", "data": {"sku": "SKU2203", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2203@example.com", "threshold": 30}},
    {"id": "EMAIL-2204", "title": "Email scenario 2204", "data": {"sku": "SKU2204", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2204@example.com", "threshold": 40}},
    {"id": "EMAIL-2205", "title": "Email scenario 2205", "data": {"sku": "SKU2205", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2205@example.com", "threshold": 50}},
    {"id": "EMAIL-2206", "title": "Email scenario 2206", "data": {"sku": "SKU2206", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2206@example.com", "threshold": 60}},
    {"id": "EMAIL-2207", "title": "Email scenario 2207", "data": {"sku": "SKU2207", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2207@example.com", "threshold": 70}},
    {"id": "EMAIL-2208", "title": "Email scenario 2208", "data": {"sku": "SKU2208", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2208@example.com", "threshold": 80}},
    {"id": "EMAIL-2209", "title": "Email scenario 2209", "data": {"sku": "SKU2209", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2209@example.com", "threshold": 90}},
    {"id": "EMAIL-2210", "title": "Email scenario 2210", "data": {"sku": "SKU2210", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2210@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
