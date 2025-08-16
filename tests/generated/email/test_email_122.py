import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-7301", "title": "Email scenario 7301", "data": {"sku": "SKU7301", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7301@example.com", "threshold": 10}},
    {"id": "EMAIL-7302", "title": "Email scenario 7302", "data": {"sku": "SKU7302", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7302@example.com", "threshold": 20}},
    {"id": "EMAIL-7303", "title": "Email scenario 7303", "data": {"sku": "SKU7303", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7303@example.com", "threshold": 30}},
    {"id": "EMAIL-7304", "title": "Email scenario 7304", "data": {"sku": "SKU7304", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7304@example.com", "threshold": 40}},
    {"id": "EMAIL-7305", "title": "Email scenario 7305", "data": {"sku": "SKU7305", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7305@example.com", "threshold": 50}},
    {"id": "EMAIL-7306", "title": "Email scenario 7306", "data": {"sku": "SKU7306", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7306@example.com", "threshold": 60}},
    {"id": "EMAIL-7307", "title": "Email scenario 7307", "data": {"sku": "SKU7307", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7307@example.com", "threshold": 70}},
    {"id": "EMAIL-7308", "title": "Email scenario 7308", "data": {"sku": "SKU7308", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7308@example.com", "threshold": 80}},
    {"id": "EMAIL-7309", "title": "Email scenario 7309", "data": {"sku": "SKU7309", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7309@example.com", "threshold": 90}},
    {"id": "EMAIL-7310", "title": "Email scenario 7310", "data": {"sku": "SKU7310", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7310@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
