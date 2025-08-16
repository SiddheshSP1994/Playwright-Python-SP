import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-8861", "title": "Email scenario 8861", "data": {"sku": "SKU8861", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8861@example.com", "threshold": 610}},
    {"id": "EMAIL-8862", "title": "Email scenario 8862", "data": {"sku": "SKU8862", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8862@example.com", "threshold": 620}},
    {"id": "EMAIL-8863", "title": "Email scenario 8863", "data": {"sku": "SKU8863", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8863@example.com", "threshold": 630}},
    {"id": "EMAIL-8864", "title": "Email scenario 8864", "data": {"sku": "SKU8864", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8864@example.com", "threshold": 640}},
    {"id": "EMAIL-8865", "title": "Email scenario 8865", "data": {"sku": "SKU8865", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8865@example.com", "threshold": 650}},
    {"id": "EMAIL-8866", "title": "Email scenario 8866", "data": {"sku": "SKU8866", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8866@example.com", "threshold": 660}},
    {"id": "EMAIL-8867", "title": "Email scenario 8867", "data": {"sku": "SKU8867", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8867@example.com", "threshold": 670}},
    {"id": "EMAIL-8868", "title": "Email scenario 8868", "data": {"sku": "SKU8868", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8868@example.com", "threshold": 680}},
    {"id": "EMAIL-8869", "title": "Email scenario 8869", "data": {"sku": "SKU8869", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8869@example.com", "threshold": 690}},
    {"id": "EMAIL-8870", "title": "Email scenario 8870", "data": {"sku": "SKU8870", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8870@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
