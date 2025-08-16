import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-3031", "title": "Payments scenario 3031", "data": {"sku": "SKU3031", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3031@example.com", "threshold": 310}},
    {"id": "PAYMENTS-3032", "title": "Payments scenario 3032", "data": {"sku": "SKU3032", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3032@example.com", "threshold": 320}},
    {"id": "PAYMENTS-3033", "title": "Payments scenario 3033", "data": {"sku": "SKU3033", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3033@example.com", "threshold": 330}},
    {"id": "PAYMENTS-3034", "title": "Payments scenario 3034", "data": {"sku": "SKU3034", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3034@example.com", "threshold": 340}},
    {"id": "PAYMENTS-3035", "title": "Payments scenario 3035", "data": {"sku": "SKU3035", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3035@example.com", "threshold": 350}},
    {"id": "PAYMENTS-3036", "title": "Payments scenario 3036", "data": {"sku": "SKU3036", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3036@example.com", "threshold": 360}},
    {"id": "PAYMENTS-3037", "title": "Payments scenario 3037", "data": {"sku": "SKU3037", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3037@example.com", "threshold": 370}},
    {"id": "PAYMENTS-3038", "title": "Payments scenario 3038", "data": {"sku": "SKU3038", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3038@example.com", "threshold": 380}},
    {"id": "PAYMENTS-3039", "title": "Payments scenario 3039", "data": {"sku": "SKU3039", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3039@example.com", "threshold": 390}},
    {"id": "PAYMENTS-3040", "title": "Payments scenario 3040", "data": {"sku": "SKU3040", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3040@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
