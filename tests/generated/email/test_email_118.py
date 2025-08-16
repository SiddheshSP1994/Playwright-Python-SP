import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-7061", "title": "Email scenario 7061", "data": {"sku": "SKU7061", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7061@example.com", "threshold": 610}},
    {"id": "EMAIL-7062", "title": "Email scenario 7062", "data": {"sku": "SKU7062", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7062@example.com", "threshold": 620}},
    {"id": "EMAIL-7063", "title": "Email scenario 7063", "data": {"sku": "SKU7063", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7063@example.com", "threshold": 630}},
    {"id": "EMAIL-7064", "title": "Email scenario 7064", "data": {"sku": "SKU7064", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7064@example.com", "threshold": 640}},
    {"id": "EMAIL-7065", "title": "Email scenario 7065", "data": {"sku": "SKU7065", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7065@example.com", "threshold": 650}},
    {"id": "EMAIL-7066", "title": "Email scenario 7066", "data": {"sku": "SKU7066", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7066@example.com", "threshold": 660}},
    {"id": "EMAIL-7067", "title": "Email scenario 7067", "data": {"sku": "SKU7067", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7067@example.com", "threshold": 670}},
    {"id": "EMAIL-7068", "title": "Email scenario 7068", "data": {"sku": "SKU7068", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7068@example.com", "threshold": 680}},
    {"id": "EMAIL-7069", "title": "Email scenario 7069", "data": {"sku": "SKU7069", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7069@example.com", "threshold": 690}},
    {"id": "EMAIL-7070", "title": "Email scenario 7070", "data": {"sku": "SKU7070", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7070@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
