import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-7481", "title": "Email scenario 7481", "data": {"sku": "SKU7481", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7481@example.com", "threshold": 810}},
    {"id": "EMAIL-7482", "title": "Email scenario 7482", "data": {"sku": "SKU7482", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7482@example.com", "threshold": 820}},
    {"id": "EMAIL-7483", "title": "Email scenario 7483", "data": {"sku": "SKU7483", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7483@example.com", "threshold": 830}},
    {"id": "EMAIL-7484", "title": "Email scenario 7484", "data": {"sku": "SKU7484", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7484@example.com", "threshold": 840}},
    {"id": "EMAIL-7485", "title": "Email scenario 7485", "data": {"sku": "SKU7485", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7485@example.com", "threshold": 850}},
    {"id": "EMAIL-7486", "title": "Email scenario 7486", "data": {"sku": "SKU7486", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7486@example.com", "threshold": 860}},
    {"id": "EMAIL-7487", "title": "Email scenario 7487", "data": {"sku": "SKU7487", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7487@example.com", "threshold": 870}},
    {"id": "EMAIL-7488", "title": "Email scenario 7488", "data": {"sku": "SKU7488", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7488@example.com", "threshold": 880}},
    {"id": "EMAIL-7489", "title": "Email scenario 7489", "data": {"sku": "SKU7489", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7489@example.com", "threshold": 890}},
    {"id": "EMAIL-7490", "title": "Email scenario 7490", "data": {"sku": "SKU7490", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7490@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
