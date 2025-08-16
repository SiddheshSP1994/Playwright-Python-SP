import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-0571", "title": "Payments scenario 571", "data": {"sku": "SKU571", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user571@example.com", "threshold": 710}},
    {"id": "PAYMENTS-0572", "title": "Payments scenario 572", "data": {"sku": "SKU572", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user572@example.com", "threshold": 720}},
    {"id": "PAYMENTS-0573", "title": "Payments scenario 573", "data": {"sku": "SKU573", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user573@example.com", "threshold": 730}},
    {"id": "PAYMENTS-0574", "title": "Payments scenario 574", "data": {"sku": "SKU574", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user574@example.com", "threshold": 740}},
    {"id": "PAYMENTS-0575", "title": "Payments scenario 575", "data": {"sku": "SKU575", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user575@example.com", "threshold": 750}},
    {"id": "PAYMENTS-0576", "title": "Payments scenario 576", "data": {"sku": "SKU576", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user576@example.com", "threshold": 760}},
    {"id": "PAYMENTS-0577", "title": "Payments scenario 577", "data": {"sku": "SKU577", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user577@example.com", "threshold": 770}},
    {"id": "PAYMENTS-0578", "title": "Payments scenario 578", "data": {"sku": "SKU578", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user578@example.com", "threshold": 780}},
    {"id": "PAYMENTS-0579", "title": "Payments scenario 579", "data": {"sku": "SKU579", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user579@example.com", "threshold": 790}},
    {"id": "PAYMENTS-0580", "title": "Payments scenario 580", "data": {"sku": "SKU580", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user580@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
