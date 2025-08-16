import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-0631", "title": "Payments scenario 631", "data": {"sku": "SKU631", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user631@example.com", "threshold": 310}},
    {"id": "PAYMENTS-0632", "title": "Payments scenario 632", "data": {"sku": "SKU632", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user632@example.com", "threshold": 320}},
    {"id": "PAYMENTS-0633", "title": "Payments scenario 633", "data": {"sku": "SKU633", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user633@example.com", "threshold": 330}},
    {"id": "PAYMENTS-0634", "title": "Payments scenario 634", "data": {"sku": "SKU634", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user634@example.com", "threshold": 340}},
    {"id": "PAYMENTS-0635", "title": "Payments scenario 635", "data": {"sku": "SKU635", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user635@example.com", "threshold": 350}},
    {"id": "PAYMENTS-0636", "title": "Payments scenario 636", "data": {"sku": "SKU636", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user636@example.com", "threshold": 360}},
    {"id": "PAYMENTS-0637", "title": "Payments scenario 637", "data": {"sku": "SKU637", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user637@example.com", "threshold": 370}},
    {"id": "PAYMENTS-0638", "title": "Payments scenario 638", "data": {"sku": "SKU638", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user638@example.com", "threshold": 380}},
    {"id": "PAYMENTS-0639", "title": "Payments scenario 639", "data": {"sku": "SKU639", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user639@example.com", "threshold": 390}},
    {"id": "PAYMENTS-0640", "title": "Payments scenario 640", "data": {"sku": "SKU640", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user640@example.com", "threshold": 400}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
