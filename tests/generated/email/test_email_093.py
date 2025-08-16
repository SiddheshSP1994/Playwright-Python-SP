import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-5561", "title": "Email scenario 5561", "data": {"sku": "SKU5561", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5561@example.com", "threshold": 610}},
    {"id": "EMAIL-5562", "title": "Email scenario 5562", "data": {"sku": "SKU5562", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5562@example.com", "threshold": 620}},
    {"id": "EMAIL-5563", "title": "Email scenario 5563", "data": {"sku": "SKU5563", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5563@example.com", "threshold": 630}},
    {"id": "EMAIL-5564", "title": "Email scenario 5564", "data": {"sku": "SKU5564", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5564@example.com", "threshold": 640}},
    {"id": "EMAIL-5565", "title": "Email scenario 5565", "data": {"sku": "SKU5565", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5565@example.com", "threshold": 650}},
    {"id": "EMAIL-5566", "title": "Email scenario 5566", "data": {"sku": "SKU5566", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5566@example.com", "threshold": 660}},
    {"id": "EMAIL-5567", "title": "Email scenario 5567", "data": {"sku": "SKU5567", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5567@example.com", "threshold": 670}},
    {"id": "EMAIL-5568", "title": "Email scenario 5568", "data": {"sku": "SKU5568", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5568@example.com", "threshold": 680}},
    {"id": "EMAIL-5569", "title": "Email scenario 5569", "data": {"sku": "SKU5569", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5569@example.com", "threshold": 690}},
    {"id": "EMAIL-5570", "title": "Email scenario 5570", "data": {"sku": "SKU5570", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5570@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
