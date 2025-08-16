import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-0511", "title": "Payments scenario 511", "data": {"sku": "SKU511", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user511@example.com", "threshold": 110}},
    {"id": "PAYMENTS-0512", "title": "Payments scenario 512", "data": {"sku": "SKU512", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user512@example.com", "threshold": 120}},
    {"id": "PAYMENTS-0513", "title": "Payments scenario 513", "data": {"sku": "SKU513", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user513@example.com", "threshold": 130}},
    {"id": "PAYMENTS-0514", "title": "Payments scenario 514", "data": {"sku": "SKU514", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user514@example.com", "threshold": 140}},
    {"id": "PAYMENTS-0515", "title": "Payments scenario 515", "data": {"sku": "SKU515", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user515@example.com", "threshold": 150}},
    {"id": "PAYMENTS-0516", "title": "Payments scenario 516", "data": {"sku": "SKU516", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user516@example.com", "threshold": 160}},
    {"id": "PAYMENTS-0517", "title": "Payments scenario 517", "data": {"sku": "SKU517", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user517@example.com", "threshold": 170}},
    {"id": "PAYMENTS-0518", "title": "Payments scenario 518", "data": {"sku": "SKU518", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user518@example.com", "threshold": 180}},
    {"id": "PAYMENTS-0519", "title": "Payments scenario 519", "data": {"sku": "SKU519", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user519@example.com", "threshold": 190}},
    {"id": "PAYMENTS-0520", "title": "Payments scenario 520", "data": {"sku": "SKU520", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user520@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
