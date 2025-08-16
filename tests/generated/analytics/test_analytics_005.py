import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-0291", "title": "Analytics scenario 291", "data": {"sku": "SKU291", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user291@example.com", "threshold": 910}},
    {"id": "ANALYTICS-0292", "title": "Analytics scenario 292", "data": {"sku": "SKU292", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user292@example.com", "threshold": 920}},
    {"id": "ANALYTICS-0293", "title": "Analytics scenario 293", "data": {"sku": "SKU293", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user293@example.com", "threshold": 930}},
    {"id": "ANALYTICS-0294", "title": "Analytics scenario 294", "data": {"sku": "SKU294", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user294@example.com", "threshold": 940}},
    {"id": "ANALYTICS-0295", "title": "Analytics scenario 295", "data": {"sku": "SKU295", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user295@example.com", "threshold": 950}},
    {"id": "ANALYTICS-0296", "title": "Analytics scenario 296", "data": {"sku": "SKU296", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user296@example.com", "threshold": 960}},
    {"id": "ANALYTICS-0297", "title": "Analytics scenario 297", "data": {"sku": "SKU297", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user297@example.com", "threshold": 970}},
    {"id": "ANALYTICS-0298", "title": "Analytics scenario 298", "data": {"sku": "SKU298", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user298@example.com", "threshold": 980}},
    {"id": "ANALYTICS-0299", "title": "Analytics scenario 299", "data": {"sku": "SKU299", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user299@example.com", "threshold": 990}},
    {"id": "ANALYTICS-0300", "title": "Analytics scenario 300", "data": {"sku": "SKU300", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user300@example.com", "threshold": 0}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
