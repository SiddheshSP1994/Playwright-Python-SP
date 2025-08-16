import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-2821", "title": "Checkout scenario 2821", "data": {"sku": "SKU2821", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2821@example.com", "threshold": 210}},
    {"id": "CHECKOUT-2822", "title": "Checkout scenario 2822", "data": {"sku": "SKU2822", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2822@example.com", "threshold": 220}},
    {"id": "CHECKOUT-2823", "title": "Checkout scenario 2823", "data": {"sku": "SKU2823", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2823@example.com", "threshold": 230}},
    {"id": "CHECKOUT-2824", "title": "Checkout scenario 2824", "data": {"sku": "SKU2824", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2824@example.com", "threshold": 240}},
    {"id": "CHECKOUT-2825", "title": "Checkout scenario 2825", "data": {"sku": "SKU2825", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2825@example.com", "threshold": 250}},
    {"id": "CHECKOUT-2826", "title": "Checkout scenario 2826", "data": {"sku": "SKU2826", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2826@example.com", "threshold": 260}},
    {"id": "CHECKOUT-2827", "title": "Checkout scenario 2827", "data": {"sku": "SKU2827", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2827@example.com", "threshold": 270}},
    {"id": "CHECKOUT-2828", "title": "Checkout scenario 2828", "data": {"sku": "SKU2828", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2828@example.com", "threshold": 280}},
    {"id": "CHECKOUT-2829", "title": "Checkout scenario 2829", "data": {"sku": "SKU2829", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2829@example.com", "threshold": 290}},
    {"id": "CHECKOUT-2830", "title": "Checkout scenario 2830", "data": {"sku": "SKU2830", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2830@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
