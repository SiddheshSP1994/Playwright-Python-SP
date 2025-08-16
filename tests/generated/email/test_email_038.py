import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-2261", "title": "Email scenario 2261", "data": {"sku": "SKU2261", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2261@example.com", "threshold": 610}},
    {"id": "EMAIL-2262", "title": "Email scenario 2262", "data": {"sku": "SKU2262", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2262@example.com", "threshold": 620}},
    {"id": "EMAIL-2263", "title": "Email scenario 2263", "data": {"sku": "SKU2263", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2263@example.com", "threshold": 630}},
    {"id": "EMAIL-2264", "title": "Email scenario 2264", "data": {"sku": "SKU2264", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2264@example.com", "threshold": 640}},
    {"id": "EMAIL-2265", "title": "Email scenario 2265", "data": {"sku": "SKU2265", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2265@example.com", "threshold": 650}},
    {"id": "EMAIL-2266", "title": "Email scenario 2266", "data": {"sku": "SKU2266", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2266@example.com", "threshold": 660}},
    {"id": "EMAIL-2267", "title": "Email scenario 2267", "data": {"sku": "SKU2267", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2267@example.com", "threshold": 670}},
    {"id": "EMAIL-2268", "title": "Email scenario 2268", "data": {"sku": "SKU2268", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2268@example.com", "threshold": 680}},
    {"id": "EMAIL-2269", "title": "Email scenario 2269", "data": {"sku": "SKU2269", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2269@example.com", "threshold": 690}},
    {"id": "EMAIL-2270", "title": "Email scenario 2270", "data": {"sku": "SKU2270", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2270@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
