import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-2801", "title": "Email scenario 2801", "data": {"sku": "SKU2801", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2801@example.com", "threshold": 10}},
    {"id": "EMAIL-2802", "title": "Email scenario 2802", "data": {"sku": "SKU2802", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2802@example.com", "threshold": 20}},
    {"id": "EMAIL-2803", "title": "Email scenario 2803", "data": {"sku": "SKU2803", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2803@example.com", "threshold": 30}},
    {"id": "EMAIL-2804", "title": "Email scenario 2804", "data": {"sku": "SKU2804", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2804@example.com", "threshold": 40}},
    {"id": "EMAIL-2805", "title": "Email scenario 2805", "data": {"sku": "SKU2805", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2805@example.com", "threshold": 50}},
    {"id": "EMAIL-2806", "title": "Email scenario 2806", "data": {"sku": "SKU2806", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2806@example.com", "threshold": 60}},
    {"id": "EMAIL-2807", "title": "Email scenario 2807", "data": {"sku": "SKU2807", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2807@example.com", "threshold": 70}},
    {"id": "EMAIL-2808", "title": "Email scenario 2808", "data": {"sku": "SKU2808", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2808@example.com", "threshold": 80}},
    {"id": "EMAIL-2809", "title": "Email scenario 2809", "data": {"sku": "SKU2809", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2809@example.com", "threshold": 90}},
    {"id": "EMAIL-2810", "title": "Email scenario 2810", "data": {"sku": "SKU2810", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2810@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
