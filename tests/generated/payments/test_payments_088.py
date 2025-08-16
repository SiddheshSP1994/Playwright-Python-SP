import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-5251", "title": "Payments scenario 5251", "data": {"sku": "SKU5251", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5251@example.com", "threshold": 510}},
    {"id": "PAYMENTS-5252", "title": "Payments scenario 5252", "data": {"sku": "SKU5252", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5252@example.com", "threshold": 520}},
    {"id": "PAYMENTS-5253", "title": "Payments scenario 5253", "data": {"sku": "SKU5253", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5253@example.com", "threshold": 530}},
    {"id": "PAYMENTS-5254", "title": "Payments scenario 5254", "data": {"sku": "SKU5254", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5254@example.com", "threshold": 540}},
    {"id": "PAYMENTS-5255", "title": "Payments scenario 5255", "data": {"sku": "SKU5255", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5255@example.com", "threshold": 550}},
    {"id": "PAYMENTS-5256", "title": "Payments scenario 5256", "data": {"sku": "SKU5256", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5256@example.com", "threshold": 560}},
    {"id": "PAYMENTS-5257", "title": "Payments scenario 5257", "data": {"sku": "SKU5257", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5257@example.com", "threshold": 570}},
    {"id": "PAYMENTS-5258", "title": "Payments scenario 5258", "data": {"sku": "SKU5258", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5258@example.com", "threshold": 580}},
    {"id": "PAYMENTS-5259", "title": "Payments scenario 5259", "data": {"sku": "SKU5259", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5259@example.com", "threshold": 590}},
    {"id": "PAYMENTS-5260", "title": "Payments scenario 5260", "data": {"sku": "SKU5260", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5260@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
