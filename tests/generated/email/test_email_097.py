import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-5801", "title": "Email scenario 5801", "data": {"sku": "SKU5801", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5801@example.com", "threshold": 10}},
    {"id": "EMAIL-5802", "title": "Email scenario 5802", "data": {"sku": "SKU5802", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5802@example.com", "threshold": 20}},
    {"id": "EMAIL-5803", "title": "Email scenario 5803", "data": {"sku": "SKU5803", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5803@example.com", "threshold": 30}},
    {"id": "EMAIL-5804", "title": "Email scenario 5804", "data": {"sku": "SKU5804", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5804@example.com", "threshold": 40}},
    {"id": "EMAIL-5805", "title": "Email scenario 5805", "data": {"sku": "SKU5805", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5805@example.com", "threshold": 50}},
    {"id": "EMAIL-5806", "title": "Email scenario 5806", "data": {"sku": "SKU5806", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5806@example.com", "threshold": 60}},
    {"id": "EMAIL-5807", "title": "Email scenario 5807", "data": {"sku": "SKU5807", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5807@example.com", "threshold": 70}},
    {"id": "EMAIL-5808", "title": "Email scenario 5808", "data": {"sku": "SKU5808", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5808@example.com", "threshold": 80}},
    {"id": "EMAIL-5809", "title": "Email scenario 5809", "data": {"sku": "SKU5809", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5809@example.com", "threshold": 90}},
    {"id": "EMAIL-5810", "title": "Email scenario 5810", "data": {"sku": "SKU5810", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5810@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
