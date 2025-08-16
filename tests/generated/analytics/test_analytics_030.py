import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-1791", "title": "Analytics scenario 1791", "data": {"sku": "SKU1791", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1791@example.com", "threshold": 910}},
    {"id": "ANALYTICS-1792", "title": "Analytics scenario 1792", "data": {"sku": "SKU1792", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1792@example.com", "threshold": 920}},
    {"id": "ANALYTICS-1793", "title": "Analytics scenario 1793", "data": {"sku": "SKU1793", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1793@example.com", "threshold": 930}},
    {"id": "ANALYTICS-1794", "title": "Analytics scenario 1794", "data": {"sku": "SKU1794", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1794@example.com", "threshold": 940}},
    {"id": "ANALYTICS-1795", "title": "Analytics scenario 1795", "data": {"sku": "SKU1795", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1795@example.com", "threshold": 950}},
    {"id": "ANALYTICS-1796", "title": "Analytics scenario 1796", "data": {"sku": "SKU1796", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1796@example.com", "threshold": 960}},
    {"id": "ANALYTICS-1797", "title": "Analytics scenario 1797", "data": {"sku": "SKU1797", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1797@example.com", "threshold": 970}},
    {"id": "ANALYTICS-1798", "title": "Analytics scenario 1798", "data": {"sku": "SKU1798", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1798@example.com", "threshold": 980}},
    {"id": "ANALYTICS-1799", "title": "Analytics scenario 1799", "data": {"sku": "SKU1799", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1799@example.com", "threshold": 990}},
    {"id": "ANALYTICS-1800", "title": "Analytics scenario 1800", "data": {"sku": "SKU1800", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1800@example.com", "threshold": 0}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
