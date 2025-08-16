import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-4891", "title": "Payments scenario 4891", "data": {"sku": "SKU4891", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4891@example.com", "threshold": 910}},
    {"id": "PAYMENTS-4892", "title": "Payments scenario 4892", "data": {"sku": "SKU4892", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4892@example.com", "threshold": 920}},
    {"id": "PAYMENTS-4893", "title": "Payments scenario 4893", "data": {"sku": "SKU4893", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4893@example.com", "threshold": 930}},
    {"id": "PAYMENTS-4894", "title": "Payments scenario 4894", "data": {"sku": "SKU4894", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4894@example.com", "threshold": 940}},
    {"id": "PAYMENTS-4895", "title": "Payments scenario 4895", "data": {"sku": "SKU4895", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4895@example.com", "threshold": 950}},
    {"id": "PAYMENTS-4896", "title": "Payments scenario 4896", "data": {"sku": "SKU4896", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4896@example.com", "threshold": 960}},
    {"id": "PAYMENTS-4897", "title": "Payments scenario 4897", "data": {"sku": "SKU4897", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4897@example.com", "threshold": 970}},
    {"id": "PAYMENTS-4898", "title": "Payments scenario 4898", "data": {"sku": "SKU4898", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4898@example.com", "threshold": 980}},
    {"id": "PAYMENTS-4899", "title": "Payments scenario 4899", "data": {"sku": "SKU4899", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4899@example.com", "threshold": 990}},
    {"id": "PAYMENTS-4900", "title": "Payments scenario 4900", "data": {"sku": "SKU4900", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4900@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
