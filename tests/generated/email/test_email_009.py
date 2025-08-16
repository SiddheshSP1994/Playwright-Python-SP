import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-0521", "title": "Email scenario 521", "data": {"sku": "SKU521", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user521@example.com", "threshold": 210}},
    {"id": "EMAIL-0522", "title": "Email scenario 522", "data": {"sku": "SKU522", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user522@example.com", "threshold": 220}},
    {"id": "EMAIL-0523", "title": "Email scenario 523", "data": {"sku": "SKU523", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user523@example.com", "threshold": 230}},
    {"id": "EMAIL-0524", "title": "Email scenario 524", "data": {"sku": "SKU524", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user524@example.com", "threshold": 240}},
    {"id": "EMAIL-0525", "title": "Email scenario 525", "data": {"sku": "SKU525", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user525@example.com", "threshold": 250}},
    {"id": "EMAIL-0526", "title": "Email scenario 526", "data": {"sku": "SKU526", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user526@example.com", "threshold": 260}},
    {"id": "EMAIL-0527", "title": "Email scenario 527", "data": {"sku": "SKU527", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user527@example.com", "threshold": 270}},
    {"id": "EMAIL-0528", "title": "Email scenario 528", "data": {"sku": "SKU528", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user528@example.com", "threshold": 280}},
    {"id": "EMAIL-0529", "title": "Email scenario 529", "data": {"sku": "SKU529", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user529@example.com", "threshold": 290}},
    {"id": "EMAIL-0530", "title": "Email scenario 530", "data": {"sku": "SKU530", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user530@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
