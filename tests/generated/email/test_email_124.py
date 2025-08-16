import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-7421", "title": "Email scenario 7421", "data": {"sku": "SKU7421", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7421@example.com", "threshold": 210}},
    {"id": "EMAIL-7422", "title": "Email scenario 7422", "data": {"sku": "SKU7422", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7422@example.com", "threshold": 220}},
    {"id": "EMAIL-7423", "title": "Email scenario 7423", "data": {"sku": "SKU7423", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7423@example.com", "threshold": 230}},
    {"id": "EMAIL-7424", "title": "Email scenario 7424", "data": {"sku": "SKU7424", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7424@example.com", "threshold": 240}},
    {"id": "EMAIL-7425", "title": "Email scenario 7425", "data": {"sku": "SKU7425", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7425@example.com", "threshold": 250}},
    {"id": "EMAIL-7426", "title": "Email scenario 7426", "data": {"sku": "SKU7426", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7426@example.com", "threshold": 260}},
    {"id": "EMAIL-7427", "title": "Email scenario 7427", "data": {"sku": "SKU7427", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7427@example.com", "threshold": 270}},
    {"id": "EMAIL-7428", "title": "Email scenario 7428", "data": {"sku": "SKU7428", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7428@example.com", "threshold": 280}},
    {"id": "EMAIL-7429", "title": "Email scenario 7429", "data": {"sku": "SKU7429", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7429@example.com", "threshold": 290}},
    {"id": "EMAIL-7430", "title": "Email scenario 7430", "data": {"sku": "SKU7430", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7430@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
