import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-7961", "title": "Email scenario 7961", "data": {"sku": "SKU7961", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7961@example.com", "threshold": 610}},
    {"id": "EMAIL-7962", "title": "Email scenario 7962", "data": {"sku": "SKU7962", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7962@example.com", "threshold": 620}},
    {"id": "EMAIL-7963", "title": "Email scenario 7963", "data": {"sku": "SKU7963", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7963@example.com", "threshold": 630}},
    {"id": "EMAIL-7964", "title": "Email scenario 7964", "data": {"sku": "SKU7964", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7964@example.com", "threshold": 640}},
    {"id": "EMAIL-7965", "title": "Email scenario 7965", "data": {"sku": "SKU7965", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7965@example.com", "threshold": 650}},
    {"id": "EMAIL-7966", "title": "Email scenario 7966", "data": {"sku": "SKU7966", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7966@example.com", "threshold": 660}},
    {"id": "EMAIL-7967", "title": "Email scenario 7967", "data": {"sku": "SKU7967", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7967@example.com", "threshold": 670}},
    {"id": "EMAIL-7968", "title": "Email scenario 7968", "data": {"sku": "SKU7968", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7968@example.com", "threshold": 680}},
    {"id": "EMAIL-7969", "title": "Email scenario 7969", "data": {"sku": "SKU7969", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7969@example.com", "threshold": 690}},
    {"id": "EMAIL-7970", "title": "Email scenario 7970", "data": {"sku": "SKU7970", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7970@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
