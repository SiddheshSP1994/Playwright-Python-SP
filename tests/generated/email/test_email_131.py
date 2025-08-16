import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-7841", "title": "Email scenario 7841", "data": {"sku": "SKU7841", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7841@example.com", "threshold": 410}},
    {"id": "EMAIL-7842", "title": "Email scenario 7842", "data": {"sku": "SKU7842", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7842@example.com", "threshold": 420}},
    {"id": "EMAIL-7843", "title": "Email scenario 7843", "data": {"sku": "SKU7843", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7843@example.com", "threshold": 430}},
    {"id": "EMAIL-7844", "title": "Email scenario 7844", "data": {"sku": "SKU7844", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7844@example.com", "threshold": 440}},
    {"id": "EMAIL-7845", "title": "Email scenario 7845", "data": {"sku": "SKU7845", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7845@example.com", "threshold": 450}},
    {"id": "EMAIL-7846", "title": "Email scenario 7846", "data": {"sku": "SKU7846", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7846@example.com", "threshold": 460}},
    {"id": "EMAIL-7847", "title": "Email scenario 7847", "data": {"sku": "SKU7847", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7847@example.com", "threshold": 470}},
    {"id": "EMAIL-7848", "title": "Email scenario 7848", "data": {"sku": "SKU7848", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7848@example.com", "threshold": 480}},
    {"id": "EMAIL-7849", "title": "Email scenario 7849", "data": {"sku": "SKU7849", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7849@example.com", "threshold": 490}},
    {"id": "EMAIL-7850", "title": "Email scenario 7850", "data": {"sku": "SKU7850", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7850@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
