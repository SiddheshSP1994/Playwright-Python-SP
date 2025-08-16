import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-0691", "title": "Payments scenario 691", "data": {"sku": "SKU691", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user691@example.com", "threshold": 910}},
    {"id": "PAYMENTS-0692", "title": "Payments scenario 692", "data": {"sku": "SKU692", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user692@example.com", "threshold": 920}},
    {"id": "PAYMENTS-0693", "title": "Payments scenario 693", "data": {"sku": "SKU693", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user693@example.com", "threshold": 930}},
    {"id": "PAYMENTS-0694", "title": "Payments scenario 694", "data": {"sku": "SKU694", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user694@example.com", "threshold": 940}},
    {"id": "PAYMENTS-0695", "title": "Payments scenario 695", "data": {"sku": "SKU695", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user695@example.com", "threshold": 950}},
    {"id": "PAYMENTS-0696", "title": "Payments scenario 696", "data": {"sku": "SKU696", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user696@example.com", "threshold": 960}},
    {"id": "PAYMENTS-0697", "title": "Payments scenario 697", "data": {"sku": "SKU697", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user697@example.com", "threshold": 970}},
    {"id": "PAYMENTS-0698", "title": "Payments scenario 698", "data": {"sku": "SKU698", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user698@example.com", "threshold": 980}},
    {"id": "PAYMENTS-0699", "title": "Payments scenario 699", "data": {"sku": "SKU699", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user699@example.com", "threshold": 990}},
    {"id": "PAYMENTS-0700", "title": "Payments scenario 700", "data": {"sku": "SKU700", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user700@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
