import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-4421", "title": "Email scenario 4421", "data": {"sku": "SKU4421", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4421@example.com", "threshold": 210}},
    {"id": "EMAIL-4422", "title": "Email scenario 4422", "data": {"sku": "SKU4422", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4422@example.com", "threshold": 220}},
    {"id": "EMAIL-4423", "title": "Email scenario 4423", "data": {"sku": "SKU4423", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4423@example.com", "threshold": 230}},
    {"id": "EMAIL-4424", "title": "Email scenario 4424", "data": {"sku": "SKU4424", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4424@example.com", "threshold": 240}},
    {"id": "EMAIL-4425", "title": "Email scenario 4425", "data": {"sku": "SKU4425", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4425@example.com", "threshold": 250}},
    {"id": "EMAIL-4426", "title": "Email scenario 4426", "data": {"sku": "SKU4426", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4426@example.com", "threshold": 260}},
    {"id": "EMAIL-4427", "title": "Email scenario 4427", "data": {"sku": "SKU4427", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4427@example.com", "threshold": 270}},
    {"id": "EMAIL-4428", "title": "Email scenario 4428", "data": {"sku": "SKU4428", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4428@example.com", "threshold": 280}},
    {"id": "EMAIL-4429", "title": "Email scenario 4429", "data": {"sku": "SKU4429", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4429@example.com", "threshold": 290}},
    {"id": "EMAIL-4430", "title": "Email scenario 4430", "data": {"sku": "SKU4430", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4430@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
