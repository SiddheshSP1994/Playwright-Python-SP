import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-0091", "title": "Payments scenario 91", "data": {"sku": "SKU91", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user91@example.com", "threshold": 910}},
    {"id": "PAYMENTS-0092", "title": "Payments scenario 92", "data": {"sku": "SKU92", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user92@example.com", "threshold": 920}},
    {"id": "PAYMENTS-0093", "title": "Payments scenario 93", "data": {"sku": "SKU93", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user93@example.com", "threshold": 930}},
    {"id": "PAYMENTS-0094", "title": "Payments scenario 94", "data": {"sku": "SKU94", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user94@example.com", "threshold": 940}},
    {"id": "PAYMENTS-0095", "title": "Payments scenario 95", "data": {"sku": "SKU95", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user95@example.com", "threshold": 950}},
    {"id": "PAYMENTS-0096", "title": "Payments scenario 96", "data": {"sku": "SKU96", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user96@example.com", "threshold": 960}},
    {"id": "PAYMENTS-0097", "title": "Payments scenario 97", "data": {"sku": "SKU97", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user97@example.com", "threshold": 970}},
    {"id": "PAYMENTS-0098", "title": "Payments scenario 98", "data": {"sku": "SKU98", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user98@example.com", "threshold": 980}},
    {"id": "PAYMENTS-0099", "title": "Payments scenario 99", "data": {"sku": "SKU99", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user99@example.com", "threshold": 990}},
    {"id": "PAYMENTS-0100", "title": "Payments scenario 100", "data": {"sku": "SKU100", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user100@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
