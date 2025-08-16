import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-0391", "title": "Payments scenario 391", "data": {"sku": "SKU391", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user391@example.com", "threshold": 910}},
    {"id": "PAYMENTS-0392", "title": "Payments scenario 392", "data": {"sku": "SKU392", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user392@example.com", "threshold": 920}},
    {"id": "PAYMENTS-0393", "title": "Payments scenario 393", "data": {"sku": "SKU393", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user393@example.com", "threshold": 930}},
    {"id": "PAYMENTS-0394", "title": "Payments scenario 394", "data": {"sku": "SKU394", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user394@example.com", "threshold": 940}},
    {"id": "PAYMENTS-0395", "title": "Payments scenario 395", "data": {"sku": "SKU395", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user395@example.com", "threshold": 950}},
    {"id": "PAYMENTS-0396", "title": "Payments scenario 396", "data": {"sku": "SKU396", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user396@example.com", "threshold": 960}},
    {"id": "PAYMENTS-0397", "title": "Payments scenario 397", "data": {"sku": "SKU397", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user397@example.com", "threshold": 970}},
    {"id": "PAYMENTS-0398", "title": "Payments scenario 398", "data": {"sku": "SKU398", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user398@example.com", "threshold": 980}},
    {"id": "PAYMENTS-0399", "title": "Payments scenario 399", "data": {"sku": "SKU399", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user399@example.com", "threshold": 990}},
    {"id": "PAYMENTS-0400", "title": "Payments scenario 400", "data": {"sku": "SKU400", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user400@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
