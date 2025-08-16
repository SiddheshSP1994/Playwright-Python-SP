import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-8331", "title": "Analytics scenario 8331", "data": {"sku": "SKU8331", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8331@example.com", "threshold": 310}},
    {"id": "ANALYTICS-8332", "title": "Analytics scenario 8332", "data": {"sku": "SKU8332", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8332@example.com", "threshold": 320}},
    {"id": "ANALYTICS-8333", "title": "Analytics scenario 8333", "data": {"sku": "SKU8333", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8333@example.com", "threshold": 330}},
    {"id": "ANALYTICS-8334", "title": "Analytics scenario 8334", "data": {"sku": "SKU8334", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8334@example.com", "threshold": 340}},
    {"id": "ANALYTICS-8335", "title": "Analytics scenario 8335", "data": {"sku": "SKU8335", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8335@example.com", "threshold": 350}},
    {"id": "ANALYTICS-8336", "title": "Analytics scenario 8336", "data": {"sku": "SKU8336", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8336@example.com", "threshold": 360}},
    {"id": "ANALYTICS-8337", "title": "Analytics scenario 8337", "data": {"sku": "SKU8337", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8337@example.com", "threshold": 370}},
    {"id": "ANALYTICS-8338", "title": "Analytics scenario 8338", "data": {"sku": "SKU8338", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8338@example.com", "threshold": 380}},
    {"id": "ANALYTICS-8339", "title": "Analytics scenario 8339", "data": {"sku": "SKU8339", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8339@example.com", "threshold": 390}},
    {"id": "ANALYTICS-8340", "title": "Analytics scenario 8340", "data": {"sku": "SKU8340", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8340@example.com", "threshold": 400}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
