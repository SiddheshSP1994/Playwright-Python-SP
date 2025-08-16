import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-5201", "title": "Email scenario 5201", "data": {"sku": "SKU5201", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5201@example.com", "threshold": 10}},
    {"id": "EMAIL-5202", "title": "Email scenario 5202", "data": {"sku": "SKU5202", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5202@example.com", "threshold": 20}},
    {"id": "EMAIL-5203", "title": "Email scenario 5203", "data": {"sku": "SKU5203", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5203@example.com", "threshold": 30}},
    {"id": "EMAIL-5204", "title": "Email scenario 5204", "data": {"sku": "SKU5204", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5204@example.com", "threshold": 40}},
    {"id": "EMAIL-5205", "title": "Email scenario 5205", "data": {"sku": "SKU5205", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5205@example.com", "threshold": 50}},
    {"id": "EMAIL-5206", "title": "Email scenario 5206", "data": {"sku": "SKU5206", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5206@example.com", "threshold": 60}},
    {"id": "EMAIL-5207", "title": "Email scenario 5207", "data": {"sku": "SKU5207", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5207@example.com", "threshold": 70}},
    {"id": "EMAIL-5208", "title": "Email scenario 5208", "data": {"sku": "SKU5208", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5208@example.com", "threshold": 80}},
    {"id": "EMAIL-5209", "title": "Email scenario 5209", "data": {"sku": "SKU5209", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5209@example.com", "threshold": 90}},
    {"id": "EMAIL-5210", "title": "Email scenario 5210", "data": {"sku": "SKU5210", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5210@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
