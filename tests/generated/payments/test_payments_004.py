import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-0211", "title": "Payments scenario 211", "data": {"sku": "SKU211", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user211@example.com", "threshold": 110}},
    {"id": "PAYMENTS-0212", "title": "Payments scenario 212", "data": {"sku": "SKU212", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user212@example.com", "threshold": 120}},
    {"id": "PAYMENTS-0213", "title": "Payments scenario 213", "data": {"sku": "SKU213", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user213@example.com", "threshold": 130}},
    {"id": "PAYMENTS-0214", "title": "Payments scenario 214", "data": {"sku": "SKU214", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user214@example.com", "threshold": 140}},
    {"id": "PAYMENTS-0215", "title": "Payments scenario 215", "data": {"sku": "SKU215", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user215@example.com", "threshold": 150}},
    {"id": "PAYMENTS-0216", "title": "Payments scenario 216", "data": {"sku": "SKU216", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user216@example.com", "threshold": 160}},
    {"id": "PAYMENTS-0217", "title": "Payments scenario 217", "data": {"sku": "SKU217", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user217@example.com", "threshold": 170}},
    {"id": "PAYMENTS-0218", "title": "Payments scenario 218", "data": {"sku": "SKU218", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user218@example.com", "threshold": 180}},
    {"id": "PAYMENTS-0219", "title": "Payments scenario 219", "data": {"sku": "SKU219", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user219@example.com", "threshold": 190}},
    {"id": "PAYMENTS-0220", "title": "Payments scenario 220", "data": {"sku": "SKU220", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user220@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
