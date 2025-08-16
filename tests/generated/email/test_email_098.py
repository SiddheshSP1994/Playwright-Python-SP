import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-5861", "title": "Email scenario 5861", "data": {"sku": "SKU5861", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5861@example.com", "threshold": 610}},
    {"id": "EMAIL-5862", "title": "Email scenario 5862", "data": {"sku": "SKU5862", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5862@example.com", "threshold": 620}},
    {"id": "EMAIL-5863", "title": "Email scenario 5863", "data": {"sku": "SKU5863", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5863@example.com", "threshold": 630}},
    {"id": "EMAIL-5864", "title": "Email scenario 5864", "data": {"sku": "SKU5864", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5864@example.com", "threshold": 640}},
    {"id": "EMAIL-5865", "title": "Email scenario 5865", "data": {"sku": "SKU5865", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5865@example.com", "threshold": 650}},
    {"id": "EMAIL-5866", "title": "Email scenario 5866", "data": {"sku": "SKU5866", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5866@example.com", "threshold": 660}},
    {"id": "EMAIL-5867", "title": "Email scenario 5867", "data": {"sku": "SKU5867", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5867@example.com", "threshold": 670}},
    {"id": "EMAIL-5868", "title": "Email scenario 5868", "data": {"sku": "SKU5868", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5868@example.com", "threshold": 680}},
    {"id": "EMAIL-5869", "title": "Email scenario 5869", "data": {"sku": "SKU5869", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5869@example.com", "threshold": 690}},
    {"id": "EMAIL-5870", "title": "Email scenario 5870", "data": {"sku": "SKU5870", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5870@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
