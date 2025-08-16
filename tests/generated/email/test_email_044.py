import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-2621", "title": "Email scenario 2621", "data": {"sku": "SKU2621", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2621@example.com", "threshold": 210}},
    {"id": "EMAIL-2622", "title": "Email scenario 2622", "data": {"sku": "SKU2622", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2622@example.com", "threshold": 220}},
    {"id": "EMAIL-2623", "title": "Email scenario 2623", "data": {"sku": "SKU2623", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2623@example.com", "threshold": 230}},
    {"id": "EMAIL-2624", "title": "Email scenario 2624", "data": {"sku": "SKU2624", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2624@example.com", "threshold": 240}},
    {"id": "EMAIL-2625", "title": "Email scenario 2625", "data": {"sku": "SKU2625", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2625@example.com", "threshold": 250}},
    {"id": "EMAIL-2626", "title": "Email scenario 2626", "data": {"sku": "SKU2626", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2626@example.com", "threshold": 260}},
    {"id": "EMAIL-2627", "title": "Email scenario 2627", "data": {"sku": "SKU2627", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2627@example.com", "threshold": 270}},
    {"id": "EMAIL-2628", "title": "Email scenario 2628", "data": {"sku": "SKU2628", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2628@example.com", "threshold": 280}},
    {"id": "EMAIL-2629", "title": "Email scenario 2629", "data": {"sku": "SKU2629", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2629@example.com", "threshold": 290}},
    {"id": "EMAIL-2630", "title": "Email scenario 2630", "data": {"sku": "SKU2630", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2630@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
