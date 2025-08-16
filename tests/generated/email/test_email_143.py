import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-8561", "title": "Email scenario 8561", "data": {"sku": "SKU8561", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8561@example.com", "threshold": 610}},
    {"id": "EMAIL-8562", "title": "Email scenario 8562", "data": {"sku": "SKU8562", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8562@example.com", "threshold": 620}},
    {"id": "EMAIL-8563", "title": "Email scenario 8563", "data": {"sku": "SKU8563", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8563@example.com", "threshold": 630}},
    {"id": "EMAIL-8564", "title": "Email scenario 8564", "data": {"sku": "SKU8564", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8564@example.com", "threshold": 640}},
    {"id": "EMAIL-8565", "title": "Email scenario 8565", "data": {"sku": "SKU8565", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8565@example.com", "threshold": 650}},
    {"id": "EMAIL-8566", "title": "Email scenario 8566", "data": {"sku": "SKU8566", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8566@example.com", "threshold": 660}},
    {"id": "EMAIL-8567", "title": "Email scenario 8567", "data": {"sku": "SKU8567", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8567@example.com", "threshold": 670}},
    {"id": "EMAIL-8568", "title": "Email scenario 8568", "data": {"sku": "SKU8568", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8568@example.com", "threshold": 680}},
    {"id": "EMAIL-8569", "title": "Email scenario 8569", "data": {"sku": "SKU8569", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8569@example.com", "threshold": 690}},
    {"id": "EMAIL-8570", "title": "Email scenario 8570", "data": {"sku": "SKU8570", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8570@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
