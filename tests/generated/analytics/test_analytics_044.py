import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-2631", "title": "Analytics scenario 2631", "data": {"sku": "SKU2631", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2631@example.com", "threshold": 310}},
    {"id": "ANALYTICS-2632", "title": "Analytics scenario 2632", "data": {"sku": "SKU2632", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2632@example.com", "threshold": 320}},
    {"id": "ANALYTICS-2633", "title": "Analytics scenario 2633", "data": {"sku": "SKU2633", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2633@example.com", "threshold": 330}},
    {"id": "ANALYTICS-2634", "title": "Analytics scenario 2634", "data": {"sku": "SKU2634", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2634@example.com", "threshold": 340}},
    {"id": "ANALYTICS-2635", "title": "Analytics scenario 2635", "data": {"sku": "SKU2635", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2635@example.com", "threshold": 350}},
    {"id": "ANALYTICS-2636", "title": "Analytics scenario 2636", "data": {"sku": "SKU2636", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2636@example.com", "threshold": 360}},
    {"id": "ANALYTICS-2637", "title": "Analytics scenario 2637", "data": {"sku": "SKU2637", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2637@example.com", "threshold": 370}},
    {"id": "ANALYTICS-2638", "title": "Analytics scenario 2638", "data": {"sku": "SKU2638", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2638@example.com", "threshold": 380}},
    {"id": "ANALYTICS-2639", "title": "Analytics scenario 2639", "data": {"sku": "SKU2639", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2639@example.com", "threshold": 390}},
    {"id": "ANALYTICS-2640", "title": "Analytics scenario 2640", "data": {"sku": "SKU2640", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2640@example.com", "threshold": 400}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
