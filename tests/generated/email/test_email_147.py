import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-8801", "title": "Email scenario 8801", "data": {"sku": "SKU8801", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8801@example.com", "threshold": 10}},
    {"id": "EMAIL-8802", "title": "Email scenario 8802", "data": {"sku": "SKU8802", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8802@example.com", "threshold": 20}},
    {"id": "EMAIL-8803", "title": "Email scenario 8803", "data": {"sku": "SKU8803", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8803@example.com", "threshold": 30}},
    {"id": "EMAIL-8804", "title": "Email scenario 8804", "data": {"sku": "SKU8804", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8804@example.com", "threshold": 40}},
    {"id": "EMAIL-8805", "title": "Email scenario 8805", "data": {"sku": "SKU8805", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8805@example.com", "threshold": 50}},
    {"id": "EMAIL-8806", "title": "Email scenario 8806", "data": {"sku": "SKU8806", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8806@example.com", "threshold": 60}},
    {"id": "EMAIL-8807", "title": "Email scenario 8807", "data": {"sku": "SKU8807", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8807@example.com", "threshold": 70}},
    {"id": "EMAIL-8808", "title": "Email scenario 8808", "data": {"sku": "SKU8808", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8808@example.com", "threshold": 80}},
    {"id": "EMAIL-8809", "title": "Email scenario 8809", "data": {"sku": "SKU8809", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8809@example.com", "threshold": 90}},
    {"id": "EMAIL-8810", "title": "Email scenario 8810", "data": {"sku": "SKU8810", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8810@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
