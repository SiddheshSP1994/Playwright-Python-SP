import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-2861", "title": "Email scenario 2861", "data": {"sku": "SKU2861", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2861@example.com", "threshold": 610}},
    {"id": "EMAIL-2862", "title": "Email scenario 2862", "data": {"sku": "SKU2862", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2862@example.com", "threshold": 620}},
    {"id": "EMAIL-2863", "title": "Email scenario 2863", "data": {"sku": "SKU2863", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2863@example.com", "threshold": 630}},
    {"id": "EMAIL-2864", "title": "Email scenario 2864", "data": {"sku": "SKU2864", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2864@example.com", "threshold": 640}},
    {"id": "EMAIL-2865", "title": "Email scenario 2865", "data": {"sku": "SKU2865", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2865@example.com", "threshold": 650}},
    {"id": "EMAIL-2866", "title": "Email scenario 2866", "data": {"sku": "SKU2866", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2866@example.com", "threshold": 660}},
    {"id": "EMAIL-2867", "title": "Email scenario 2867", "data": {"sku": "SKU2867", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2867@example.com", "threshold": 670}},
    {"id": "EMAIL-2868", "title": "Email scenario 2868", "data": {"sku": "SKU2868", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2868@example.com", "threshold": 680}},
    {"id": "EMAIL-2869", "title": "Email scenario 2869", "data": {"sku": "SKU2869", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2869@example.com", "threshold": 690}},
    {"id": "EMAIL-2870", "title": "Email scenario 2870", "data": {"sku": "SKU2870", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2870@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
