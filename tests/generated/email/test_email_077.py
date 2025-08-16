import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-4601", "title": "Email scenario 4601", "data": {"sku": "SKU4601", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4601@example.com", "threshold": 10}},
    {"id": "EMAIL-4602", "title": "Email scenario 4602", "data": {"sku": "SKU4602", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4602@example.com", "threshold": 20}},
    {"id": "EMAIL-4603", "title": "Email scenario 4603", "data": {"sku": "SKU4603", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4603@example.com", "threshold": 30}},
    {"id": "EMAIL-4604", "title": "Email scenario 4604", "data": {"sku": "SKU4604", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4604@example.com", "threshold": 40}},
    {"id": "EMAIL-4605", "title": "Email scenario 4605", "data": {"sku": "SKU4605", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4605@example.com", "threshold": 50}},
    {"id": "EMAIL-4606", "title": "Email scenario 4606", "data": {"sku": "SKU4606", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4606@example.com", "threshold": 60}},
    {"id": "EMAIL-4607", "title": "Email scenario 4607", "data": {"sku": "SKU4607", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4607@example.com", "threshold": 70}},
    {"id": "EMAIL-4608", "title": "Email scenario 4608", "data": {"sku": "SKU4608", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4608@example.com", "threshold": 80}},
    {"id": "EMAIL-4609", "title": "Email scenario 4609", "data": {"sku": "SKU4609", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4609@example.com", "threshold": 90}},
    {"id": "EMAIL-4610", "title": "Email scenario 4610", "data": {"sku": "SKU4610", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4610@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
