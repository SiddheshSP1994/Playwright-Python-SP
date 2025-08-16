import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-8551", "title": "Payments scenario 8551", "data": {"sku": "SKU8551", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8551@example.com", "threshold": 510}},
    {"id": "PAYMENTS-8552", "title": "Payments scenario 8552", "data": {"sku": "SKU8552", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8552@example.com", "threshold": 520}},
    {"id": "PAYMENTS-8553", "title": "Payments scenario 8553", "data": {"sku": "SKU8553", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8553@example.com", "threshold": 530}},
    {"id": "PAYMENTS-8554", "title": "Payments scenario 8554", "data": {"sku": "SKU8554", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8554@example.com", "threshold": 540}},
    {"id": "PAYMENTS-8555", "title": "Payments scenario 8555", "data": {"sku": "SKU8555", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8555@example.com", "threshold": 550}},
    {"id": "PAYMENTS-8556", "title": "Payments scenario 8556", "data": {"sku": "SKU8556", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8556@example.com", "threshold": 560}},
    {"id": "PAYMENTS-8557", "title": "Payments scenario 8557", "data": {"sku": "SKU8557", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8557@example.com", "threshold": 570}},
    {"id": "PAYMENTS-8558", "title": "Payments scenario 8558", "data": {"sku": "SKU8558", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8558@example.com", "threshold": 580}},
    {"id": "PAYMENTS-8559", "title": "Payments scenario 8559", "data": {"sku": "SKU8559", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8559@example.com", "threshold": 590}},
    {"id": "PAYMENTS-8560", "title": "Payments scenario 8560", "data": {"sku": "SKU8560", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8560@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
