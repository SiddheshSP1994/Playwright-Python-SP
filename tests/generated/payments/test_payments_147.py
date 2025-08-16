import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-8791", "title": "Payments scenario 8791", "data": {"sku": "SKU8791", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8791@example.com", "threshold": 910}},
    {"id": "PAYMENTS-8792", "title": "Payments scenario 8792", "data": {"sku": "SKU8792", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8792@example.com", "threshold": 920}},
    {"id": "PAYMENTS-8793", "title": "Payments scenario 8793", "data": {"sku": "SKU8793", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8793@example.com", "threshold": 930}},
    {"id": "PAYMENTS-8794", "title": "Payments scenario 8794", "data": {"sku": "SKU8794", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8794@example.com", "threshold": 940}},
    {"id": "PAYMENTS-8795", "title": "Payments scenario 8795", "data": {"sku": "SKU8795", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8795@example.com", "threshold": 950}},
    {"id": "PAYMENTS-8796", "title": "Payments scenario 8796", "data": {"sku": "SKU8796", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8796@example.com", "threshold": 960}},
    {"id": "PAYMENTS-8797", "title": "Payments scenario 8797", "data": {"sku": "SKU8797", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8797@example.com", "threshold": 970}},
    {"id": "PAYMENTS-8798", "title": "Payments scenario 8798", "data": {"sku": "SKU8798", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8798@example.com", "threshold": 980}},
    {"id": "PAYMENTS-8799", "title": "Payments scenario 8799", "data": {"sku": "SKU8799", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8799@example.com", "threshold": 990}},
    {"id": "PAYMENTS-8800", "title": "Payments scenario 8800", "data": {"sku": "SKU8800", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8800@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
